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


LABEL = ['Internal-Reference']

TRAIN_DATA = [
    (
        """The Notes are limited recourse obligations of the Issuer which are payable solely out of amounts received by or on behalf of the Issuer in respect of the Collateral (as defined herein). The net proceeds of the realisation of the security over the Collateral upon acceleration of the Notes following a Note Event of Default (as defined herein) may be insufficient to pay all amounts due to the Noteholders (as defined herein) after making payments to other creditors of the Issuer ranking prior thereto or pari passu therewith. In the event of a shortfall in such proceeds, the Issuer will not be obliged to pay, and the other assets (including the Issuer Profit Account and the rights of the Issuer under the Corporate Services Agreement (each as defined herein)) of the Issuer will not be available for payment of such shortfall, all claims in respect of which shall be extinguished. See Condition 4 (Security).""",
        {"entities": [(889, 911, "Internal-Reference")]}
    ),
    (
        """The Notes have not been, and will not be, registered under the United States Securities Act of 1933, as amended (the “Securities Act”) and will be offered only: (a) outside the United States to non-U.S. Persons (as defined in Regulation S under the Securities Act (“Regulation S”)); and (b) within the United States to persons and outside the United States to U.S. Persons (as such term is defined in Regulation S (“U.S. Persons”)), in each case, who are both qualified institutional buyers (as defined in Rule 144A (“Rule 144A”) under the Securities Act) in reliance on Rule 144A and qualified purchasers for the purposes of Section 3(c)(7) of the United States Investment Company Act of 1940, as amended (the “Investment Company Act”). Neither the Issuer nor the Collateral Manager will be registered under the Investment Company Act. Interests in the Notes will be subject to certain restrictions on transfer, and each purchaser of Notes offered hereby in making its purchase will be deemed to have made certain acknowledgements, representations and agreements. See “Plan of Distribution” and “Transfer Restrictions”.""",
        {"entities": [(1069, 1090, "Internal-Reference"),
                      (1096, 1118, "Internal-Reference")]}
    ),
    (
        """Notwithstanding the foregoing, there is substantial uncertainty surrounding the U.S. Risk Retention Rules. See “Risk Factors— Regulatory Initiatives—Risk Retention and Due Diligence Requirements―U.S. Risk Retention Rules”.""",
        {"entities": [(111, 220, "Internal-Reference")]}
    ),
    (
        """This Offering Circular does not constitute an offer of, or an invitation by or on behalf of, the Issuer, the Arranger, the Initial Purchaser or any of its Affiliates, the Collateral Manager, the Collateral Administrator, the Liquidity Facility Provider, the Retention Holder or any other person to subscribe for or purchase any of the Notes. The distribution of this Offering Circular and the offering of the Notes in certain jurisdictions may be restricted by law. Persons into whose possession this Offering Circular comes are required by the Issuer, the Arranger and the Initial Purchaser to inform themselves about and to observe any such restrictions. In particular, the communication constituted by this Offering Circular is directed only at persons who (i) are outside the United Kingdom and are offered and accept this Offering Circular in compliance with such restrictions or (ii) are persons falling within Article 49(2)(a) to (d) (High net worth companies, unincorporated associations etc.) of the Financial Services and Markets Act 2000 (Financial Promotion) Order 2005 or who otherwise fall within an exemption set forth in such Order so that Section 21(1) of the Financial Services and Markets Act 2000, as amended, does not apply to the Issuer (all such persons together being referred to as “relevant persons”). This communication must not be distributed to, acted on or relied on by persons who are not relevant persons. Any investment or investment activity to which this communication relates is available only to relevant persons and will be engaged in only with relevant persons. For a description of certain further restrictions on offers and sales of Notes and distribution of this Offering Circular, see “Plan of Distribution” and “Transfer Restrictions” below. The Notes are not intended to be sold and should not be sold to retail investors. See further “Plan of Distribution” of this Offering Circular for further information.""",
        {"entities": [(1728, 1749, "Internal-Reference"), (1755, 1777,
                                                           "Internal-Reference"), (1880, 1901, "Internal-Reference")]}
    ),
    (
        """2 Subordinated Notes, as applicable, and thereafter will accrue interest on such unpaid amount at the rate of interest applicable to such Notes. See Condition 6(c) (Deferral of Interest),""",
        {"entities": [(149, 185, "Internal-Reference")]}
    ),
    (
        """(a) on the Maturity Date (see Condition 7(a) (Final Redemption));""",
        {"entities": [(29, 62, "Internal-Reference")]}
    ),
    (
        """required to be satisfied on such Determination Date) (see Condition 7(c) (Mandatory Redemption upon Breach of Coverage Tests));""",
        {"entities": [(58, 124, "Internal-Reference")]}
    ),
    (
        """exclusive of any applicable VAT). See “Description of the Collateral Management Agreement”.""",
        {"entities": [(38, 89, "Internal-Reference")]}
    ),
    (
        """Bivariate Risk TableN/A See limits set out in “The Portfolio— Bivariate Risk Table”""",
        {"entities": [(46, 82, "Internal-Reference")]}
    ),
    (
        """The Rule 144A Global Certificates will bear a legend and such Rule 144A Global Certificates, or any interest therein, may not be transferred except in compliance with the transfer restrictions set out in such legend. See “Transfer Restrictions”.""",
        {"entities": [(221, 243, "Internal-Reference")]}
    ),
    (
        """Issuer. See Condition 9 (Taxation).""",
        {"entities": [(12, 33, "Internal-Reference")]}
    ),    (
        """It is intended that the Issuer will invest in loans, bonds and other financial assets with certain risk characteristics as described below and subject to the investment policies, restrictions and guidelines described in “The Portfolio”. There can be no assurance that the Issuer’s investments will be successful, that its investment objectives will be achieved, that the Noteholders will receive the full amounts payable by the Issuer under the Notes or that they will receive any return on their investment in the Notes. Prospective investors are therefore advised to review this entire Offering Circular carefully and should consider, among other things, the risk factors set out in this section before deciding whether to invest in the Notes. Except as is otherwise stated below, such risk factors are generally applicable to all Classes of Notes, although the degree of risk associated with each Class of Notes will vary in accordance with the position of such Class of Notes in the Priorities of Payments. See Condition 3(c) (Priorities of Payments). In particular, (i) payments in respect of the Class A Notes are generally higher in the Priorities of Payments than those of the other Classes of Notes; (ii) payments in respect of the Class B Notes are generally higher in the Priorities of Payments than those of the Class C Notes, the Class D """,
        {"entities": [(1015, 1053, "Internal-Reference")]}
    ),    (
        """In particular, rating actions (including, in respect of the potential downgrade of ratings applicable to Collateral Debt Obligations, such ratings being downgraded between the date of this Offering Circular and the Issue Date) may result in the Initial Ratings of any Class of Rated Notes published by the Rating Agencies being lower than is described in this Offering Circular. Furthermore, any such rating actions taken between the Issue Date and the Effective Date could result in (a) a downgrade of one of more Classes of Rated Notes from their Initial Ratings and (b) certain Collateral Quality Tests and Portfolio Profile Tests not being satisfied as at the Effective Date, resulting in an Effective Date Rating Event and following which the applicable Rated Notes will be subject to redemption in part in an amount and in the manner described under Condition 7(e) (Redemption upon Effective Date Rating Event) (see also “Considerations Relating to the Initial Investment Period”). If any rating assigned to the Notes is subject""",
        {"entities": [(927, 984, "Internal-Reference")]}
    ),    (
        """While the extent and impact of these issues are unknown, investors should be aware that they could have an adverse impact on the Issuer, its service providers, the payment of interest and repayment of principal on the Notes and therefore, the Noteholders. For further information on counterparties, see “Counterparty Risk” below.""",
        {"entities": [(303, 313, "Internal-Reference")]}
    ),    (
        """In light of the Joint Statement, the transaction described herein will initially seek to comply with subparagraphs (a) and (e) of Article 7(1) and make available the information referred to in Annex VIII of the CRA3 RTS through the Monthly Reports and the Payment Date Reports (see “Description of the Reports”).""",
        {"entities": [(282, 309, "Internal-Reference")]}
    ), (
        """(d) if any of the relevant EURIBOR benchmarks referenced in Condition 6 (Interest) is discontinued, interest on the Notes will be calculated under Condition 6(e)(i) (Floating Rate of Interest). In general, fall-back mechanisms which may govern the determination of interest rates where a benchmark rate is not available (such as those described in paragraph (c) immediately above) are not suitable for long term use. Accordingly, in the event a benchmark rate is permanently discontinued, it may be desirable to amend the applicable interest rate provisions in the affected Collateral Debt Obligation, Hedge Agreement or the Notes. Investors should note that the Issuer may, in certain circumstances, amend the Transaction Documents to modify or amend the reference rate in respect of the Notes without the consent of Noteholders, provided that the Controlling Class and the Subordinated Noteholders have, where applicable, consented within the timescale provided in Condition 14(c) (Modification and Waiver), in each case, acting by way of Ordinary Resolution. Condition 14(c)(xxxi) (Modification and Waiver) provides that the Issuer may, subject to certain conditions, enter into one or more supplemental trust deeds or make any other modification or waiver to any provision of any Transaction Document to change the applicable reference rate. See Condition 14(c) (Modification and Waiver); and""",
        {"entities": [(60, 81, "Internal-Reference"), (147, 191, "Internal-Reference"), (967, 1007,
                                                                                         "Internal-Reference"), (1062, 1108, "Internal-Reference"), (1350, 1390, "Internal-Reference")]}
    ),
    (
        """(D) it shall not knowingly take any action (save to the extent necessary for the Issuer to comply with its obligations under the Transaction Documents) which will cause its “centre of main interests” (within the meaning of Regulation (EU) No. 2015/848 of the European Parliament and of the Council of 20 May 2015 on insolvency proceedings (recast) (the “Insolvency Regulations”) to be located in any jurisdiction other than The Netherlands and will not establish any offices, branches or other permanent establishments (as defined in the Insolvency Regulations) or register as a Company in any jurisdiction other than The Netherlands;""",
        {"entities": []}
    ),
    (
        """(A) by way of a first priority security interest to a Hedge Counterparty over a Counterparty Downgrade Collateral Account and any Counterparty Downgrade Collateral deposited by such Hedge Counterparty in the relevant Counterparty Downgrade Collateral Account as security for the Issuer’s obligations to make any payment and/or delivery to the relevant Hedge Counterparty pursuant to the terms of the applicable Hedge Agreement and Condition 3(j)(iv) (Counterparty Downgrade Collateral Accounts) (subject to such security documentation as may be agreed between such third party, the Collateral Manager acting on behalf of the Issuer and the Trustee); and/or""",
        {"entities": [(431, 494, "Internal-Reference")]}
    ),
    (
        """obtain on the Issue Date, and retain after the Issue Date, any Notes for the purpose of satisfying the U.S. Risk Retention Rules nor will any party seek to satisfy any other requirements (including with respect to disclosure) set forth under the U.S. Risk Retention Rules. See "Risk Factors – Regulatory Initiatives – Risk Retention and Due Diligence Requirements – U.S. Risk Retention Rules""",
        {"entities": [(278, 390, "Internal-Reference")]}
    ),
    (
        """The Notes will be subject to Optional Redemption and Mandatory Redemption and Special Redemption, each as described herein. See Condition 7 (Redemption and Purchase).""",
        {"entities": [(128, 164, "Internal-Reference")]}
    ),
    (
        """See the section entitled “Risk Factors” herein for a discussion of certain factors to be considered in connection with an investment in the Notes.""",
        {"entities": [(25, 38, "Internal-Reference")]}
    ),
    (
        """The Notes are limited recourse obligations of the Issuer which are payable solely out of amounts received by or on behalf of the Issuer in respect of the Collateral (as defined herein). The net proceeds of the realisation of the security over the Collateral upon acceleration of the Notes following a Note Event of Default (as defined herein) may be insufficient to pay all amounts due to the Noteholders (as defined herein) after making payments to other creditors of the Issuer ranking prior thereto or pari passu therewith. In the event of a shortfall in such proceeds, the Issuer will not be obliged to pay, and the other assets (including the Issuer Profit Account and the rights of the Issuer under the Corporate Services Agreement (each as defined herein)) of the Issuer will not be available for payment of such shortfall, all claims in respect of which shall be extinguished. See Condition 4 (Security).""",
        {"entities": [(889, 910, "Internal-Reference")]}
    ),
    (
        """The Notes have not been, and will not be, registered under the United States Securities Act of 1933, as amended (the “Securities Act”) and will be offered only: (a) outside the United States to non-U.S. Persons (as defined in Regulation S under the Securities Act (“Regulation S”)); and (b) within the United States to persons and outside the United States to U.S. Persons (as such term is defined in Regulation S (“U.S. Persons”)), in each case, who are both qualified institutional buyers (as defined in Rule 144A (“Rule 144A”) under the Securities Act) in reliance on Rule 144A and qualified purchasers for the purposes of Section 3(c)(7) of the United States Investment Company Act of 1940, as amended (the “Investment Company Act”). Neither the Issuer nor the Collateral Manager will be registered under the Investment Company Act. Interests in the Notes will be subject to certain restrictions on transfer, and each purchaser of Notes offered hereby in making its purchase will be deemed to have made certain acknowledgements, representations and agreements. See “Plan of Distribution” and “Transfer Restrictions”.""",
        {"entities": [(1070, 1089, "Internal-Reference"),
                      (1097, 1117, "Internal-Reference")]}
    ),
    (
        """The Notes will be subject to Optional Redemption, Mandatory Redemption and Special Redemption, each as described herein. See Condition 7 (Redemption and Purchase).""",
        {"entities": [(125, 161, "Internal-Reference")]}
    ),
    (
        """SEE THE SECTION ENTITLED “RISK FACTORS” HEREIN FOR A DISCUSSION OF CERTAIN FACTORS TO BE CONSIDERED IN CONNECTION WITH AN INVESTMENT IN THE NOTES.""",
        {"entities": [(26, 37, "Internal-Reference")]}
    ),
    (
        """See Condition 4 (Security).""",
        {"entities": [(4, 25, "Internal-Reference")]}
    ),
    (
        """IN EACH CASE, WHO ARE BOTH QUALIFIED INSTITUTIONAL BUYERS (AS DEFINED IN RULE 144A UNDER THE SECURITIES ACT) IN RELIANCE ON RULE 144A UNDER THE SECURITIES ACT AND QUALIFIED PURCHASERS FOR THE PURPOSES OF SECTION 3(C)(7) OF THE UNITED STATES INVESTMENT COMPANY ACT OF 1940, AS AMENDED (THE “INVESTMENT COMPANY ACT”). THE ISSUER HAS NOT BEEN AND WILL NOT BE REGISTERED UNDER THE INVESTMENT COMPANY ACT. INTERESTS IN THE NOTES WILL BE SUBJECT TO CERTAIN RESTRICTIONS ON TRANSFER, AND EACH PURCHASER OF NOTES OFFERED HEREBY IN MAKING ITS PURCHASE WILL BE REQUIRED TO OR DEEMED TO HAVE MADE CERTAIN ACKNOWLEDGEMENTS, REPRESENTATIONS AND AGREEMENTS. SEE “PLAN OF DISTRIBUTION” AND “TRANSFER RESTRICTIONS”.""",
        {"entities": [(649, 668, "Internal-Reference"),
                      (676, 696, "Internal-Reference")]}
    ),
    (
        """requirements contained in subparagraphs (a) and (e) of Article 7(1) of the Securitisation Regulation through the provision of the Monthly Reports and the Payment Date Reports (see "Description of the Reports") and (B) the Investment Manager shall not be required to provide any reports, data or other information (other than such information and data necessary for completion of the Monthly Reports and the Payment Date Reports) in connection with the reporting requirements contained in subparagraphs (a) and (e) of Article 7(1) of the Securitisation Regulation to the Issuer pursuant to the Investment Management and Collateral Administration Agreement prior to the entry into force of such final disclosure templates. Once the Transparency RTS (as defined below) apply, the Loan Reports and Investor Reports (each as defined below) will be prepared in accordance with the requirements of the Transparency RTS. The Issuer, with the consent of the Investment Manager, will propose in writing to the Collateral Administrator the form, content, method of distribution and timing of such reports and other information. The Collateral Administrator shall consult with the Issuer and the Investment Manager and, if it agrees to assist the Issuer in providing such reporting on such proposed terms, shall confirm such agreement in writing to the Issuer and the Investment Manager and shall make such information (as provided to it by the Issuer (or the Investment Manager on behalf of the Issuer)) available via a website (or procure that such information is made available) currently located at https://pivot.usbank.com (or such other website as may be notified in writing by the Collateral Administrator to the Issuer, the Trustee, the Investment Manager, the Arranger, the Initial Purchaser, the Registrar, each Hedge Counterparty, the Rating Agencies, Bloomberg L.P., Intex Solutions Inc. and the Noteholders in accordance with Condition 16 (Notices)) which shall be accessible to any person (x) who certifies to the Collateral Administrator (such certification to be in the form set out in the Investment Management and Collateral Administration Agreement, which may be given electronically and upon which the Collateral Administrator shall be entitled to rely absolutely and without enquiry or liability) that it is: (i) the Issuer, (ii) the Trustee, (iii) the Investment Manager, (iv) the Arranger, (v) the Initial Purchaser, (vi) a Hedge Counterparty, (vii) a Rating Agency; (viii) Bloomberg L.P., (ix) Intex Solutions Inc., (x) a holder of a beneficial interest in any Note,""",
        {"entities": [(181, 206, "Internal-Reference")]}
    ),
    (
        """No assurance can be made as to the effect of the Volcker Rule on the ability of certain investors subject thereto to acquire or retain an interest in the Notes. Each prospective investor in the Notes should independently consider the potential impact of the Volcker Rule in respect of any investment in the Notes. Investors should conduct their own analysis to determine whether the Issuer is a “covered fund” for their purposes. See further also “Risk Factors– Regulatory Initiatives – Volcker Rule”.""",
        {"entities": [(448, 498, "Internal-Reference")]}
    ),
    (
        """See Condition 7(b)(viii) (Optional Redemption of Subordinated Notes);""",
        {"entities": [(4, 67, "Internal-Reference")]}
    ),
    (
        """(f) on any Payment Date on and after the Effective Date following a Determination Date on which a Coverage Test is not satisfied (to the extent such test is required to be satisfied on such Determination Date) (see Condition 7(c) (Mandatory Redemption upon Breach of Coverage Tests));""",
        {"entities": [(211, 281, "Internal-Reference")]}
    ),
    (
        """on each subsequent Payment Date (to the extent required) out of Interest Proceeds and thereafter out of Principal Proceeds subject to the Priorities of Payment, in each case until redeemed in full or, if earlier, until an Effective Date Rating Event is no longer continuing (see Condition 7(e) (Redemption Upon Effective Date Rating Event));""",
        {"entities": [(279, 338, "Internal-Reference")]}
    ),
    (
        """(i) following expiry of the Reinvestment Period, on each Payment Date out of Principal Proceeds transferred to the Payment Account immediately prior to the related Payment Date (see Condition 7(f) (Redemption Following Expiry of the Reinvestment Period));""",
        {"entities": [(182, 252, "Internal-Reference")]}
    )
]


