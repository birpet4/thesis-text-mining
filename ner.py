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


LABEL = ['Cause']

TRAIN_DATA = [
    (
        """'""",
        {"entities": []}
    ),
    (
        """Notes """,
        {"entities": []}
    ),
    (
        """the Issuer""",
        {"entities": []}
    ),
    (
        """If investment by “banking entities” in the Notes of any Class is prohibited or restricted by the Volcker Rule, this could impair the marketability and liquidity of such Notes.""",
        {"entities": [(0, 109, "Cause")]}
    ),
    (
        """Information as to placement within the United States The Notes of each Class offered pursuant to an exemption from registration requirements under Rule 144A under the Securities Act (“Rule 144A”) (the “Rule 144A Notes”) will be sold only to “qualified institutional buyers” (as defined in Rule 144A) (“QIBs”) that are also “qualified purchasers” for purposes of Section 3(c)(7) of the Investment Company Act (“QPs”). Rule 144A Notes of each Class (other than, in certain circumstances, the Class E Notes, the Class F Notes, the Class Z Notes and the Subordinated Notes) will each be represented on issue by beneficial interests in one or more permanent global certificates of such Class (each, a “Rule 144A Global Certificate” and together, the “Rule 144A Global Certificates”) or may in some cases be represented by definitive certificates of such Class (each a “Rule 144A Definitive Certificate” and, together, the “Rule 144A Definitive Certificates”), in each case in fully registered form, without interest coupons or principal receipts, which will be deposited on or about the Issue Date with, and registered in the name of, a nominee of a common depositary for Euroclear Bank S.A./N.V., as operator of the Euroclear System (“Euroclear”) and Clearstream Banking, société anonyme (“Clearstream, Luxembourg”), or, in the case of Rule 144A Definitive Certificates, the registered holder thereof. The Notes of each Class (other than in certain circumstances, the Class E Notes, the Class F Notes, the Class Z Notes and the Subordinated Notes) sold to non-“U.S. Persons” in an “offshore transaction”, as such terms are defined in, and in accordance with Regulation S (“Regulation S”) under the Securities Act (the “Regulation S Notes”) will each be represented on issue by beneficial interests in one or more permanent global certificates of such Class (each, a “Regulation S Global Certificate” and together, the “Regulation S Global Certificates”) or may in some cases be represented by definitive certificates of such Class (each a “Regulation S Definitive Certificate” and, together, the “Regulation S Definitive Certificates”), in each case in fully registered form, without interest coupons or principal receipts, which will be deposited on or about the Issue Date with, and registered in the name of, a nominee of a common depositary for Euroclear and Clearstream, Luxembourg or, in the case of Regulation S Definitive Certificates, the registered holder thereof. Neither U.S. Persons nor U.S. residents (as determined for the purposes of the Investment Company Act) (“U.S. Residents”) may hold an interest in a Regulation S Global Certificate or a Regulation S Definitive Certificate.""",
        {"entities": []}
    ),
    (
        """UPON OR ENDORSED THE MERITS OF THIS OFFERING OR THE ACCURACY OR ADEQUACY OF THIS DOCUMENT. ANY REPRESENTATION TO THE CONTRARY IS A CRIMINAL OFFENCE. This Offering Circular has been prepared by the Issuer solely for use in connection with the offering of the Notes described herein (the “Offering”). Each of the Issuer and the Initial Purchaser reserves the right to reject any offer to purchase Notes in whole or in part for any reason, or to sell less than the stated initial principal amount of any Class of Notes offered hereby. This Offering Circular is personal to each offeree to whom it has been delivered by the Issuer, the Initial Purchaser or any Affiliate thereof and does not constitute an offer to any other person or to the public generally to subscribe for or otherwise acquire the Notes. Distribution of this Offering Circular to any persons other than the offeree and those persons, if any, retained to advise such offeree with respect thereto is unauthorised and any disclosure of any of its contents, without the prior written consent of the Issuer, is prohibited. Any reproduction or distribution of this Offering Circular in whole or in part and any disclosure of its contents or use of any information herein for any purpose other than considering an investment in the securities offered herein is prohibited. Notwithstanding anything to the contrary herein, each recipient (and each employee, representative, or other agent of such recipient) may disclose to any and all persons, without limitation of any kind, the U.S. federal, state, and local tax treatment of the Issuer, the Notes, or the transactions referenced herein and all materials of any kind (including opinions or other U.S. tax analyses) relating to such U.S. federal, state, and local tax treatment and that may be relevant to understanding such U.S. federal, state, and local tax treatment. Available Information To permit compliance with the Securities Act in connection with the sale of the Notes in reliance on Rule 144A, the Issuer will be required under the Trust Deed to furnish upon request to a holder or beneficial owner who is a QIB of a Note sold in reliance on Rule 144A or a prospective investor who is a QIB designated by such holder or beneficial owner the information required to be delivered under Rule 144A(d)(4) under the Securities Act if at the time of the request the Issuer is neither a reporting company under Section 13 or Section 15(d) of the United States Securities Exchange Act of 1934, as amended, nor exempt from reporting pursuant to Rule 12g3-2(b) under the Exchange Act. All information made available by the Issuer pursuant to the terms of this paragraph may also be obtained during usual business hours free of charge at the office of the Principal Paying Agent.""",
        {"entities": []}
    ),
    (
        """IF THE COLLATERAL MANAGER IS REQUIRED TO REGISTER AS A CPO OR A CTA, IT WILL BECOME SUBJECT TO NUMEROUS REPORTING AND OTHER REQUIREMENTS AND IT IS EXPECTED THAT IT WILL INCUR SIGNIFICANT ADDITIONAL COSTS IN COMPLYING WITH ITS OBLIGATIONS AS A REGISTERED CPO OR CTA, WHICH COSTS ARE EXPECTED TO BE PASSED ON TO THE ISSUER AND MAY ADVERSELY AFFECT THE ISSUER’S ABILITY TO MAKE PAYMENT ON THE NOTES. Applicability of EU Law in the UK THE UK WITHDREW FROM AND CEASED TO BE A MEMBER STATE OF THE EU AT 11:00 P.M. GMT ON 31 JANUARY 2020. THE NEGOTIATED WITHDRAWAL AGREEMENT ENTERED INTO BETWEEN THE UK AND THE EU PROVIDES FOR A TRANSITION PERIOD, COMMENCING ON 31 JANUARY 2020 AND ENDING AT 11.00 P.M. GMT ON 31 DECEMBER 2020 (SUCH PERIOD, THE “TRANSITION PERIOD”). UNLESS OTHERWISE PROVIDED IN THE NEGOTIATED WITHDRAWAL AGREEMENT, EU LAW WILL BE APPLICABLE TO AND IN THE UK DURING THE TRANSITION PERIOD. ACCORDINGLY, DURING THE TRANSITION PERIOD ANY REFERENCES IN THIS OFFERING CIRCULAR TO THE “EU” AND ITS “MEMBER STATES” IN THE CONTEXT OF EU LEGISLATION AND THE APPLICATION THEREOF SHALL BE INTERPRETED SO AS TO INCLUDE THE UK (EXCEPT WHERE EXPRESSLY INDICATED OTHERWISE). MIFID II Product Governance Solely for the purposes of each manufacturer’s product approval process, the target market assessment in respect of the Notes has led to the conclusion that: (i) the target market for the Notes is eligible counterparties and professional clients only, each as defined in Directive 2014/65/EU (as amended, “MiFID II”); and (ii) all channels for distribution of the Notes to eligible counterparties and professional clients are appropriate. Any person subsequently offering, selling or recommending the Notes (a “distributor”) should take into consideration the manufacturer target market assessment; however, a distributor subject to MiFID II is responsible for undertaking its own target market assessment in respect of the Notes (by either adopting or refining the manufacturer target market assessment) and determining appropriate distribution channels. PRIIPs Regulation and Prospectus Regulation The Notes are not intended to be offered, sold or otherwise made available to and should not be offered, sold or otherwise made available to any retail investor in the European Economic Area (“EEA”) or in the United Kingdom (the “UK”). For these purposes, a retail investor means a person who is one (or more) of: (i) a retail client as defined in point (11) of Article 4(1) of MiFID II; or (ii) a customer within the meaning of Directive (EU) 2016/97, where that customer would not qualify as a professional client as defined in point (10) of Article 4(1) of MiFID II; or (iii) not a qualified investor within the meaning of Article 2(e) of the Prospectus Regulation. Consequently no key information document required by Regulation (EU) No 1286/2014 (as amended, the “PRIIPs Regulation”) for offering or selling the Notes or otherwise making them available to retail investors in the EEA or in the UK has been prepared and therefore offering or selling the Notes or otherwise making them available to any retail investor in the EEA or in the UK may be unlawful under the PRIIPS Regulation.""",
        {"entities": [(0, 67, "Cause")]}
    ),
    (
        """4 The Initial Purchaser and the Issuer may offer the Notes at prices as may be negotiated at the time of sale , which may vary among different purchasers and may be different from the issue price of the Notes.""",
        {"entities": []}
    ),
    (
        """Management Fee on each Payment Date on which the Incentive Collateral Management Fee IRR Threshold has been met or surpassed, equal to 20 per cent. of any Interest Proceeds and Principal Proceeds that would otherwise be available to distribute to the Subordinated Noteholders in accordance with the Priorities of Payment. See “Description of the Collateral Management and Administration Agreement — Compensation of the Collateral Manager”. Security for the Notes""",
        {"entities": []}
    ),
    (
        """will """,
        {"entities": []}
    ),
    (
        """At this time, the full consequences of such withdrawal are not clear. In particular, there is uncertainty as to the final trade arrangements to be put in place following the expiry of the Transition Period (as defined below). Investors should be aware that the Issuer’s risk profile may be materially affected by this uncertainty which might also have an adverse impact on the Portfolio and the Issuer’s business, financial condition, results of operations and prospects and could therefore also be materially detrimental to Noteholders""",
        {"entities": []}
    ),
    (
        """Any such potential adverse economic conditions may also affect the ability of the obligors to make payment under the Collateral Obligations which in turn may adversely affect the ability of the Issuer to pay interest and repay principal to the Noteholders.""",
        {"entities": []}
    ),
    (
        """If, at the end of the Transition Period, the UK were no longer within the scope of EU Directive 2014/65/EU and EU Regulation 600/2014/EU on Markets in Financial Instruments (collectively referred to as “MiFID II”) and an alternative passporting regime or third country recognition of the UK is not in place, then (a) a UK manager such as the Collateral Manager may be unable to continue to provide collateral management services to the Issuer in reliance upon the passporting of relevant regulated services within the EU on a cross-border basis provided for under MiFID II and (b) the Collateral Manager may not be able to continue to act as Retention Holder to the extent it was required to hold the retention solely as “sponsor” in accordance with the EU Retention Requirements (even if the Collateral Manager were to remain subject to UK financial services regulation), however, we note that the Collateral Manager intends to act as an “originator” retention holder for the purposes of this transaction. As of the date hereof, an “originator” retention holder is not required to be regulated in the EU in order to act in such capacity. In connection with the issue and sale of the Notes, no person is authorised to give any information or to make any representation not contained in this Offering Circular and, if given or made, such information or representation must not be relied upon as having been authorised by or on behalf of the Issuer, the Arranger, the Initial Purchaser, the Trustee, the Collateral Manager, the Retention Holder, the Liquidity Facility Provider or the Collateral Administrator. The delivery of this Offering Circular at any time does not imply that the information contained in it is correct as at any time subsequent to its date.""",
        {"entities": [(0, 306, "Cause")]}
    ),
    (
        """If the Collateral Administrator does not agree on the terms of reporting or, in the reasonable opinion of the Issuer (acting on the advice of the Collateral Manager), the Collateral Administrator is or will be unable or unwilling to provide such reporting, the Issuer (with the consent of the Collateral Manager) shall be entitled to appoint another entity to make the relevant information available for the purposes of Article 7 (Transparency requirements for originators, sponsors and SSPEs) of the Securitisation Regulation.""",
        {"entities": [(0, 165, "Cause")]}
    ),
    (
        """If the Issuer is deemed to be a “covered fund”, this could significantly impair the marketability and liquidity of the Refinancing Notes.""",
        {"entities": [(0, 46, "Cause")]}
    ),
    (
        """IF THE COLLATERAL MANAGER IS REQUIRED TO REGISTER AS A CPO/CTA, IT WILL BECOME SUBJECT TO NUMEROUS REPORTING AND OTHER REQUIREMENTS AND IT IS EXPECTED THAT IT WILL INCUR SIGNIFICANT ADDITIONAL COSTS IN COMPLYING WITH ITS OBLIGATIONS AS A REGISTERED CPO, WHICH COSTS ARE EXPECTED TO BE PASSED ON TO THE ISSUER AND MAY ADVERSELY AFFECT THE ISSUER’S ABILITY TO MAKE PAYMENT ON THE NOTES.""",
        {"entities": [(0, 62, "Cause")]}
    ),
    (
        """To permit compliance with the Securities Act in connection with the sale of the Refinancing Notes in reliance on Rule 144A, the Issuer will be required under the Trust Deed to furnish upon request to a holder or beneficial owner who is a QIB of a Note sold in reliance on Rule 144A or a prospective investor who is a QIB designated by such holder or beneficial owner the information required to be delivered under Rule 144A(d)(4) under the Securities Act if at the time of the request the Issuer is neither a reporting company under Section 13 or Section 15(d) of the United States Securities Exchange Act of 1934, as amended, nor exempt from reporting pursuant to Rule 12g3- 2(b) under the Exchange Act.""",
        {"entities": []}
    ),
    (
        """If the Collateral Administrator does not agree on the terms of reporting or, in the reasonable opinion of the Issuer (acting on the advice of the Collateral Manager), the Collateral Administrator is or will be unable or unwilling to provide such reporting, the Issuer (with the consent of the Collateral Manager) shall be entitled to appoint another entity to make the relevant information available for the purposes of Article 7 (Transparency requirements for originators, sponsors and SSPEs) of the Securitisation Regulation.""",
        {"entities": [(0, 255, "Cause")]}
    ),
    (
        """The Collateral Manager does not have any obligation to consider or take any Retention Cure Action and, if the Collateral Manager determines not to take any Retention Cure Action, it may no longer be eligible to act as the Retention Holder pursuant to the EU Retention and Transparency Requirements (and for the avoidance of doubt, even if a Retention Cure Action is taken, it is not certain whether such action would result in compliance with the EU Retention and Transparency Requirements).""",
        {"entities": [(103, 177, "Cause")]}
    ),
    (
        """If the Collateral Administrator does not agree on the terms of reporting or, in the reasonable opinion of the Issuer (acting on the advice of the Collateral Manager), the Collateral Administrator is or will be unable or unwilling to provide such reporting, the Issuer (with the consent of the Collateral Manager) shall be entitled to appoint another entity to make the relevant information available for the purposes of Article 7 (Transparency requirements for originators, sponsors and SSPEs) of the Securitisation Regulation.""",
        {"entities": [(0, 165, "Cause")]}
    ),
    (
        """However, the SEC has indicated that it is continuing to consider amendments that were proposed with respect to Regulation AB but not adopted, and that further amendments may be forthcoming in the future. If such amendments are made to Regulation AB in the future, they may place additional requirements and expenses on the Issuer in the event of the issuance and sale of any additional notes, which expenses may reduce the amounts available for distribution to the Noteholders.""",
        {"entities": [(204, 262, "Cause")]}
    ),
    (
        """Moreover, if the Priorities of Payment are the subject of litigation in any jurisdiction outside England and Wales, in particular in the United States of America, and such litigation results in a conflicting judgment in respect of the binding nature of the Priorities of Payment, it is possible that termination payments due to the Hedge Counterparties would not be subordinated as envisaged by the Priority of Payments and as a result, the Issuer’s ability to repay the Noteholders in full may be adversely affected.""",
        {"entities": [(10, 278, "Cause")]}
    ),
    (
        """If the Issuer is considered to be a member of a “group” (as defined in EMIR) (which may, for example, potentially be the case if the Issuer is consolidated by a Noteholder as a result of such Noteholder’s holding of a significant proportion of the Subordinated Notes) and if the aggregate notional value of OTC derivative contracts entered into by the Issuer and any non- financial entities within such group exceeds the applicable thresholds (excluding eligible hedging transactions), the Issuer would be subject to the clearing obligation, or if the relevant contract is not a type required to be cleared, to the risk mitigation obligations, including the margin requirement.""",
        {"entities": [(0, 266, "Cause"), (272, 484, "Cause")]}
    ),
    (
        """If the Issuer exceeds the applicable thresholds and its swaps become subject to mandatory clearing, this may also lead to a termination of the Hedge Agreements.""",
        {"entities": [(0, 98, "Cause")]}
    ),
    (
        """If the Issuer becomes subject to the clearing obligation or to the margin requirement, it is unlikely that it would be able to comply with such requirements, which would adversely affect the Issuer’s ability to enter into Hedge Transactions or significantly increase the cost thereof, negatively affecting the Issuer’s ability to acquire Non-Euro Obligations and/or hedge its interest rate risk.""",
        {"entities": [(0, 85, "Cause")]}
    ),
    (
        """If the Issuer were to be considered to be an AIF within the meaning in AIFMD, it would need to be managed by a manager authorised under AIFMD (an “AIFM”).""",
        {"entities": [(0, 76, "Cause")]}
    ),
    (
        """If considered to be an AIF managed by an AIFM, the Issuer would also be classified as an FC under EMIR and may be required to comply with clearing obligations and/or other risk mitigation techniques (including obligations to post margin to any central clearing counterparty or market counterparty) with respect to Hedge Transactions (under the EMIR Refit, all AIFs will be FCs whether or not managed by an authorised AIFM).""",
        {"entities": [(0, 45, "Cause")]}
    ),
    (
        """If the SSPE Exemption does not apply and the Issuer is considered to be an AIF, the Collateral Manager may not be able to continue to manage the Issuer’s assets, or its ability to do so may be impaired.""",
        {"entities": [(0, 78, "Cause")]}
    ),
    (
        """If such amendments are made to Regulation AB in the future, they may place additional requirements and expenses on the Issuer in the event of the issuance and sale of any additional notes, which expenses may reduce the amounts available for distribution to the Noteholders.""",
        {"entities": [(0, 58, "Cause")]}
    ),
    (
        """If the Collateral Manager elects to file for a registration exemption under CFTC Rule 4.13(a)(3), then unlike a CFTC-registered CPO, the Collateral Manager would not be required to deliver a CFTC-mandated disclosure document or a certified annual report to investors, or otherwise comply with the requirements applicable to CFTC-registered CPOs and CTAs.""",
        {"entities": [(0, 131, "Cause")]}
    ),
    (
        """Further, if the Collateral Manager determines that additional Hedge Transactions should be entered into by the Issuer in excess of the trading limitations set forth in any applicable exemption from registration as a CPO and/or a CTA, the Collateral Manager may elect to withdraw its exemption from registration and instead register with the CFTC as the Issuer’s CPO and/or CTA. The costs of obtaining and maintaining these registrations and the related compliance obligations may be paid by the Issuer as Administrative Expenses.""",
        {"entities": [(9, 232, "Cause")]}
    ),
    (
        """If the Issuer is deemed to be a “covered fund” the provisions of the Volcker Rule and its related regulatory provisions, will severely limit the ability of “banking entities” to hold an “ownership interest” in the Issuer or enter into certain credit related financial transactions with the Issuer.""",
        {"entities": [(0, 119, "Cause")]}
    ),
    (
        """If investment by “banking entities” in the Refinancing Notes of any Class is prohibited or restricted by the Volcker Rule, this could impair the marketability and liquidity of such Refinancing Notes.""",
        {"entities": [(0, 121, "Cause")]}
    ),
    (
        """Moreover, if the Priorities of Payment are the subject of litigation in any jurisdiction outside England and Wales, in particular in the United States of America, and such litigation results in a conflicting judgment in respect of the binding nature of the Priorities of Payment, it is possible that termination payments due to the Hedge Counterparties would not be subordinated as envisaged by the Priority of Payments and as a result, the Issuer’s ability to repay the Noteholders in full may be adversely affected.""",
        {"entities": [(10, 278, "Cause")]}
    ),
    (
        """It is possible that the LIBOR administrator, ICE Benchmark Administration Limited, and the panel banks could continue to produce LIBOR on the current basis after 2021, if they are willing and able to do so. However, the survival of LIBOR in its current form, or at all, is not guaranteed after 2021.""",
        {"entities": [(168, 298, "Cause")]}
    ),
    (
        """If LIBOR does not survive in its current form or at all, this could adversely affect the value of, and amounts payable under, any Collateral Obligations which pay interest calculated with reference to LIBOR and therefore reduce amounts which may be available to the Issuer to pay Noteholders.""",
        {"entities": [(0, 55, "Cause")]}
    ),
    (
        """Benchmarks such as EURIBOR or LIBOR may be discontinued if they do not comply with the requirements of the Benchmarks Regulation, or if the administrator of the benchmark either fails to apply for authorisation or is refused authorisation by its home regulator.""",
        {"entities": [(56, 260, "Cause")]}
    ),
    (
        """If a relevant institution enters into an arrangement with the Issuer and is deemed likely to fail in the circumstances identified in the BRRD, the relevant Resolution Authority may employ such tools and powers in order to intervene in the relevant institution’s failure (including in the case of derivatives transactions, powers to close-out such transactions or suspend any rights to close-out such transactions).""",
        {"entities": [(0, 141, "Cause")]}
    ),
    (
        """If the relevant Resolution Authority decides to “bail-in” the liabilities of a relevant institution, then subject to certain exceptions set out in the BRRD, the liabilities of such relevant institution could, among other things, be reduced, converted or extinguished in full.""",
        {"entities": [(0, 100, "Cause")]}
    ),
    (
        """If a Member State outside the Euro zone (such as the UK) has chosen not to participate in the bank single supervisory mechanism, relevant institutions established in such Member State will not be subject to the SRM Regulation, but to the application of the BRRD by the Resolution Authorities.""",
        {"entities": [(0, 127, "Cause")]}
    ),
    (
        """If a Covered Entity enters into a contract with the Issuer that is subject to the QFC Stay Rules, the Covered Entity will be responsible for ensuring that such QFC complies with the QFC Stay Rules. As a result of the application of such rules, the Issuer may be required to accept limitations in its insolvency-related default rights against the Covered Entity.""",
        {"entities": [(0, 96, "Cause")]}
    ),
    (
        """If the Issuer’s COMI is not located in The Netherlands and is held to be in a different jurisdiction within the European Union, Dutch insolvency proceedings would not be applicable to the Issuer.""",
        {"entities": [(0, 126, "Cause")]}
    ),
    (
        """If a Refinancing is obtained meeting the requirements of the Trust Deed, the Issuer may amend the Trust Deed and the Trustee shall concur with such amendments to the Trust Deed and no further consent for such amendments shall be required from the holders of the Subordinated Notes.""",
        {"entities": [(0, 71, "Cause")]}
    ),
    (
        """The Collateral Manager or the Retention Holder may also cause the Issuer to redeem the Rated Notes in whole from Sale Proceeds on any Business Day falling on or after the expiry of the Non-Call Period, if the Collateral Principal Amount is less than 15 per cent. of the Target Par Amount.""",
        {"entities": [(201, 287, "Cause")]}
    ),
    (
        """Each Noteholder will agree, and each beneficial owner of Notes will be deemed to agree, pursuant to the Trust Deed, that it will be subject to non-petition covenants. If such provision failed to be enforceable under applicable bankruptcy laws, and a winding-up (or similar) petition was presented in respect of the Issuer, then the presentation of such a petition could (subject to certain conditions) result in one or more payments on the Notes made during the period prior to such presentation being deemed to be preferential transfers subject to avoidance by the bankruptcy trustee or similar official exercising authority with respect to the Issuer’s bankruptcy estate.""",
        {"entities": [(167, 321, "Cause")]}
    ),
    (
        """If the holders of the Controlling Class do not have an interest in the outcome of the conflict, the Trustee shall give priority to the interests of the most senior Class of Notes Outstanding.""",
        {'entities':  [(0, 94, "Cause")]}
    ),
    (
        """If the relevant EURIBOR screen rate does not appear, or the relevant page is unavailable, in the manner described in Condition 6(e)(i) (Floating Rate of Interest) there can be no guarantee that the Collateral Manager will be able to select four Reference Banks to provide quotations, in order to determine any Rate of Interest in respect of the Notes.""",
        {"entities": [(0, 88, "Cause")]}
    ),
    (
        """If a EURIBOR screen rate does not appear, or the relevant page is unavailable, and the Collateral Manager is unable to select Reference Banks to provide quotations in the manner described in Condition 6(e)(i) (Floating Rate of Interest), the relevant Rate of Interest in respect of such Payment Date shall be determined, pursuant to Condition 6(e)(i) (Floating Rate of Interest), as the Rate of Interest in effect as at the immediately preceding Accrual Period that was determined by reference to a EURIBOR screen rate or through quotations provided by four Reference Banks provided that, in respect of any Accrual Period during which a Frequency Switch Event occurs, the relevant Rate of Interest shall be calculated using the offered rate for six month Euro deposits using the rate available as at the previous Interest Determination Date.""",
        {"entities": [(0, 236, "Cause")]}
    ),
    (
        """If a rating initially assigned to any of the Notes is subsequently lowered for any reason, no person or entity is required to provide any additional support or credit enhancement with respect to any such Notes and the market value of such Notes is likely to be adversely affected.""",
        {"entities": [(0, 89, "Cause")]}
    ),
    (
        """If the Transaction Documents require that written confirmation from a Rating Agency be obtained before certain actions may be taken and an applicable Rating Agency is unwilling to provide the required confirmation, it may be impossible to effect such action, which could result in losses being realised by the Issuer and, indirectly, by holders of the Refinancing Notes.""",
        {"entities": [(0, 213, "Cause")]}
    ),
    (
        """If a Rating Agency announces or informs the Trustee, the Collateral Manager or the Issuer that confirmation from such Rating Agency is not required for a certain action or that its practice is to not give such confirmations for certain types of actions, the requirement for confirmation from such Rating Agency will not apply.""",
        {"entities": [(0, 51, "Cause")]}
    ),
    (
        """If the arranger does not comply with its undertakings to any Rating Agency with respect to this transaction, such Rating Agency may withdraw its ratings of the Rated Notes. In such case, the withdrawal of ratings by any Rating Agency may adversely affect the price or transferability of the Rated Notes and may adversely affect any beneficial owner that relies on ratings of securities for regulatory or other compliance purposes.""",
        {"entities": [(0, 107, "Cause")]}
    ),
    (
        """If the Issuer or any third party that provides due diligence services to the Issuer does not comply with its obligations under Rule 17g-10, the Rating Agencies may withdraw (or fail to confirm) their ratings of the Rated Notes. In such case, the price or transferability of the Notes (and any beneficial owner of the Rated Notes that relies on ratings of securities for regulatory or other compliance purposes) may be adversely affected.""",
        {"entities": [(0, 138, "Cause")]}
    ),
    (
        """If any withholding tax or deduction for tax is imposed on payments of principal or interest on the Notes (including FATCA), the holders of the Notes will not be entitled to receive grossed-up amounts to compensate for such withholding tax and no Note Event of Default shall occur as a result of any such withholding or deduction.""",
        {"entities": [(0, 122, "Cause")]}
    ),
    (
        """If a meeting of Noteholders is called to consider a Resolution, determination as to whether the requisite number of Notes has been voted in favour of such Resolution will be determined by reference to the percentage which the aggregate Principal Amount Outstanding of Notes held or represented by any person or persons who vote in favour of such Resolution represents of the aggregate Principal Amount Outstanding of all applicable Notes which are represented at such meeting and are voted and not the aggregate Principal Amount Outstanding of all such Notes held or represented by any person or persons entitled to vote at such meeting.""",
        {"entities": [(0, 62, "Cause")]}
    ),
    (
        """Similarly, investors in the other Classes of Notes should be aware that if there are no Notes in their Class that would be entitled to vote and be counted in respect of a CM Removal Resolution or CM Replacement Resolution such right shall pass to a more junior Class of Notes.""",
        {"entities": [(72, 275, "Cause")]}
    ),
    (
        """If at any time one or more investors that are affiliated hold a majority of any Class of Notes, it may be more difficult for other investors to take certain actions that require consent of any such Classes of Notes without their consent.""",
        {"entities": [(0, 94, "Cause")]}
    ),
    (
        """If a Note Event of Default occurs and is continuing, the Trustee may, at its discretion, and shall, at the request of the Controlling Class acting by way of Ordinary Resolution (subject, in each case, to the Trustee being indemnified and/or secured and/or prefunded to its satisfaction against all liabilities, proceedings, claims and demands to which it may thereby become liable and all costs, charges and expenses which may be incurred by it in connection therewith), give notice to the Issuer and the Collateral Manager that all the Notes are immediately due and repayable, provided that following the occurrence of a Note Event of Default described in Condition 10(a)(vi) (Insolvency Proceedings) such notice shall be deemed to have been given and all the Notes shall automatically become immediately due and payable.""",
        {"entities": [(0, 51, "Cause")]}
    ),
    (
        """At any time after the Notes become due and repayable and the security under the Trust Deed becomes enforceable, the Trustee may, at its discretion (subject to being indemnified and/or secured and/or prefunded to its satisfaction), and shall, if so directed by the Controlling Class acting by Extraordinary Resolution, take Enforcement Action (as defined in the Conditions) in respect of the security over the Collateral provided that no such Enforcement Action may be taken by the Trustee unless: (A) it determines that the anticipated proceeds realised from such Enforcement Action (after deducting and allowing for any expenses properly incurred in connection therewith) would be sufficient to discharge in full all amounts due and payable in respect of all Classes of Notes other than the Subordinated Notes (including, without limitation, Deferred Interest on the Class C Notes, the Class D Notes, the Class E Notes and the Class F Notes) and all amounts payable in priority to the Subordinated Notes pursuant to the Post-Acceleration Priority of Payments or (B) otherwise, in the case of a Note Event of Default specified in sub-paragraphs (i), (ii), (iv) or (vi) of Condition 10 (Events of Default) the Controlling Class acting by way of Extraordinary Resolution (and no other Class of Notes) may direct the Trustee to take Enforcement Action without regard to any other Note Event of Default which has occurred prior to, contemporaneously or subsequent to such Note Event of Default.""",
        {"entities": [(242, 316, "Cause")]}
    ),
    (
        """Under a regulation of the U.S. Department of Labor, as modified by Section 3(42) of ERISA, if certain employee benefit plans or other retirement arrangements subject to the fiduciary responsibility provisions of Title I of the U.S. Employee Retirement Income Security Act of 1974, as amended, (“ERISA”) or Section 4975 of the U.S. Internal Revenue Code of 1986, as amended, (the “Code”) or entities whose underlying assets are treated as assets of such plans or arrangements (collectively, “Plans”) invest in a Class of Notes that is treated as equity under the regulation (which could include the Class E Notes, the Class F Notes and the Subordinated Notes), the assets of the Issuer could be considered to be assets of such Plans. In addition, certain of the transactions contemplated under such Notes could be considered “prohibited transactions” under Section 406 of ERISA or Section 4975 of the Code. See the section entitled “Certain ERISA Considerations” below.""",
        {"entities": [(91, 658, "Cause")]}
    ),
    (
        """U.S. person as defined under Regulation S under the Securities Act (a “U.S. Person”) and is not both a QIB and a QP at the time it acquires an interest in a Rule 144A Note (any such person, a “Non-Permitted Noteholder”), the Issuer shall, promptly after determination that such person is a Non-Permitted Noteholder by the Issuer, send notice to such Non-Permitted Noteholder demanding that such holder transfer its interest outside the United States to a non-U.S. Person or within the United States to a U.S. Person that is a QIB/QP within 30 days of the date of such notice. If such holder fails to effect the transfer required within such 30-day period, (a) the Issuer or the Collateral Manager on its behalf and at the expense of the Issuer shall cause such Rule 144A Notes to be transferred in a sale to a person or entity that certifies to the Issuer, in connection with such transfer, that such person or entity either is not a U.S. Person or is a QIB/QP and (b) pending such transfer, no further payments will be made in respect of such Rule 144A Notes.""",
        {"entities": [(576, 654, "Cause")]}
    ),
    (
        """When the Issuer holds a Participation in a loan it generally will not have the right to participate directly in any vote to waive enforcement of any covenants breached by a borrower.""",
        {"entities": [(0, 46, "Cause")]}
    ),
    (
        """When CVC Credit Partners is required to take action with respect to a security or loan investment held by a client, it is CVC Credit Partners’ policy to act in the best interest of the holder of the investment with respect to which action is being taken, even though such actions may be to the detriment of others invested in the company’s capital structure.""",
        {"entities": [(0, 114, "Cause")]}
    ),
    (
        """“Aggregate Principal Balance” means the aggregate of the Principal Balances of all the Collateral Debt Obligations and when used with respect to some portion of the Collateral Debt Obligations, means the aggregate of such portion of the Principal Balances of such Collateral Debt Obligations, in each case, as at the date of determination.""",
        {"entities": [(119, 192, "Cause")]}
    )
]
# TRAIN_DATA = [
# #     # (
# #     #     """The credit rating of a country affects the ratings of entities operating in its territory,
# #     #     and in particular the ratings of financial institutions. Accordingly, such downgrades of the UK’s sovereign credit
# #     #     rating and any further downgrade action may trigger downgrades in respect of parties to the Transaction Documents.
# #     #     If a counterparty no longer satisfies the relevant Rating Requirement, the Transaction Documents may require
# #     #     that such counterparty be replaced with an entity that satisfies the relevant Rating Requirement.
# #     #     If rating downgrades are widespread, it may become difficult or impossible to replace counterparties with entities that satisfy the relevant
# #     #     Rating Requirement.""",
# #     #     {"entities": [(345, 414, "Cause"), (415, 558, "Effect"),
# #     #                   (568, 603, "Cause"), (604, 735, "Effect")]}
# #     # ),
# #     # (
# #     #     """In Europe, the U.S. and elsewhere there has been, and there continues to be increased political and regulatory scrutiny of banks,
# #     #     financial institutions, “shadow banking entities” and the asset-backed securities industry. This has resulted in a raft of measures
# #     #     for increased regulation which are currently at various stages of implementation and which may have an adverse impact on the regulatory
# #     #     capital charge to certain investors in securitisation exposures and/or the incentives for certain investors to hold or trade asset-backed
# #     #     securities, and may thereby affect the liquidity of such securities.""",
# #     #     {"entities": []}
# #     # ),
# #     # (
# #     #     """If any determination is made that this transaction is subject to the U.S. Risk Retention Rules, the Collateral Manager may fail to comply
# #     #     (or not be able to comply) with the U.S. Risk Retention Rules, which may have a material adverse effect on the Collateral Manager, the Issuer
# #     #     and/or the market value and/or liquidity of the Notes.""",
# #     #     {"entities": [(0, 94, "Cause"), (95, 349, "Effect")]}
# #     # ),
# #     # (
# #     #     """IFMD introduced authorisation and regulatory requirements for managers of AIFs. If the Issuer were to be considered to be an AIF within the meaning in AIFMD, it would need to be managed by a manager authorised under AIFMD (an “AIFM”). The Collateral Manager is not authorised under AIFMD but is authorised under MiFID II. If considered to be an AIF, the Issuer would also be classified as an FC under EMIR and may be required to comply with clearing obligations and/or other risk mitigation techniques (including obligations to post margin to any central clearing counterparty or market counterparty) with respect to Hedge Transactions (under the EMIR REFIT
# #     #     all AIFs will be FCs whether or not managed by an authorised AIFM). See also “European Market Infrastructure Regulation (EMIR)” above.""",
# #     #     {"entities": [(80, 156, "Cause"), (157, 233, "Effect"),
# #     #                   (322, 348, "Cause"), (349, 732, "Effect")]}
# #     # ),
# #     # (
# #     #     """If the SSPE Exemption does not apply and the Issuer is considered to be an AIF, the Collateral Manager may not be
# #     #     able to continue to manage the Issuer's assets, or its ability to do so may be impaired. As a result, any application of
# #     #     the AIFMD may affect the return investors receive from their investment""",
# #     #     {"entities": [(0, 78, "Cause"), (79, 209, "Effect")]}
# #     # ),
# #     # (
# #     #     """The Issuer (or the Investment Manager acting on behalf of the Issuer) reserves the right to request such information as is necessary to verify the identity of a Noteholder and the source of the payment of subscription monies, or as is necessary to comply with any customer identification programs required by FinCEN and/or the SEC or any other applicable AML Requirements. If there is a delay or failure by the applicant to produce any information required for verification purposes,
# #     #     an application for or transfer of Notes and the subscription monies relating thereto may be refused.""",
# #     #     {"entities": [(373, 482, "Cause"), (483, 590, "Effect")]}
# #     # ),
# #     # (
# #     #     """If there is an early redemption, the holders of the Notes will be repaid prior to the Maturity Date. Where the Notes are to be redeemed by liquidation, there can be no assurance that the Sale Proceeds realised and other available funds would permit any distribution on the Subordinated Notes after all required payments are made to the holders of the Rated Notes. In addition, an Optional Redemption could require the Investment Manager to liquidate positions more rapidly than would otherwise be desirable,
# #     #     which could adversely affect the realised value of the Collateral Debt Obligations sold.""",
# #     #     {"entities": [(0, 31, "Cause"), (32, 100, "Effect"), (101, 150,"Cause"), (151, 362, "Effect")]}
# #     # ),
# #     # (
# #     #     """If at any time one or more investors that are affiliated hold a majority of any Class of Notes, it may be more difficult for other investors to take certain actions that require consent of any such Classes of Notes without their consent. For example, optional redemption and the removal of the Investment Manager for cause and appointment
# #     #     are at the direction of Noteholders of specified percentages of Subordinated Notes and/or the Controlling Class (as applicable).""",
# #     #     {"entities": [(0, 94, "Cause"), (95, 236, "Effect")]}
# #     # ),
# #     # (
# #     #     """If a Hedge Counterparty is subject to a rating withdrawal or downgrade by the Rating Agencies to below the applicable Rating Requirement, there will generally be a termination event under the applicable Hedge Agreement unless, within the applicable grace period following such rating withdrawal or downgrade, such Hedge Counterparty either transfers its obligations under the applicable Hedge Agreement to a replacement counterparty with the requisite ratings, obtains a guarantee of its obligations by a guarantor with the requisite ratings, collateralises its obligations in a manner satisfactory
# #     #     to the Rating Agencies or employs some other strategy as may be approved by the Rating Agencies.""",
# #     #     {"entities": [(0, 136, "Cause"), (137, 217, "Effect")]}
# #     # ),
# #     # (
# #     #     """The Issuer will depend upon the Asset Swap Counterparty to perform its obligations under any hedges. If the Asset Swap Counterparty defaults or becomes unable to perform due to insolvency or otherwise, the Issuer may not receive payments it would otherwise be entitled to from the Asset Swap Counterparty to cover its foreign exchange exposure.""",
# #     #     {"entities": [(101, 200, "Cause"), (202, 343, "Effect")]}
# #     # ),
# #     # (
# #     #     """In considering proposals by the examiner, it is likely that secured and unsecured creditors would form separate classes of creditors. In the case of the Issuer, if the Trustee represented the majority in number and value of claims within the secured creditor class, the Trustee would be in a position to reject any proposal not in favour of the Noteholders.""",
# #     #     {"entities": [(134, 264, "Cause"), (265, 356, "Effect")]}
# #     # ),
# #     # (
# #     #     """The Issuer will depend upon the Asset Swap Counterparty to perform its obligations under any hedges. If the Asset Swap Counterparty defaults or becomes unable to perform due to insolvency or otherwise, the Issuer may not receive payments it would otherwise be entitled to from the Asset Swap Counterparty to cover its foreign exchange exposure.""",
# #     #     {"entities": [(101, 200, "Cause"), (201, 343, "Effect")]}
# #     # ),
# #     # (
# #     #     """“Principal Proceeds” means all amounts paid or payable into the Principal Account from time to time and, with respect to any Payment Date, means Principal Proceeds received or receivable by the Issuer during the related Due Period and any other amounts to be disbursed as Principal Proceeds on such
# #     #     Payment Date pursuant to Condition 3(c)(ii) (Application of Principal Proceeds) or Condition 11(b) (Enforcement).""",
# #     #     {"entities": []}
# #     # ),
# #     # (
# #     #     """In connection with the issue and sale of the Notes, no person is authorised to give any information or to make any representation not contained in this Prospectus and, if given or made, such information or representation must not be relied upon as having been authorised by or on behalf of the Issuer, the Placement Agent, the Trustee, the Collateral Manager, the Retention Holder or the Collateral Administrator.
# #     #     The delivery of this Prospectus at any time does not imply that the information contained in it is correct as at any time subsequent to its date.""",
# #     #     {"entities": [(51, 183, "Cause"), (184, 412, "Effect")]}
# #     # ),
#     (
#         """'""",
#         {"entities": []}
#     ),
#     (
#         """Notes """,
#         {"entities": []}
#     ),
#     (
#         """the Issuer""",
#         {"entities": []}
#     ),
#     (
#         """If investment by “banking entities” in the Notes of any Class is prohibited or restricted by the Volcker Rule, this could impair the marketability and liquidity of such Notes.""",
#         {"entities": [(0,109, "Cause"), (110, 173, "Effect")]}
#     ),
#     (
#         """Information as to placement within the United States The Notes of each Class offered pursuant to an exemption from registration requirements under Rule 144A under the Securities Act (“Rule 144A”) (the “Rule 144A Notes”) will be sold only to “qualified institutional buyers” (as defined in Rule 144A) (“QIBs”) that are also “qualified purchasers” for purposes of Section 3(c)(7) of the Investment Company Act (“QPs”). Rule 144A Notes of each Class (other than, in certain circumstances, the Class E Notes, the Class F Notes, the Class Z Notes and the Subordinated Notes) will each be represented on issue by beneficial interests in one or more permanent global certificates of such Class (each, a “Rule 144A Global Certificate” and together, the “Rule 144A Global Certificates”) or may in some cases be represented by definitive certificates of such Class (each a “Rule 144A Definitive Certificate” and, together, the “Rule 144A Definitive Certificates”), in each case in fully registered form, without interest coupons or principal receipts, which will be deposited on or about the Issue Date with, and registered in the name of, a nominee of a common depositary for Euroclear Bank S.A./N.V., as operator of the Euroclear System (“Euroclear”) and Clearstream Banking, société anonyme (“Clearstream, Luxembourg”), or, in the case of Rule 144A Definitive Certificates, the registered holder thereof. The Notes of each Class (other than in certain circumstances, the Class E Notes, the Class F Notes, the Class Z Notes and the Subordinated Notes) sold to non-“U.S. Persons” in an “offshore transaction”, as such terms are defined in, and in accordance with Regulation S (“Regulation S”) under the Securities Act (the “Regulation S Notes”) will each be represented on issue by beneficial interests in one or more permanent global certificates of such Class (each, a “Regulation S Global Certificate” and together, the “Regulation S Global Certificates”) or may in some cases be represented by definitive certificates of such Class (each a “Regulation S Definitive Certificate” and, together, the “Regulation S Definitive Certificates”), in each case in fully registered form, without interest coupons or principal receipts, which will be deposited on or about the Issue Date with, and registered in the name of, a nominee of a common depositary for Euroclear and Clearstream, Luxembourg or, in the case of Regulation S Definitive Certificates, the registered holder thereof. Neither U.S. Persons nor U.S. residents (as determined for the purposes of the Investment Company Act) (“U.S. Residents”) may hold an interest in a Regulation S Global Certificate or a Regulation S Definitive Certificate.""",
#         {"entities": []}
#     ),
#     (
#         """UPON OR ENDORSED THE MERITS OF THIS OFFERING OR THE ACCURACY OR ADEQUACY OF THIS DOCUMENT. ANY REPRESENTATION TO THE CONTRARY IS A CRIMINAL OFFENCE. This Offering Circular has been prepared by the Issuer solely for use in connection with the offering of the Notes described herein (the “Offering”). Each of the Issuer and the Initial Purchaser reserves the right to reject any offer to purchase Notes in whole or in part for any reason, or to sell less than the stated initial principal amount of any Class of Notes offered hereby. This Offering Circular is personal to each offeree to whom it has been delivered by the Issuer, the Initial Purchaser or any Affiliate thereof and does not constitute an offer to any other person or to the public generally to subscribe for or otherwise acquire the Notes. Distribution of this Offering Circular to any persons other than the offeree and those persons, if any, retained to advise such offeree with respect thereto is unauthorised and any disclosure of any of its contents, without the prior written consent of the Issuer, is prohibited. Any reproduction or distribution of this Offering Circular in whole or in part and any disclosure of its contents or use of any information herein for any purpose other than considering an investment in the securities offered herein is prohibited. Notwithstanding anything to the contrary herein, each recipient (and each employee, representative, or other agent of such recipient) may disclose to any and all persons, without limitation of any kind, the U.S. federal, state, and local tax treatment of the Issuer, the Notes, or the transactions referenced herein and all materials of any kind (including opinions or other U.S. tax analyses) relating to such U.S. federal, state, and local tax treatment and that may be relevant to understanding such U.S. federal, state, and local tax treatment. Available Information To permit compliance with the Securities Act in connection with the sale of the Notes in reliance on Rule 144A, the Issuer will be required under the Trust Deed to furnish upon request to a holder or beneficial owner who is a QIB of a Note sold in reliance on Rule 144A or a prospective investor who is a QIB designated by such holder or beneficial owner the information required to be delivered under Rule 144A(d)(4) under the Securities Act if at the time of the request the Issuer is neither a reporting company under Section 13 or Section 15(d) of the United States Securities Exchange Act of 1934, as amended, nor exempt from reporting pursuant to Rule 12g3-2(b) under the Exchange Act. All information made available by the Issuer pursuant to the terms of this paragraph may also be obtained during usual business hours free of charge at the office of the Principal Paying Agent.""",
#         {"entities": []}
#     ),
#     (
#         """IF THE COLLATERAL MANAGER IS REQUIRED TO REGISTER AS A CPO OR A CTA, IT WILL BECOME SUBJECT TO NUMEROUS REPORTING AND OTHER REQUIREMENTS AND IT IS EXPECTED THAT IT WILL INCUR SIGNIFICANT ADDITIONAL COSTS IN COMPLYING WITH ITS OBLIGATIONS AS A REGISTERED CPO OR CTA, WHICH COSTS ARE EXPECTED TO BE PASSED ON TO THE ISSUER AND MAY ADVERSELY AFFECT THE ISSUER’S ABILITY TO MAKE PAYMENT ON THE NOTES. Applicability of EU Law in the UK THE UK WITHDREW FROM AND CEASED TO BE A MEMBER STATE OF THE EU AT 11:00 P.M. GMT ON 31 JANUARY 2020. THE NEGOTIATED WITHDRAWAL AGREEMENT ENTERED INTO BETWEEN THE UK AND THE EU PROVIDES FOR A TRANSITION PERIOD, COMMENCING ON 31 JANUARY 2020 AND ENDING AT 11.00 P.M. GMT ON 31 DECEMBER 2020 (SUCH PERIOD, THE “TRANSITION PERIOD”). UNLESS OTHERWISE PROVIDED IN THE NEGOTIATED WITHDRAWAL AGREEMENT, EU LAW WILL BE APPLICABLE TO AND IN THE UK DURING THE TRANSITION PERIOD. ACCORDINGLY, DURING THE TRANSITION PERIOD ANY REFERENCES IN THIS OFFERING CIRCULAR TO THE “EU” AND ITS “MEMBER STATES” IN THE CONTEXT OF EU LEGISLATION AND THE APPLICATION THEREOF SHALL BE INTERPRETED SO AS TO INCLUDE THE UK (EXCEPT WHERE EXPRESSLY INDICATED OTHERWISE). MIFID II Product Governance Solely for the purposes of each manufacturer’s product approval process, the target market assessment in respect of the Notes has led to the conclusion that: (i) the target market for the Notes is eligible counterparties and professional clients only, each as defined in Directive 2014/65/EU (as amended, “MiFID II”); and (ii) all channels for distribution of the Notes to eligible counterparties and professional clients are appropriate. Any person subsequently offering, selling or recommending the Notes (a “distributor”) should take into consideration the manufacturer target market assessment; however, a distributor subject to MiFID II is responsible for undertaking its own target market assessment in respect of the Notes (by either adopting or refining the manufacturer target market assessment) and determining appropriate distribution channels. PRIIPs Regulation and Prospectus Regulation The Notes are not intended to be offered, sold or otherwise made available to and should not be offered, sold or otherwise made available to any retail investor in the European Economic Area (“EEA”) or in the United Kingdom (the “UK”). For these purposes, a retail investor means a person who is one (or more) of: (i) a retail client as defined in point (11) of Article 4(1) of MiFID II; or (ii) a customer within the meaning of Directive (EU) 2016/97, where that customer would not qualify as a professional client as defined in point (10) of Article 4(1) of MiFID II; or (iii) not a qualified investor within the meaning of Article 2(e) of the Prospectus Regulation. Consequently no key information document required by Regulation (EU) No 1286/2014 (as amended, the “PRIIPs Regulation”) for offering or selling the Notes or otherwise making them available to retail investors in the EEA or in the UK has been prepared and therefore offering or selling the Notes or otherwise making them available to any retail investor in the EEA or in the UK may be unlawful under the PRIIPS Regulation.""",
#         {"entities": [(0, 67, "Cause"), (68, 395, "Effect")]}
#     ),
#     (
#         """4 The Initial Purchaser and the Issuer may offer the Notes at prices as may be negotiated at the time of sale , which may vary among different purchasers and may be different from the issue price of the Notes.""",
#         {"entities": []}
#     ),
#     (
#         """Management Fee on each Payment Date on which the Incentive Collateral Management Fee IRR Threshold has been met or surpassed, equal to 20 per cent. of any Interest Proceeds and Principal Proceeds that would otherwise be available to distribute to the Subordinated Noteholders in accordance with the Priorities of Payment. See “Description of the Collateral Management and Administration Agreement — Compensation of the Collateral Manager”. Security for the Notes""",
#         {"entities": []}
#     ),
#     (
#         """will """,
#         {"entities": []}
#     ),
#     (
#         """At this time, the full consequences of such withdrawal are not clear. In particular, there is uncertainty as to the final trade arrangements to be put in place following the expiry of the Transition Period (as defined below). Investors should be aware that the Issuer’s risk profile may be materially affected by this uncertainty which might also have an adverse impact on the Portfolio and the Issuer’s business, financial condition, results of operations and prospects and could therefore also be materially detrimental to Noteholders""",
#         {"entities": []}
#     ),
#     (
#         """Any such potential adverse economic conditions may also affect the ability of the obligors to make payment under the Collateral Obligations which in turn may adversely affect the ability of the Issuer to pay interest and repay principal to the Noteholders.""",
#         {"entities": []}
#     ),
#     (
#         """If, at the end of the Transition Period, the UK were no longer within the scope of EU Directive 2014/65/EU and EU Regulation 600/2014/EU on Markets in Financial Instruments (collectively referred to as “MiFID II”) and an alternative passporting regime or third country recognition of the UK is not in place, then (a) a UK manager such as the Collateral Manager may be unable to continue to provide collateral management services to the Issuer in reliance upon the passporting of relevant regulated services within the EU on a cross-border basis provided for under MiFID II and (b) the Collateral Manager may not be able to continue to act as Retention Holder to the extent it was required to hold the retention solely as “sponsor” in accordance with the EU Retention Requirements (even if the Collateral Manager were to remain subject to UK financial services regulation), however, we note that the Collateral Manager intends to act as an “originator” retention holder for the purposes of this transaction. As of the date hereof, an “originator” retention holder is not required to be regulated in the EU in order to act in such capacity. In connection with the issue and sale of the Notes, no person is authorised to give any information or to make any representation not contained in this Offering Circular and, if given or made, such information or representation must not be relied upon as having been authorised by or on behalf of the Issuer, the Arranger, the Initial Purchaser, the Trustee, the Collateral Manager, the Retention Holder, the Liquidity Facility Provider or the Collateral Administrator. The delivery of this Offering Circular at any time does not imply that the information contained in it is correct as at any time subsequent to its date.""",
#         {"entities": [(0, 306, "Cause"), (307, 871, "Effect")]}
#     ),
#     (
#         """If the Collateral Administrator does not agree on the terms of reporting or, in the reasonable opinion of the Issuer (acting on the advice of the Collateral Manager), the Collateral Administrator is or will be unable or unwilling to provide such reporting, the Issuer (with the consent of the Collateral Manager) shall be entitled to appoint another entity to make the relevant information available for the purposes of Article 7 (Transparency requirements for originators, sponsors and SSPEs) of the Securitisation Regulation.""",
#         {"entities": [(0, 165, "Cause"), (166, 526, "Effect")]}
#     ),
#     (
#         """If the Issuer is deemed to be a “covered fund”, this could significantly impair the marketability and liquidity of the Refinancing Notes.""",
#         {"entities": [(0, 46, "Cause"), (47, 136, "Effect")]}
#     ),
#     (
#         """IF THE COLLATERAL MANAGER IS REQUIRED TO REGISTER AS A CPO/CTA, IT WILL BECOME SUBJECT TO NUMEROUS REPORTING AND OTHER REQUIREMENTS AND IT IS EXPECTED THAT IT WILL INCUR SIGNIFICANT ADDITIONAL COSTS IN COMPLYING WITH ITS OBLIGATIONS AS A REGISTERED CPO, WHICH COSTS ARE EXPECTED TO BE PASSED ON TO THE ISSUER AND MAY ADVERSELY AFFECT THE ISSUER’S ABILITY TO MAKE PAYMENT ON THE NOTES.""",
#         {"entities": [(0, 62, "Cause"), (62, 252, "Effect")]}
#     ),
#     (
#         """To permit compliance with the Securities Act in connection with the sale of the Refinancing Notes in reliance on Rule 144A, the Issuer will be required under the Trust Deed to furnish upon request to a holder or beneficial owner who is a QIB of a Note sold in reliance on Rule 144A or a prospective investor who is a QIB designated by such holder or beneficial owner the information required to be delivered under Rule 144A(d)(4) under the Securities Act if at the time of the request the Issuer is neither a reporting company under Section 13 or Section 15(d) of the United States Securities Exchange Act of 1934, as amended, nor exempt from reporting pursuant to Rule 12g3- 2(b) under the Exchange Act.""",
#         {"entities": []}
#     ),
#     (
#         """If the Collateral Administrator does not agree on the terms of reporting or, in the reasonable opinion of the Issuer (acting on the advice of the Collateral Manager), the Collateral Administrator is or will be unable or unwilling to provide such reporting, the Issuer (with the consent of the Collateral Manager) shall be entitled to appoint another entity to make the relevant information available for the purposes of Article 7 (Transparency requirements for originators, sponsors and SSPEs) of the Securitisation Regulation.""",
#         {"entities": [(0, 255, "Cause"), (256, 526, "Effect")]}
#     ),
#     (
#         """The Collateral Manager does not have any obligation to consider or take any Retention Cure Action and, if the Collateral Manager determines not to take any Retention Cure Action, it may no longer be eligible to act as the Retention Holder pursuant to the EU Retention and Transparency Requirements (and for the avoidance of doubt, even if a Retention Cure Action is taken, it is not certain whether such action would result in compliance with the EU Retention and Transparency Requirements).""",
#         {"entities": [(103,177, "Cause"), (178, 328, "Effect")]}
#     ),
#     (
#         """If the Collateral Administrator does not agree on the terms of reporting or, in the reasonable opinion of the Issuer (acting on the advice of the Collateral Manager), the Collateral Administrator is or will be unable or unwilling to provide such reporting, the Issuer (with the consent of the Collateral Manager) shall be entitled to appoint another entity to make the relevant information available for the purposes of Article 7 (Transparency requirements for originators, sponsors and SSPEs) of the Securitisation Regulation.""",
#         {"entities": [(0, 165, "Cause"), (166, 526, "Effect")]}
#     ),
#     (
#         """However, the SEC has indicated that it is continuing to consider amendments that were proposed with respect to Regulation AB but not adopted, and that further amendments may be forthcoming in the future. If such amendments are made to Regulation AB in the future, they may place additional requirements and expenses on the Issuer in the event of the issuance and sale of any additional notes, which expenses may reduce the amounts available for distribution to the Noteholders.""",
#         {"entities": [(204, 262, "Cause"), (262, 390, "Effect")]}
#     ),
#     (
#         """Moreover, if the Priorities of Payment are the subject of litigation in any jurisdiction outside England and Wales, in particular in the United States of America, and such litigation results in a conflicting judgment in respect of the binding nature of the Priorities of Payment, it is possible that termination payments due to the Hedge Counterparties would not be subordinated as envisaged by the Priority of Payments and as a result, the Issuer’s ability to repay the Noteholders in full may be adversely affected.""",
#         {"entities": [(10, 278, "Cause"), (279, 516, "Effect")]}
#     ),
#     (
#         """If the Issuer is considered to be a member of a “group” (as defined in EMIR) (which may, for example, potentially be the case if the Issuer is consolidated by a Noteholder as a result of such Noteholder’s holding of a significant proportion of the Subordinated Notes) and if the aggregate notional value of OTC derivative contracts entered into by the Issuer and any non- financial entities within such group exceeds the applicable thresholds (excluding eligible hedging transactions), the Issuer would be subject to the clearing obligation, or if the relevant contract is not a type required to be cleared, to the risk mitigation obligations, including the margin requirement.""",
#         {"entities": [(0,266, "Cause"), (272, 484, "Cause"), (485, 676, "Effect")]}
#     ),
#         (
#         """If the Issuer exceeds the applicable thresholds and its swaps become subject to mandatory clearing, this may also lead to a termination of the Hedge Agreements.""",
#         {"entities": [(0,98, "Cause"), (99, 159, "Effect")]}
#     ),
#         (
#         """If the Issuer becomes subject to the clearing obligation or to the margin requirement, it is unlikely that it would be able to comply with such requirements, which would adversely affect the Issuer’s ability to enter into Hedge Transactions or significantly increase the cost thereof, negatively affecting the Issuer’s ability to acquire Non-Euro Obligations and/or hedge its interest rate risk.""",
#         {"entities": [(0, 85, "Cause"), (88, 394, "Effect")]}
#     ),
#         (
#         """If the Issuer were to be considered to be an AIF within the meaning in AIFMD, it would need to be managed by a manager authorised under AIFMD (an “AIFM”).""",
#         {"entities": [(0, 76, "Cause"), (77, 153, "Effect")]}
#     ),
#         (
#         """If considered to be an AIF managed by an AIFM, the Issuer would also be classified as an FC under EMIR and may be required to comply with clearing obligations and/or other risk mitigation techniques (including obligations to post margin to any central clearing counterparty or market counterparty) with respect to Hedge Transactions (under the EMIR Refit, all AIFs will be FCs whether or not managed by an authorised AIFM).""",
#         {"entities": [(0, 45, "Cause"), (46, 422, "Effect")]}
#     ),
#         (
#         """If the SSPE Exemption does not apply and the Issuer is considered to be an AIF, the Collateral Manager may not be able to continue to manage the Issuer’s assets, or its ability to do so may be impaired.""",
#         {"entities": [(0, 78, "Cause"), (78, 201, "Effect")]}
#     ),
#         (
#         """If such amendments are made to Regulation AB in the future, they may place additional requirements and expenses on the Issuer in the event of the issuance and sale of any additional notes, which expenses may reduce the amounts available for distribution to the Noteholders.""",
#         {"entities": [(0, 58, "Cause"), (59, 272, "Effect")]}
#     ),
#         (
#         """If the Collateral Manager elects to file for a registration exemption under CFTC Rule 4.13(a)(3), then unlike a CFTC-registered CPO, the Collateral Manager would not be required to deliver a CFTC-mandated disclosure document or a certified annual report to investors, or otherwise comply with the requirements applicable to CFTC-registered CPOs and CTAs.""",
#         {"entities": [(0, 131, "Cause"), (132, 353, "Effect")]}
#     ),
#         (
#         """Further, if the Collateral Manager determines that additional Hedge Transactions should be entered into by the Issuer in excess of the trading limitations set forth in any applicable exemption from registration as a CPO and/or a CTA, the Collateral Manager may elect to withdraw its exemption from registration and instead register with the CFTC as the Issuer’s CPO and/or CTA. The costs of obtaining and maintaining these registrations and the related compliance obligations may be paid by the Issuer as Administrative Expenses.""",
#         {"entities": [(9, 232, "Cause"), (233, 376, "Effect")]}
#     ),
#         (
#         """If the Issuer is deemed to be a “covered fund” the provisions of the Volcker Rule and its related regulatory provisions, will severely limit the ability of “banking entities” to hold an “ownership interest” in the Issuer or enter into certain credit related financial transactions with the Issuer.""",
#         {"entities": [(0, 119, "Cause"), (120, 296, "Effect")]}
#     ),
#         (
#         """If investment by “banking entities” in the Refinancing Notes of any Class is prohibited or restricted by the Volcker Rule, this could impair the marketability and liquidity of such Refinancing Notes.""",
#         {"entities": [(0, 121, "Cause"), (122, 198, "Effect")]}
#     ),
#         (
#         """Moreover, if the Priorities of Payment are the subject of litigation in any jurisdiction outside England and Wales, in particular in the United States of America, and such litigation results in a conflicting judgment in respect of the binding nature of the Priorities of Payment, it is possible that termination payments due to the Hedge Counterparties would not be subordinated as envisaged by the Priority of Payments and as a result, the Issuer’s ability to repay the Noteholders in full may be adversely affected.""",
#         {"entities": [(10, 278, "Cause"), (279, 516, "Effect")]}
#     ),
#         (
#         """It is possible that the LIBOR administrator, ICE Benchmark Administration Limited, and the panel banks could continue to produce LIBOR on the current basis after 2021, if they are willing and able to do so. However, the survival of LIBOR in its current form, or at all, is not guaranteed after 2021.""",
#         {"entities": [(0, 166, "Effect"), (168, 298, "Cause")]}
#     ),
#         (
#         """If LIBOR does not survive in its current form or at all, this could adversely affect the value of, and amounts payable under, any Collateral Obligations which pay interest calculated with reference to LIBOR and therefore reduce amounts which may be available to the Issuer to pay Noteholders.""",
#         {"entities": [(0, 55, "Cause"), (56, 291, "Effect")]}
#     ),
#         (
#         """Benchmarks such as EURIBOR or LIBOR may be discontinued if they do not comply with the requirements of the Benchmarks Regulation, or if the administrator of the benchmark either fails to apply for authorisation or is refused authorisation by its home regulator.""",
#         {"entities": [(0, 54, "Effect"), ( 56, 260, "Cause")]}
#     ),
#         (
#         """If a relevant institution enters into an arrangement with the Issuer and is deemed likely to fail in the circumstances identified in the BRRD, the relevant Resolution Authority may employ such tools and powers in order to intervene in the relevant institution’s failure (including in the case of derivatives transactions, powers to close-out such transactions or suspend any rights to close-out such transactions).""",
#         {"entities": [(0, 141, "Cause"), (142, 413, "Effect")]}
#     ),
#         (
#         """If the relevant Resolution Authority decides to “bail-in” the liabilities of a relevant institution, then subject to certain exceptions set out in the BRRD, the liabilities of such relevant institution could, among other things, be reduced, converted or extinguished in full.""",
#         {"entities": [(0, 100, "Cause"), (101, 274, "Effect")]}
#     ),
#         (
#         """If a Member State outside the Euro zone (such as the UK) has chosen not to participate in the bank single supervisory mechanism, relevant institutions established in such Member State will not be subject to the SRM Regulation, but to the application of the BRRD by the Resolution Authorities.""",
#         {"entities": [(0, 127, "Cause"), (128, 291, "Effect")]}
#     ),
#         (
#         """If a Covered Entity enters into a contract with the Issuer that is subject to the QFC Stay Rules, the Covered Entity will be responsible for ensuring that such QFC complies with the QFC Stay Rules. As a result of the application of such rules, the Issuer may be required to accept limitations in its insolvency-related default rights against the Covered Entity.""",
#         {"entities": [(0, 96, "Cause"), (98, 196, "Effect")]}
#     ),
#         (
#         """If the Issuer’s COMI is not located in The Netherlands and is held to be in a different jurisdiction within the European Union, Dutch insolvency proceedings would not be applicable to the Issuer.""",
#         {"entities": [(0, 126, "Cause"), (127, 194, "Effect")]}
#     ),
#         (
#         """If a Refinancing is obtained meeting the requirements of the Trust Deed, the Issuer may amend the Trust Deed and the Trustee shall concur with such amendments to the Trust Deed and no further consent for such amendments shall be required from the holders of the Subordinated Notes.""",
#         {"entities": [(0, 71, "Cause"), (72, 280, "Effect")]}
#     ),
#         (
#         """The Collateral Manager or the Retention Holder may also cause the Issuer to redeem the Rated Notes in whole from Sale Proceeds on any Business Day falling on or after the expiry of the Non-Call Period, if the Collateral Principal Amount is less than 15 per cent. of the Target Par Amount.""",
#         {"entities": [(0, 200, "Effect"), (201, 287, "Cause")]}
#     ),
#         (
#         """Each Noteholder will agree, and each beneficial owner of Notes will be deemed to agree, pursuant to the Trust Deed, that it will be subject to non-petition covenants. If such provision failed to be enforceable under applicable bankruptcy laws, and a winding-up (or similar) petition was presented in respect of the Issuer, then the presentation of such a petition could (subject to certain conditions) result in one or more payments on the Notes made during the period prior to such presentation being deemed to be preferential transfers subject to avoidance by the bankruptcy trustee or similar official exercising authority with respect to the Issuer’s bankruptcy estate.""",
#         {"entities": [(167, 321, "Cause"), (322, 672, "Effect")]}
#     ),
# ]


