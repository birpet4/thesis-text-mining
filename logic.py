import spacy
import spacy
import pandas as pd
import numpy as np
from spacy.util import minibatch, compounding
import json
import random
from pandas import DataFrame
import sklearn.metrics as metrics
import matplotlib.pyplot as plt
from pathlib import Path
from sklearn.utils import shuffle


def check_for_if_statements(file):
    if_paragraphs = []
    Lines = file.readlines()
    i = 0
    for line in Lines:
        if " if " in line:
            i = i + 1
            if_paragraphs.append(line)
            if i > 9:
                break

    return if_paragraphs


def check_for_noif_statements(file):
    paragraphs = []
    Lines = file.readlines()
    i = 0
    for line in Lines:
        if " if " not in line and len(line) > 1000:
            i = i + 1
            paragraphs.append(line)
            if i > 9:
                break

    return paragraphs


def create_data():
    contracts = ""
    if_paragraphs = []

    with open('sample/1acf000d.p.html.9e269fc7.txt', 'r', encoding='utf-8') as file:
        if_paragraphs.extend(check_for_noif_statements(file))

    with open('sample/5ae3b1c8.p.html.57e47d17.txt', 'r', encoding='utf-8') as file:
        if_paragraphs.extend(check_for_noif_statements(file))

    with open('sample/24bc5b9b.p.html.56f20ee0.txt', 'r', encoding='utf-8') as file:
        if_paragraphs.extend(check_for_noif_statements(file))

    with open('sample/83ade9f7.p.html.25b3b5c0.txt', 'r', encoding='utf-8') as file:
        if_paragraphs.extend(check_for_noif_statements(file))

    with open('sample/351dce62.p.html.94a8017a.txt', 'r', encoding='utf-8') as file:
        if_paragraphs.extend(check_for_noif_statements(file))

    with open('sample/3851e801.p.html.e851e606.txt', 'r', encoding='utf-8') as file:
        if_paragraphs.extend(check_for_noif_statements(file))

    with open('sample/3766090a.p.html.4b263f41.txt', 'r', encoding='utf-8') as file:
        if_paragraphs.extend(check_for_noif_statements(file))

    with open('sample/47352562.p.html.a78164e2.txt', 'r', encoding='utf-8') as file:
        if_paragraphs.extend(check_for_noif_statements(file))

    with open('sample/a1f57859.p.html.f18ba3b9.txt', 'r', encoding='utf-8') as file:
        if_paragraphs.extend(check_for_noif_statements(file))

    with open('sample/a310bb91.p.html.293e9e18.txt', 'r', encoding='utf-8') as file:
        if_paragraphs.extend(check_for_noif_statements(file))

    with open('fold/noif_statement2s.txt', 'a') as the_file:
        for line in if_paragraphs:
            the_file.write(line)


def roc_auc_curve(data):
    fpr, tpr, threshold = metrics.roc_curve(data['val'], data['pred'])
    roc_auc = metrics.auc(fpr, tpr)

    plt.title('Receiver Operating Characteristic')
    plt.plot(fpr, tpr, 'b', label='AUC = %0.2f' % roc_auc)
    plt.legend(loc='lower right')
    plt.plot([0, 1], [0, 1], 'r--')
    plt.xlim([0, 1])
    plt.ylim([0, 1])
    plt.ylabel('True Positive Rate')
    plt.xlabel('False Positive Rate')
    # plt.show()
    plt.savefig("mygraph.png")


def create_training_dataset():
    train = []
    with open('train/noif_10.txt', 'r', encoding='utf-8') as file:
        Lines = file.readlines()

        for line in Lines:
            value = False
            cat = {"cats": {'Conditional': value, 'NoConditional': not value}}
            train.append(tuple([line, cat]))

    with open('train/if_10.txt', 'r', encoding='utf-8') as file:
        Lines = file.readlines()
        for line in Lines:
            value = True
            cat = {"cats": {'Conditional': value, 'NoConditional': not value}}
            train.append(tuple([line, cat]))

    return train


def evaluate(tokenizer, textcat, texts, cats):
    docs = (tokenizer(text) for text in texts)
    tp = 0.0  # True positives
    fp = 1e-8  # False positives
    fn = 1e-8  # False negatives
    tn = 0.0  # True negatives
    for i, doc in enumerate(textcat.pipe(docs)):
        gold = cats[i]
        for label, score in doc.cats.items():
            if label not in gold:
                continue
            if label == "NEGATIVE":
                continue
            if score >= 0.5 and gold[label] >= 0.5:
                tp += 1.0
            elif score >= 0.5 and gold[label] < 0.5:
                fp += 1.0
            elif score < 0.5 and gold[label] < 0.5:
                tn += 1
            elif score < 0.5 and gold[label] >= 0.5:
                fn += 1
    precision = tp / (tp + fp)
    recall = tp / (tp + fn)
    if (precision + recall) == 0:
        f_score = 0.0
    else:
        f_score = 2 * (precision * recall) / (precision + recall)
    return {"textcat_p": precision, "textcat_r": recall, "textcat_f": f_score}