def train_custom_ner():
    model = "int_reference"
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
    #     for itn in range(30):
    #         random.shuffle(TRAIN_DATA)
    #         losses = {}
    #         batches = minibatch(TRAIN_DATA, size=compounding(4., 32., 1.001))
    #         for batch in batches:
    #             texts, annotations = zip(*batch)
    #             nlp.update(texts, annotations, sgd=optimizer, drop=0.35,
    #                        losses=losses)
    #         print('Losses', losses)
    nlp.max_length = 200000000

    output_dir = "int_reference"
    if output_dir is not None:
        output_dir = Path(output_dir)
        if not output_dir.exists():
            output_dir.mkdir()
        nlp.meta['name'] = "intref"  # rename model
        nlp.to_disk(output_dir)
        print("Saved model to", output_dir)

    with open('sample/eurlex_03.txt', 'r', encoding='utf-8') as file:
        all_of_it = file.read()
        doc = nlp(all_of_it)
        displacy.serve(doc, style="ent")

    # with open('sample/eurlex_01.txt', 'r', encoding='utf-8') as file:
    #     all_of_it = file.read()
    #     doc = nlp(all_of_it)
    #     displacy.serve(doc, style="ent")

    # # Test the trained model
    # test_text = """If the Issuer becomes subject to an insolvency proceeding and the Issuer has obligations to creditors that are treated under Irish law as creditors that are senior relative to the Noteholders and other Secured Parties, the Noteholders (and other Secured Parties) may suffer losses as a result of their subordinated status during such insolvency proceedings. In particular, under Irish law, upon an insolvency of an Irish company, such as the Issuer, when applying the proceeds of assets subject to fixed security which may have been realised in the course of a liquidation or receivership, the claims of a limited category of preferential creditors will take priority over the claims of creditors holding the relevant fixed security. These preferred claims include the remuneration, costs and expenses properly incurred by any examiner of the company (which may include any borrowings made by an examiner to fund the company’s requirements for the duration of his appointment) which have been approved by the relevant Irish courts. See 7.3 “Examinership”."""
    # # test_text = """The Issuer will depend upon the Asset Swap Counterparty to perform its obligations under any hedges. If the Asset Swap Counterparty defaults or becomes unable to perform due to insolvency or otherwise, the Issuer may not receive payments it would otherwise be entitled to from the Asset Swap Counterparty to cover its foreign exchange exposure."""
    # doc = nlp(test_text)
    # print("Entities")
    # for ent in doc.ents:
    #     print("lab:", ent.label_, ent.text)


if __name__ == "__main__":
    train_custom_ner()
