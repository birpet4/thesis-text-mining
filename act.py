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

TRAIN_DATA = [
    (
        """The Issuer has not registered with the United States Securities and Exchange Commission (the “SEC”) as an investment company pursuant to the Investment Company Act, in reliance on an exclusion under Section 3(c)(7) of the Investment Company Act for securities issuers (a) whose outstanding securities are beneficially owned only by “qualified purchasers” (within the meaning given to such term in the Investment Company Act and the regulations of the SEC thereunder) and certain transferees thereof identified in Rule 3c 6 under the Investment Company Act and (b) which do not make a public offering of their securities in the United States.""",
        {"entities": [(137, 163, "Reference"), (199, 246, "Reference"),
                      (397, 423, "Reference"), (513, 555, "Reference")]}
    ),
    (
        """If the SEC or a court of competent jurisdiction were to find that the Issuer is required, but in violation of the Investment Company Act had failed, to register as an investment company, possible consequences include, but are not limited to, the following: (i) the SEC could apply to a district court to enjoin the violation; (ii) investors in the Issuer could sue the Issuer and seek recovery of any damages caused by the violation; and (iii) any contract to which the Issuer is party could be declared unenforceable unless a court were to find that under the circumstances enforcement would produce a more equitable result than non-enforcement and would not be inconsistent with the purposes of the Investment Company Act. Should the Issuer be subjected to any or all of the foregoing, the Issuer would be materially and adversely affected""",
        {"entities": [(110, 136, "Reference")]}
    ),
    (
        """“CEA” means the United States Commodity Exchange Act of 1936, as amended.""",
        {"entities": [(12, 60, "Reference")]}
    ),
    (
        """“Dodd-Frank Act” means the Dodd-Frank Wall Street Reform and Consumer Protection Act including any related regulation as may be amended, supplemented or replaced from time to time.""",
        {"entities": [(1, 15, "Reference"), (23, 84, "Reference")]}
    ),
    (
        """“ERISA” means the Employee Retirement Income Security Act of 1974, as amended.""",
        {"entities": [(14, 65, "Reference")]}
    ),
    (
        """“Investment Company Act” means the United States Investment Company Act of 1940, as amended.""",
        {"entities": [(1, 25, "Reference"), (31, 79, "Reference")]}
    ),
    (
        """(vii) use its best endeavours to obtain and maintain the listing on the Global Exchange Market of the Outstanding Notes of each Class. If, however, it is unable to do so, having used such endeavours, or if the maintenance of such listings are agreed by the Trustee to be unduly onerous and the Trustee is satisfied that the interests of the holders of the Outstanding Notes of each Class would not thereby be materially prejudiced, the Issuer will instead use all reasonable endeavours promptly to obtain and thereafter to maintain a listing for such Notes on such other stock exchange(s) as it may (with the prior written approval of the Trustee) decide, provided that any such other stock exchange is (a) a recognised stock exchange for the purposes of Section 64 of the TCA and (b) a recognised stock exchange for the purposes of section 1005 of the United Kingdom Income Tax Act 2007;""",
        {"entities": [(833, 887, "Reference")]}
    ),
    (
        """the Issuer or any of the Collateral becomes required to register as an “Investment Company” under the Investment Company Act and such requirement continues for 45 days.""",
        {"entities": [(98, 124, "Reference")]}
    ),
    (
        """(xi) to modify the restrictions on and procedures for resales and other transfers of Notes to reflect any changes in ERISA or other applicable law or regulation (or the interpretation thereof) to enable the Issuer to rely upon any exemption from registration under the Securities Act or the Investment Company Act or to remove restrictions on resale and transfer to the extent not required thereunder;""",
        {"entities": [(265, 283, "Reference"), (287, 313, "Reference")]}
    ),
    (
        """(xxvi) to modify the terms of the Transaction Documents (including but not limited to any Hedge Agreements) and/or the Conditions in order to enable the Issuer to comply with any requirements of the CFTC or in relation to the Dodd-Frank Act, subject to receipt by the Trustee of a certificate of the Issuer certifying to the Trustee that the requested amendments are to be made solely for the purpose of enabling the Issuer to comply with CFTC requirements or the Dodd-Frank Act (upon which certification the Trustee shall be entitled to rely without further enquiry and without liability);""",
        {"entities": [(460, 478, "Reference")]}
    ),
    (
        """oteholders over the Class E Noteholders and the Subordinated Noteholders; and (v) the Class E Noteholders over the Subordinated Noteholders. If the Trustee receives conflicting or inconsistent requests from two or more groups of holders of a Class, given priority as described in this paragraph, each representing less than the majority by principal amount of such Class, the Trustee shall give priority to the group which holds the greater aggregate principal amount of Notes Outstanding of such Class. The Trust Deed provides further that the Trustee will act upon the directions of the holders of the Controlling Class (or other Class given priority as described in this paragraph) in such circumstances subject to being indemnified and/or secured and/or prefunded to its satisfaction, and shall not be obliged to consider the interests of and is exempted from any liability to the holders of any other Class of Notes""",
        {"entities": []}
    ),
    (
        """The Trust Deed contains provisions for the indemnification of the Trustee and for its relief from responsibility in certain circumstances, including provisions relieving it from instituting proceedings to enforce repayment or to enforce the security constituted by or pursuant to the Trust Deed, unless indemnified and/or secured and/or prefunded to its satisfaction. The Trustee is entitled to enter into business transactions with the Issuer or any other party to any Transaction Document and any entity related to the Issuer or any other party to any Transaction Document without accounting for any profit. The Trustee is exempted from any liability in respect of any loss or theft or reduction of value of the Collateral from any obligation to insure, or to monitor the provisions of any insurance arrangements in respect of, the Collateral (for the avoidance of doubt, under the Trust Deed the Trustee is under no such obligation) and from any claim arising from the fact that the Collateral is held by the Custodian or is otherwise held in safe custody by a bank or other custodian. The Trustee shall not be responsible for the performance by the Custodian of any of its duties under the Agency Agreement or for the performance by the Collateral Manager of any of its duties under the Collateral Management Agreement, for the performance by the Collateral Administrator of its duties under the Collateral Management Agreement or for the performance by any other person appointed by the Issuer in relation to the Notes or by any other party to any Transaction Document. The Trustee shall not have any responsibility for the administration, management or operation of the Collateral including the request by the Collateral Manager to release any of the Collateral from time to time.""",
        {"entities": []}
    ),
    (
        """The Issuer is a special purpose vehicle established for the purpose of issuing asset backed securities and was incorporated in Ireland as a designated activity company on 4 November 2019 under the Companies Act (as amended, the “Companies Act”) with the name of CVC Cordatus Loan Fund XVII DAC and with company registration number 660005 and having its registered office at 32 Molesworth Street, Dublin 2, Ireland.""",
        {"entities": [(193, 210, "Reference"), (223, 243, "Reference")]}
    ),
    (
        """The Collateral Manager is an English limited liability partnership registered under the Limited Liability Partnership Act 2000 with number OC404529 on 25 February 2016. The Collateral Manager is authorised and regulated in the conduct of its collateral manager business by the UK Financial Conduct Authority as of October 2016 with firm reference number: 740003.""",
        {"entities": [(84, 167, "Reference")]}
    ),
    (
        """Further, the Collateral Manager has established an investment committee that will draw on the investment committee established for the benefit of CVC Credit Partners, while makings its own separate determinations based on the specific facts and circumstances of the applicable to this transaction. The investment committee will be comprised of the persons listed below being either employees or as provided pursuant to arrangements with CVC Credit Partners. In addition to the brief biographies set out above, the brief biographies of Gretchen L. Bergstresser, Andrew Davies, Cary Ho, Pieter Staelens, Simone Zacchi, Mark DeNatale and Tom Newberry are also set out below:""",
        {"entities": []}
    ),
    (
        """The Notes have not been, and will not be, registered under the United States Securities Act of 1933, as amended (the “Securities Act”) and will be offered only: (a) outside the United States to non-U.S. Persons (as defined in Regulation S under the Securities Act (“Regulation S”)); and (b) within the United States to persons and outside the United States to U.S. Persons (as such term is defined in Regulation S (“U.S. Persons”)), in each case, who are both qualified institutional buyers (as defined in Rule 144A (“Rule 144A”) under the Securities Act) in reliance on Rule 144A and qualified purchasers for the purposes of Section 3(c)(7) of the United States Investment Company Act of 1940, as amended (the “Investment Company Act”). Neither the Issuer nor the Collateral Manager will be registered under the Investment Company Act. Interests in the Notes will be subject to certain restrictions on transfer, and each purchaser of Notes offered hereby in making its purchase will be deemed to have made certain acknowledgements, representations and agreements. See “Plan of Distribution” and “Transfer Restrictions”.""",
        {"entities": [(59, 99, "Reference"), (113, 133, "Reference"),
                      (245, 280, "Reference"), (506, 554, "Reference"), (626, 693, "Reference"), (707, 735, "Reference"), (809, 835, "Reference")]}
    ),
    (
        """Act 2000 (Financial Promotion) Order 2005 or who otherwise fall within an exemption set forth in such Order so that Section 21(1) of the Financial Services and Markets Act 2000, as amended, does not apply to the Issuer (all such persons together being referred to as “relevant persons”). This communication must not be distributed to, acted on or relied on by persons who are not relevant persons. Any investment or investment activity to which this communication relates is available only to relevant persons and will be engaged in only with relevant persons. For a description of certain further restrictions on offers and sales of Notes and distribution of this Offering Circular, see “Plan of Distribution” and “Transfer Restrictions” below. The Notes are not intended to be sold and should not be sold to retail investors. See further “Plan of Distribution” of this Offering Circular for further information.""",
        {"entities": [(0, 41, "Reference"), (116, 176, "Reference")]}
    ),
    (
        """Key terms are defined under the Volcker Rule, including “banking entity”, “ownership interest”, “sponsor” and “covered fund”. In particular, “banking entity” is defined to include certain non-U.S. affiliates of U.S. banking entities as well as non-U.S. banking entities that conduct operations in the United States either directly or through branches or affiliates, “covered fund” is defined to include an issuer that would be an investment company, as defined in the U.S. Investment Company Act of 1940, but for section 3(c)(1) or 3(c)(7) thereof, subject to certain exemptions and exclusions found in the Volcker Rule’s implementing regulations (which would extend to the Issuer given its intention to rely on section 3(c)(7)) and “ownership interest” is defined to include, among other things, interests arising through a holder’s exposure to profits and losses in the covered fund or through any right of the holder to participate in the selection or removal of, among others, an investment manager or advisor, general partner or the board of directors of such covered fund. It should be noted that the Subordinated Notes will be characterised as ownership interests in the Issuer for this purpose. It is uncertain whether any of the Rated Notes may be similarly characterised as ownership interests. Providing that the right of holders of the Notes in respect of the removal of the Collateral Manager and selection of a successor collateral manager shall only be exercisable upon a Collateral Manager Event of Default may not be sufficient to ensure that the Rated Notes are not characterised as ownership interests. If the Issuer is deemed to be a covered fund then in the absence of regulatory relief such prohibitions may have adverse effects on the Issuer and the liquidity and value of the Notes including limiting the secondary market of the Notes and affecting the Issuer’s access to liquidity and ability to hedge its exposures.""",
        {"entities": [(464, 503, "Reference")]}
    ),
    (
        """The Notes of each Class offered pursuant to an exemption from registration under Rule 144A (“Rule 144A”) under the Securities Act (the “Rule 144A Notes”) will be sold only to “qualified institutional buyers” (as defined in Rule 144A) (“QIBs”) that are also “qualified purchasers” for purposes of Section 3(c)(7) of the Investment Company Act (“QPs”). The Rule 144A Notes of each Class (including, where applicable, the CM Voting Notes, the CM Non-Voting Exchangeable Notes and the CM Non-Voting Notes of such Class) (other than, in certain circumstances, the Class E Notes and the Subordinated Notes) will each be represented on issue by beneficial interests in one or more permanent global certificates of such Class (each, a “Rule 144A Global Certificate” and together, the “Rule 144A Global Certificates”) or in some cases (including, in certain circumstances, the Class E Notes and the Subordinated Notes) definitive certificates (each a “Rule 144A Definitive Certificate” and together the “Rule 144A Definitive Certificates”), in each case in fully registered form, without interest coupons or principal receipts, which will be deposited on or about the Issue Date with, and registered in the name of, a nominee of a common depositary for Euroclear Bank S.A./N.V., as operator of the Euroclear system (“Euroclear”) and Clearstream Banking, société anonyme (“Clearstream, Luxembourg”) or in the case of Rule 144A Definitive Certificates, the registered holder thereof. The Notes of each Class (including, where applicable, the CM Voting Notes, the CM Non-Voting Exchangeable Notes and the CM Non-Voting Notes of such Class) sold outside the United States to non-U.S. Persons in reliance on Regulation S (“Regulation S”) under the Securities Act (the “Regulation S Notes”) (other than, in certain circumstances, the Class E Notes and the Subordinated Notes) will each be represented on issue by beneficial interests in one or more permanent global certificates of such Class (each, a “Regulation S Global Certificate” and together, the “Regulation S Global Certificates”), or in some cases (including, in certain circumstances, the Class E Notes and the Subordinated Notes) by definitive certificates of such Class (each a “Regulation S Definitive Certificate” and together, the “Regulation S Definitive Certificates”) in fully registered form, without interest coupons or principal receipts, which will be deposited on or about the Issue Date with, and registered in the name of, a nominee of a common depositary for Euroclear and Clearstream, Luxembourg or, in the case of Regulation S Definitive Certificates, the registered holder thereof. Neither U.S. Persons nor U.S. residents (as determined for the purposes of the Investment Company Act) (“U.S. Residents”) may hold an interest in a Regulation S Global Certificate or a Regulation S Definitive Certificate. Ownership interests in the Regulation S Global Certificates and the Rule 144A Global Certificates (together, the “Global Certificates”) will be shown on, and transfers thereof will only be effected through, records maintained by Euroclear and Clearstream, Luxembourg and their respective participants. Other than with respect to the Retention Notes and the Class M-2 Subordinated Notes, Notes in definitive certificated form will be issued only in limited circumstances and will be registered in the name of the holder (or a nominee thereof).The Class E Notes and the Subordinated Notes (including the Retention Notes) may in certain circumstances described herein be issued in definitive, certificated, fully registered form, pursuant to the Trust Deed and will be offered outside the United States to non-U.S. Persons in reliance on Regulation S and within the United States to persons who are both QIBs and QPs and, in each case, will be registered in the name of the holder (or a nominee thereof).""",
        {"entities": [(111, 151, "Reference"), (296, 249,
                                                "Reference"), (1730, 1775, "Reference"), (2722, 2748, "Reference")]}
    ),
    (
        """THE NOTES HAVE NOT BEEN AND WILL NOT BE REGISTERED UNDER THE UNITED STATES SECURITIES ACT OF 1933, AS AMENDED (THE “SECURITIES ACT”) AND WILL BE OFFERED ONLY:""",
        {"entities": [(57, 97, "Reference"), (111, 131, "Reference")]}
    ),
    (
        """(A) OUTSIDE THE UNITED STATES TO NON-U.S. PERSONS (AS DEFINED IN REGULATION S UNDER THE SECURITIES ACT (“REGULATION S”)); AND (B) WITHIN THE UNITED STATES TO PERSONS AND OUTSIDE THE UNITED STATES TO U.S. PERSONS (AS SUCH TERM IS DEFINED IN REGULATION S (“U.S. PERSONS”)), IN EACH CASE, WHO ARE BOTH QUALIFIED INSTITUTIONAL BUYERS (AS DEFINED IN RULE 144A UNDER THE SECURITIES ACT) IN RELIANCE ON RULE 144A UNDER THE SECURITIES ACT AND QUALIFIED PURCHASERS FOR THE PURPOSES OF SECTION 3(C)(7) OF THE UNITED STATES INVESTMENT COMPANY ACT OF 1940, AS AMENDED (THE “INVESTMENT COMPANY ACT”). THE ISSUER HAS NOT BEEN AND WILL NOT BE REGISTERED UNDER THE INVESTMENT COMPANY ACT. INTERESTS IN THE NOTES WILL BE SUBJECT TO CERTAIN RESTRICTIONS ON TRANSFER, AND EACH PURCHASER OF NOTES OFFERED HEREBY IN MAKING ITS PURCHASE WILL BE REQUIRED TO OR DEEMED TO HAVE MADE CERTAIN ACKNOWLEDGEMENTS, REPRESENTATIONS AND AGREEMENTS. SEE “PLAN OF DISTRIBUTION” AND “TRANSFER RESTRICTIONS”.""",
        {"entities": [(84, 119, "Reference"), (345, 379,
                                               "Reference"), (412, 430, "Reference"), (495, 543, "Reference"), (557, 585, "Reference"), (645, 672, "Reference")]}
    ),
    (
        """The Issuer accepts responsibility for the information contained in this Offering Circular and to the best of the knowledge and belief of the Issuer (which has taken all reasonable care to ensure that such is the case), such information is in accordance with the facts and does not omit anything likely to affect the import of such information. BlueMountain accepts responsibility for the information contained in the sections of this document headed “Risk Factors – Certain conflicts of interest – The Investment Manager and other matters relating to BlueMountain”, “BlueMountain and the Investment Manager and the provision of investment management services”, “Description of the Investment Management and Collateral Administration Agreement – Cross Transactions”, “BlueMountain and the EU Retention and Transparency Requirements – BlueMountain B as Retention Holder”, “BlueMountain and the EU Retention and Transparency Requirements – Origination of Collateral Debt Obligations”, “BlueMountain and the EU Retention and Transparency Requirements – Securitisation Regulation – Comparable Assets” and “BlueMountain and the EU Retention and Transparency Requirements – Securitisation Regulation – Credit Granting Criteria” (together the “BlueMountain Information”). To the best of the knowledge and belief of BlueMountain (which has taken all reasonable care to ensure that such is the case), such information is in accordance with the facts and does not omit anything likely to affect the import of such information. The Collateral Administrator accepts responsibility for the information contained in the sections of this document headed “The Collateral Administrator”. To the best of the knowledge and belief of the Collateral Administrator (which has taken all reasonable care to ensure that such is the case), such information is in accordance with the facts and does not omit anything likely to affect the import of such information. Except for the BlueMountain Information in the case of BlueMountain and the sections of this document headed “The Collateral Administrator” in the case of Elavon Financial Services DAC, none of BlueMountain, the Collateral Administrator, the other Agents, the Arranger, the Initial Purchaser or its Affiliates accept any responsibility for the accuracy and completeness of any information contained in this Offering Circular. The delivery of this Offering Circular at any time does not imply that the information herein is correct at any time subsequent to the date of this Offering Circular or any document or agreement relating to the Notes or any Transaction Document. None of the Investment Manager, the Arranger or the Initial Purchaser nor any of its Affiliates shall be responsible for, any matter which is the subject of, any statement, representation, warranty or covenant of the Issuer contained in the Notes or any Transaction Documents, or any other agreement or document relating to the Notes or any Transaction Document, or for the execution, legality, effectiveness, adequacy, genuineness, validity, enforceability or admissibility in evidence thereof.""",
        {"entities": []}
    ),
    (
        """certain EU member states (the “Member States”), """,
        {"entities": []}
    ),
    (
        """In previous years, events in the collateralised debt obligation (including CLO), leveraged finance and fixed income markets have resulted in substantial fluctuations in prices for leveraged loans and high- yield debt securities and limited liquidity for such instruments. No assurance can be made that conditions giving rise to similar price fluctuations and limited liquidity may not emerge following the Issue Date. During periods of limited liquidity and higher price volatility, the Issuer’s ability to acquire or dispose of Collateral Debt Obligations at a price and time that the Issuer deems advantageous may be severely impaired. As a result, in periods of rising market prices, the Issuer may be unable to participate in price increases fully to the extent that it is unable to acquire desired positions quickly; and the Issuer’s inability to dispose fully and promptly of positions in declining markets may exacerbate losses suffered by the Issuer when Collateral Debt Obligations are sold. Furthermore, significant additional risks for the Issuer""",
        {"entities": []}
    ),
    (
        """Article 50 of the Treaty on European Union (“Article 50”) provides that a Member State which decides to withdraw from the EU is required to notify the European Council of its intention to do so.""",
        {"entities": [(0, 57, "Reference")]}
    ),
    (
        """The UK government gave formal notice of the UK’s intention to withdraw from the EU pursuant to Article 50 on 29 March 2017, which triggered the commencement of a negotiation process between the UK and the EU in respect of the arrangements for the UK’s withdrawal from the EU. Article 50 provides for a two year period for such negotiations to take place (unless the European Council, in agreement with the UK, unanimously decides to extend this period in respect of which, please see below) (the “Article 50 Period”).""",
        {"entities": [(95, 122, "Reference"), (276, 286,
                                               "Reference"), (492, 515, "Reference")]}
    ),
    (
        """The Investment Manager shall notify the Issuer, the Trustee, the Collateral Administrator, each Hedge Counterparty and the Principal Paying Agent in writing upon satisfaction of all of the conditions set out in this Condition 7(b) (Optional Redemption) and shall arrange for liquidation and/or realisation of the Portfolio in whole or in part as necessary, on behalf of the Issuer in accordance with the Investment Management and Collateral Administration Agreement. The Issuer shall deposit, or cause to be deposited, the funds required for an optional redemption of the Notes in accordance with this Condition 7(b) (Optional Redemption) in the Payment Account on or prior to the applicable Redemption Date. Principal Proceeds and Interest Proceeds received in connection with a redemption in whole of all the Rated Notes shall be payable in accordance with the""",
        {"entities": []}
    ),
    (
        """The Issuer shall procure that notice of any redemption in accordance with this Condition 7 (Redemption and Purchase) (which notice shall be irrevocable) is given to the Trustee and Noteholders in accordance with Condition 16 (Notices) and promptly in writing to the Rating Agencies and each Hedge Counterparty.""",
        {"entities": []}
    ),
    (
        """Subject as provided below, if the Issuer certifies to (upon which certification the Trustee may rely without further enquiry) the Trustee that it has or will on the occasion of the next payment due in respect of the Notes of any Class become obliged by the laws of Ireland to withhold or account for tax so that it would be unable to make payment of the full amount that would otherwise be due because of the imposition of such tax, the Issuer (save as provided below) shall use all reasonable endeavours to arrange for the substitution of a company incorporated in another jurisdiction approved by the Trustee as the principal obligor under the Notes of such Class, or to change its tax residence to another jurisdiction approved by the Trustee, subject to receipt of Rating Agency Confirmation in relation to such change and in accordance with the Trust Deed. Notwithstanding the above, if any taxes referred to in this Condition 9 (Taxation) arise:""",
        {"entities": []}
    ),
    (
        """10. Events of Default""",
        {"entities": []}
    ),
    (
        """the Issuer fails to pay any interest in respect of any Class X Notes, Class A Notes or Class B Notes, when the same becomes due and payable (save, in each case, as the result of any deduction therefrom or the imposition of withholding thereon in the circumstances described in Condition 9 (Taxation)) and failure to pay such interest in such circumstances continues for a period of at least five consecutive Business Days provided that, in the case of a failure to disburse due to an administrative error or omission by the Investment Manager, the Collateral Administrator or any Paying Agent, such failure continues for a period of at least seven consecutive Business Days, after the Investment Manager, the Collateral Administrator or such Paying Agent receives written notice of, or has actual knowledge of, such administrative error or omission;""",
        {"entities": []}
    ),
    (
        """to make any changes necessary to reflect any additional issuances of Notes in accordance with Condition 17 (Additional Issuances) or, subject to the consent of the Subordinated Noteholders acting by Ordinary Resolution (as provided for thereunder), to issue replacement notes in accordance with Condition 7(b)(v) (Optional Redemption effected in whole or in part through Refinancing);""",
        {"entities": []}
    ),
    (
        """to modify the Transaction Documents in order to comply with Rule 17g-5 of the Exchange Act; to modify the terms of the Transaction Documents in order that they may be consistent with the""",
        {"entities": [(60, 90, "Reference")]}
    ),
    (
        """to make such changes as shall be necessary to facilitate the Issuer to effect a Refinancing in part in accordance with Condition 7(b)(v) (Optional Redemption effected in whole or in part through Refinancing) subject to the consent of the Subordinated Noteholders acting by Ordinary Resolution as provided for thereunder;""",
        {"entities": []}
    ),
    (
        """to make any modification or amendment determined by the Issuer, as advised by the Investment Manager (in consultation with legal counsel experienced in such matters), as necessary or advisable for any Class of Rated Notes to not be considered an “ownership interest” as defined for the purposes of section 13 of the U.S. Bank Holding Company Act of 1956, as amended, and the applicable rules and regulations thereunder, provided that: such modification or amendment would not, in the opinion of the Issuer, be materially prejudicial to the interests of the Noteholders of any Class;""",
        {"entities": [(298, 353, "Reference")]}
    ),
    (
        """replace references to “LIBOR”, “EURIBOR”, “London Interbank Offered Rate” and “Euro Interbank Offered Rate” (or similar terms) to an alternative base rate when used with respect to a Floating Rate Collateral Debt Obligation (and, in respect of Condition 6(e)(i)(E) (Floating Rate of Interest), maintaining, for the avoidance of doubt, the deeming of any reference to such Alternative Base Rate in replacement of the reference to EURIBOR to also be zero for""",
        {"entities": []}
    ),
    (
        """(bb) on any Interest Determination Date one only or none of the Reference Banks providing a quotation required under Condition 6(e)(i) (Floating Rate of Interest); or""",
        {"entities": []}
    ),
    (
        """“Designated Base Rate” means the sum of (a) the Reference Rate Modifier and (b) either (i) the quarterly rate or, following the occurrence of a Frequency Switch Event, the semi-annual rate (and, if applicable the methodology for calculating such rate) formally proposed, recommended or recognised as an industry standard rate (whether by press release, letter, protocol, publication of standard terms or otherwise) as a replacement reference rate for the calculation of the Euro Interbank Offered Rate by the Loan Markets Association or any successor organisation thereto (the “LMA”), or if there is no such LMA reference rate, by the Loan Syndications & Trading Association or any successor organisation thereto (the “LSTA”), or if there is no such LMA reference rate or LSTA reference rate, by the Alternative Reference Rates Committee or any successor organisation thereto (the “ARRC”), or (ii) the quarterly rate or, following the occurrence of a Frequency Switch Event, the semi-annual rate that is used in calculating the interest rate of (x) at least 50 per cent. of the Floating Rate Collateral Debt Obligations (by par amount) or (y) in the commercially reasonable judgment of the Investment Manager, floating rate notes issued in the preceding three months in new issue European collateralised loan obligation transactions, in the case of (x) or (y), as determined by the Investment Manager as of the first day of the Accrual Period during which the Alternative Base Rate amendment is proposed.""",
        {"entities": []}
    ),
    (
        """No person shall have any right to enforce any term or condition of the Note under the Contracts (Rights of Third Parties) Act 1999.""",
        {"entities": [(82, 130, "Reference")]}
    ),
    (
        """THE ISSUER, IN ORDER TO PERMIT THE RATING AGENCIES TO COMPLY WITH THEIR OBLIGATIONS UNDER RULE 17G-5 PROMULGATED UNDER THE EXCHANGE ACT (“RULE 17G-5”), HAS AGREED TO POST (OR HAVE ITS AGENT POST) ON A PASSWORD-PROTECTED INTERNET WEBSITE (THE “RULE 17G-5 WEBSITE”), AT THE SAME TIME SUCH INFORMATION IS PROVIDED TO THE RATING AGENCIES, ALL INFORMATION (WHICH WILL NOT INCLUDE ANY REPORTS FROM THE ISSUER’S INDEPENDENT PUBLIC ACCOUNTANTS) THAT THE ISSUER OR OTHER PARTIES ON ITS BEHALF, INCLUDING THE INVESTMENT MANAGER, PROVIDE TO THE RATING AGENCIES FOR THE PURPOSES OF DETERMINING THE INITIAL CREDIT RATING OF THE RATED NOTES OR UNDERTAKING CREDIT RATING SURVEILLANCE OF THE RATED NOTES; PROVIDED, HOWEVER, THAT, PRIOR TO THE OCCURRENCE OF AN EVENT OF DEFAULT, WITHOUT THE PRIOR WRITTEN CONSENT OF THE INVESTMENT MANAGER NO PARTY OTHER THAN THE ISSUER OR ELAVON FINANCIAL SERVICES DAC MAY PROVIDE INFORMATION TO THE RATING AGENCIES ON THE ISSUER’S BEHALF. ON THE ISSUE DATE, THE ISSUER WILL ENGAGE ELAVON FINANCIAL SERVICES DAC, IN ACCORDANCE WITH THE INVESTMENT MANAGEMENT AND COLLATERAL ADMINISTRATION AGREEMENT, TO ASSIST THE ISSUER IN COMPLYING WITH CERTAIN OF THE POSTING REQUIREMENTS UNDER RULE 17G-5 (IN SUCH CAPACITY, THE “INFORMATION AGENT”). ANY NOTICES OR REQUESTS TO, OR ANY OTHER WRITTEN COMMUNICATIONS WITH OR WRITTEN INFORMATION PROVIDED TO, THE RATING AGENCIES, OR ANY OF ITS OFFICERS, DIRECTORS OR EMPLOYEES, TO BE GIVEN OR PROVIDED TO SUCH RATING AGENCIES PURSUANT TO, IN CONNECTION WITH OR RELATED, DIRECTLY OR INDIRECTLY, TO THE TRUST DEED, THE INVESTMENT MANAGEMENT AND COLLATERAL ADMINISTRATION AGREEMENT, ANY TRANSACTION DOCUMENT RELATING THERETO, THE PORTFOLIO OR THE NOTES, WILL BE IN EACH CASE FURNISHED DIRECTLY TO THE RATING AGENCIES AFTER A COPY HAS BEEN DELIVERED TO THE INFORMATION AGENT OR THE ISSUER FOR POSTING TO THE RULE 17G-5 WEBSITE.""",
        {"entities": [(119, 150, "Reference")]}
    ),
    (
        """The Issuer was incorporated in Ireland as a designated activity company limited by shares on 2 August 2018 under the name BlueMountain Fuji EUR CLO V DAC, with company registration number 631461 pursuant to the Companies Acts. The registered office of the Issuer is at 3rd Floor, Kilmore House, Park Lane, Spencer Dock, Dublin 1, Ireland. The telephone number of the Issuer is +353 (0) 1 614 6240""",
        {"entities": [(207, 225, "Reference")]}
    ),
    (
        """Article 3(4) of the regulatory technical standards adopted by the EU Commission on 12 March 2014 provides that, where the securitised exposures are created by multiple originators (as is the case in a managed CLO, where assets are acquired from numerous sellers in the market), the EU Retention and Transparency Requirements may be fulfilled in full by a single originator in circumstances where the relevant originator has established and is managing the scheme.""",
        {"entities": [(0, 50, "Reference")]}
    ),
    (
        """The Investment Manager may cause the Issuer to acquire certain assets for the purposes of paragraph (b) of the definition of “Originator” under the Securitisation Regulation which are intended to form part of the Collateral Debt Obligations (“Limb (b) Originated Assets”), pursuant to a conditional sale agreement (“Conditional Sale Agreement”) between the Investment Manager (as purchaser) and the Issuer (as seller) under which the Issuer shall, in the event any such Originated Assets becomes a Defaulted Obligation within 15 Business Days of the date upon which the Issuer (or the Investment Manager on its behalf) entered into a binding commitment to acquire the relevant Collateral Debt Obligation (the “Seasoning Period”), have the right to require the Investment Manager to purchase from it the relevant Originated Assets for the same purchase price as the Issuer committed to purchase and settle such Originated Assets.""",
        {"entities": []}
    ),
    (
        """In accordance with Article 7(2) of the Securitisation Regulation, each of the originator, the sponsor and the Issuer are required to designate amongst themselves one entity to fulfil the Transparency Requirements. The Issuer has agreed to be the designated entity.""",
        {"entities": [(19, 64, "Reference")]}
    ),
    (
        """In addition, in relation to the reporting obligations in the EU Retention and Transparency Requirements, (a) the Issuer will be designated as the entity responsible to fulfil such reporting obligations, (b) the Investment Manager shall on behalf of and at the expense of the Issuer, provide to the Collateral Administrator (and/or any applicable third party reporting entity) and the Issuer any reports, data and other information (or access to such other information) which (i) is in the possession of the Investment Manager, (ii) is not subject to legal or contractual restrictions on its disclosure, (iii) the Collateral Administrator or the Issuer does not otherwise have access, is not already required to be provided to the Issuer directly, or is not otherwise in the Issuer's possession (in each case, as applicable), and (iv) is required by the Collateral Administrator and the Issuer in connection with the proper performance by the Issuer, as the designated entity, of its obligation to make available to the Noteholders, potential investors in the Notes and the competent authorities the reports, data and other information necessary to fulfil the reporting requirements of the Transparency Requirements; provided that, prior to the entry into force of final disclosure templates in respect of the Transparency Requirements (A) the Issuer intends to fulfil those requirements contained in subparagraphs (a) and (e) of Article 7(1) of the Securitisation Regulation through the provision of the Monthly Reports and the Payment Date Reports (see "Description of the Reports") and (B) the Investment Manager shall not be required to provide any reports, data or other information (other than such""",
        {"entities": [(1429, 1474, "Reference")]}
    ),
    (
        """information and data necessary for completion of the Monthly Reports and the Payment Date Reports) in connection with the reporting requirements contained in subparagraphs (a) and (e) of Article 7(1) of the Securitisation Regulation to the Issuer pursuant to the Investment Management and Collateral Administration Agreement prior to the entry into force of such final disclosure templates. Once the Transparency RTS apply, the Loan Reports and Investor Reports will be prepared in accordance with the requirements of the Transparency RTS. The Issuer, with the consent of the Investment Manager, will propose in writing to the Collateral Administrator the form, content, method of distribution and timing of such reports and other information. The Collateral Administrator shall consult with the Issuer and the Investment Manager and, if it agrees to assist the Issuer in providing such reporting on such proposed terms, shall confirm such agreement in writing to the Issuer and the Investment Manager and shall make such information (as provided to it by the Issuer (or the Investment Manager on behalf of the Issuer)) available via a website (or procure that such information is made available) currently located at https://pivot.usbank.com (or such other website as may be notified in writing by the Collateral Administrator to the Issuer, the Trustee, the Investment Manager, the Arranger, the Initial Purchaser, the Registrar, each Hedge Counterparty, the Rating Agencies, Bloomberg L.P., Intex Solutions Inc. and the Noteholders in accordance with Condition 16 (Notices)) which shall be accessible to any person (x) who certifies to the Collateral Administrator (such certification to be in the form set out in the Investment Management and Collateral Administration Agreement, which may be given electronically and upon which the Collateral Administrator shall be entitled to rely absolutely and without enquiry or liability) that it is: (i) the Issuer, (ii) the Trustee, (iii) the Investment Manager, (iv) the Arranger, (v) the Initial Purchaser, (vi) a Hedge Counterparty, (vii) a Rating Agency;""",
        {"entities": [(187, 232, "Reference")]}
    ),
    (
        """The Originator, as an entity established in a country outside the European Union and in its capacity as an “originator” for the purposes of the EU Retention and Transparency Requirements, reasonably believes, having made such enquiries as would be reasonable in the circumstances, that it has (i) used adequate resources and has made reasonable efforts to obtain as much information as is available and appropriate to make the verification in Article 9(3) of the Securitisation Regulation in accordance with market standards of due diligence for the class of assets and the nature and type of securitisation; and (ii) granted all the credits giving rise to the underlying exposures on the basis of sound and well-defined criteria and clearly established processes for approving, amending, renewing and financing those credits and has effective systems in place to apply those criteria and processes to ensure that credit-granting is based on a thorough assessment of the obligor’s creditworthiness.""",
        {"entities": [(443, 488, "Reference")]}
    ),
    (
        """it will not require the Issuer or the Collateral to be registered as an investment company under the Investment Company Act;""",
        {"entities": [(97, 123, "Reference")]}
    ),
    (
        """its acquisition by the Issuer will not result in the Issuer being required to be authorised as, or to appoint a “credit servicing firm” within the meaning of the Central Bank Act 1997 of Ireland (as amended);""",
        {"entities": [(158, 194, "Reference")]}
    ),
    (
        """(iv) shall not (a) cause the Issuer, or the Portfolio to become required to register as an investment company under the provisions of the Investment Company Act, (b) subject the Issuer to taxation in any jurisdiction (including states and localities) where it would otherwise not be subject to tax or (c) cause the Issuer to be engaged in a trade or business in the United States for U.S. federal income tax purposes;""",
        {"entities": [(134, 160, "Reference")]}
    ),
    (
        """the appointment of it will not cause either of the Issuer or the Collateral to become required to register under the provisions of the Investment Company Act;""",
        {"entities": [(131, 157, "Reference")]}
    ),
    (
        """The Notes have not been and will not be registered under the Securities Act and may not be offered, sold or delivered within the United States or to, or for the account or benefit of, U.S. Persons or to U.S. residents (as determined for the purposes of the Investment Company Act) (“U.S. Residents”) except in certain transactions exempt from, or not subject to, the registration requirements of the Securities Act and in the manner so as not to require the registration of the Issuer as an “investment company” pursuant to the Investment Company Act.""",
        {"entities": [(253, 279, "Reference"), (398, 414,
                                                "Reference"), (525, 550, "Reference")]}
    ),
    (
        """Any offer or sale of Notes that are Rule 144A Notes in reliance on Rule 144A will be made by broker dealers who are registered as such under the Exchange Act. After the Notes are released for sale, the offering price and other selling terms may from time to time be varied by the Initial Purchaser.""",
        {"entities": [(141, 157, "Reference")]}
    ),
    (
        """(i) Regulation (EU) 2017/1129 of the European Parliament and of the Council of 14 June 2017 on the prospectus to be published when securities are offered to the public or admitted to trading on a regulated market and any applicable supporting law, rule or regulation and any Central Bank of Ireland (“Central Bank”) rules issued and / or in force pursuant to Section 1363 of the Companies Act 2014 (as amended) (the “Companies Act”);""",
        {"entities": [(4, 56, "Reference"), (359, 397,
                                             "Reference"), (412, 431, "Reference")]}
    ),
    (
        """(ii) the Companies Act;""",
        {"entities": [(5, 22, "Reference")]}
    ),
    (
        """(iv) Regulation (EU) No 596/2014 of the European Parliament and of the Council of 16 April 2014 on market abuse, the European Union (Market Abuse) Regulations 2016 and any Central Bank rules issued and / or in force pursuant to Section 1370 of the Companies Act;""",
        {"entities": [(5, 59, "Reference"), (228, 261, "Reference")]}
    ),
    (
        """(vi) the Central Bank Acts 1942 to 2018 (as amended) and any codes of conduct rules made under Section 117(1) of the Central Bank Act 1989.""",
        {"entities": [(5, 39, "Reference"), (95, 139, "Reference")]}
    ),
    (
        """Japan: The Notes have not been and will not be registered under the Financial Instruments and Exchange Act of Japan (Act No. 25 of 1948, as amended; the FIEA) and the Initial Purchaser has represented and agreed that none of the Notes nor any interest therein will be offered or sold, directly or indirectly, in Japan or to, or for the benefit of, any resident of Japan (as defined under Item 5, Paragraph 1, Article 6 of the Foreign Exchange and Foreign Trade Act (Act No. 228 of 1949, as amended)), or to others for re- offering or resale, directly or indirectly, in Japan or to, or for the benefit of, a resident of Japan except pursuant to an exemption from the registration requirements of, and otherwise in compliance with, the FIEA and any other applicable laws, regulations and ministerial guidelines of Japan.""",
        {"entities": [(64, 115, "Reference"), (117, 135, "Reference"),
                      (388, 464, "Reference"), (466, 486, "Reference")]}
    ),
    (
        """Switzerland: Notes qualifying as structured products according to article 5 of the Collective Investment Schemes Act (“CISA”) may be distributed to non-qualified investors (nicht-qualifizierte Anlegerinnen und Anleger) in or from Switzerland either (i) by means of a listing of such Notes on the SIX Swiss Exchange, or (ii) by means of making available a simplified Prospectus relating to such Notes pursuant to article 5 of the CISA. If neither of these requirements is met, then such Notes may only be distributed to Qualified Investors in Switzerland. In such case, this Offering Circular shall not be despatched, copied to or otherwise made available to, and the Notes may not be offered for sale to any person in Switzerland,""",
        {"entities": [(66, 125, "Reference"), (419, 433, "Reference")]}
    ),
    (
        """Rule 144A Notes""",
        {"entities": []}
    )
]


