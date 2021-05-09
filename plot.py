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
    df = pd.read_csv('plot.csv')

    
