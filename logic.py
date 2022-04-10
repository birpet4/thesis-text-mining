import spacy
import spacy
import pandas as pd
import numpy as np
from spacy.util import minibatch, compounding
import json
import random
from pandas import DataFrame


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


def main():
    nlp = spacy.load("en_core_web_sm")
    train = []

    with open('fold/noif_statement2s.txt', 'r', encoding='utf-8') as file:
        Lines = file.readlines()

        for line in Lines:
            value = False
            cat = {"cats": {'POSITIVE': value}}
            # train.append(tuple([line, cat]))
            train.append([line, cat])

            doc = nlp(line)
            with open('fold/postags.txt', 'w', encoding='utf-8') as fileTag:
                Lines = file.readlines()

                for line in Lines:
                    doc = nlp(line)

                    for token in doc:
                        print(token.text, token.dep_, token.head.text, token.head.pos_, [
                              child for child in token.children])
                        fileTag.write(token.text + "," + token.dep_ + ",")

    with open('fold/if_statements.txt', 'r', encoding='utf-8') as file:
        Lines = file.readlines()
        for line in Lines:
            value = True
            cat = {"cats": {'POSITIVE': value}}
            # train.append(tuple([line, cat]))
            train.append([line, cat])

            doc = nlp(line)

            # for token in doc:
            # print(token.text, token.dep_, token.head.text, token.head.pos_,
            #      [child for child in token.children])

    if 'textcat' not in nlp.pipe_names:
        textcat = nlp.create_pipe('textcat')
        # textcat = nlp.create_pipe(
        #     "textcat", config={"exclusive_classes": True, "architecture": "ensemble"})
        nlp.add_pipe(textcat, last=True)
    else:
        textcat = nlp.get_pipe("textcat")

    textcat.add_label('POSITIVE')
    # textcat.add_label("OTHER")
    other_pipes = [pipe for pipe in nlp.pipe_names if pipe != 'textcat']

    n_iter = 1
    random.shuffle(train)
    # Only train the textcat pipe
    # with nlp.disable_pipes(*other_pipes):
    #     optimizer = nlp.begin_training()
    #     print("Training model...")
    #     for i in range(n_iter):
    #         losses = {}
    #         batches = minibatch(train, size=compounding(4, 32, 1.001))
    #         for batch in batches:
    #             texts, annotations = zip(*batch)
    #             nlp.update(texts, annotations, sgd=optimizer,
    #                        drop=0.2, losses=losses)

    # Only train the textcat pipe
    # with nlp.disable_pipes(*other_pipes):
    #     optimizer = nlp.begin_training()
    #     print("Training model...")
    #     for i in range(n_iter):
    #         losses = {}
    #         batches = minibatch(train, size=compounding(4, 32, 1.001))
    #         for batch in batches:
    #             texts, annotations = zip(*batch)
    #             texts = [nlp(text) for text, entities in batch]
    #             annotations = [{"cats": entities} for text, entities in batch]
    #             nlp.update(texts, annotations, sgd=optimizer,
    #                        drop=0.2, losses=losses)

    other_pipes = [pipe for pipe in nlp.pipe_names if pipe != 'textcat']
    with nlp.disable_pipes(*other_pipes):  # only train textcat
        optimizer = nlp.begin_training()
        print("Training the model...")
        print('{:^5}\t{:^5}\t{:^5}\t{:^5}'.format('LOSS', 'P', 'R', 'F'))
        for i in range(n_iter):
            losses = {}
            # batch up the examples using spaCy's minibatch
            batches = minibatch(train, size=compounding(4., 32., 1.001))
            for batch in batches:
                texts, annotations = zip(*batch)
                nlp.update(texts, annotations, sgd=optimizer, drop=0.2,
                           losses=losses)

    test_data = pd.read_csv("fold/if_else.csv", sep=";", encoding='cp1252')
    for index, row in test_data.iterrows():
        doc = nlp(row["line"])
        test_data.loc[index, 'cats'] = doc.cats["POSITIVE"]

        if doc.cats["POSITIVE"] > 0.5:
            test_data.loc[index, 'pred'] = 1
        else:
            test_data.loc[index, 'pred'] = 0

    test_data.to_csv('fold/result_1.csv', index=False)
    print(test_data.head())

    # with open('fold/if_test.txt', 'r', encoding='utf-8') as file:
    #     Lines = file.readlines()
    #     random.shuffle(Lines)

    #     with open('fold/res.txt', 'a', encoding='utf-8') as the_file:
    #         for line in Lines:
    #             doc = nlp(line)

    #             the_file.write(
    #                 line + "," + "Poz:" + str(doc.cats["POSITIVE"]) + ",")


if __name__ == "__main__":
    main()
