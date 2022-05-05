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


LABEL = ['Cause', 'Effect']

TRAIN_DATA = [
    (
        """The credit rating of a country affects the ratings of entities operating in its territory, and in particular the ratings of financial institutions. Accordingly, such downgrades of the UK’s sovereign credit rating and any further downgrade action may trigger downgrades in respect of parties to the Transaction Documents. If a counterparty no longer satisfies the relevant Rating Requirement, the Transaction Documents may require that such counterparty be replaced with an entity that satisfies the relevant Rating Requirement. If rating downgrades are widespread, it may become difficult or impossible to replace counterparties with entities that satisfy the relevant Rating Requirement.""",
        {"entities": [(321, 526, "Conditional"), (528, 686, "Conditional")]}
    ),
    (
        """In Europe, the U.S. and elsewhere there has been, and there continues to be increased political and regulatory scrutiny of banks, financial institutions, “shadow banking entities” and the asset-backed securities industry. This has resulted in a raft of measures for increased regulation which are currently at various stages of implementation and which may have an adverse impact on the regulatory capital charge to certain investors in securitisation exposures and/or the incentives for certain investors to hold or trade asset-backed securities, and may thereby affect the liquidity of such securities.""",
        {"entities": []}
    ),
    (
        """If any determination is made that this transaction is subject to the U.S. Risk Retention Rules, the Collateral Manager may fail to comply (or not be able to comply) with the U.S. Risk Retention Rules, which may have a material adverse effect on the Collateral Manager, the Issuer and/or the market value and/or liquidity of the Notes.""",
        {"entities": [(0, 332, "Conditional")]}
    ),
    (
        """IFMD introduced authorisation and regulatory requirements for managers of AIFs. If the Issuer were to be considered to be an AIF within the meaning in AIFMD, it would need to be managed by a manager authorised under AIFMD (an “AIFM”). The Collateral Manager is not authorised under AIFMD but is authorised under MiFID II. If considered to be an AIF, the Issuer would also be classified as an FC under EMIR and may be required to comply with clearing obligations and/or other risk mitigation techniques (including obligations to post margin to any central clearing counterparty or market counterparty) with respect to Hedge Transactions (under the EMIR REFIT all AIFs will be FCs whether or not managed by an authorised AIFM). See also “European Market Infrastructure Regulation (EMIR)” above.""",
        {"entities": [(80, 233, "Conditional"), (321, 790, "Conditional")]}
    ),
    (
        """If the SSPE Exemption does not apply and the Issuer is considered to be an AIF, the Collateral Manager may not be able to continue to manage the Issuer’s assets, or its ability to do so may be impaired. As a result, any application of the AIFMD may affect the return investors receive from their investment""",
        {"entities": [(0, 307, "Conditional")]}
    ),
    (
        """The Issuer (or the Investment Manager acting on behalf of the Issuer) reserves the right to request such information as is necessary to verify the identity of a Noteholder and the source of the payment of subscription monies, or as is necessary to comply with any customer identification programs required by FinCEN and/or the SEC or any other applicable AML Requirements. If there is a delay or failure by the applicant to produce any information required for verification purposes, an application for or transfer of Notes and the subscription monies relating thereto may be refused.""",
        {"entities": [(372, 583, "Conditional")]}
    ),
    (
        """If there is an early redemption, the holders of the Notes will be repaid prior to the Maturity Date. Where the Notes are to be redeemed by liquidation, there can be no assurance that the Sale Proceeds realised and other available funds would permit any distribution on the Subordinated Notes after all required payments are made to the holders of the Rated Notes. In addition, an Optional Redemption could require the Investment Manager to liquidate positions more rapidly than would otherwise be desirable, which could adversely affect the realised value of the Collateral Debt Obligations sold.""",
        {"entities": [(0, 99, "Conditional")]}
    ),
    (
        """If at any time one or more investors that are affiliated hold a majority of any Class of Notes, it may be more difficult for other investors to take certain actions that require consent of any such Classes of Notes without their consent. For example, optional redemption and the removal of the Investment Manager for cause and appointment are at the direction of Noteholders of specified percentages of Subordinated Notes and/or the Controlling Class (as applicable).""",
        {"entities": [(0, 236, "Conditional")]}
    ),
    (
        """If a Hedge Counterparty is subject to a rating withdrawal or downgrade by the Rating Agencies to below the applicable Rating Requirement, there will generally be a termination event under the applicable Hedge Agreement unless, within the applicable grace period following such rating withdrawal or downgrade, such Hedge Counterparty either transfers its obligations under the applicable Hedge Agreement to a replacement counterparty with the requisite ratings, obtains a guarantee of its obligations by a guarantor with the requisite ratings, collateralises its obligations in a manner satisfactory to the Rating Agencies or employs some other strategy as may be approved by the Rating Agencies.""",
        {"entities": [(0, 217, "Conditional")]}
    ),
    (
        """The Issuer will depend upon the Asset Swap Counterparty to perform its obligations under any hedges. If the Asset Swap Counterparty defaults or becomes unable to perform due to insolvency or otherwise, the Issuer may not receive payments it would otherwise be entitled to from the Asset Swap Counterparty to cover its foreign exchange exposure.""",
        {"entities": [(101, 343, "Conditional")]}
    ),
    (
        """In considering proposals by the examiner, it is likely that secured and unsecured creditors would form separate classes of creditors. In the case of the Issuer, if the Trustee represented the majority in number and value of claims within the secured creditor class, the Trustee would be in a position to reject any proposal not in favour of the Noteholders. The Trustee would also be entitled to argue at the relevant Irish court hearing at which the proposed scheme of arrangement is considered that the proposals are unfair and inequitable in relation to the Noteholders, especially if such proposals included a writing down to the value of amounts due by the Issuer to the Noteholders.""",
        {"entities": [(160, 356, "Conditional")]}
    ),
    (
        """The Issuer will depend upon the Asset Swap Counterparty to perform its obligations under any hedges. If the Asset Swap Counterparty defaults or becomes unable to perform due to insolvency or otherwise, the Issuer may not receive payments it would otherwise be entitled to from the Asset Swap Counterparty to cover its foreign exchange exposure.""",
        {"entities": [(100, 343, "Conditional")]}
    ),
    (
        """“Principal Proceeds” means all amounts paid or payable into the Principal Account from time to time and, with respect to any Payment Date, means Principal Proceeds received or receivable by the Issuer during the related Due Period and any other amounts to be disbursed as Principal Proceeds on such Payment Date pursuant to Condition 3(c)(ii) (Application of Principal Proceeds) or Condition 11(b) (Enforcement).""",
        {"entities": []}
    ),
    (
        """“Rating Agencies” means S&P and Fitch, provided that if at any time S&P and/or Fitch ceases to provide rating services, “Rating Agencies” shall mean any other nationally recognised investment rating agency or rating agencies (as applicable) selected by the Issuer (a “Replacement Rating Agency”) and “Rating Agency” means any such rating agency. If at any time a Rating Agency is replaced by a Replacement Rating Agency, references to rating categories of the original Rating Agency in these Conditions, the Trust Deed and the Investment Management and Collateral Administration Agreement shall be deemed instead to be references to the equivalent categories of the relevant Replacement Rating Agency as of the most recent date on which such other rating agency published ratings for the type of security in respect of which such Replacement Rating Agency is used and all references herein to “Rating Agencies” shall be construed accordingly. Any rating agency shall cease to be a Rating Agency if, at any time, it ceases to assign a rating in respect of any Class of Rated Notes.""",
        {"entities": [(52, 344, "Conditional"), (345, 941,
                                                 "Conditional"), (942, 1079, "Conditional")]}
    ),
    (
        """The Collateral Manager is not authorised under AIFMD but is authorised under MiFID II. If considered to be an AIF, the Issuer would also be classified as an FC under EMIR and may be required to comply with clearing obligations and/or other risk mitigation techniques (including obligations to post margin to any central clearing counterparty or market counterparty) with respect to Hedge Transactions (under the EMIR REFIT all AIFs will be FCs whether or not managed by an authorised AIFM). See also “European Market Infrastructure Regulation (EMIR)” above.""",
        {"entities": [(85, 489, "Conditional")]}
    ),
    (
        """If the Collateral Manager elects to file for a registration exemption under CFTC Rule 4.13(a)(3), then unlike a CFTC-registered CPO, the Collateral Manager would not be required to deliver a CFTC-mandated disclosure document or a certified annual report to investors, or otherwise comply with the requirements applicable to CFTC-registered CPOs and CTAs. Utilising any such exemption from registration may impose additional costs on the Collateral Manager and the Issuer and may significantly limit the Collateral Manager’s ability to engage in hedging activities on behalf of the Issuer.""",
        {"entities": [(0, 353, "Conditional")]}
    ),
    (
        """Further, if the Collateral Manager determines that additional Hedge Transactions should be entered into by the Issuer in excess of the trading limitations set forth in any applicable exemption from registration as a CPO and/or a CTA, the Collateral Manager may elect to withdraw its exemption from registration and instead register with the CFTC as the Issuer’s CPO and/or CTA.""",
        {"entities": [(8, 376, "Conditional")]}
    ),
    (
        """If the Issuer is deemed to be a “covered fund”, the provisions of the Volcker Rule and its related regulatory provisions, will severely limit the ability of “banking entities” to hold an “ownership interest” in the Issuer or enter into certain credit related financial transactions with the Issuer. Any entity that is a “banking entity” as defined under the Volcker Rule and is considering an investment in “ownership interests” of the Issuer should consult its own legal advisors and consider the potential impact of the Volcker Rule in respect of such investment. If investment by “banking entities” in the Notes of any Class is prohibited or restricted by the Volcker Rule, this could impair the marketability and liquidity of such Notes.""",
        {"entities": [(0, 297, "Conditional"), (565, 740, "Conditional")]}
    ),
    (
        """The Dodd-Frank Act requires that federal banking agencies amend their regulations to remove reference to or reliance on credit agency ratings, including but not limited to those found in the federal banking agencies’ risk-based capital regulations. Investments in asset-backed securities like the Notes by such institutions may result in greater capital charges to financial institutions that own such securities, or otherwise adversely affect the treatment of such securities for regulatory capital purposes. Changes in capital requirements have been announced by the Basel Committee on Banking Supervision and it is uncertain when all such changes will be fully implemented. When fully implemented, investments in asset-backed securities like the Notes by such institutions may result in greater capital charges to financial institutions that own such securities, or otherwise adversely affect the treatment of such securities for regulatory capital purposes. Furthermore, all prospective investors in the Notes whose investment activities are subject to legal investment laws and regulations, regulatory capital requirements, or review by regulatory authorities should consult with their own legal, accounting and other advisors in determining whether, and to what extent, the Notes will constitute legal investments for them or are subject to investment or other regulatory restrictions, unfavourable accounting treatment, capital charges or reserve requirements.""",
        {"entities": []}
    ),
    (
        """It is possible that the LIBOR administrator, ICE Benchmark Administration, and the panel banks could continue to produce LIBOR on the current basis after 2021, if they are willing and able to do so. However, the survival of LIBOR in its current form, or at all, is not guaranteed after 2021. If LIBOR does not survive in its current form or at all, this could adversely affect the value of, and amounts payable under, any Collateral Debt Obligations which pay interest calculated with reference to LIBOR and therefore reduce amounts which may be available to the Issuer to pay Noteholders. Furthermore, the uncertainty as to whether LIBOR will survive in its current form or at all may lead to adverse market conditions, which may have an adverse effect on the amounts available to the Issuer to pay to Noteholders.""",
        {"entities": [(0, 197, "Conditional"), (291, 588, "Conditional")]}
    ),
    (
        """If the Issuer becomes subject to the clearing obligation or to the margin requirement, it is unlikely that it would be able to comply with such requirements, which would adversely affect the Issuer’s ability to enter into Hedge Transactions or significantly increase the cost thereof, negatively affecting the Issuer’s ability to acquire Non-Euro Obligations and/or hedge its interest rate risk. As a result of such increased costs, additional regulatory requirements and limitations on the ability of the Issuer to hedge interest rate and currency risk, the amounts payable to Noteholders may be negatively affected as the Collateral Manager may be precluded from executing its investment strategy in full.""",
        {"entities": [(0, 394, "Conditional")]}
    ),
    (
        """There is an exemption from the definition of AIF in AIFMD for “SSPEs” (the “SSPE Exemption”). The European Securities and Markets Authority (“ESMA”) has not yet given any formal guidance on the application of the SSPE Exemption or whether a vehicle such as the Issuer would fall within it. However, as regards the position in Ireland, the Central Bank of Ireland (the “Central Bank”) has confirmed that pending such further clarification from ESMA, “registered financial vehicle corporations” with the meaning of Article 1(2) of Regulation (EC) No 24/2009 of the European Central Bank (which has now been recast pursuant to Regulation (EU) No 1075/2013 of the European Central Bank), such as the Issuer, do not need to seek authorisation as an AIF or appoint an AIFM unless the Central Bank issues further guidance advising them to do so.""",
        {"entities": []}
    ),
    (
        """If the SSPE Exemption does not apply and the Issuer is considered to be an AIF, the Collateral Manager may not be able to continue to manage the Issuer’s assets, or its ability to do so may be impaired. As a result, any application of the AIFMD may affect the return investors receive from their investment.""",
        {"entities": [(0, 201, "Conditional")]}
    ),
    (
        """Further, if the Collateral Manager determines that additional Hedge Transactions should be entered into by the Issuer in excess of the trading limitations set forth in any applicable exemption from registration as a CPO and/or a CTA, the Collateral Manager may elect to withdraw its exemption from registration and instead register with the CFTC as the Issuer’s CPO and/or CTA. The costs of obtaining and maintaining these registrations and the related compliance obligations may be paid by the Issuer as Administrative Expenses. Such costs would reduce the amount of funds available to make payments on the Notes. These costs are uncertain and could be materially greater than the Collateral Manager anticipated when deciding to enter into the transaction and register as a CPO and/or a CTA. In addition, it may not be possible or advisable for the Collateral Manager to withdraw from registration as a CPO and/or a CTA after any relevant swap transactions terminate or expire. The costs of CPO and/or CTA registration and the ongoing CPO and/or CTA compliance obligations of the Collateral Manager could exceed, perhaps significantly, the financial risks that are being hedged pursuant to any Hedge Transaction.""",
        {"entities": [(8, 376, "Conditional")]}
    ),
    (
        """If the Issuer is deemed to be a “covered fund”, the provisions of the Volcker Rule and its related regulatory provisions, will severely limit the ability of “banking entities” to hold an “ownership interest” in the Issuer or enter into certain credit related financial transactions with the Issuer. Any entity that is a “banking entity” as defined under the Volcker Rule and is considering an investment in “ownership interests” of the Issuer should consult its own legal advisors and consider the potential impact of the Volcker Rule in respect of such investment. If investment by “banking entities” in the Notes of any Class is prohibited or restricted by the Volcker Rule, this could impair the marketability and liquidity of such Notes.""",
        {"entities": [(0, 297, "Conditional"), (565, 740, "Conditional")]}
    ),
    (
        """Moreover, if the Priorities of Payments are the subject of litigation in any jurisdiction outside England and Wales, in particular in the United States of America, and such litigation results in a conflicting judgment in respect of the binding nature of the Priorities of Payments, it is possible that termination payments due to the Hedge Counterparties would not be subordinated as envisaged by the Priorities of Payments and as a result, the Issuer’s ability to repay the Noteholders in full may be adversely affected. There is a particular risk of such conflicting judgments where a Hedge Counterparty is the subject of bankruptcy or insolvency proceedings outside England and Wales.""",
        {"entities": [(9, 520, "Conditional")]}
    ),
    (
        """The Issuer is not aware of any proposal to amend Irish domestic law to remove the exemption from VAT on collateral management fees paid by entities such as the Issuer. However, it is possible that some Member States (including Ireland) could change their domestic VAT laws, or the European Commission could require them to do so. If so, the Issuer could from then be required to account for VAT in Ireland in respect of the Collateral Management Fees. The standard VAT rate in Ireland is currently 23%. It is also possible that Ireland could be required to recover the benefit of the VAT exemption obtained before the date on which the law changes from the Issuer together with interest.""",
        {"entities": [(0, 474, "Conditional")]}
    ),
    (
        """
        
        2.24 U.S. Stay Rules Relating to Qualified Financial Contracts
        
        """,
        {"entities": []}
    ),
    (
        """U.S. regulators have adopted final rules and interpretative guidance setting forth limitations on certain insolvency-related default rights of parties to certain “qualified financial contracts” (“QFCs”) entered into with counterparties that have been designated as systemically important, along with certain of such entities’ subsidiaries and affiliates (each, a “Covered Entity”). Such rules and guidance (the “QFC Stay Rules”) generally require: (i) the Covered Entity to ensure that any stays imposed as a result of the entry of such entity into certain liquidation proceedings are contractually acknowledged by the counterparty to the QFC (in particular, where the relevant QFC is governed by non-U.S. law and/or the counterparty is located in a non-U.S. jurisdiction); and (ii) the Covered Entity to not agree in its QFCs to certain types of cross-defaults that are related, directly or indirectly, to the entry into a receivership, insolvency, liquidation, resolution or similar proceeding of certain affiliates of the Covered Entity. If a Covered Entity enters into a contract with the Issuer that is subject to the QFC Stay Rules, the Covered Entity will be responsible for ensuring that such QFC complies with the QFC Stay Rules. As a result of the application of such rules, the Issuer may be required to accept limitations in its insolvency-related default rights against the Covered Entity.""",
        {"entities": [(1040, 1237, "Conditional")]}
    ),
    (
        """Neither the Arranger nor the Initial Purchaser (or any of their Affiliates) is under any obligation to make a market for the Notes. The Notes are illiquid investments. There can be no assurance that any secondary market for any of the Notes will develop or, if a secondary market does develop, that it will provide the Noteholders with liquidity of investment or that it will continue for the life of such Notes. Consequently, a purchaser must be prepared to hold such Notes for an indefinite period of time or until the Maturity Date. In addition, no sale, assignment, participation, pledge or transfer of the Notes may be effected if, among other things, it would require any of the Issuer or any of their officers or directors to register under, or otherwise be subject to the provisions of, the Investment Company Act or any other similar legislation or regulatory action. Furthermore, the Notes will not be registered under the Securities Act or any U.S. state securities laws, and the Issuer has no plans, and is under no obligation, to register the Notes under the Securities Act. The Notes are subject to certain transfer restrictions and can be transferred only to certain transferees. See “Plan of Distribution” and “Transfer Restrictions”. Such restrictions on the transfer of the Notes may further limit their liquidity.""",
        {"entities": [(257, 534, "Conditional")]}
    ),
    (
        """The Trust Deed provides that the holders of the Subordinated Notes will not have any cause of action against any of the Issuer, the Collateral Manager, the Collateral Administrator, the Initial Purchaser, the Arranger or the Trustee for any failure to obtain a Refinancing. If a Refinancing is obtained meeting the requirements of the Trust Deed, the Issuer may amend the Trust Deed and the Trustee shall concur with such amendments to the Trust Deed to the extent the Issuer certifies to the Trustee that such amendments are necessary to facilitate the Issuer to effect a Refinancing in part. No assurance can be given that any such amendments to the Trust Deed or the terms of any Refinancing will not adversely affect the holders of any Class or Classes of Notes not subject to redemption (or, in the case of the Subordinated Notes, the holders of the Subordinated Notes who do not direct such redemption).""",
        {"entities": []}
    ),
    (
        """The Collateral Manager may also cause the Issuer to redeem the Rated Notes in whole from Sale Proceeds on any Payment Date falling on or after the expiry of the Non-Call Period, if the Aggregate Collateral Balance is less than 20.0 per cent. of the Target Par Amount.""",
        {"entities": [(0, 266, "Conditional")]}
    ),
    (
        """Collateral Manager""",
        {"entities": []}
    ),
    (
        """may""",
        {"entities": []}
    ),
    (
        """The Notes will be subject to redemption in part by the Issuer on any Payment Date during the Reinvestment Period if the Collateral Manager in its sole discretion certifies to the Trustee that it has been unable, for a period of at least 20 consecutive Business Days, to identify additional Collateral Debt Obligations or Substitute Collateral Debt Obligations that are deemed appropriate by the Collateral Manager in its sole discretion and which would meet the Eligibility Criteria and where acquisition by the Issuer would be in compliance with, to the extent applicable, the Reinvestment Criteria in sufficient amounts to permit the investment or reinvestment of all or a portion of the funds then in the Principal Account to be invested in additional Collateral Debt Obligations. On the Special Redemption Date, the Special Redemption Amount will be applied in accordance with the Priorities of Payments. The application of funds in that manner could result in an elimination, deferral or reduction of amounts available to make payments with respect to the Subordinated Notes.""",
        {"entities": [(0, 782, "Conditional")]}
    ),
    (
        """The Reinvestment Period may terminate early if any of the following occur: (a) acceleration following a Note Event of Default or (b) the Collateral Manager certifies to the Issuer, the Collateral Administrator, the Rating Agencies and the Trustee that it is unable to reinvest in additional Collateral Debt Obligations in accordance with the Collateral Management Agreement. Early termination of the Reinvestment Period could adversely affect returns to the Subordinated Noteholders and may also cause the holders of Rated Notes to receive principal payments earlier than anticipated.""",
        {"entities": [(0, 373, "Conditional")]}
    ),
    (
        """After the end of the Reinvestment Period, the Collateral Manager may continue to reinvest Unscheduled Principal Proceeds received in respect of Collateral Debt Obligations and the Sale Proceeds from the sale of Credit Impaired Obligations and Credit Improved Obligations, subject to certain conditions set forth in the Collateral Management Agreement. See “The Portfolio – Management of the Portfolio — Following the Expiry of the Reinvestment Period” below. Reinvestment of Unscheduled Principal Proceeds and Sale Proceeds from the sale of Credit Impaired Obligations and Credit Improved Obligations will likely have the effect of extending the Weighted Average Life of the Collateral Debt Obligations and the average lives of the Notes.""",
        {"entities": []}
    ),
    (
        """The Issuer may issue and sell additional Notes, subject to the satisfaction of a number of conditions, including that the holders of the relevant Class of Notes in respect of which further Notes are issued shall have been afforded the opportunity to purchase additional Notes of the relevant Class in an amount not to exceed the percentage of the relevant Class of Notes each holder held immediately prior to the issuance of such additional Notes. However, this requirement does not apply to any additional issuance of Class M-1 Subordinated Notes if such additional issuance is required in order to prevent or cure an EU Retention Deficiency for any reason including but not limited to where such EU Retention Deficiency will occur due to an additional issuance of any Class of Notes. Accordingly, the proportion of Class M- 1 Subordinated Notes held by a Class M-1 Subordinated Noteholder may be diluted following an additional issuance of Class M-1 Subordinated Notes. See Condition 17 (Additional Issuance).""",
        {"entities": [(447, 784, "Conditional")]}
    ),
    (
        """Each Noteholder will agree, and each beneficial owner of Notes will be deemed to agree, pursuant to the Trust Deed, that it will be subject to non-petition covenants. If such provision failed to be enforceable under applicable bankruptcy laws, and a winding-up (or similar) position was presented in respect of the Issuer, then the presentation of such a petition could (subject to certain Conditions) result in one or more payments on the Notes made during the period prior to such presentation being deemed to be preferential transfers subject to avoidance by the bankruptcy trustee or similar official exercising authority with respect to the Issuer’s bankruptcy estate. It could also result in the bankruptcy court, trustee or receiver liquidating the assets of the Issuer without regard to any votes or directions required for such liquidation pursuant to the Trust Deed and could result in any payments under the Notes made during the period prior to such presentation being deemed to be a fraudulent or improper disposition of the Issuer’s assets.""",
        {"entities": [(166, 672, "Conditional")]}
    ),
    (
        """If a EURIBOR screen rate does not appear, or the relevant page is unavailable, and the Issuer is unable to select Reference Banks to provide quotations in the manner described in Condition 6(e)(i)(B) (Floating Rate of Interest), the relevant Floating Rate of Interest in respect of such Payment Date shall be determined, pursuant to Condition 6(e)(i)(C) (Floating Rate of Interest), as the Floating Rate of Interest in effect as at the immediately preceding Accrual Period that was determined by reference to a EURIBOR screen rate or through quotations provided by four Reference Banks provided that, in respect of any Accrual Period during which a Frequency Switch Event occurs, the relevant Floating Rate of Interest shall be calculated using the offered rate for six month Euro deposits using the rate available as at the previous Interest Determination Date. To the extent interest amounts in respect of the Notes are determined by reference to a previously calculated rate, Noteholders may be adversely affected. In such circumstances, neither the Calculation Agent nor the Trustee shall have any obligation to determine the Floating Rate of Interest on any other basis.""",
        {"entities": [(0, 861, "Conditional")]}
    ),
    (
        """The SEC adopted Rule 15Ga-2 and Rule 17g-10 to the United States Securities Exchange Act of 1934, on 27 August 2014, which require certain filings or certifications to be made in connection with the performance of “due diligence services” for rated asset-backed securities on or after 15 June 2015. Under Rule 17g-10, a provider of third-party due diligence services must provide to each nationally recognised statistical rating organisation that is rating the applicable transaction, a written certification in a prescribed form (which obligation may be satisfied if the Issuer posts such certification in the required form to the Rule 17g-5 website referred to above, maintained in connection with the transaction). In connection with the Effective Date, the Collateral Management Agreement requires an accountant’s agreed upon procedures report to be delivered to the Issuer and the Collateral Manager, and portions of this report may constitute “due diligence services” under Rule 17g-10. Although the Issuer has agreed to post any certification in the required form that it receives in respect of such portion of such report to the Rule 17g-5 website, it is unclear what, if any, other services provided or to be provided by third parties to the Issuer in connection with the transaction described in this Offering Circular, would constitute “due diligence services” under Rule 17g-10. Consequently, no assurance can be given as to whether any certification will be posted by the Issuer or delivered by any applicable third party service provider to the Rating Agencies in circumstances where such certification is deemed to have been required under the rules.""",
        {"entities": [(530, 715, "Conditional"), (1176, 1289, "Conditional")]}
    ),
    (
        """It is anticipated that the net proceeds received by the Issuer on the Issue Date from the issuance of the Notes will be less than the aggregate Principal Amount Outstanding of the Notes in full. Consequently, it is anticipated that on the Issue Date the Collateral would be insufficient to redeem the Notes in full upon the occurrence of a Note Event of Default on or about that date.""",
        {"entities": []}
    ),
    (
        """So long as the Notes remain listed on the Global Exchange Market or another recognised stock exchange for the purposes of Section 64 of the TCA and the Notes are held in a “recognised clearing system” for the purposes of Section 64 of the TCA or interest on the Notes is paid by a paying agent that is not in Ireland, no withholding tax under current law is expected to be imposed in Ireland on payments of interest on the Notes. However there can be no assurance that the law will not change. In addition, as described under Condition 2(i) (Forced transfer pursuant to FATCA), the Issuer is authorised to withhold amounts otherwise distributable to a holder if the holder fails to provide the Issuer or its agents with any correct, complete and accurate information that may be required for the Issuer to comply with FATCA and to prevent the imposition of U.S. federal withholding tax under FATCA on payments to or for the benefit of the Issuer, or if the holder’s ownership of any Notes would otherwise cause the Issuer to be subject to tax under FATCA.""",
        {"entities": [(577, 1054, "Conditional")]}
    ),
    (
        """3.21 Book entry Holders are not Considered Noteholders under the Trust Deed, which may Delay Receipt of Payments on the Notes""",
        {"entities": []}
    ),
    (
        """Holders of beneficial interests in any Notes held in global form will not be considered holders of such Notes under the Trust Deed. After payment of any interest, principal or other amount to the applicable Clearing System, the Issuer will have no responsibility or liability for the payment of such amount by the applicable Clearing System or to any holder of a beneficial interest in a Note. The applicable Clearing System or its nominee will be the sole holder for any Notes held in global form, and therefore each person owning a beneficial interest in a Note held in global form must rely on the procedures of such Clearing System (and if such Person is not a participant in the applicable Clearing System on the procedures of the participant through which such Person holds such interest) with respect to the exercise of any rights of a Noteholder under the Trust Deed.""",
        {"entities": [(641, 874, "Conditional")]}
    ),
    (
        """There are, however, quorum provisions which provide that a minimum number of Noteholders representing a minimum amount of the aggregate Principal Amount Outstanding of the applicable Class or Classes of Notes be present at any meeting to consider an Extraordinary Resolution or an Ordinary Resolution. In the case of an Extraordinary Resolution, this is one or more persons holding or representing not less than 66⅔ per cent. of the aggregate Principal Amount Outstanding of each Class of Notes (or the relevant Class or Classes only, if applicable) and in the case of an Ordinary Resolution this is one or more persons holding or representing not less than 50 per cent. of the aggregate Principal Amount Outstanding of each Class of Notes (or the relevant Class or Classes only, if applicable). Such quorum provisions still, however, require considerably lower thresholds than would be required for a Written Resolution.""",
        {"entities": [(495, 548, "Conditional"), (740, 793, "Conditional")]}
    ),
    (
        """Investors in Class A Notes should be aware that for so long as Class A Notes have not been redeemed and paid in full, if no Class A Notes are held in the form of CM Voting Notes, the Class A Notes will not be entitled to vote in respect of such CM Removal Resolution or CM Replacement Resolution and such right shall pass to a more junior Class of Notes in accordance with the definition of Controlling Class.""",
        {"entities": [(117, 408, "Conditional")]}
    ),
    (
        """Each Hedge Counterparty or Liquidity Facility Provider may also need to be notified and its consent required to the extent provided for in the applicable Hedge Agreement or Liquidity Facility Agreement in respect of a modification, amendment or supplement to any provision of the Transaction Documents. Any such consent, if withheld, may prevent the modification of the Transaction Documents which may be beneficial to or in the best interests of the Noteholders.""",
        {"entities": [(320, 462, "Conditional")]}
    ),
    (
        """Under a regulation of the U.S. Department of Labor, as modified by Section 3(42) of ERISA, if certain employee benefit plans or other retirement arrangements subject to the fiduciary responsibility provisions of Title I of the U.S. Employee Retirement Income Security Act of 1974, as amended, (“ERISA”) or Section 4975 of the U.S. Internal Revenue Code of 1986, as amended, (the “Code”) or entities whose underlying assets are treated as assets of such plans or arrangements (collectively, “Plans”) invest in a Class of Notes that is treated as equity under the regulation (which could include the Class E Notes or the Subordinated Notes), the assets of the Issuer could be considered to be assets of such Plans and certain of the transactions contemplated under such Notes could be considered “prohibited transactions” under Section 406 of ERISA or Section 4975 of the Code. See the section entitled “Certain ERISA Considerations” below.""",
        {"entities": [(90, 937, "Conditional")]}
    ),
    (
        """In addition, the Trust Deed generally provides that, if a Noteholder fails to provide the Issuer or its agents with any correct, complete and accurate information or documentation that may be required for the Issuer to comply with FATCA and to prevent the imposition of tax under FATCA on payments to or for the benefit of the Issuer, or if the Noteholder’s ownership of any Notes would otherwise cause the Issuer to be subject to tax under FATCA, the Issuer is authorised to withhold amounts otherwise distributable to the Noteholder, to compel the Noteholder to sell its Notes, and, if the Noteholder does not sell its Notes within 10 Business Days after notice from the Issuer, to sell the Noteholder’s Notes on behalf of the Noteholder.""",
        {"entities": [(12, 739, "Conditional")]}
    ),
    (
        """If the Issuer were to breach certain of its covenants and acquire certain assets (for example, a “United States real property interest” or an equity interest in an entity that is treated as a partnership for U.S. federal income tax purposes and that is itself engaged in a trade or business in the United States), including upon a foreclosure, or breach certain of its other covenants, the Issuer could be treated as engaged in a U.S. trade or business for U.S. federal income tax purposes. Moreover, a breach of certain of these covenants may not give rise to a Note Event of Default or a Collateral Manager Event of Default and may not give rise to a claim against the Issuer or the Collateral Manager. A change in law or its interpretation also could result in the Issuer being treated as engaged in a trade or business in the United States for U.S. federal income tax purposes, or otherwise subject to U.S. federal income tax on a net income basis. If it is determined that the Issuer is treated as engaged in a trade or business in the United States for U.S. federal income tax purposes, and the Issuer has taxable income that is effectively connected with such U.S. trade or business, the Issuer will be subject under the Code to the regular U.S. corporate income tax on its effectively connected taxable income, which may be imposed on a gross basis, and possibly to a 30 per cent. branch profits tax and state and local taxes as well. The imposition of such a tax liability could materially adversely affect the Issuer’s ability to make payments on the Notes.""",
        {"entities": [(0, 489, "Conditional"), (952, 1441, "Conditional")]}
    ),
    (
        """Under FATCA, the Issuer may be subject to a 30 per cent. withholding tax on certain income. Under an intergovernmental agreement entered into between the United States and Ireland, the Issuer will not be subject to withholding under FATCA if it complies with Irish implementing regulations that require the Issuer to provide the name, address and taxpayer identification number of, and certain other information with respect to, certain holders of Notes to the Office of the Revenue Commissioners of Ireland, which would then provide this information to the IRS. The Issuer shall use reasonable best efforts to comply with the intergovernmental agreement and these regulations; however, there can be no assurance that the Issuer will be able to do so. Moreover, the intergovernmental agreement or the Irish implementing regulations could be amended to require the Issuer to withhold on “passthru” payments to holders that fail to provide certain information to the Issuer or are certain “foreign financial institutions” that do not comply with FATCA.""",
        {"entities": []}
    ),
    (
        """If a Noteholder fails to provide the Issuer or its agents with any correct, complete and accurate information or documentation that may be required for the Issuer to comply with FATCA and to prevent the imposition of tax under FATCA on payments to or for the benefit of the Issuer, or if the Noteholder’s ownership of any Notes would otherwise cause the Issuer to be subject to tax under FATCA, the Issuer is authorised to withhold amounts otherwise distributable to the Noteholder, to compel the Noteholder to sell its Notes, and, if the Noteholder does not sell its Notes within 10 Business Days after notice from the Issuer, to sell the Noteholder’s Notes on behalf of the Noteholder.""",
        {"entities": [(0, 808, "Conditional")]}
    ),
    (
        """The subordination levels of each Class of Notes will be established to withstand certain assumed deficiencies in payment caused by defaults on the related Collateral Debt Obligations. If, however, actual payment deficiencies CONDITIONAL exceed such assumed levels, payments on the relevant Class of Notes could be adversely affected. Whether and by how CONDITIONAL much defaults on the Collateral Debt Obligations adversely affect each Class of Notes will be directly related to the level of subordination thereof pursuant to the Priorities of Payments. The risk that payments on the Notes could be adversely affected by defaults on the related Collateral Debt Obligations is likely to be increased to the extent that the Portfolio of Collateral Debt Obligations is concentrated in any one issuer, industry, region or country as a result of the increased potential for correlated defaults in respect of a single issuer or within a single industry, region or country as a result of downturns relating generally to such industry, region or country. Subject to any confidentiality obligations binding on the Issuer, Noteholders will receive information through the Reports from time to time of the identity of Collateral Debt Obligations which are Defaulted Obligations.""",
        {"entities": [(183, 320, "Conditional")]}
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
        for itn in range(30):
            random.shuffle(TRAIN_DATA)
            losses = {}
            batches = minibatch(TRAIN_DATA, size=compounding(4., 32., 1.001))
            for batch in batches:
                texts, annotations = zip(*batch)
                nlp.update(texts, annotations, sgd=optimizer, drop=0.35,
                           losses=losses)
            print('Losses', losses)
    nlp.max_length = 200000000

    output_dir = "conditional_model"
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


if __name__ == "__main__":
    nlp = spacy.load("en_core_web_sm")
    train_custom_ner()
