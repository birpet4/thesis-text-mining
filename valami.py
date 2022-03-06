import spacy
import pandas as pd
import numpy as np
from spacy.util import minibatch, compounding

def checkSimpleSentence(sentence, nlp) -> bool:
    hasFewVerbs = False
    isUpperCaseOnly = False
    isShort = False
    isStartWithUpper = False
    onlyNumber = True
    isParagraphBefore = False
    isParagraphAfter = False

    doc = nlp(sentence)
    verbs = 0
    for token in doc:
        if token.pos_ == 'VERB':
            verbs += 1
        if token.pos_ != 'NUM':
            onlyNumber = False

    #     # print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_,
    #     #     token.shape_, token.is_alpha, token.is_stop)

    if verbs < 3:
        hasFewVerbs = True

    if not sentence:
        return 'td'

    if len(sentence) < 50 and len(sentence) > 1:
        isShort = 1

    # conditions
    if onlyNumber or not isShort and not hasFewVerbs:
        return 'p'

    return 'uncertain'

def checkSentence(doc, sentence, index, df, nlp) -> bool:
    hasFewVerbs = False
    isUpperCaseOnly = False
    isShort = False
    isStartWithUpper = False
    onlyNumber = True
    isParagraphBefore = False
    isParagraphAfter = False

    verbs = 0
    for token in doc:
        if token.pos_ == 'VERB':
            verbs += 1
        if token.pos_ != 'NUM':
            onlyNumber = False

    #     # print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_,
    #     #     token.shape_, token.is_alpha, token.is_stop)

    if verbs < 3:
        hasFewVerbs = True

    if sentence:
        if sentence.isupper() or sentence.istitle() or sentence[0].isupper() or sentence[0].isnumeric():
            isUpperCaseOnly = 1
    else:
        return 'td'

    if index != 0 or len(df) != index - 1:
        if checkSimpleSentence(df['line'].iloc[index-1], nlp) == 'p':
            isParagraphBefore = True
        
        if checkSimpleSentence(df['line'].iloc[index+1], nlp)  == 'p':
            isParagraphAfter = True
        
    if len(sentence) < 50 and len(sentence) > 1:
        isShort = 1

    # conditions
    if onlyNumber or not isShort and not hasFewVerbs or isParagraphBefore and not isParagraphAfter:
        return 'p'

    if isUpperCaseOnly and isShort and hasFewVerbs and isParagraphBefore and isParagraphAfter:
        return 'title'

    return 'uncertain'

def main():
    df = pd.read_csv('elso.csv')
    df2 = pd.read_csv('masodik.csv')
    df3 = pd.read_csv('harmadik.csv')
    df4 = pd.read_csv('negyedik.csv')
    df5 = pd.read_csv('otodik.csv')
    df6 = pd.read_csv('hatodik.csv')
    df7 = pd.read_csv('hetedik.csv')
    df8 = pd.read_csv('nyolcadik.csv')
    df9 = pd.read_csv('kilencedik.csv')
    df10 = pd.read_csv('tizedik.csv')

    training_data = pd.concat([df, df2, df3, df4, df5, df6, df7])
    # training_data = df2
    test_data = pd.concat([df8, df9, df10])

    training_data = training_data.replace(np.nan, '', regex=True)
    test_data = test_data.replace(np.nan, '', regex=True)

    nlp = spacy.load("en_core_web_sm")

    # d = [df['line'].iloc[380],df['line'].iloc[103]] 

    # for x in d:
    #     doc = nlp(x)
    #     for token in doc:
    #         print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_,
    #             token.shape_, token.is_alpha, token.is_stop)

    # for index, row in training_data.iterrows():
    #     doc = nlp(row['line'])
    #     row['pred'] = checkSentence(doc, row['line'], index, training_data, nlp)

    # training_data.to_csv('train2.csv', index = False)
    training_data = pd.read_csv('train2.csv')
    training_data = training_data.drop(training_data[(training_data['pred'] == "uncertain")].index)
    train = []
    training_data = training_data.replace(np.nan, '', regex=True)
    for index, row in training_data.iterrows():
        value = False
        if row['pred'] == "title":
            value = True
        cat = { "cats": { 'POSITIVE': value}}
        train.append(tuple([row['line'], cat]))

    # textcat=nlp.create_pipe( "textcat", config={"exclusive_classes": True, "architecture": "simple_cnn"})
    # nlp.add_pipe(text_cat, last=True)

    if 'textcat' not in nlp.pipe_names:
        textcat = nlp.create_pipe("textcat", config={"exclusive_classes": False, "architecture": "simple_cnn"})
        nlp.add_pipe(textcat, last=True) 
    else:
        textcat = nlp.get_pipe("textcat")

    textcat.add_label('POSITIVE')
    textcat.add_label("OTHER")
    other_pipes = [pipe for pipe in nlp.pipe_names if pipe != 'textcat']

    n_iter = 1

    # Only train the textcat pipe
    with nlp.disable_pipes(*other_pipes):
        optimizer = nlp.begin_training()
        print("Training model...")
        for i in range(n_iter):
            losses = {}
            batches = minibatch(train, size=compounding(4,32,1.001))
            for batch in batches:
                texts, annotations = zip(*batch)
                nlp.update(texts, annotations, sgd=optimizer,
                        drop=0.2, losses=losses)

    # test

    for index, row in test_data.iterrows():
        doc = nlp(row['line'])
        row['pred'] = doc.cats

    # category = nlp.create_pipe("textcat")
    # category.add_label("KAT")
    # nlp.add_pipe(category)

    # # Start the training
    # nlp.begin_training()

    # # Loop for 10 iterations
    # for itn in range(100):
    #     losses = {}

    #     # Batch the examples and iterate over them
    #     for batch in spacy.util.minibatch(train, size=1):
    #         texts = [nlp(text) for text, entities in batch]
    #         annotations = [{"cats": entities} for text, entities in batch]
    #         nlp.update(texts, annotations, losses=losses)
    #     if itn % 20 == 0:
    #         print(losses)

    test_data.to_csv('kesz2.csv', index = False)


    #     print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_,
    #             token.shape_, token.is_alpha, token.is_stop)


if __name__ == "__main__":
    main()