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
        if token.pos_ is 'VERB':
            verbs += 1
        if token.pos_ is not 'NUM':
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
        if token.pos_ is 'VERB':
            verbs += 1
        if token.pos_ is not 'NUM':
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

    if index != 0 or len(df) is not index - 1:
        if checkSimpleSentence(df['line'].iloc[index-1], nlp) is 'p':
            isParagraphBefore = True
        
        if checkSimpleSentence(df['line'].iloc[index+1], nlp)  is 'p':
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
    df2 = pd.read_csv('masodik.csv')
    df3 = pd.read_csv('harmadik.csv')
    df4 = pd.read_csv('negyedik.csv')
    df5 = pd.read_csv('otodik.csv')
    df6 = pd.read_csv('hatodik.csv')
    df7 = pd.read_csv('hetedik.csv')
    df8 = pd.read_csv('nyolcadik.csv')
    df9 = pd.read_csv('kilencedik.csv')
    df10 = pd.read_csv('tizedik.csv')

    training_data = pd.concat([df2, df3, df4, df5, df6, df7, df8])
    # training_data = df2
    test_data = pd.concat([df9, df10])
    nlp = spacy.load("en_core_web_sm")
    # for index, row in training_data.iterrows():
    #     doc = nlp(row['line'])
    #     row['pred'] = checkSentence(doc, row['line'], index, training_data, nlp)


    training_data = pd.read_csv('train2.csv')
    training_data = training_data.replace(np.nan, '', regex=True)
    test_data = test_data.replace(np.nan, '', regex=True)

    training_data = training_data.drop(training_data[(training_data['line'] == "")].index)
    test_data = test_data.drop(test_data[(test_data['line'] == "")].index)

    train = []
    for index, row in training_data.iterrows():
        value = False
        if row['tag'] is "h2" or row['tag'] is "h1" or row['tag'] is "h3" or row['pred'] is 'title':
            value = True
        cat = { "cats": { 'Title': value, 'Paragraph': not value}}
        train.append([row['line'], { 'Title': value, 'Paragraph': not value} ])

    test_data.to_csv('traines.csv', index = False)
    if 'textcat' not in nlp.pipe_names:
        textcat = nlp.create_pipe("textcat", config={"exclusive_classes": True, "architecture": "simple_cnn"})
        nlp.add_pipe(textcat, last=True) 
    else:
        textcat = nlp.get_pipe("textcat")

    textcat.add_label('Title')
    textcat.add_label("Paragraph")
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
                texts = [nlp(text) for text, entities in batch]
                annotations = [{ "cats" : entities} for text, entities in batch]
                nlp.update(texts, annotations, sgd=optimizer,
                        drop=0.2, losses=losses)

    # test
    for index, row in test_data.iterrows():
        doc = nlp(row['line'])
        row['pred'] = doc.cats

    test_data.to_csv('kedd6.csv', index = False)

if __name__ == "__main__":
    main()