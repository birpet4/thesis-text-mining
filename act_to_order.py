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


LABEL = ['Section', 'Order', 'Abbreviation']

TRAIN_DATA = [
    (
        """Article 6 of Regulation 2017/1129/EU (as amended, the “Prospectus Regulation”)""",
        {"entities": [(0, 8, "Section"), (13, 35, "Order"),
                      (55, 75, "Abbreviation")]}
    ),
    (
        """United States Securities Act of 1933, as amended (the “Securities Act”)""",
        {"entities": [(0, 35, "Order"), (55, 68, "Abbreviation")]}
    ),
    (
        """Regulation S under the Securities Act (“Regulation S”));""",
        {"entities": [(0, 11, "Section"), (23, 36, "Order"),
                      (40, 51, "Abbreviation")]}
    ),
    (
        """Section 3(c)(7) of the United States Investment Company Act of 1940, as amended (the “Investment Company Act”)""",
        {"entities": [(0, 14, "Section"), (23, 66, "Order"),
                      (86, 107, "Abbreviation")]}
    ),
    (
        """""",
        {"entities": []}
    ),
    (
        """""",
        {"entities": []}
    ),
    (
        """""",
        {"entities": []}
    ),
    (
        """""",
        {"entities": []}
    ),
    (
        """""",
        {"entities": []}
    ),
    (
        """""",
        {"entities": []}
    ),
    (
        """""",
        {"entities": []}
    ),
    (
        """""",
        {"entities": []}
    ),    (
        """""",
        {"entities": []}
    ),    (
        """""",
        {"entities": []}
    ),    (
        """""",
        {"entities": []}
    )

]


def train_custom_ner():
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
    # with nlp.disable_pipes(*other_pipes):  # only train NER
    #     for itn in range(1000):
    #         random.shuffle(TRAIN_DATA)
    #         losses = {}
    #         batches = minibatch(TRAIN_DATA, size=compounding(4., 32., 1.001))
    #         for batch in batches:
    #             texts, annotations = zip(*batch)
    #             nlp.update(texts, annotations, sgd=optimizer, drop=0.35,
    #                        losses=losses)
    #         print('Losses', losses)
    nlp.max_length = 200000000

    output_dir = "act_model_v2"
    # if output_dir is not None:
    #     output_dir = Path(output_dir)
    #     if not output_dir.exists():
    #         output_dir.mkdir()
    #     nlp.meta['name'] = "CustomNER"  # rename model
    #     nlp.to_disk(output_dir)
    #     print("Saved model to", output_dir)

    # with open('sample/a310bb91.p.html.293e9e18.txt', 'r', encoding='utf-8') as file:
    #     all_of_it = file.read()
    #     doc = nlp(all_of_it)
    #     displacy.serve(doc, style="ent")

    # with open('sample/eurlex_01.txt', 'r', encoding='utf-8') as file:
    #     all_of_it = file.read()
    #     doc = nlp(all_of_it)
    #     displacy.serve(doc, style="ent")

    with open('sample/a310bb91.p.html.293e9e18.txt', 'r', encoding='utf-8') as file:
        all_of_it = file.read()
        doc = nlp(all_of_it)
        displacy.serve(doc, style="ent")
        # with open('test/act-ner.txt', 'w+', encoding='utf-8') as f:
        #     for line in list(doc.ents):
        #         f.write(line.text)
        #         f.write('\n')

    # # Test the trained model
    # test_text = """If the Issuer becomes subject to an insolvency proceeding and the Issuer has obligations to creditors that are treated under Irish law as creditors that are senior relative to the Noteholders and other Secured Parties, the Noteholders (and other Secured Parties) may suffer losses as a result of their subordinated status during such insolvency proceedings. In particular, under Irish law, upon an insolvency of an Irish company, such as the Issuer, when applying the proceeds of assets subject to fixed security which may have been realised in the course of a liquidation or receivership, the claims of a limited category of preferential creditors will take priority over the claims of creditors holding the relevant fixed security. These preferred claims include the remuneration, costs and expenses properly incurred by any examiner of the company (which may include any borrowings made by an examiner to fund the company’s requirements for the duration of his appointment) which have been approved by the relevant Irish courts. See 7.3 “Examinership”."""
    # # test_text = """The Issuer will depend upon the Asset Swap Counterparty to perform its obligations under any hedges. If the Asset Swap Counterparty defaults or becomes unable to perform due to insolvency or otherwise, the Issuer may not receive payments it would otherwise be entitled to from the Asset Swap Counterparty to cover its foreign exchange exposure."""
    # doc = nlp(test_text)
    # print("Entities")
    # for ent in doc.ents:
    #     print("lab:", ent.label_, ent.text)


if __name__ == "__main__":
    nlp = spacy.load("en_core_web_sm")
    train_custom_ner()
