import spacy
import spacy
import pandas as pd
import numpy as np
from spacy.util import minibatch, compounding
import json
import random
from pandas import DataFrame
from spacy import displacy
from pathlib import Path
from docx import Document
from docx.shared import Inches
from docx.enum.text import WD_COLOR_INDEX
from spacy import displacy


def graph(doc):
    output_path = Path("test/if" + str("_test") + ".svg")
    svg = displacy.render(doc, style='dep')
    with output_path.open("w", encoding="utf-8") as fh:
        fh.write(svg)


LABEL = ['Reference']
TRAIN_DATA = []
TRIGGER_WORDS = ["Act", "Regulation",
                 "Directive", "Treaty", "Article", "Section"]


def train_custom_ner():
    is_save = True
    model = "act_model_v2"
    if model is not None:
        nlp = spacy.load(model)  # load existing spacy model
        print("Loaded model '%s'" % model)
    else:
        nlp = spacy.blank('en')  # create blank Language class
        print("Created blank 'en' model")
    if 'ner' not in nlp.pipe_names:
        ner = nlp.create_pipe('ner')
        nlp.add_pipe(ner)
    else:
        ner = nlp.get_pipe('ner')

    for i in LABEL:
        ner.add_label(i)   # Add new entity labels to entity recognizer

    if model is None:
        optimizer = nlp.begin_training()
    else:
        optimizer = nlp.entity.create_optimizer()

    # Get names of other pipes to disable them during training to train only NER
    other_pipes = [pipe for pipe in nlp.pipe_names if pipe != 'ner']
    with nlp.disable_pipes(*other_pipes):  # only train NER
        for itn in range(100):
            random.shuffle(TRAIN_DATA)
            losses = {}
            batches = minibatch(TRAIN_DATA, size=compounding(4., 32., 1.001))
            for batch in batches:
                texts, annotations = zip(*batch)
                nlp.update(texts, annotations, sgd=optimizer, drop=0.35,
                           losses=losses)
            print('Losses', losses)
    nlp.max_length = 200000000

    output_dir = "act_model_v2"
    if output_dir is not None and is_save:
        output_dir = Path(output_dir)
        if not output_dir.exists():
            output_dir.mkdir()
        nlp.meta['name'] = "CustomNER"  # rename model
        nlp.to_disk(output_dir)
        print("Saved model to", output_dir)

    # with open('sample/a310bb91.p.html.293e9e18.txt', 'r', encoding='utf-8') as file:
    #     all_of_it = file.read()
    #     doc = nlp(all_of_it)
    #     displacy.serve(doc, style="ent")

    # with open('sample/eurlex_01.txt', 'r', encoding='utf-8') as file:
    #     all_of_it = file.read()
    #     doc = nlp(all_of_it)
    #     displacy.serve(doc, style="ent")

    with open("sample/a310bb91.p.html.293e9e18.txt", 'r', encoding='utf-8') as file:
        all_of_it = file.read()
        doc = nlp(all_of_it)
        with open('test/act-ner2.txt', 'w+', encoding='utf-8') as f:
            for line in list(doc.ents):
                f.write(line.text)
                f.write('\n')
        displacy.serve(doc, style="ent")


if __name__ == "__main__":

    train_custom_ner()
