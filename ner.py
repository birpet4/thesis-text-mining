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

from ner_conditional_training_data import TRAIN_DATA


def graph(doc):
    output_path = Path("test/if" + str("_test") + ".svg")
    svg = displacy.render(doc, style='dep')
    with output_path.open("w", encoding="utf-8") as fh:
        fh.write(svg)


# LABEL = ['Cause', 'Effect'
LABEL = ['Conditional']


# TRAIN_DATA = [
#     (
#         """The credit rating of a country affects the ratings of entities operating in its territory,
#         and in particular the ratings of financial institutions. Accordingly, such downgrades of the UK’s sovereign credit
#         rating and any further downgrade action may trigger downgrades in respect of parties to the Transaction Documents.
#         If a counterparty no longer satisfies the relevant Rating Requirement, the Transaction Documents may require
#         that such counterparty be replaced with an entity that satisfies the relevant Rating Requirement.
#         If rating downgrades are widespread, it may become difficult or impossible to replace counterparties with entities that satisfy the relevant
#         Rating Requirement.""",
#         {"entities": [(321, 390, "Cause"), (391, 526, "Effect"),
#                       (528, 563, "Cause"), (564, 686, "Effect")]}
#     ),
#     (
#         """In Europe, the U.S. and elsewhere there has been, and there continues to be increased political and regulatory scrutiny of banks,
#         financial institutions, “shadow banking entities” and the asset-backed securities industry. This has resulted in a raft of measures
#         for increased regulation which are currently at various stages of implementation and which may have an adverse impact on the regulatory
#         capital charge to certain investors in securitisation exposures and/or the incentives for certain investors to hold or trade asset-backed
#         securities, and may thereby affect the liquidity of such securities.""",
#         {"entities": []}
#     ),
#     (
#         """If any determination is made that this transaction is subject to the U.S. Risk Retention Rules, the Collateral Manager may fail to comply
#         (or not be able to comply) with the U.S. Risk Retention Rules, which may have a material adverse effect on the Collateral Manager, the Issuer
#         and/or the market value and/or liquidity of the Notes.""",
#         {"entities": [(0, 94, "Cause"), (95, 332, "Effect")]}
#     ),
#     (
#         """IFMD introduced authorisation and regulatory requirements for managers of AIFs. If the Issuer were to be considered to be an AIF within the meaning in AIFMD, it would need to be managed by a manager authorised under AIFMD (an “AIFM”). The Collateral Manager is not authorised under AIFMD but is authorised under MiFID II. If considered to be an AIF, the Issuer would also be classified as an FC under EMIR and may be required to comply with clearing obligations and/or other risk mitigation techniques (including obligations to post margin to any central clearing counterparty or market counterparty) with respect to Hedge Transactions (under the EMIR REFIT
#         all AIFs will be FCs whether or not managed by an authorised AIFM). See also “European Market Infrastructure Regulation (EMIR)” above.""",
#         {"entities": [(80, 157, "Cause"), (158, 233, "Effect"),
#                       (321, 328, "Cause"), (329, 790, "Effect")]}
#     ),
#     (
#         """If the SSPE Exemption does not apply and the Issuer is considered to be an AIF, the Collateral Manager may not be
#         able to continue to manage the Issuer’s assets, or its ability to do so may be impaired. As a result, any application of
#         the AIFMD may affect the return investors receive from their investment""",
#         {"entities": [(0, 78, "Cause"), (79, 307, "Effect")]}
#     ),
#     (
#         """The Issuer (or the Investment Manager acting on behalf of the Issuer) reserves the right to request such information as is necessary to verify the identity of a Noteholder and the source of the payment of subscription monies, or as is necessary to comply with any customer identification programs required by FinCEN and/or the SEC or any other applicable AML Requirements. If there is a delay or failure by the applicant to produce any information required for verification purposes,
#         an application for or transfer of Notes and the subscription monies relating thereto may be refused.""",
#         {"entities": [(372, 482, "Cause"), (483, 583, "Effect")]}
#     ),
#     (
#         """If there is an early redemption, the holders of the Notes will be repaid prior to the Maturity Date. Where the Notes are to be redeemed by liquidation, there can be no assurance that the Sale Proceeds realised and other available funds would permit any distribution on the Subordinated Notes after all required payments are made to the holders of the Rated Notes. In addition, an Optional Redemption could require the Investment Manager to liquidate positions more rapidly than would otherwise be desirable,
#         which could adversely affect the realised value of the Collateral Debt Obligations sold.""",
#         {"entities": [(0, 31, "Cause"), (32, 99, "Effect")]}
#     ),
#     (
#         """If at any time one or more investors that are affiliated hold a majority of any Class of Notes, it may be more difficult for other investors to take certain actions that require consent of any such Classes of Notes without their consent. For example, optional redemption and the removal of the Investment Manager for cause and appointment
#         are at the direction of Noteholders of specified percentages of Subordinated Notes and/or the Controlling Class (as applicable).""",
#         {"entities": [(0, 94, "Cause"), (95, 236, "Effect")]}
#     ),
#     (
#         """If a Hedge Counterparty is subject to a rating withdrawal or downgrade by the Rating Agencies to below the applicable Rating Requirement, there will generally be a termination event under the applicable Hedge Agreement unless, within the applicable grace period following such rating withdrawal or downgrade, such Hedge Counterparty either transfers its obligations under the applicable Hedge Agreement to a replacement counterparty with the requisite ratings, obtains a guarantee of its obligations by a guarantor with the requisite ratings, collateralises its obligations in a manner satisfactory
#         to the Rating Agencies or employs some other strategy as may be approved by the Rating Agencies.""",
#         {"entities": [(0, 136, "Cause"), (137, 217, "Effect")]}
#     ),
#     (
#         """The Issuer will depend upon the Asset Swap Counterparty to perform its obligations under any hedges. If the Asset Swap Counterparty defaults or becomes unable to perform due to insolvency or otherwise, the Issuer may not receive payments it would otherwise be entitled to from the Asset Swap Counterparty to cover its foreign exchange exposure.""",
#         {"entities": [(101, 201, "Cause"), (202, 343, "Effect")]}
#     ),
#     (
#         """In considering proposals by the examiner, it is likely that secured and unsecured creditors would form separate classes of creditors. In the case of the Issuer, if the Trustee represented the majority in number and value of claims within the secured creditor class, the Trustee would be in a position to reject any proposal not in favour of the Noteholders. The Trustee would also be entitled to argue at the relevant Irish court hearing at which the proposed scheme of arrangement is considered that the proposals are unfair and inequitable in relation to the Noteholders,
#          especially if such proposals included a writing down to the value of amounts due by the Issuer to the Noteholders.""",
#         {"entities": [(160, 266, "Cause"), (267, 356, "Effect")]}
#     ),
#     (
#         """The Issuer will depend upon the Asset Swap Counterparty to perform its obligations under any hedges. If the Asset Swap Counterparty defaults or becomes unable to perform due to insolvency or otherwise, the Issuer may not receive payments it would otherwise be entitled to from the Asset Swap Counterparty to cover its foreign exchange exposure.""",
#         {"entities": [(100, 201, "Cause"), (202, 343, "Effect")]}
#     ),
#     (
#         """“Principal Proceeds” means all amounts paid or payable into the Principal Account from time to time and, with respect to any Payment Date, means Principal Proceeds received or receivable by the Issuer during the related Due Period and any other amounts to be disbursed as Principal Proceeds on such
#         Payment Date pursuant to Condition 3(c)(ii) (Application of Principal Proceeds) or Condition 11(b) (Enforcement).""",
#         {"entities": []}
#     ),
#     (
#         """In connection with the issue and sale of the Notes, no person is authorised to give any information or to make any representation not contained in this Prospectus and, if given or made, such information or representation must not be relied upon as having been authorised by or on behalf of the Issuer, the Placement Agent, the Trustee, the Collateral Manager, the Retention Holder or the Collateral Administrator.
#         The delivery of this Prospectus at any time does not imply that the information contained in it is correct as at any time subsequent to its date.""",
#         {"entities": [(51, 183, "Cause"), (184, 412, "Effect")]}
#     )
# ]


