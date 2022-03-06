import spacy
import pandas as pd
import numpy as np
from spacy.util import minibatch, compounding
import sklearn.metrics as metrics
import matplotlib.pyplot as plt

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
        if token.pos_ =='VERB':
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
        if checkSimpleSentence(df['line'].iloc[index-1], nlp) =='p':
            isParagraphBefore = True
        
        if checkSimpleSentence(df['line'].iloc[index+1], nlp)  =='p':
            isParagraphAfter = True
        
    if len(sentence) < 50 and len(sentence) > 1:
        isShort = 1

    # conditions
    if onlyNumber or not isShort and not hasFewVerbs or isParagraphBefore and not isParagraphAfter:
        return 'p'

    if isUpperCaseOnly and isShort and hasFewVerbs and isParagraphBefore and isParagraphAfter:
        return 'title'

    return 'uncertain'

nlp = spacy.load("en_core_web_sm")

test_data = pd.concat([df8, df9, df10])
test_data = test_data.replace(np.nan, '', regex=True)


for index, row in test_data.iterrows():
    doc = nlp(row['line'])
    row['pred'] = checkSentence(doc, row['line'], index, test_data, nlp)

test_data.to_csv('testes.csv', index = False)

test_data = test_data.drop(test_data[(test_data['pred'] == "uncertain")].index)
test_data.loc[test_data.tag == "h2" or test_data.tag == "h3" or test_data.tag == "h1", 'tag'] = "title"


fpr, tpr, threshold = metrics.roc_curve(test_data['tag'], test_data['pred'])
roc_auc = metrics.auc(fpr, tpr)

plt.title('Receiver Operating Characteristic')
plt.plot(fpr, tpr, 'b', label = 'AUC = %0.2f' % roc_auc)
plt.legend(loc = 'lower right')
plt.plot([0, 1], [0, 1],'r--')
plt.xlim([0, 1])
plt.ylim([0, 1])
plt.ylabel('True Positive Rate')
plt.xlabel('False Positive Rate')
plt.show()