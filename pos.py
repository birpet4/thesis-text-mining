
import random
from pathlib import Path
import spacy


# You need to define a mapping from your data's part-of-speech tag names to the
# Universal Part-of-Speech tag set, as spaCy includes an enum of these tags.
# See here for the Universal Tag Set:
# http://universaldependencies.github.io/docs/u/pos/index.html
# You may also specify morphological features for your tags, from the universal
# scheme.
TAG_MAP = {
    'C': {'pos': 'CAUSE'},
    'E': {'pos': 'EFFECT'},
    'N': {'pos': 'NONE'}
}

# Usually you'll read this in, of course. Data formats vary. Ensure your
# strings are unicode and that the number of tags assigned matches spaCy's
# tokenization. If not, you can always add a 'words' key to the annotations
# that specifies the gold-standard tokenization, e.g.:
# ("Eatblueham", {'words': ['Eat', 'blue', 'ham'] 'tags': ['V', 'J', 'N']})

TRAIN_DATA = [
    ("ThermostatFailedOpen", {'tags': ['V']}),
    ("EThermostatFailedClose", {'tags': ['V']})
]


def main(lang='en', output_dir=None, n_iter=25):
    """Create a new model, set up the pipeline and train the tagger. In order to
    train the tagger with a custom tag map, we're creating a new Language
    instance with a custom vocab.
    """
    nlp = spacy.blank(lang)
    # add the tagger to the pipeline
    # nlp.create_pipe works for built-ins that are registered with spaCy
    tagger = nlp.create_pipe('tagger')
    # Add the tags. This needs to be done before you start training.
    for tag, values in TAG_MAP.items():
        tagger.add_label(tag, values)
    nlp.add_pipe(tagger)
    nlp.vocab.vectors.name = 'spacy_pretrained_vectors'
    optimizer = nlp.begin_training()
    for i in range(n_iter):
        random.shuffle(TRAIN_DATA)
        losses = {}
        for text, annotations in TRAIN_DATA:
            nlp.update([text], [annotations], sgd=optimizer, losses=losses)
        print(losses)

    # test the trained model
    test_text = "If ThermostatFailedOpen moves from false to true, we are going to party"
    doc = nlp(test_text)
    print('Tags', [(t.text, t.tag_, t.pos_) for t in doc])

    # save model to output directory
    if output_dir is not None:
        output_dir = Path(output_dir)
        if not output_dir.exists():
            output_dir.mkdir()
        nlp.to_disk(output_dir)
        print("Saved model to", output_dir)

        # test the save model
        print("Loading from", output_dir)
        nlp2 = spacy.load(output_dir)
        doc = nlp2(test_text)
        print('Tags', [(t.text, t.tag_, t.pos_) for t in doc])


if __name__ == '__main__':
    main('en', 'customPOS')
