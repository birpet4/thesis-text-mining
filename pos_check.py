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


def graph(doc):
    output_path = Path("test/if" + str("_test") + ".svg")
    svg = displacy.render(doc, style='dep')
    with output_path.open("w", encoding="utf-8") as fh:
        fh.write(svg)


def test(doc):
    # output_path = Path("test/if30.svg")
    # svg = displacy.render(doc, style='dep')
    # with output_path.open("w", encoding="utf-8") as fh:
    #     fh.write(svg)

    mark = ""
    advcl = ""
    position = 0
    tok = ""
    punct = 0
    lastp = 0
    lastlast = 0
    if_pos = 0
    for token in doc:
        if token.text == "If":
            if_pos = token.idx
            mark = token.head.text

        if token.dep_ == "punct":
            punct = token.idx
            if lastp != 0:
                lastlast = token.idx

        if token.text == mark:
            if token.dep_ == "advcl" and "If" in [children.text for children in token.children]:
                advcl = token.head.text
            elif token.dep_ == "ROOT" and mark in [children.text for children in token.children]:
                position = token.idx

        if token.text == advcl:
            if mark in [children.text for children in token.children] and token.dep_ == "ROOT":
                position = token.idx
                tok = token.text
                lastp = punct

            elif advcl in [children.text for children in token.children]:
                advcl = token.head.text

    # print(lastp, tok, position)
    print(doc.text[
          lastp:])
    print(doc.text[
          :lastp])


if __name__ == "__main__":
    nlp = spacy.load("en_core_web_sm")
    doc = nlp("If the Collateral Administrator does not agree to assist the Issuer and the Collateral Manager (or the Issuer (acting on the advice of the Collateral Manager) elects not the appoint the Collateral Administrator) in providing such reporting, the Issuer and the Collateral Manager shall appoint another entity to make such information available to any Competent Authority, any Noteholder and any potential investor in the Notes")
    test(doc)