def train_custom_ner():
    model = "logic_ner_model_100"
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
    # other_pipes = [pipe for pipe in nlp.pipe_names if pipe != 'ner']
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
    nlp.max_length = 1616300

    # Test the trained model
    # test_text = """If the Issuer becomes subject to an insolvency proceeding and the Issuer has obligations to creditors that are treated under Irish law as creditors that are senior relative to the Noteholders and other Secured Parties, the Noteholders (and other Secured Parties) may suffer losses as a result of their subordinated status during such insolvency proceedings. In particular, under Irish law, upon an insolvency of an Irish company, such as the Issuer, when applying the proceeds of assets subject to fixed security which may have been realised in the course of a liquidation or receivership, the claims of a limited category of preferential creditors will take priority over the claims of creditors holding the relevant fixed security. These preferred claims include the remuneration, costs and expenses properly incurred by any examiner of the company (which may include any borrowings made by an examiner to fund the company’s requirements for the duration of his appointment) which have been approved by the relevant Irish courts. See 7.3 “Examinership”."""
    # #test_text = """The Issuer will depend upon the Asset Swap Counterparty to perform its obligations under any hedges. If the Asset Swap Counterparty defaults or becomes unable to perform due to insolvency or otherwise, the Issuer may not receive payments it would otherwise be entitled to from the Asset Swap Counterparty to cover its foreign exchange exposure."""
    # doc = nlp(test_text)
    # print("Entities")
    # for ent in doc.ents:
    #     print("lab:", ent.label_, ent.text)

    output_dir = "logic_ner_model_100"
    if output_dir is not None:
        output_dir = Path(output_dir)
        if not output_dir.exists():
            output_dir.mkdir()
        nlp.meta['name'] = "logic_ner_model_92"  # rename model
        nlp.to_disk(output_dir)
        print("Saved model to", output_dir)

    with open('test/test_ner.txt', 'r', encoding='utf-8') as file:
        all_of_it = file.read()
        doc = nlp(all_of_it)
        displacy.serve(doc, style="ent")


if __name__ == "__main__":
    train_custom_ner()