def train_custom_ner():
    model = None
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
        for itn in range(1000):
            random.shuffle(TRAIN_DATA)
            losses = {}
            batches = minibatch(TRAIN_DATA, size=compounding(4., 32., 1.001))
            for batch in batches:
                texts, annotations = zip(*batch)
                nlp.update(texts, annotations, sgd=optimizer, drop=0.35,
                           losses=losses)
            print('Losses', losses)
    nlp.max_length = 200000000

    output_dir = "act_model"
    if output_dir is not None:
        output_dir = Path(output_dir)
        if not output_dir.exists():
            output_dir.mkdir()
        nlp.meta['name'] = "CustomNER"  # rename model
        nlp.to_disk(output_dir)
        print("Saved model to", output_dir)

    with open('sample/a310bb91.p.html.293e9e18.txt', 'r', encoding='utf-8') as file:
        all_of_it = file.read()
        doc = nlp(all_of_it)
        displacy.serve(doc, style="ent")

    # with open('sample/eurlex_01.txt', 'r', encoding='utf-8') as file:
    #     all_of_it = file.read()
    #     doc = nlp(all_of_it)
    #     displacy.serve(doc, style="ent")

    # Test the trained model
    test_text = """If the Issuer becomes subject to an insolvency proceeding and the Issuer has obligations to creditors that are treated under Irish law as creditors that are senior relative to the Noteholders and other Secured Parties, the Noteholders (and other Secured Parties) may suffer losses as a result of their subordinated status during such insolvency proceedings. In particular, under Irish law, upon an insolvency of an Irish company, such as the Issuer, when applying the proceeds of assets subject to fixed security which may have been realised in the course of a liquidation or receivership, the claims of a limited category of preferential creditors will take priority over the claims of creditors holding the relevant fixed security. These preferred claims include the remuneration, costs and expenses properly incurred by any examiner of the company (which may include any borrowings made by an examiner to fund the company’s requirements for the duration of his appointment) which have been approved by the relevant Irish courts. See 7.3 “Examinership”."""
    # test_text = """The Issuer will depend upon the Asset Swap Counterparty to perform its obligations under any hedges. If the Asset Swap Counterparty defaults or becomes unable to perform due to insolvency or otherwise, the Issuer may not receive payments it would otherwise be entitled to from the Asset Swap Counterparty to cover its foreign exchange exposure."""
    doc = nlp(test_text)
    print("Entities")
    for ent in doc.ents:
        print("lab:", ent.label_, ent.text)


if __name__ == "__main__":
    nlp = spacy.load("en_core_web_sm")
    train_custom_ner()
