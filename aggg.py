
import spacy
import pandas as pd
import numpy as np
from spacy.util import minibatch, compounding

df2 = pd.read_csv('masodik.csv')
df3 = pd.read_csv('harmadik.csv')
df4 = pd.read_csv('negyedik.csv')
df5 = pd.read_csv('otodik.csv')
df6 = pd.read_csv('hatodik.csv')
df7 = pd.read_csv('hetedik.csv')
df8 = pd.read_csv('nyolcadik.csv')
df9 = pd.read_csv('kilencedik.csv')

training_data = pd.concat([df2, df3, df4, df5, df6, df7])
# training_data = df2
test_data = pd.concat([df8, df9])
# for index, row in training_data.iterrows():
#     doc = nlp(row['line'])
#     row['pred'] = checkSentence(doc, row['line'], index, training_data, nlp)

training_data = training_data.replace(np.nan, '', regex=True)
test_data = test_data.replace(np.nan, '', regex=True)

training_data = training_data.drop(
    training_data[(training_data['line'] == "")].index)
test_data = test_data.drop(test_data[(test_data['line'] == "")].index)
nlp = spacy.load('en_core_web_sm')  # create english Language class
# nlp.create_pipe works for built-ins that are registered with spaCy
if 'textcat' not in nlp.pipe_names:
    textcat = nlp.create_pipe('textcat')
    nlp.add_pipe(textcat, last=True)
# otherwise, get it, so we can add labels to it
else:
    textcat = nlp.get_pipe('textcat')
#("Number of texts to train from","t" , int)
n_texts = 30000
# You can increase texts count if you have more computational power.

# ("Number of training iterations", "n", int))
n_iter = 10
# add label to text classifier
textcat.add_label('POSITIVE')

# load the dataset
print("Loading food reviews data...")

# training_data = pd.read_csv('kamu.csv')
# test_data = pd.read_csv("kamutest.csv")
training_data = training_data.replace(np.nan, '', regex=True)
test_data = test_data.replace(np.nan, '', regex=True)
training_data = training_data.drop(
    training_data[(training_data['line'] == "")].index)
test_data = test_data.drop(test_data[(test_data['line'] == "")].index)

train = []
for index, row in training_data.iterrows():
    value = False
    if row['tag'] == "h2" or row['tag'] == "h4" or row['tag'] == "h3" or row['pred'] == 'title':
        value = True
    cat = {"cats": {'POSITIVE': value}}
    train.append([row['line'], cat])

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

for index, row in test_data.iterrows():
    doc = nlp(row['line'])
    row['pred'] = doc.cats

test_data.to_csv('kedd12.csv', index=False)