def mas():
    test_data = pd.read_csv("fold/test_doc.csv", encoding='utf8')
    for index, row in test_data.iterrows():
        doc = row["text"]
        if doc.find("if ") != -1 or doc.find("if,") != -1 or doc.find("If ") != -1 or doc.find("If,") != -1 or doc.find("when") != -1 or doc.find("When") != -1 or doc.find("where") != -1 or doc.find("Where") != -1:
            test_data.loc[index, 'val'] = 1
        else:
            test_data.loc[index, 'val'] = 0

    test_data.to_csv('fold/test_doc.csv', index=False)


def main():
    model = "logic_model_10"
    if model is not None:
        nlp = spacy.load(model)  # load existing spacy model
        print("Loaded model '%s'" % model)
    else:
        nlp = spacy.blank('en')  # create blank Language class
        print("Created blank 'en' model")

    if 'textcat' not in nlp.pipe_names:
        textcat = nlp.create_pipe(
            "textcat", config={"exclusive_classes": True, "architecture": "ensemble"})
        nlp.add_pipe(textcat, last=True)
    else:
        textcat = nlp.get_pipe("textcat")

    # Add labels to text classifier
    textcat.add_label("Conditional")
    textcat.add_label("NoConditional")

    training_set = create_training_dataset()
    random.shuffle(training_set)

    pipe_exceptions = ["textcat", "trf_wordpiecer", "trf_tok2vec"]
    other_pipes = [
        pipe for pipe in nlp.pipe_names if pipe not in pipe_exceptions]
    n_iter = 30
    with nlp.disable_pipes(*other_pipes):  # only train textcat
        optimizer = nlp.begin_training()
        print("Training the model...")
        print("{:^5}\t{:^5}\t{:^5}\t{:^5}".format("LOSS", "P", "R", "F"))
        batch_sizes = compounding(4.0, 32.0, 1.001)
        for i in range(n_iter):
            losses = {}
            # batch up the examples using spaCy's minibatch
            random.shuffle(training_set)
            batches = minibatch(training_set, size=batch_sizes)
            for batch in batches:
                texts, annotations = zip(*batch)
                nlp.update(texts, annotations, sgd=optimizer,
                           drop=0.2, losses=losses)

    test_data = pd.read_csv("test/test_set.csv", sep=";", encoding='utf-8')
    test_data = shuffle(test_data)
    test_data = test_data.iloc[:-20]
    for index, row in test_data.iterrows():
        doc = nlp(row["text"])
        test_data.loc[index, 'pred'] = doc.cats["Conditional"]
        if doc.cats["Conditional"] > 0.5:
            test_data.loc[index, 'pred_val'] = 1
        else:
            test_data.loc[index, 'pred_val'] = 0

    print('Precision: %.3f' % metrics.precision_score(
        test_data["val"].to_list(), test_data["pred_val"].to_list()))
    print('Recall: %.3f' % metrics.recall_score(
        test_data["val"].to_list(), test_data["pred_val"].to_list()))
    print('Accuracy: %.3f' % metrics.accuracy_score(
        test_data["val"].to_list(), test_data["pred_val"].to_list()))
    print('F1 Score: %.3f' % metrics.f1_score(
        test_data["val"].to_list(), test_data["pred_val"].to_list()))
    # test_data.to_csv('fold/test_eur_100.csv', index=False)

    # output_dir = "logic_model_100_ensemble"
    # if output_dir is not None:
    #     output_dir = Path(output_dir)
    #     if not output_dir.exists():
    #         output_dir.mkdir()
    #     nlp.meta['name'] = "Logic"  # rename model
    #     nlp.to_disk(output_dir)
    #     print("Saved model to", output_dir)

    # df = pd.DataFrame(columns=['text', 'prediction'])
    # with open('sample/eurlex_01.txt', 'r', encoding='utf-8') as file:
    #     Lines = file.readlines()
    #     for line in Lines:
    #         doc = nlp(line)
    #         df = df.append(
    #             {'text': line, 'prediction': doc.cats["Conditional"]}, ignore_index=True)

    # test_data = pd.read_csv("fold/test_doc.csv", encoding='utf8')
    # for index, row in df.iterrows():
    #     doc = row["text"]
    #     if doc.find("if ") != -1 or doc.find("if,") != -1 or doc.find("If ") != -1 or doc.find("If,") != -1 or doc.find("when") != -1 or doc.find("When") != -1 or doc.find("where") != -1 or doc.find("Where") != -1:
    #         df.loc[index, 'val'] = 1
    #     else:
    #         df.loc[index, 'val'] = 0
    test_data = shuffle(test_data)
    roc_auc_curve(test_data)

    # df.to_csv('test/test_100_eur.csv', index=False)


if __name__ == "__main__":
    main()