def train_custom_ner():
    model = "idementsdamodelleket/ner"
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
    nlp.max_length = 1787772

    # Test the trained model
    # test_text = """If the Issuer becomes subject to an insolvency proceeding and the Issuer has obligations to creditors that are treated under Irish law as creditors that are senior relative to the Noteholders and other Secured Parties, the Noteholders (and other Secured Parties) may suffer losses as a result of their subordinated status during such insolvency proceedings. In particular, under Irish law, upon an insolvency of an Irish company, such as the Issuer, when applying the proceeds of assets subject to fixed security which may have been realised in the course of a liquidation or receivership, the claims of a limited category of preferential creditors will take priority over the claims of creditors holding the relevant fixed security. These preferred claims include the remuneration, costs and expenses properly incurred by any examiner of the company (which may include any borrowings made by an examiner to fund the company’s requirements for the duration of his appointment) which have been approved by the relevant Irish courts. See 7.3 “Examinership”."""
    # #test_text = """The Issuer will depend upon the Asset Swap Counterparty to perform its obligations under any hedges. If the Asset Swap Counterparty defaults or becomes unable to perform due to insolvency or otherwise, the Issuer may not receive payments it would otherwise be entitled to from the Asset Swap Counterparty to cover its foreign exchange exposure."""
    # doc = nlp(test_text)
    # print("Entities")
    # for ent in doc.ents:
    #     print("lab:", ent.label_, ent.text)

    # output_dir = "idementsdamodelleket/ner"
    # if output_dir is not None:
    #     output_dir = Path(output_dir)
    #     if not output_dir.exists():
    #         output_dir.mkdir()
    #     nlp.meta['name'] = "logic_ner_model_92"  # rename model
    #     nlp.to_disk(output_dir)
    #     print("Saved model to", output_dir)

    with open('sample/eurlex_01.txt', 'r', encoding='utf-8') as file:
        all_of_it = file.read()
        doc = nlp(all_of_it)
        displacy.serve(doc, style="ent")


if __name__ == "__main__":
    train_custom_ner()
