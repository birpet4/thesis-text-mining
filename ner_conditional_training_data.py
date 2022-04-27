TRAIN_DATA = [
    (
        """The credit rating of a country affects the ratings of entities operating in its territory, and in particular the ratings of financial institutions. Accordingly, such downgrades of the UK’s sovereign credit rating and any further downgrade action may trigger downgrades in respect of parties to the Transaction Documents. If a counterparty no longer satisfies the relevant Rating Requirement, the Transaction Documents may require that such counterparty be replaced with an entity that satisfies the relevant Rating Requirement. If rating downgrades are widespread, it may become difficult or impossible to replace counterparties with entities that satisfy the relevant Rating Requirement.""",
        {"entities": [(321, 526, "Conditional"),
                      (528, 687, "Conditional")]}
    ),
    (
        """In Europe, the U.S. and elsewhere there has been, and there continues to be increased political and regulatory scrutiny of banks,
        financial institutions, “shadow banking entities” and the asset-backed securities industry. This has resulted in a raft of measures
        for increased regulation which are currently at various stages of implementation and which may have an adverse impact on the regulatory
        capital charge to certain investors in securitisation exposures and/or the incentives for certain investors to hold or trade asset-backed
        securities, and may thereby affect the liquidity of such securities.""",
        {"entities": []}
    ),
    (
        """If any determination is made that this transaction is subject to the U.S. Risk Retention Rules, the Collateral Manager may fail to comply
        (or not be able to comply) with the U.S. Risk Retention Rules, which may have a material adverse effect on the Collateral Manager, the Issuer
        and/or the market value and/or liquidity of the Notes.""",
        {"entities": [(0, 332, "Conditional")]}
    ),
    (
        """IFMD introduced authorisation and regulatory requirements for managers of AIFs. If the Issuer were to be considered to be an AIF within the meaning in AIFMD, it would need to be managed by a manager authorised under AIFMD (an “AIFM”). The Collateral Manager is not authorised under AIFMD but is authorised under MiFID II. If considered to be an AIF, the Issuer would also be classified as an FC under EMIR and may be required to comply with clearing obligations and/or other risk mitigation techniques (including obligations to post margin to any central clearing counterparty or market counterparty) with respect to Hedge Transactions (under the EMIR REFIT
        all AIFs will be FCs whether or not managed by an authorised AIFM). See also “European Market Infrastructure Regulation (EMIR)” above.""",
        {"entities": [(80, 233, "Conditional"),
                      (321, 790, "Conditional")]}
    ),
    (
        """If the SSPE Exemption does not apply and the Issuer is considered to be an AIF, the Collateral Manager may not be
        able to continue to manage the Issuer’s assets, or its ability to do so may be impaired. As a result, any application of
        the AIFMD may affect the return investors receive from their investment""",
        {"entities": [(0, 307, "Conditional")]}
    ),
    (
        """The Issuer (or the Investment Manager acting on behalf of the Issuer) reserves the right to request such information as is necessary to verify the identity of a Noteholder and the source of the payment of subscription monies, or as is necessary to comply with any customer identification programs required by FinCEN and/or the SEC or any other applicable AML Requirements. If there is a delay or failure by the applicant to produce any information required for verification purposes,
        an application for or transfer of Notes and the subscription monies relating thereto may be refused.""",
        {"entities": [(372, 583, "Conditional")]}
    ),
    (
        """If there is an early redemption, the holders of the Notes will be repaid prior to the Maturity Date. Where the Notes are to be redeemed by liquidation, there can be no assurance that the Sale Proceeds realised and other available funds would permit any distribution on the Subordinated Notes after all required payments are made to the holders of the Rated Notes. In addition, an Optional Redemption could require the Investment Manager to liquidate positions more rapidly than would otherwise be desirable,
        which could adversely affect the realised value of the Collateral Debt Obligations sold.""",
        {"entities": [(0, 99, "Conditional")]}
    ),
    (
        """If at any time one or more investors that are affiliated hold a majority of any Class of Notes, it may be more difficult for other investors to take certain actions that require consent of any such Classes of Notes without their consent. For example, optional redemption and the removal of the Investment Manager for cause and appointment
        are at the direction of Noteholders of specified percentages of Subordinated Notes and/or the Controlling Class (as applicable).""",
        {"entities": [(0, 236, "Conditional")]}
    ),
    (
        """If a Hedge Counterparty is subject to a rating withdrawal or downgrade by the Rating Agencies to below the applicable Rating Requirement, there will generally be a termination event under the applicable Hedge Agreement unless, within the applicable grace period following such rating withdrawal or downgrade, such Hedge Counterparty either transfers its obligations under the applicable Hedge Agreement to a replacement counterparty with the requisite ratings, obtains a guarantee of its obligations by a guarantor with the requisite ratings, collateralises its obligations in a manner satisfactory
        to the Rating Agencies or employs some other strategy as may be approved by the Rating Agencies.""",
        {"entities": [(0, 217, "Conditional")]}
    ),
    (
        """The Issuer will depend upon the Asset Swap Counterparty to perform its obligations under any hedges. If the Asset Swap Counterparty defaults or becomes unable to perform due to insolvency or otherwise, the Issuer may not receive payments it would otherwise be entitled to from the Asset Swap Counterparty to cover its foreign exchange exposure.""",
        {"entities": [(101, 343, "Conditional")]}
    ),
    (
        """In considering proposals by the examiner, it is likely that secured and unsecured creditors would form separate classes of creditors. In the case of the Issuer, if the Trustee represented the majority in number and value of claims within the secured creditor class, the Trustee would be in a position to reject any proposal not in favour of the Noteholders. The Trustee would also be entitled to argue at the relevant Irish court hearing at which the proposed scheme of arrangement is considered that the proposals are unfair and inequitable in relation to the Noteholders,
         especially if such proposals included a writing down to the value of amounts due by the Issuer to the Noteholders.""",
        {"entities": [(160, 356, "Conditional")]}
    ),
    (
        """The Issuer will depend upon the Asset Swap Counterparty to perform its obligations under any hedges. If the Asset Swap Counterparty defaults or becomes unable to perform due to insolvency or otherwise, the Issuer may not receive payments it would otherwise be entitled to from the Asset Swap Counterparty to cover its foreign exchange exposure.""",
        {"entities": [(100, 343, "Conditional")]}
    ),
    (
        """“Principal Proceeds” means all amounts paid or payable into the Principal Account from time to time and, with respect to any Payment Date, means Principal Proceeds received or receivable by the Issuer during the related Due Period and any other amounts to be disbursed as Principal Proceeds on such
        Payment Date pursuant to Condition 3(c)(ii) (Application of Principal Proceeds) or Condition 11(b) (Enforcement).""",
        {"entities": []}
    ),
    (
        """In connection with the issue and sale of the Notes, no person is authorised to give any information or to make any representation not contained in this Prospectus and, if given or made, such information or representation must not be relied upon as having been authorised by or on behalf of the Issuer, the Placement Agent, the Trustee, the Collateral Manager, the Retention Holder or the Collateral Administrator.
        The delivery of this Prospectus at any time does not imply that the information contained in it is correct as at any time subsequent to its date.""",
        {"entities": [(51, 412, "Conditional")]}
    ),
    (
        """Where Notes are redeemable at the discretion of a transaction party or a particular Class of Noteholders, there is no obligation to consider the interests of any other party or Class of Noteholders when exercising such discretion. Furthermore, where one or more Classes of Rated Notes are redeemed through a Refinancing, Noteholders should be aware that any such redemption would occur outside of the Note Payment Sequence and the Priorities of Payment. In addition Noteholders of a Class of Rated Notes that are redeemed through a Refinancing should be aware that the Applicable Margin of any new Notes will be equal to or lower than the Applicable Margin of such Rated Notes immediately prior to such Refinancing. In addition, a Refinancing may result in a Class of Rated Notes having a shorter maturity date than other Classes of Rated Notes.""",
        {"entities": [(0, 230, "Conditional"), (231, 453, "Conditional")]}
    ),
    (
        """U.S. Federal Tax Treatment of U.S. Holders of Subordinated Notes""",
        {"entities": []}
    ),
    (
        """(""",
        {"entities": []}
    ),
    (
        """)""",
        {"entities": []}
    ),
    (
        """This extent will not be taxable to such U.S. Holder.""",
        {"entities": []}
    ),
    (
        """The EU Bank Recovery and Resolution Directive (2014/59/EU) (collectively with secondary and implementing EU rules, and national implementing legislation, the “BRRD”) equips national authorities in Member States (the “Resolution Authorities”) with tools and powers for preparatory and preventive measures, early supervisory intervention and resolution of credit institutions and significant investment firms (collectively, “relevant institutions”). If a relevant institution enters into an arrangement with the Issuer and is deemed likely to fail in the circumstances identified in the BRRD, the relevant Resolution Authority may employ such tools and powers in order to intervene in the relevant institution’s failure (including in the case of derivatives transactions, powers to close-out such transactions or suspend any rights to close-out such transactions). In particular, liabilities of relevant institutions arising out of the Transaction Documents or Underlying Instruments (for example, liabilities arising under Participations or provisions in Underlying Instruments requiring lenders to share amounts) not otherwise subject to an exception, could be subject to the exercise of “bail-in” powers of the relevant Resolution Authorities. It should be noted that certain secured liabilities of relevant institutions are excepted. If the relevant Resolution Authority decides to “bail-in” the liabilities of a relevant institution, then subject to certain exceptions set out in the BRRD, the liabilities of such relevant institution could, among other things, be reduced, converted or extinguished in full. As a result, the Issuer and ultimately, the Noteholders may not be able to recover any liabilities owed by such an entity to the Issuer. In addition, a relevant Resolution Authority may exercise its discretions in a manner that produces different outcomes amongst institutions resolved in different EU Member States. It should also be noted that similar powers and provisions are being considered in the context of financial institutions of other jurisdictions.""",
        {"entities": [(447, 861, "Conditional")]}
    ),
    (
        """The Trust Deed provides that in the event of any conflict of interest among or between the Noteholders, the interests of the Controlling Class will prevail. If the holders of the Controlling Class do not have an interest in the outcome of the conflict, the Trustee shall give priority to the interests of the most senior Class of Notes Outstanding. If the Trustee receives conflicting or inconsistent requests from two or more groups of holders of the Controlling Class (or another Class is given priority as described in this paragraph), the Trustee shall give priority to the group which holds the greater amount of Notes Outstanding of such Class. The Trust Deed provides further that the Trustee will act upon the directions of the holders of the Controlling Class (or other Class given priority as described in this paragraph) in such circumstances, and shall not be obliged to consider the interests of the holders of any other Class of Notes. See Condition 14(e) (Entitlement of the Trustee and Conflicts of Interest).""",
        {"entities": [(156, 348, "Conditional"), (349, 649, "Conditional")]}
    ),
    (
        """If the relevant EURIBOR screen rate does not appear, or the relevant page is unavailable, in the manner described in Condition 6(e)(i) (Floating Rate of Interest) there can be no guarantee that the Calculation Agent will be able to select four Reference Banks to provide quotations, in order to determine any Floating Rate of Interest in respect of the Floating Rate Notes. Certain financial institutions that have historically acted as Reference Banks have indicated that they will not currently provide quotations and there can be no assurance that they will agree to do so in the future. No Reference Banks have been selected as at the date of this Offering Circular.""",
        {"entities": [(0, 372, "Conditional")]}
    ),
    (
        """If a EURIBOR screen rate does not appear, or the relevant page is unavailable, and the Calculation Agent is unable to select Reference Banks to provide quotations in the manner described in Condition 6(e)(i)(B) (Floating Rate of Interest), the relevant Floating Rate of Interest in respect of such Payment Date shall be determined, pursuant to Condition 6(e)(i)(C) (Floating Rate of Interest), as the Floating Rate of Interest in effect as at the immediately preceding Accrual Period that was determined by reference to a EURIBOR screen rate or through quotations provided by four Reference Banks. To the extent interest amounts in respect of the Floating Rate Notes are determined by reference to a previously calculated rate, Noteholders may be adversely affected. In such circumstances, neither the Calculation Agent nor the Trustee shall have any obligation to determine the Floating Rate of Interest on any other basis.""",
        {"entities": [(0, 596, "Conditional")]}
    ),
    (
        """If a Rating Agency announces or informs the Trustee, the Investment Manager or the Issuer that confirmation from such Rating Agency is not required for a certain action or that its practice is to not give such confirmations for certain types of actions, the requirement for confirmation from such Rating Agency will not apply. Further, in connection with the Effective Date, if either Rating Agency has not yet confirmed or been deemed to have confirmed its initial ratings of the applicable Rated Notes, the applicable Rated Notes will be subject to redemption in part in an amount and in the manner described under Condition 7(e) (Redemption upon Effective Date Rating Event). There can be no assurance that a Rating Agency will provide such rating confirmations upon request, regardless of the terms agreed to among transaction participants, or not subsequently withdraw or downgrade its ratings on one or more Classes of Rated Notes, which could materially adversely affect the value or liquidity of the Rated Notes.""",
        {"entities": [(0, 325, "Conditional"), (375, 677, "Conditional")]}
    ),
    (
        """If any withholding tax or deduction for tax is imposed on payments of interest on the Notes, the holders of the Notes will not be entitled to receive grossed-up amounts to compensate for such withholding tax and no Event of Default shall occur as a result of any such withholding or deduction.""",
        {"entities": [(0, 292, "Conditional")]}
    ),
    (
        """If a Note Tax Event occurs pursuant to which any payment on the Notes of any Class becomes properly subject to any withholding tax or deduction on account of tax, the Notes may be redeemed in whole but not in part at the direction of the holders of either of the Controlling Class or the Subordinated Notes, in each case acting by way of Extraordinary Resolution, subject to certain conditions including a threshold test pursuant to which determination is made as to whether the anticipated proceeds of liquidation of the security over the Collateral would be sufficient to pay all amounts due and payable on the Rated Notes in such circumstances in accordance with the Priorities of Payment.""",
        {"entities": [(0, 440, "Conditional")]}
    ),
    (
        """If at any time one or more investors that are affiliated hold a majority of any Class of Notes, it may be more difficult for other investors to take certain actions that require consent of any such Classes of Notes without their consent. For example, optional redemption and the removal of the Investment Manager for cause and appointment are at the direction of Noteholders of specified percentages of Subordinated Notes and/or the Controlling Class (as applicable).""",
        {"entities": [(0, 236, "Conditional")]}
    ),
    (
        """If an Event of Default occurs and is continuing, the Trustee may, at its discretion, and shall, at the request of the Controlling Class acting by way of Ordinary Resolution (subject, in each case, to the Trustee being indemnified and/or secured and/or prefunded to its satisfaction), give notice to the Issuer and the Investment Manager that all the Notes are immediately due and repayable.""",
        {"entities": [(0, 389, "Conditional")]}
    ),
    (
        """In order to induce banks and institutional investors to invest in a Senior Obligation, Second Lien Loan or Mezzanine Obligation, and to obtain a favourable rate of interest, an Obligor under such an obligation often provides the investors therein with extensive information about its business, which is not generally available to the public. Because of the provision of confidential information, the unique and customised nature of the loan agreement relating to such Senior Obligation, Second Lien Loan or Mezzanine Obligation, and the private syndication of the Senior Obligations, Second Lien Loans and Mezzanine Obligations are not as easily purchased or sold as a publicly traded security, and historically the trading volume in the loan market has been small relative to, for example, the high yield bond market. Historically, investors in or lenders under European Senior Obligations, Second Lien Loans and Mezzanine Obligations have been predominantly commercial banks and investment banks. The range of investors for such loans has broadened significantly to include money managers, insurance companies, arbitrageurs, bankruptcy investors and mutual funds seeking increased potential total returns and investment managers of trusts or special purpose companies issuing collateralised bond and loan obligations. As secondary market trading volumes increase, new loans are frequently adopting more standardised documentation to facilitate loan trading which should improve market liquidity. There can be no assurance, however, that future levels of supply and demand in loan trading will provide the degree of liquidity which currently exists in the market. This means that such assets will be subject to greater disposal risk if such assets are sold following enforcement of the security over the Collateral or otherwise. The European market for Mezzanine Obligations is also generally less liquid than that for Senior Obligations, resulting in increased disposal risk for such obligations.""",
        {"entities": [(1665, 1828, "Conditional")]}
    ),
    (
        """In addition to the characteristics described above, high yield securities frequently have call or redemption features that permit the issuer to redeem such obligations prior to their final maturity date. If such a call or redemption were exercised by an issuer during a period of declining interest rates, the Investment Manager, acting on behalf of the Issuer, may only be able to replace such called obligation with a lower yielding obligation, thus decreasing the net investment income from the Portfolio.""",
        {"entities": [(204, 507, "Conditional")]}
    ),
    (
        """Liens arising by operation of law may take priority over the Issuer’s liens on an Obligor’s underlying collateral and impair the Issuer’s recovery on a Collateral Debt Obligation if a default or foreclosure on that Collateral Debt Obligation occurs.""",
        {"entities": [(0, 248, "Conditional")]}
    ),
    (
        """Liens on the collateral (if any) securing a Collateral Debt Obligation may arise at law that have priority over the Issuer’s interest. An example of a lien arising under law is a tax or other government lien on property of an Obligor. A tax lien may have priority over the Issuer’s lien on such collateral. To the extent a lien having priority over the Issuer’s lien exists with respect to the collateral related to any Collateral Debt Obligation, the Issuer’s interest in the asset will be subordinate to such lien. If the creditor holding such lien exercises its remedies, it is possible that, after such creditor is repaid, sufficient cash proceeds from the underlying collateral will not be available to pay the outstanding principal amount of such Collateral Debt Obligation.""",
        {"entities": [(0, 133, "Conditional"), (517, 779, "Conditional")]}
    ),
    (
        """If a recovery range is not available for a given obligation with an S&P Recovery Rating of “1” through “6” (inclusive), the lower recovery range for the applicable S&P Recovery Rating shall apply""",
        {"entities": [(0, 194, "Conditional")]}
    ),
    (
        """(i) if any representation that we made hereunder is subsequently shown to be false or misleading or our beneficial ownership otherwise causes a violation of the 25 per cent. Limitation, the Issuer shall, promptly after such discovery, send notice to us demanding that we transfer our interest to a person that is not a Non-Permitted ERISA Holder within 10 calendar days after the date of such notice;""",
        {"entities": [(3, 172, "Conditional")]}
    ),
    (
        """5. No Prohibited Transaction. If we checked any of the boxes in Sections (1) to (3) above, we represent, warrant and agree that our acquisition, holding and disposition of the Class E Notes, Class F Notes or Subordinated Notes do not and will not constitute or result in a non-exempt prohibited transaction under Section 406 of ERISA or Section 4975 of the Code.""",
        {"entities": [(30, 361, "Conditional")]}
    ),
    (
        """IF YOU DO NOT INCLUDE ANY PERCENTAGE IN THE BLANK SPACE, YOU WILL BE COUNTED AS IF YOU FILLED IN 100 per cent. IN THE BLANK SPACE.""",
        {"entities": [(0, 109, "Conditional")]}
    ),
    (
        """If a box is not checked, you are representing, warranting and agreeing that the applicable Section does not, and will not, apply to you.""",
        {"entities": [(0, 135, "Conditional")]}
    ),
    (
        """the Notes may not be acquired using the assets of any Plan if any of the Issuer, the Arranger, the Initial Purchaser, the Investment Manager or their respective affiliates has investment authority with respect to such assets (except to the extent that a favourable statutory or administrative""",
        {"entities": [(688, 979, "Conditional")]}
    ),
    (
        """Even if the Class X Notes, the Class A Notes, the Class B Notes, the Class C Notes and the Class D Notes would not be treated as equity interests in the Issuer for the purposes of ERISA, it is possible that an investment in such Notes by a Benefit Plan Investor (or with the use of the assets of a Benefit Plan Investor) could be treated as a prohibited transaction under ERISA and/or Section 4975 of the Code. Such a prohibited transaction, however, may be subject to a statutory or administrative exemption. Even if an exemption were to apply, such exemption may not, however, apply to all of the transactions that could be deemed prohibited transactions in connection with an investment in the Notes by a Benefit Plan Investor.""",
        {"entities": [(510, 729, "Conditional")]}
    ),
    (
        """Backup withholding is not an additional tax and may be refunded (or credited against the holder’s U.S. federal income tax liability, if any),""",
        {"entities": [(0, 141, "Conditional")]}
    ),
    (
        """A U.S. Holder of Subordinated Notes (or any Class of Notes that are treated as equity in the Issuer for U.S. federal income tax purposes) may be required to file FinCEN Form 114 with respect to foreign financial accounts in which the Issuer has a financial interest if the U.S. Holder holds more than 50 per cent. of the aggregate outstanding principal amount of such Notes or is otherwise treated as owning more than 50 per cent. of the total value or voting power of the Issuer’s outstanding equity.""",
        {"entities": [(0, 312, "Conditional")]}
    ),
    (
        """If a U.S. Holder does not make a timely QEF election with respect to the Issuer as described above and is not subject to the CFC rules, any gain realised on the sale, redemption, or other disposition of a Subordinated Note (or any gain deemed to accrue prior to the time a non-timely QEF election is made) will be taxed as ordinary income and subject to an additional tax reflecting a deemed interest charge under the special tax rules described above. See “Investment in a Passive Foreign Investment Company”.""",
        {"entities": [(0, 451, "Conditional")]}
    ),
    (
        """Phantom Income. U.S. Holders may be subject to U.S. federal income tax on the amounts that exceed the distributions they receive on the Subordinated Notes. For example, if the Issuer is a CFC and a U.S. Holder is a 10 per cent. United States shareholder with respect to the Issuer, or a U.S. Holder makes a QEF election with respect to the Issuer, the U.S. Holder will be subject to federal income tax with respect to its share of the Issuer’s income and gain (to the extent of the Issuer’s “earnings and profits”), which may exceed the Issuer’s distributions. It is expected that the Issuer’s income and gain (and earnings and profits) will exceed cash distributions with respect to (i) debt instruments that were issued with OID and are held by the Issuer, (ii) the acquisition at a discount of the Rated Notes by the Issuer (including by reason of a Refinancing, change to an Alternative Base Rate or any deemed exchange that occurs for U.S. federal income tax purposes as a result of a modification of the Trust Deed) and (iii) the use of interest proceeds to make payments on the Class X Principal Amortisation Amount. U.S. Holders should consult their tax advisors regarding the timing of income and gain on the Subordinated Notes.""",
        {"entities": [(169, 559, "Conditional")]}
    ),
    (
        """Distributions. The treatment of actual distributions of cash on the Subordinated Notes will vary depending on whether the U.S. Holder of such Subordinated Notes has made a timely QEF election (as described above). See “Investment in a Passive Foreign Investment Company”. If a timely QEF election has been made, distributions should be allocated first to amounts previously taxed pursuant to the QEF election (or pursuant to the CFC rules, if applicable) and to this extent will not be taxable to such U.S. Holder. Distributions in excess of such previously taxed amounts will be treated first as a nontaxable return of capital, to the extent of the U.S. Holder’s adjusted tax basis in the Subordinated Notes (as described below under “Sale, Redemption, or Other Disposition”), and then as a disposition of a portion of the Subordinated Notes. In addition, a U.S. Holder will recognise exchange gain""",
        {"entities": [(272, 513, "Conditional")]}
    ),
    (
        """Accordingly, if the U.S. Holder has not made a QEF election with respect to the indirectly held PFIC, the U.S. Holder would be subject to the adverse consequences described above under “Investment in a Passive Foreign Investment Company” with respect to any Excess Distributions of such indirectly held PFIC, any gain indirectly realised by such U.S. Holder on the sale by the Issuer of such PFIC, and any gain indirectly realised by such U.S. Holder with respect to the indirectly held PFIC on the sale by the U.S. Holder of its Subordinated Notes (which may arise even if the U.S. Holder realises a loss on such sale). Moreover, if the U.S. Holder has made a QEF election with respect to the indirectly held PFIC, the U.S. Holder will be required to include in income the U.S. dollar value of its pro rata share of the indirectly held PFIC’s ordinary earnings and net capital gain as if the indirectly held PFIC were held directly (as described above), and the U.S. Holder will not be permitted to use any losses or other expenses of the Issuer to offset such ordinary earnings and/or net capital gains. Accordingly, if any of the Collateral Debt Obligations are treated as equity interests in a PFIC, U.S. Holders could experience significant amounts of “phantom” income with respect to such interests.""",
        {"entities": [(13, 619, "Conditional"), (631, 1104,
                                                 "Conditional"), (1119, 1304, "Conditional")]}
    ),
    (
        """Investment in a Passive Foreign Investment Company. The Issuer will be a PFIC for U.S. federal income tax purposes, and U.S. Holders of Subordinated Notes will be subject to the PFIC rules, except for certain U.S. Holders that are subject to the rules relating to a CFC (as described below under “Investment in a Controlled Foreign Corporation”). U.S. Holders of Subordinated Notes should consider making an election to treat the Issuer as a QEF. Generally, a U.S. Holder makes a QEF election on IRS Form 8621, attaching a copy of that form to its U.S. federal income tax return for the first taxable year for which it held its Subordinated Notes. If a U.S. Holder makes a timely QEF election with respect to the Issuer, the electing U.S. Holder will be required in each taxable year to include in gross income (i) as ordinary income, the U.S. dollar value of the U.S. Holder’s pro rata share of the Issuer’s ordinary earnings and (ii) as long-term capital gain, the U.S. dollar value of the U.S. Holder’s pro rata share of the Issuer’s net capital gain, whether or not distributed. A U.S. Holder will not be eligible for the dividends received deduction in respect of such income or gain. In addition, any losses of the Issuer in a taxable year will not be available to the U.S. Holder and may not be carried back or forward in computing the Issuer’s ordinary earnings and net capital gain in other taxable years. If applicable, the rules relating to a CFC, discussed below generally override those relating to a PFIC with respect to which a QEF election is in effect.""",
        {"entities": [(648, 1081, "Conditional"), (1415, 1568, "Conditional")]}
    ),
    (
        """Finally, if the Class E Notes or Class F Notes represent equity in the Issuer for U.S. federal income tax purposes, a U.S. Holder of such Notes will be required to file an IRS Form 5471 with the IRS if the U.S. Holder is treated as owning (actually or constructively) at least 10 per cent. by vote or value of the equity of the Issuer for U.S. federal income tax purposes, and may be required to provide additional information regarding the Issuer annually on IRS Form 5471 if the U.S. Holder is treated as owning (actually or constructively) more than 50 per cent. by vote or value of the equity of the Issuer for U.S. federal income tax purposes. U.S. Holders may wish to file a “protective” IRS Form 5471 with respect to their Class E Notes and Class F Notes.""",
        {"entities": [(8, 647, "Conditional")]}
    ),
    (
        """In addition, if the Class E Notes or Class F Notes represent equity in the Issuer for U.S. federal income tax purposes, a U.S. Holder of such Notes would be required to file an IRS Form 926 with the IRS if (i) such person is treated as owning, directly or by attribution, immediately after the U.S. Holder’s purchase of Notes, at least 10 per cent. by vote or value of the Issuer or (ii) the amount of cash transferred by such person (or any related person) to the Issuer during the 12-month period ending on the date of such purchase exceeds $100,000. U.S. Holders""",
        {"entities": [(13, 564, "Conditional")]}
    ),
    (
        """the Principal Amount Outstanding of the Notes of each Class and such aggregate amount as a percentage of the original aggregate Principal Amount Outstanding of the Notes of such Class at the beginning of the Accrual Period, the amount of principal payments to be made on the Notes of each Class on the related Payment Date, and the aggregate amount of the Notes of each Class Outstanding and such aggregate amount as a percentage of the original aggregate amount of the Notes of such Class Outstanding after giving effect to the principal payments, if any, on the next Payment Date;""",
        {"entities": [(391, 580, "Conditional")]}
    ),
    (
        """Accrual basis U.S. Holders of Class X Notes, Class A Notes or Class B Notes also will recognise foreign currency exchange gain or loss on the receipt of interest payments on their Class X Notes, Class A Notes or Class B Notes to the extent that the U.S. dollar value of such payments (based on the euro-to-U.S. dollar spot exchange rate on the date such payments are received) differs from the U.S. dollar value of such payments when they were accrued. The foreign currency exchange gain or loss generally will be treated as ordinary income or loss.""",
        {"entities": [(0, 451, "Conditional")]}
    ),
    (
        """U.S. Holders of Class X Notes, Class A Notes or Class B Notes that are issued with OID also will recognise foreign currency exchange gain or loss on the receipt of principal payments on their Class X Notes, Class A Notes or Class B Notes to the extent that the U.S. dollar value of such payments (based on the euro-to-U.S. dollar spot exchange rate on the date such payments are received) differs from the U.S. dollar value of the corresponding amounts of OID when they were accrued""",
        {"entities": [(0, 481, "Conditional")]}
    ),
    (
        """U.S. Holders of Class C Notes, Class D Notes, Class E Notes, or Class F Notes also will recognise foreign currency exchange gain or loss on the receipt of interest and/or principal payments on their Notes to the extent that the U.S. dollar value of such payments (based on the euro-to-U.S. dollar spot exchange rate on the date such payments are received) differs from the U.S. dollar value of the corresponding amounts of OID when they were accrued. The foreign currency exchange gain or loss generally will be treated as ordinary income or loss.""",
        {"entities": [(0, 449, "Conditional")]}
    ),
    (
        """U.S. Holders that are individuals or estates and certain trusts are subject to an additional 3.8 per cent. tax on all or a portion of their “net investment income,” or “undistributed net investment income” in the case of an estate or trust, which may include any income or gain with respect to the Notes, to the extent of their net investment income or undistributed net investment income (as the case may be) that, when added to their other modified adjusted gross income, exceeds $200,000 for an unmarried individual, $250,000 for a married taxpayer filing a joint return (or a surviving spouse), $125,000 for a married individual filing a separate return, or the dollar amount at which the highest tax bracket begins for an estate or trust. The 3.8 per cent. Medicare tax is determined in a different manner than the regular income tax and special rules apply with respect to the PFIC and CFC rules described above. U.S. Holders should consult their advisors with respect to the 3.8 per cent. Medicare tax.""",
        {"entities": [(0, 741, "Conditional")]}
    ),
    (
        """(i) Regulation (EU) 2017/1129 of the European Parliament and of the Council of 14 June 2017 on the prospectus to be published when securities are offered to the public or admitted to trading on a regulated market and any applicable supporting law, rule or regulation and any Central Bank of Ireland (“Central Bank”) rules issued and / or in force pursuant to Section 1363 of the Companies Act 2014 (as amended) (the “Companies Act”);""",
        {"entities": [(0, 432, "Conditional")]}
    ),
    (
        """5. The purchaser and each account for which the purchaser is acquiring such Rule 144A Notes is a QP. The purchaser is acquiring the Rule 144A Notes in a principal amount of not less than €250,000. The purchaser and each such account are acquiring the Rule 144A Notes as principal for its own account for investment and not for sale in connection with any distribution thereof. The purchaser and each such account: (a) was not formed for the specific purpose of investing in the Rule 144A Notes (except when each beneficial owner of the purchaser and each such account is a QP); (b) to the extent the purchaser is a private investment company formed before 30 April 1996, the purchaser has received the necessary consent from its beneficial owners; (c) is not a pension, profit sharing or other retirement trust fund or plan in which the partners, beneficiaries or participants, as applicable, may designate the particular investments to be made; and (d) is not a broker dealer that owns and invests on a discretionary basis less than $25,000,000 in securities of unaffiliated issues. Further, the purchaser agrees with respect to itself and each such account: (x) that it shall not hold such Rule 144A Notes for the benefit of any other person and shall be the sole beneficial owner thereof for all purposes; (y) that it shall not sell participation interests in the Rule 144A Notes or enter into any other arrangement pursuant to which any other person shall be entitled to a beneficial interest in the distributions on the Rule 144A Notes; and (z) that the Rule 144A Notes purchased directly or indirectly by it constitute an investment of no more than 40 per cent. of the purchaser’s and each such account’s assets (except when each beneficial owner of the purchaser and each such account is a QP). The purchaser understands and agrees that any purported transfer of the Rule 144A Notes to a purchaser that does not comply with the requirements of this paragraph (5) will be of no force and effect, will be void ab initio and the Issuer will have the right to direct the purchaser to transfer its Rule 144A Notes to a Person who meets the foregoing criteria.""",
        {"entities": [(377, 575, "Conditional")]}
    ),
    (
        """5. The purchaser and each account for which the purchaser is acquiring such Rule 144A Notes is a QP. The purchaser is acquiring the Rule 144A Notes in a principal amount of not less than €250,000. The purchaser and each such account are acquiring the Rule 144A Notes as principal for its own account for investment and not for sale in connection with any distribution thereof. The purchaser and each such account: (a) was not formed for the specific purpose of investing in the Rule 144A Notes (except when each beneficial owner of the purchaser and each such account is a QP); (b) to the extent the purchaser is a private investment company formed before 30 April 1996, the purchaser has received the necessary consent from its beneficial owners; (c) is not a pension, profit sharing or other retirement trust fund or plan in which the partners, beneficiaries or participants, as applicable, may designate the particular investments to be made; and (d) is not a broker dealer that owns and invests on a discretionary basis less than $25,000,000 in securities of unaffiliated issues. Further, the purchaser agrees with respect to itself and each such account: (x) that it shall not hold such Rule 144A Notes for the benefit of any other person and shall be the sole beneficial owner thereof for all purposes; (y) that it shall not sell participation interests in the Rule 144A Notes or enter into any other arrangement pursuant to which any other person shall be entitled to a beneficial interest in the distributions on the Rule 144A Notes; and (z) that the Rule 144A Notes purchased directly or indirectly by it constitute an investment of no more than 40 per cent. of the purchaser’s and each such account’s assets (except when each beneficial owner of the purchaser and each such account is a QP). The purchaser understands and agrees that any purported transfer of the Rule 144A Notes to a purchaser that does not comply with the requirements of this paragraph (5) will be of no force and effect, will be void ab initio and the Issuer will have the right to direct the purchaser to transfer its Rule 144A Notes to a Person who meets the foregoing criteria.""",
        {"entities": [(1542, 1800, "Conditional")]}
    ),
    (
        """The Notes will be issued at a maximum issue price of up to 100 per cent. of the principal amount thereof. The Notes will be offered by the Issuer through Credit Suisse Securities (Europe) Limited in its capacity as arranger and initial purchaser of the offering of such Notes (the “Arranger” and “Initial Purchaser”) subject to prior sale, when, as and if delivered to and accepted by the Initial Purchaser, and to certain conditions. It is expected that delivery of the Notes will be made on or about the Issue Date. The Retention Notes to be held by the Retention Holder shall be purchased by the Retention Holder directly from the Initial Purchaser on the Issue Date. The Initial Purchaser may offer the Notes at prices as may be negotiated at the time of sale which may vary among different purchasers and which may be different to the issue price of the Notes.""",
        {"entities": [(106, 432, "Conditional")]}
    ),
    (
        """ and the Issuer’s inability to dispose fully and promptly of positions in declining markets may exacerbate losses suffered by the Issuer when Collateral Debt Obligations are sold.""",
        {"entities": [(821, 999, "Conditional")]}
    ),
    (
        """At this time it is not possible to state with certainty if and when any withdrawal agreement will be entered into, what might be the final terms and effective date of such a withdrawal agreement or the date on which any transition period will end if such an agreement is entered into.""",
        {"entities": [(0, 283, "Conditional")]}
    ),
    (
        """The ESAs stated that they expect Competent Authorities to generally apply their supervisory powers in their day-to-day supervision and enforcement of applicable legislation in a proportionate and risk-based manner. This approach entails that the Competent Authorities can, when examining reporting entities’ compliance with the disclosure requirements of the Securitisation Regulation, take into account the type and extent of information already being disclosed by reporting entities. The ESAs also noted that they expect that difficulties with compliance will be solved with the final application of the disclosure templates in the Transparency RTS. As such, the Joint Statement from the ESAs should be viewed as a temporary measure. The Joint Statement went on to state that this approach does not entail general forbearance, but a case-by-case assessment by the Competent Authorities of the degree of compliance with the Securitisation Regulation. As the Joint Statement does not “grandfather” transactions that are issued after 1 January 2019 but before the application of the disclosure templates in the Transparency RTS, such transactions, including the transaction described herein, will need to comply with the disclosure templates in the Transparency RTS once they apply.""",
        {"entities": [(215, 484, "Conditional")]}
    ),
    (
        """On October 21, 2014, the final rules implementing the credit risk retention requirements of Section 941 of the Dodd-Frank Act (the “U.S. Risk Retention Rules”) were issued. Except with respect to asset- backed securities transactions that satisfy certain exemptions, the U.S. Risk Retention Rules generally require a “sponsor” of asset-backed securities or its “majority-owned affiliate” (as defined in the U.S. Risk Retention Rules) to retain not less than 5 per cent. of the credit risk of the assets collateralizing asset-backed securities (the “Minimum Risk Retention Requirement”). On February 9, 2018, a three- judge panel (the “Panel”) of the United States Court of Appeals for the District of Columbia Circuit ruled in favor of the Loan Syndicates and Trading Association in its lawsuit against the Securities and Exchange Commission and the Board of Governors of the Federal Reserve System and held that collateral managers of “open market CLOs” (described in the LSTA Decision as CLOs where assets are acquired from “arms-length negotiations and trading on an open market”) are not “securitizers” or “sponsors” under Section 941 of the Dodd-Frank Act and, therefore, are not subject to risk retention and do not have to comply with the U.S. Risk Retention Rules (the “LSTA Decision”). The Panel’s opinion in the LSTA Decision became effective on April 5, 2018, when the district court entered its order following the issuance of the appellate mandate on April 3, 2018 (the “Mandate”) in respect thereof.""",
        {"entities": [(1295, 1512, "Conditional")]}
    ),
    (
        """The most significant amendment in EMIR REFIT is the change to the definition of financial counterparty (“FC”). EMIR REFIT brings into that definition all alternative investment funds (“AIFs”), that are either established in the EEA or whose investment manager is authorised/registered under Directive 2011/61/EU on Alternative Investment Fund Managers (“AIFMD”). Notably, the FC definition will effectively capture non-EU AIFs managed by non-EU managers when they are a counterparty to an EU FC. Previously, such funds were usually determined to be third country entities (“TCEs”) that would be non-financial counterparties (“NFCs”) if they were established in the EU, meaning that such funds would be out of scope of the clearing obligation and risk mitigation obligations (subject to the fund not exceeding the relevant clearing threshold for NFCs) when dealing with EU FCs. Under the amended definition of a FC in EMIR REFIT, such funds will now be regarded as TCEs that would be FCs if they were established in the EU, meaning that EU FCs will be required to ensure compliance with the clearing obligation and margin requirements for uncleared derivatives in respect of their trading with such funds.""",
        {"entities": [(363, 494, "Conditional"), (496, 875, "Conditional")]}
    ),
    (
        """Further, if the Investment Manager determines that additional Hedge Transactions should be entered into by the Issuer in excess of the trading limitations set forth in any applicable exemption from registration as a CPO and/or a CTA, the Investment Manager may elect to withdraw its exemption from registration and instead register with the CFTC as the Issuer’s CPO and/or CTA. The costs of obtaining and maintaining these registrations and the related compliance obligations may be paid by the Issuer as Administrative Expenses. Such costs would reduce the amount of funds available to make payments on the Notes. These costs are uncertain and could be materially greater than the Investment Manager anticipated when deciding to enter into the transaction and register as a CPO and/or a CTA. In addition, it may not be possible or advisable for the Investment Manager to withdraw from registration as a CPO and/or a CTA after any relevant swap transactions terminate or expire. The costs of CPO and/or CTA registration and the ongoing CPO and/or CTA compliance obligations of the Investment Manager could exceed, perhaps significantly, the financial risks that are being hedged pursuant to any Hedge Transaction.""",
        {"entities": [(9, 376, "Conditional")]}
    ),
    (
        """that""",
        {"entities": []}
    ),
    (
        """of""",
        {"entities": []}
    ),
    (
        """The contents of the document are confidential and may not be copied, distributed, published, reproduced or reported (in whole or in part) or disclosed by you to any other person. If at any time we request that the document be returned, you will (a) return the document and (b) arrange to destroy all analyses, compilations, notes, structures, memoranda or other documents prepared by you to the extent that the same contain, reflect or derive from information in the document and (c) so far as is practicable to do so (but, in any event, without prejudice to the obligations of confidentiality imposed herein) expunge any information relating to the document in electronic form from any computer, word processor or other device. The document and any information contained herein shall remain our property and in sending the document to you, no rights (including any intellectual property rights) over the document and the information contained therein has been given to you. We specifically prohibit the redistribution of the document and accept no liability whatsoever for the actions of third parties in this respect.""",
        {"entities": [(179, 726, "Conditional")]}
    ),
    (
        """The document has been sent to you in electronic form. You are reminded that documents transmitted via this medium may be altered or changed during the process of transmission and consequently none of Jubilee CLO 2014- XI B.V., Merrill Lynch International or Alcentra Limited (or any person who controls any of them or any director, officer, employee or agent of any of them, or affiliate of any of them or of any such person) accepts any liability or responsibility whatsoever in respect of any difference between the document distributed to you in electronic format and the hard copy version available to you on request from us.""",
        {"entities": []}
    ),
    (
        """€27,000,000 Class C Senior Secured Deferrable Floating Rate Notes due 2027""",
        {"entities": []}
    ),
    (
        """The Notes will be subject to Optional Redemption, Mandatory Redemption and Special Redemption, each as described herein . See Condition 7 (Redemption and Purchase).""",
        {"entities": []}
    ),
    (
        """(A) OUTSIDE THE UNITED STATES TO NON-U.S. PERSONS (AS DEFINED IN REGULATION S UNDER THE SECURITIES ACT (“REGULATION S”)); AND (B) WITHIN THE UNITED STATES TO PERSONS AND OUTSIDE THE UNITED STATES TO U.S. PERSONS (AS SUCH TERM IS DEFINED IN REGULATION S (“U.S. PERSONS”)), IN EACH CASE, WHO ARE BOTH QUALIFIED INSTITUTIONAL BUYERS (AS DEFINED IN RULE 144A UNDER THE SECURITIES ACT) IN RELIANCE ON RULE 144A UNDER THE SECURITIES ACT AND QUALIFIED PURCHASERS FOR THE PURPOSES OF SECTION 3(C)(7) OF THE UNITED STATES INVESTMENT COMPANY ACT OF 1940, AS AMENDED (THE “INVESTMENT COMPANY ACT” ) . THE ISSUER WILL NOT BE REGISTERED UNDER THE INVESTMENT COMPANY ACT. INTERESTS IN THE NOTES WILL BE SUBJECT TO CERTAIN RESTRICTIONS ON TRANSFER, AND EACH PURCHASER OF NOTES OFFERED HEREBY IN MAKING ITS PURCHASE WILL BE REQUIRED TO OR DEEMED TO HAVE MADE CERTAIN ACKNOWLEDGEMENTS, REPRESENTATIONS AND AGREEMENTS. SEE “PLAN OF DISTRIBUTION” AND “TRANSFER RESTRICTIONS”.""",
        {"entities": []}
    ),
    (
        """In connection with the issue and sale of the Notes, no person is authorised to give any information or to make any representation not contained in this Offering Circular and, if given or made, such information or representation must not be relied upon as having been authorised by or on behalf of the Issuer, the Arranger, the Initial Purchaser, the Trustee, the Investment Manager or the Collateral Administrator. The delivery of this Offering Circular at any time does not imply that the information contained in it is correct as at any time subsequent to its date .""",
        {"entities": [(175, 414, "Conditional")]}
    ),
    (
        """THE SECURITIES OFFERED HEREBY HAVE NOT BEEN AND WILL NOT BE REGISTERED WITH, OR APPROVED BY, ANY UNITED STATES FEDERAL OR STATE SECURITIES COMMISSION OR REGULATORY AUTHORITY. FURTHERMORE, THE FOREGOING AUTHORITIES HAVE NOT PASSED UPON OR ENDORSED THE MERITS OF THIS OFFERING OR THE ACCURACY OR ADEQUACY OF THIS DOCUMENT. ANY REPRESENTATION TO THE CONTRARY IS A CRIMINAL OFFENCE.""",
        {"entities": []}
    ),
    (
        """This Offering Circular has been prepared by the Issuer solely for use in connection with the offering of the Notes described herein (the “Offering” ). Each of the Issuer, the Arranger and the Initial Purchaser reserves the right to reject any offer to purchase Notes in whole or in part for any reason, or to sell less than the stated initial principal amount of any Class of Notes offered hereby. This Offering Circular is personal to each offeree to whom it has been delivered by the Issuer, the Arranger, the Initial Purchaser or any Affiliate thereof and does not constitute an offer to any other person or to the public generally to subscribe for or otherwise acquire the Notes. Distribution of this Offering Circular to any persons other than the offeree and those persons, if any, retained to advise such offeree with respect thereto is unauthorised and any disclosure of any of its contents, without the prior written consent of the Issuer, is prohibited. Any reproduction or distribution of this Offering Circular in whole or in part and any disclosure of its contents or use of any information herein for any purpose other than considering an investment in the securities offered herein is prohibited.""",
        {"entities": [(779, 962, "Conditional")]}
    ),
    (
        """Commodity Pool Regulation IF TRADING OR ENTERING INTO HEDGE AGREEMENTS WOULD RESULT IN THE ISSUER’S ACTIVITIES FALLING WITHIN THE DEFINITION OF A “COMMODITY POOL” UNDER THE COMMODITY EXCHANGE ACT, THE INVESTMENT MANAGER EXPECTS TO BE EXEMPT FROM REGISTRATION WITH THE COMMODITY FUTURES TRADING COMMISSION (THE “CFTC”) AS A COMMODITY POOL OPERATOR (A “CPO”) PURSUANT TO CFTC RULE 4.13(a)(3 ). THEREFORE, UNLIKE A REGISTERED CPO, THE INVESTMENT MANAGER WOULD NOT BE REQUIRED TO DELIVER A CFTC DISCLOSURE DOCUMENT TO PROSPECTIVE INVESTORS, NOR WOULD IT BE REQUIRED TO PROVIDE INVESTORS WITH CERTIFIED ANNUAL REPORTS THAT SATISFY THE REQUIREMENTS OF CFTC RULES APPLICABLE TO REGISTERED CPOs. FURTHER, THE TRADING OR ENTERING INTO SUCH HEDGE AGREEMENT MUST NOT ELIMINATE THE ISSUER’S ABILITY TO RELY ON RULE 3A-7 UNDER THE INVESTMENT COMPANY ACT, UNLESS AND UNTIL THE ISSUER ELECTS TO RELY SOLELY ON THE EXEMPTION UNDER SECTION 3(C)(7) UNDER THE INVESTMENT COMPANY ACT.""",
        {"entities": [(25, 389, "Conditional")]}
    ),
    (
        """Condition 10(b) (Acceleration) or following an acceleration of the Notes which has subsequently been rescinded and annulled in accordance with Condition 10(c) (Curing of Default) and other than in connection with an Optional Redemption in whole but not in part pursuant to Condition 7(b) (Optional Redemption) or in connection with a redemption in whole but not in part pursuant to Condition 7(g) (Redemption following Note Tax Event), Interest Proceeds will be applied in accordance with the Interest Proceeds Priority of Payments and Principal Proceeds will be applied in accordance with the Principal Proceeds Priority of Payments. Upon any redemption in whole but not in part of the Notes in accordance with Condition 7(b) (Optional Redemption) or in accordance with Condition 7(g) (Redemption following Note Tax Event) or following an acceleration of the Notes in accordance with Condition 10(b) (Acceleration) which has not been rescinded and annulled in accordance with Condition 10(c) (Curing of Default), Interest Proceeds and Principal Proceeds will be applied in accordance with the Post-Acceleration Priority of Payments, in each case as described in the Conditions of the Notes.""",
        {"entities": []}
    ),
    (
        """The Dodd-Frank Act requires that federal banking agencies amend their regulations to remove reference to or reliance on credit agency ratings, including but not limited to those found in the federal banking agencies’ risk-based capital regulations. New regulations have been proposed but have not yet been fully implemented in all respects. When such regulations are fully implemented, investments in asset-backed securities like the Notes by such institutions may result in greater capital charges to financial institutions that own such securities, or otherwise adversely affect the treatment of such securities for regulatory capital purposes. Furthermore, all prospective investors in the Notes whose investment activities are subject to legal investment laws and regulations, regulatory capital requirements, or review by regulatory authorities should consult with their own legal, accounting and other advisors in determining whether, and to what extent, the Notes will constitute legal investments for them or are subject to investment or other regulatory restrictions, unfavourable accounting treatment, capital charges or reserve requirements.""",
        {"entities": [(341, 645, "Conditional")]}
    ),
    (
        """Certain entrenched rights relating to the Terms and Conditions of the Notes including (but not limited to) the currency thereof, Payment Dates applicable thereto, the Priorities of Payment, the provisions relating to quorums and the percentages of votes required for the passing of an Extraordinary Resolution, cannot be amended or waived by Ordinary Resolution but require an Extraordinary Resolution. It should however be noted that amendments may still be effected and waivers may still be granted in respect of such provisions in circumstances where not all Noteholders agree with the terms thereof and any amendments or waivers once passed in accordance with the provisions of the Terms and Conditions of the Notes and the provisions of the Trust Deed will be binding on all such dissenting Noteholders. In addition to the Trustee’s right to agree to changes to the Transaction Documents to correct a manifest error, or to changes which, in its opinion, are not materially prejudicial to the interests of the Noteholders of any Class without the consent of the Noteholders, modifications may also be made and waivers granted in respect of certain other matters which the Trustee is obliged to consent to without the consent of the Noteholders as set out in Condition 14(c) (Modification and Waiver). Certain amendments and modifications may be made without the consent of Noteholders or the Trustee. See Condition 14(c) (Modification and Waiver). Such amendment or modification could be adverse to certain Noteholders.""",
        {"entities": []}
    ),
    (
        """If a meeting of Noteholders is called to consider a Resolution, determination as to whether the requisite number of Notes has been voted in favour of such Resolution will be determined by reference to the percentage which the Notes voted in favour represent of the total amount of Notes held or represented by any person or persons entitled to vote which are present at such meeting and not by the aggregate Principal Amount Outstanding of all such Notes which are entitled to be voted in respect of such Resolution. This means that a lower percentage of Noteholders may pass a Resolution which is put to a meeting of Noteholders than would be required for a Written Resolution in respect of the same matter. There are, however, quorum provisions which provide that a minimum number of Noteholders representing a minimum amount of the aggregate Principal Amount Outstanding of the applicable Class or Classes of Notes be present at any meeting to consider an Extraordinary Resolution or Ordinary Resolution (as applicable). In the case of an Extraordinary Resolution, this is one or more persons holding or representing not less than 50 per cent. of the aggregate Principal Amount Outstanding of each Class of Notes (or the relevant Class or Classes only, if applicable) and in the case of an Ordinary Resolution this is one or more persons holding or representing not less than 10 per cent. of the aggregate Principal Amount Outstanding of each Class of Notes (or the relevant Class or Classes only, if applicable). Such quorum provisions still, however, require considerably lower thresholds than would be required for a Written Resolution. In addition, if a quorum requirement is not satisfied at any meeting, lower quorum thresholds will apply at any meeting previously adjourned for want of quorum as set out in Condition 14 (Meetings of Noteholders, Modification, Waiver and Substitution) and in the Trust Deed. However, no Extraordinary Resolution or Ordinary Resolution may be passed without meeting the “Minimum Percentage Voting Requirements” set out in Condition 14(b)(iii) (Minimum Voting Rights). Each Hedge Counterparty will also need to be notified and its consent obtained (unless not required by virtue of the expiry of a notice period set out in the relevant Hedge Agreement) in respect of any proposed modification, amendment or supplement to certain provisions of the Transaction Documents specified in the applicable Hedge Agreement. Any such consent, if withheld in accordance with the terms of the applicable Hedge Agreement, may prevent the Transaction Documents from being modified in a manner which may be beneficial to Noteholders.""",
        {"entities": [(0, 515, "Conditional"), (1068, 1269,
                                                "Conditional"), (1275, 1515, "Conditional"), (1656, 1916, "Conditional"), (2472, 2657, "Conditional")]}
    ),
    (
        """The validity and enforceability of certain provisions in contractual priorities of payment (such as the Priorities of Payment) which purport to alter the priority in which a particular secured creditor is paid as a result of the occurrence of one or more specified trigger events, including the insolvency of such creditor (“flip clauses”), have been challenged recently in the English and U.S. courts on the basis that the operation of a flip clause as a result of such creditor’s insolvency breaches the “anti-deprivation” principles of English and U.S. insolvency law. This principle prevents a party from agreeing to a provision that deprives its creditors of an asset upon its insolvency.""",
        {"entities": []}
    ),
    (
        """The Euro Interbank Offered Rate (for the purposes of this paragraph only, “EURIBOR” and other so called “benchmarks” are the subject of proposals for reform by a number of international authorities and other bodies. In September 2013, the European Commission published a proposed regulation (the “Proposed Benchmark Regulation”) on indices used as benchmarks in financial instruments and financial contracts. The date the Proposed Benchmark Regulation will come into force is not yet clear. The Proposed Benchmark Regulation will, if enacted, make significant changes to the way in which EURIBOR is calculated, including detailed codes of conduct for contributors and transparency requirements applying to contributions of data. Benchmarks such as EURIBOR may be discontinued if they do not comply with these requirements or if the administrator of the benchmark either fails to apply for authorisation or is refused authorisation by its home regulator. Investors should be aware that: (a) any of these changes or any other changes to EURIBOR could affect the level of the published rate, including to cause it to be lower and/or more volatile than it would otherwise be; (b) if the applicable rate of interest on any Collateral Debt Obligation is calculated with reference to a EURIBOR currency or tenor which is discontinued, such rate of interest will then be determined by the provisions of the affected Collateral Debt Obligation, which may include determination by the relevant calculation agent in its discretion; (c) if the EURIBOR benchmark referenced in the Conditions of the Notes is discontinued, interest on the Notes will be calculated on the alternative basis set out in Condition 6 (Interest); and (d) the administrator of EURIBOR will not have any involvement in the Collateral Debt Obligations or the Notes and may take any actions in respect of EURIBOR without regard to the effect of such actions on the Collateral Debt Obligations or the Notes. Any of the above or any other significant changes to EURIBOR or any other benchmark could have a material adverse effect on the value of, and the amount payable under (i) any Collateral Debt Obligations which pay interest linked to a EURIBOR rate or other benchmark (as applicable) and (ii) the Notes.""",
        {"entities": [(491, 727, "Conditional"), (729, 1708, "Conditional")]}
    ),
    (
        """The assets comprising the Portfolio will consist of obligations of, or securities issued by, obligors organised under the laws of a variety of different countries. Investing in certain countries may involve greater risks than investing in other countries, including: (a) less publicly available information; (b) varying levels of governmental regulation and supervision; (c) the difficulty of enforcing legal rights in a foreign jurisdiction and uncertainties as to the status, interpretation and application of laws; and (d) foreign exchange controls. Moreover accounting, auditing and financial reporting standards, practices and requirements may vary from jurisdiction to jurisdiction. Different markets also have different clearance and settlement procedures, which could create delays in the purchase and sale of assets forming part of the Portfolio. Delays in settlement could result in periods when assets of the Issuer are uninvested or invested in short term investments with low yields. The inability to sell assets due to settlement problems could result in losses due to subsequent declines in the value of the assets.""",
        {"entities": []}
    ),
    (
        """The offering of the Notes has been structured so that the Notes are assumed to be able to withstand certain assumed losses relating to defaults on the underlying Collateral Debt Obligations. See “Ratings of the Notes”. There is no assurance that actual losses will not exceed such assumed losses. If any losses exceed such assumed levels, payments on the Notes could be adversely affected by such defaults. To the extent that a default occurs with respect to any Collateral Debt Obligation securing the Notes and the Issuer sells or otherwise disposes of such Collateral Debt Obligation, it is likely that the proceeds of such sale or disposition will be less than the unpaid principal and interest thereon.""",
        {"entities": [(297, 405, "Conditional")]}
    ),
    (
        """Group B: Austria, Belgium, Canada, Germany, Israel, Japan, Luxembourg, Portugal, South Africa, Switzerland, U.S. Group C: Argentina, Brazil, Chile, France, Greece, Italy, Mexico, South Korea, Spain, Taiwan, Turkey, United Arab Emirates""",
        {"entities": []}
    ),
    (
        """The purpose of this ERISA Certificate (this “Certificate”) is, among other things, to (i) endeavour to ensure that less than 25 per cent. of the value of the [Class E Notes] [Class F Notes] [Subordinated Notes] (determined separately by class) issued by Jubilee CLO 2014-XI B.V. (the “Issuer”) is held by (a) an employee benefit plan that is subject to the fiduciary responsibility provisions of Title I of the Employee Retirement Income Security Act of 1974, as amended (“ERISA”), (b) a plan that is subject to Section 4975 of the Internal Revenue Code of 1986 (the “Code”) or (c) any entity whose underlying assets include “plan assets” by reason of any such employee benefit plan’s or plan’s investment in the entity (collectively, “Benefit Plan Investors”), (ii) obtain from you certain representations and agreements and (iii) provide you with certain related information with respect to your acquisition, holding or disposition of [Class E Notes] [Class F Notes] [Subordinated Notes]. By signing this Certificate, you agree to be bound by its terms.""",
        {"entities": []}
    ),
    (
        """Please be aware that the information contained in this Certificate is not intended to constitute advice and the examples given below are not intended to be, and are not, comprehensive. You should contact your own counsel if you have any questions in completing this Certificate. Capitalised terms not defined in this Certificate shall have the meanings ascribed to them in the Trust Deed.""",
        {"entities": [(185, 277, "Conditional")]}
    ),
    (
        """If a box is not checked, you are agreeing that the applicable Section does not, and will not, apply to you.""",
        {"entities": [(0, 106, "Conditional")]}
    ),
    (
        """1. □ Employee Benefit Plans Subject to ERISA or the Code. We, or the entity on whose behalf we are acting, are an “employee benefit plan” within the meaning of Section 3(3) of ERISA that is subject to the fiduciary responsibility provisions of Title I of ERISA or a “plan” within the meaning of Section 4975(e)(1) of the Code that is subject to Section 4975 of the Code.""",
        {"entities": []}
    ),
    (
        """2. □ Entity Holding Plan Assets. We, or the entity on whose behalf we are acting, are an entity or fund whose underlying assets include “plan assets” by reason of a Benefit Plan Investor’s investment in such entity.""",
        {"entities": []}
    ),
    (
        """(iv) by our acceptance of an interest in the [Class E Notes] [Class F Notes] [Subordinated Notes], we agree to cooperate with the Issuer to effect such transfers; (v) the proceeds of such sale, net of any commissions, expenses and taxes due in connection with such sale shall be remitted to us; and (vi) the terms and conditions of any sale under this sub-section shall be determined in the sole discretion of the Issuer, and the Issuer shall not be liable to us as a result of any such sale or the exercise of such discretion.""",
        {"entities": []}
    ),
    (
        """9. Further Acknowledgement and Agreement. We acknowledge and agree that (i) all of the assurances contained in this Certificate are for the benefit of the Issuer, the Trustee, Merrill Lynch International and the Investment Manager as third party beneficiaries hereof, (ii) copies of this Certificate and any information contained herein may be provided to the Issuer, the Trustee, Merrill Lynch International, the Investment Manager, affiliates of any of the foregoing parties and to each of the foregoing parties’ respective counsel for purposes of making the determinations described above and (iii) any acquisition or transfer of [Class E Notes] [Class F Notes] [Subordinated Notes] by us that is not in accordance with the provisions of this Certificate shall be null and void from the beginning, and of no legal effect.""",
        {"entities": []}
    ),
    (
        """(a) if the Collateral Debt Obligation has been specifically assigned a recovery rate by Moody’s (for example, in connection with the assignment by Moody’s of an estimated rating), such recovery rate;""",
        {"entities": [(3, 198, "Conditional")]}
    ),
    (
        """(c) if the Collateral Debt Obligation is a Corporate Rescue Loan (other than a Corporate Rescue Loan which has been specifically assigned a recovery rate by Moody’s), 50 per cent. * If such Collateral Debt Obligation is publicly rated by Moody’s and does not have both a CFR and an Assigned Moody’s Rating, such Collateral Debt Obligation will be deemed to be an Unsecured Senior Obligation or High- Yield Bond for purposes of this table. REGISTERED OFFICE OF THE ISSUER Jubilee CLO 2014-XI B.V. Herikerbergweg 238 1101 CM Amsterdam Zuidoost INVESTMENT MANAGER Alcentra Limited 10 Gresham Street London EC2V 7JD CALCULATION AGENT, PRINCIPAL PAYING AGENT, ACCOUNT BANK, COLLATERAL ADMINISTRATOR, CUSTODIAN and INFORMATION AGENT The Bank of New York Mellon, London Branch One Canada Square London E14 5AL ‎TRUSTEE Law Debenture Trust Company of New York 400 Madison Avenue Suite 4D New York NY 10017 REGISTRAR and TRANSFER AGENT The Bank of New York Mellon (Luxembourg) S.A. Vertigo Building – Polaris 2-4 rue Eugène Ruppert L-2453 Luxembourg ‎LIQUIDITY FACILITY PROVIDER The Bank of New York Mellon One Canada Square London E14 5AL ‎IRISH LISTING AGENT The Bank of New York Mellon S.A./ N.V. Dublin Branch Hanover Building Windmill Lane Dublin 2 LEGAL ADVISERS To the Arranger and Initial Purchaser as to English Law and as to U.S. Law Weil, Gotshal & Manges 110 Fetter Lane London EC4A 1AY ‎To the Issuer as to Dutch Law Baker & McKenzie Amsterdam N.V. Claude Debussylaan 54 1082MD Amsterdam To the Investment Manager as to English Law Linklaters LLP One Silk Street London EC2Y 8HQ ‎To the Trustee and Liquidity Facility Provider as to English Law Allen & Overy LLP One Bishops Square London E1 6AD""",
        {"entities": [(4, 178, "Conditional"), (182, 437, "Conditional")]}
    ),
    (
        """0.01 per cent.) without exceeding the Non-Adjusted Weighted Average Spread as of such Measurement Date (the “S&P Matrix Spread”) and (B) the applicable weighted average coupon will be the coupon between 6 per cent. and 15 per cent. (in increments of 0.01 per cent.) without exceeding the Non-Adjusted Weighted Average Fixed Rate Coupon as of such Measurement Date (the “S&P Matrix Coupon” and together with the S&P Matrix Spread, the “S&P Matrix Spread and Coupon” ) and (C) the applicable weighted average recovery rate with respect to each Class of Notes, chosen independently, will be the recovery between (i) in the case of the Class A Notes, 20 per cent. and 50 per cent., (ii) in the case of the Class B Notes, 26 per cent. and 60 per cent., (iii) in the case of the Class C Notes, 33 per cent. and 66 per cent., (iv) in the case of the Class D Notes, 38 per cent. and 72 per cent., (v) in the case of the Class E Notes, 43 per cent. and 78 per cent. and (vi) in the case of the Class F Notes, 50 per cent. and 85 per cent. (in each case, in increments of 0.05 per cent.) (the “Recovery Rate Case”) in each case as selected by the Investment Manager.""",
        {"entities": []}
    ),
    (
        """Subject to the satisfaction of certain conditions in the Investment Management and Collateral Administration Agreement and the Trading Requirements (so long as they are applicable), the Investment Manager shall be authorised to purchase, on behalf of the Issuer, Non-Euro Obligations from time to time provided that any such Non- Euro Obligation shall only constitute a Collateral Debt Obligation that satisfies paragraph (b) of the Eligibility Criteria if the Investment Manager, on behalf of the Issuer, enters, as soon as practicable following entry into a binding commitment to purchase such Collateral Debt Obligation and no later than the settlement date of the acquisition of the relevant Collateral Debt Obligation, into an Asset Swap Transaction (which shall relate to the purchased Collateral Debt Obligation) pursuant to which the currency risk arising from receipt of cash flows from such Non-Euro Obligations, including interest and principal payments, is hedged through the swapping of such cash flows for Euro payments to be made by an Asset Swap Counterparty. Subject to the satisfaction of the Hedging Condition, the Investment Manager (on behalf of the Issuer) shall be authorised to enter into spot exchange transactions, as necessary, but solely to fund the Issuer’s payment obligations under any Asset Swap Transaction. Rating Agency Confirmation shall be required in relation to entry into each Asset Swap Transaction unless such Asset Swap Transaction is a Form-Approved Asset Swap. See the “Hedging Arrangements” section of this Offering Circular.""",
        {"entities": [(206, 1074, "Conditional")]}
    ),
    (
        """The Notes will be offered by the Issuer through Merrill Lynch International in its capacity as initial purchaser of the offering of such Notes (the “Initial Purchaser”) subject to prior sale, when, as and if delivered to and accepted by the Initial Purchaser, and to certain conditions. It is expected that delivery of the Notes will be made on or about the Issue Date. The Initial Purchaser may offer the Notes at prices as may be negotiated at the time of sale which may vary among different purchasers.""",
        {"entities": [(0, 285, "Conditional")]}
    ),
    (
        """therefor""",
        {"entities": []}
    ),
    (
        """To permit compliance with the Securities Act in connection with the sale of the Notes in reliance on Rule 144A, the Issuer will be required under the Trust Deed to furnish upon request to a holder or beneficial owner who is a QIB of a Note sold in reliance on Rule 144A or a prospective investor who is a QIB designated by such holder or beneficial owner the information required to be delivered under Rule 144A(d)(4) under the Securities Act if at the time of the request the Issuer is neither a reporting company under section 13 or section 15(d) of the United States Securities Exchange Act of 1934, as amended, nor exempt from reporting pursuant to Rule 12g3-2(b) under the Exchange Act. All information made available by the Issuer pursuant to the terms of this paragraph may also be obtained during usual business hours free of charge at the office of the Principal Paying Agent.""",
        {"entities": [(112, 691, "Conditional")]}
    ),
    (
        """IF TRADING OR ENTERING INTO HEDGE AGREEMENTS WOULD RESULT IN THE ISSUER’S ACTIVITIES FALLING WITHIN THE DEFINITION OF A “COMMODITY POOL” UNDER THE COMMODITY EXCHANGE ACT, THE INVESTMENT MANAGER EXPECTS TO BE EXEMPT FROM REGISTRATION WITH THE COMMODITY FUTURES TRADING COMMISSION (THE “CFTC”) AS A COMMODITY POOL OPERATOR (A “CPO”) PURSUANT TO CFTC RULE 4.13(a)(3). THEREFORE, UNLIKE A REGISTERED CPO, THE INVESTMENT MANAGER WOULD NOT BE REQUIRED TO DELIVER A CFTC DISCLOSURE DOCUMENT TO PROSPECTIVE INVESTORS, NOR WOULD IT BE REQUIRED TO PROVIDE INVESTORS WITH CERTIFIED ANNUAL REPORTS THAT SATISFY THE REQUIREMENTS OF CFTC RULES APPLICABLE TO REGISTERED CPOs. FURTHER, THE TRADING OR ENTERING INTO SUCH HEDGE AGREEMENT MUST NOT ELIMINATE THE ISSUER’S ABILITY TO RELY ON RULE 3A-7 UNDER THE INVESTMENT COMPANY ACT, UNLESS AND UNTIL THE ISSUER ELECTS TO RELY SOLELY ON THE EXEMPTION UNDER SECTION 3(C)(7) UNDER THE INVESTMENT COMPANY ACT.""",
        {"entities": [(0, 363, "Conditional")]}
    ),
    (
        """Agency""",
        {"entities": []}
    ),
    (
        """2 Applicable during a Frequency Switch Period (or from the Interest Determination Date immediately prior to a Frequency Switch Period if a Frequency Switch Period will commence during the following Accrual Period or, if at the time of the Interest Determination Date immediately prior to a Frequency Switch Period it was not known that a Frequency Switch Period would commence during the following Accrual Period, commencing from the Interest Determination Date immediately after the Frequency Switch Period begins).""",
        {"entities": [(47, 513, "Conditional")]}
    ),
    (
        """Obligations which are to constitute Collateral Debt Obligations in respect of which the Issuer or the Investment Manager, on behalf of the Issuer, has entered into a binding commitment to purchase but which have not yet settled shall be included as Collateral Debt Obligations in the calculation of the Portfolio Profile Tests and Collateral Quality Tests at any time as if such purchase had been completed. Collateral Debt Obligations in respect of which the Issuer has entered into a binding commitment to sell but which have not yet settled shall be excluded as Collateral Debt Obligations in the calculation of the Collateral Quality Tests and Portfolio Profile Tests at any time as if such sale had been completed. Coverage TestsEach of the Par Value Tests and Interest Coverage Tests shall be satisfied on a Measurement Date in the case of: (i) the Par Value Tests, on and after the Effective Date; and (ii) the Interest Coverage Tests on and after the Determination Date immediately preceding the second Payment Date, if the corresponding Par Value Ratio or Interest Coverage Ratio (as the case may be) is at least equal to the percentage specified in the table below in relation to that Coverage Test""",
        {"entities": [(201, 405, "Conditional"), (408, 717,
                                                  "Conditional"), (720, 1208, "Conditional")]}
    ),
    (
        """If the Class F Par Value Ratio is less than 104.24 per cent., on the relevant Determination Date, Interest Proceeds shall be paid to the Principal Account during the Reinvestment Period, for the acquisition of additional Collateral Debt Obligations in an amount (such amount, the “Required Diversion Amount”) equal to the lesser of (1) 50 per cent. of all remaining Interest Proceeds available for payment pursuant to paragraph (W) of the Interest Proceeds Priority of Payments and (2) the amount which, after giving effect to the payment of all amounts payable in respect of paragraphs (A) to (V) (inclusive) of the Interest Proceeds Priority of Payments, would be sufficient to cause the Reinvestment Overcollateralisation Test to be met as of the relevant Determination Date after giving effect to any payments made pursuant to paragraph (W) of the Interest Proceeds Priority of Payments, such amounts to be applied during the Reinvestment Period to purchase additional Collateral Debt Obligations.""",
        {"entities": [(0, 1000, "Conditional")]}
    ),
    (
        """This Offering Circular does not constitute a prospectus for the purposes of Article 5 of Directive 2003/71/EC (as such directive may be amended from time to time, the “Prospectus Directive”). The Issuer is not offering the Notes in any jurisdiction in circumstances that would require a prospectus to be prepared pursuant to the Prospectus Directive. Application has been made to the Irish Stock Exchange for the Notes to be admitted to the official list (the “Official List”) and trading on the Global Exchange Market of the Irish Stock Exchange (the “Global Exchange Market”). There can be no assurance that any such approval will be granted or, if granted, that such listing will be maintained. Application has been made to the Irish Stock Exchange to approve this Offering Circular. This Offering Circular constitutes listing particulars for the purpose of this application.""",
        {"entities": [(579, 696, "Conditional")]}
    )
]

TEST_DATA = [
    (
        """In this Offering Circular, unless otherwise specified or the context otherwise requires, all references to “Euro”, “euro”, “€” and “EUR” are to the lawful currency of the member states of the European Union that have adopted and retain the single currency in accordance with the Treaty establishing the European Community, as amended from time to time provided that if any member state or states ceases to have such single currency as its lawful currency (such member state(s) being the “Exiting State(s)”), the euro shall, for the avoidance of doubt, mean for all purposes the single currency adopted and retained as the lawful currency of the remaining member states and shall not include any successor currency introduced by the Exiting State(s) but for the avoidance of doubt shall not affect any definition of euro used in respect of the Collateral and any references to “US Dollar”, “US dollar”, “USD”, “U.S. Dollar” or “$” shall mean the lawful currency of the United States of America.""",
        {"entities": [(365, 992, "Conditional")]}
    ),
    (
        """In Europe, the U.S. and elsewhere there has been, and there continues to be increased political and regulatory scrutiny of banks,
        financial institutions, “shadow banking entities” and the asset-backed securities industry. This has resulted in a raft of measures
        for increased regulation which are currently at various stages of implementation and which may have an adverse impact on the regulatory
        capital charge to certain investors in securitisation exposures and/or the incentives for certain investors to hold or trade asset-backed
        securities, and may thereby affect the liquidity of such securities.""",
        {"entities": []}
    ),
    (
        """If any determination is made that this transaction is subject to the U.S. Risk Retention Rules, the Collateral Manager may fail to comply
        (or not be able to comply) with the U.S. Risk Retention Rules, which may have a material adverse effect on the Collateral Manager, the Issuer
        and/or the market value and/or liquidity of the Notes.""",
        {"entities": [(0, 332, "Conditional")]}
    ),
    (
        """IFMD introduced authorisation and regulatory requirements for managers of AIFs. If the Issuer were to be considered to be an AIF within the meaning in AIFMD, it would need to be managed by a manager authorised under AIFMD (an “AIFM”). The Collateral Manager is not authorised under AIFMD but is authorised under MiFID II. If considered to be an AIF, the Issuer would also be classified as an FC under EMIR and may be required to comply with clearing obligations and/or other risk mitigation techniques (including obligations to post margin to any central clearing counterparty or market counterparty) with respect to Hedge Transactions (under the EMIR REFIT
        all AIFs will be FCs whether or not managed by an authorised AIFM). See also “European Market Infrastructure Regulation (EMIR)” above.""",
        {"entities": [(80, 233, "Conditional"),
                      (321, 790, "Conditional")]}
    ),
    (
        """If the SSPE Exemption does not apply and the Issuer is considered to be an AIF, the Collateral Manager may not be
        able to continue to manage the Issuer’s assets, or its ability to do so may be impaired. As a result, any application of
        the AIFMD may affect the return investors receive from their investment""",
        {"entities": [(0, 307, "Conditional")]}
    ),
    (
        """The Issuer (or the Investment Manager acting on behalf of the Issuer) reserves the right to request such information as is necessary to verify the identity of a Noteholder and the source of the payment of subscription monies, or as is necessary to comply with any customer identification programs required by FinCEN and/or the SEC or any other applicable AML Requirements. If there is a delay or failure by the applicant to produce any information required for verification purposes,
        an application for or transfer of Notes and the subscription monies relating thereto may be refused.""",
        {"entities": [(372, 583, "Conditional")]}
    ),
    (
        """If there is an early redemption, the holders of the Notes will be repaid prior to the Maturity Date. Where the Notes are to be redeemed by liquidation, there can be no assurance that the Sale Proceeds realised and other available funds would permit any distribution on the Subordinated Notes after all required payments are made to the holders of the Rated Notes. In addition, an Optional Redemption could require the Investment Manager to liquidate positions more rapidly than would otherwise be desirable,
        which could adversely affect the realised value of the Collateral Debt Obligations sold.""",
        {"entities": [(0, 99, "Conditional")]}
    ),
    (
        """If at any time one or more investors that are affiliated hold a majority of any Class of Notes, it may be more difficult for other investors to take certain actions that require consent of any such Classes of Notes without their consent. For example, optional redemption and the removal of the Investment Manager for cause and appointment
        are at the direction of Noteholders of specified percentages of Subordinated Notes and/or the Controlling Class (as applicable).""",
        {"entities": [(0, 236, "Conditional")]}
    ),
    (
        """If a Hedge Counterparty is subject to a rating withdrawal or downgrade by the Rating Agencies to below the applicable Rating Requirement, there will generally be a termination event under the applicable Hedge Agreement unless, within the applicable grace period following such rating withdrawal or downgrade, such Hedge Counterparty either transfers its obligations under the applicable Hedge Agreement to a replacement counterparty with the requisite ratings, obtains a guarantee of its obligations by a guarantor with the requisite ratings, collateralises its obligations in a manner satisfactory
        to the Rating Agencies or employs some other strategy as may be approved by the Rating Agencies.""",
        {"entities": [(0, 217, "Conditional")]}
    ),
    (
        """The Issuer will depend upon the Asset Swap Counterparty to perform its obligations under any hedges. If the Asset Swap Counterparty defaults or becomes unable to perform due to insolvency or otherwise, the Issuer may not receive payments it would otherwise be entitled to from the Asset Swap Counterparty to cover its foreign exchange exposure.""",
        {"entities": [(101, 343, "Conditional")]}
    ),
    (
        """In considering proposals by the examiner, it is likely that secured and unsecured creditors would form separate classes of creditors. In the case of the Issuer, if the Trustee represented the majority in number and value of claims within the secured creditor class, the Trustee would be in a position to reject any proposal not in favour of the Noteholders. The Trustee would also be entitled to argue at the relevant Irish court hearing at which the proposed scheme of arrangement is considered that the proposals are unfair and inequitable in relation to the Noteholders,
         especially if such proposals included a writing down to the value of amounts due by the Issuer to the Noteholders.""",
        {"entities": [(160, 356, "Conditional")]}
    ),
    (
        """The Issuer will depend upon the Asset Swap Counterparty to perform its obligations under any hedges. If the Asset Swap Counterparty defaults or becomes unable to perform due to insolvency or otherwise, the Issuer may not receive payments it would otherwise be entitled to from the Asset Swap Counterparty to cover its foreign exchange exposure.""",
        {"entities": [(100, 343, "Conditional")]}
    ),
    (
        """“Principal Proceeds” means all amounts paid or payable into the Principal Account from time to time and, with respect to any Payment Date, means Principal Proceeds received or receivable by the Issuer during the related Due Period and any other amounts to be disbursed as Principal Proceeds on such
        Payment Date pursuant to Condition 3(c)(ii) (Application of Principal Proceeds) or Condition 11(b) (Enforcement).""",
        {"entities": []}
    ),
    (
        """In connection with the issue and sale of the Notes, no person is authorised to give any information or to make any representation not contained in this Prospectus and, if given or made, such information or representation must not be relied upon as having been authorised by or on behalf of the Issuer, the Placement Agent, the Trustee, the Collateral Manager, the Retention Holder or the Collateral Administrator.
        The delivery of this Prospectus at any time does not imply that the information contained in it is correct as at any time subsequent to its date.""",
        {"entities": [(51, 412, "Conditional")]}
    ),
    (
        """Where Notes are redeemable at the discretion of a transaction party or a particular Class of Noteholders, there is no obligation to consider the interests of any other party or Class of Noteholders when exercising such discretion. Furthermore, where one or more Classes of Rated Notes are redeemed through a Refinancing, Noteholders should be aware that any such redemption would occur outside of the Note Payment Sequence and the Priorities of Payment. In addition Noteholders of a Class of Rated Notes that are redeemed through a Refinancing should be aware that the Applicable Margin of any new Notes will be equal to or lower than the Applicable Margin of such Rated Notes immediately prior to such Refinancing. In addition, a Refinancing may result in a Class of Rated Notes having a shorter maturity date than other Classes of Rated Notes.""",
        {"entities": [(0, 230, "Conditional"), (231, 453, "Conditional")]}
    ),
    (
        """U.S. Federal Tax Treatment of U.S. Holders of Subordinated Notes""",
        {"entities": []}
    ),
    (
        """So long as any of the Notes remain outstanding, the Issuer will be subject to the restrictions set out in the Conditions and in the Trust Deed. In particular, the Issuer has undertaken not to carry out any business other than the issue of the Notes and acquiring, holding and disposing of the Portfolio in accordance with the Conditions and the Collateral Management and Administration Agreement, entering into the Trust Deed, the Agency and Account Bank Agreement, the Collateral Management and Administration Agreement, the Issuer Management Agreement, any Collateral Acquisition Agreements, the Subscription Agreement, the Forward Purchase Agreement and any Hedge Agreements and exercising the rights and performing the obligations under each such agreement and all other transaction documents incidental thereto. The Issuer will not have any substantial liabilities other than in connection with the Notes and any secured obligations. The Issuer will not have any subsidiaries and, save in respect of the fees and expenses generated in connection with the issue of the Notes (referred to below), any related profits and the proceeds of any deposits and investments made from such fees or from amounts representing the proceeds of the Issuer’s issued share capital, the Issuer will not accumulate any surpluses.""",
        {"entities": []}
    ),
    (
        """For the avoidance of doubt, and following the adoption of the final disclosure templates in respect of the EU Retention and Transparency Requirements if the Collateral Administrator agrees to assist the Issuer and the Collateral Manager in providing reporting on behalf of the Issuer, the Collateral Administrator will not assume any responsibility for the Issuer’s obligations as the entity responsible for fulfilling the reporting obligations under the EU Retention and Transparency Requirements. In making available such information and reporting, the Collateral Administrator will not assume responsibility or liability to any third party, including the Noteholders and potential Noteholders (including for the use or onward disclosure of any such information or documentation), and shall have the benefit of the powers, protections and indemnities granted to it under the Collateral Management and Administration Agreement and the other Transaction Documents.""",
        {"entities": [(150, 497, "Conditional")]}
    ),
    (
        """In addition, in relation to the reporting obligations in the EU Retention and Transparency Requirements, (a) the Issuer will be designated as the entity responsible to fulfil such reporting obligations, (b) the Collateral Manager will undertake to provide to the Collateral Administrator and the Issuer (and any applicable third party reporting entity) any reports, data and other information, as may be reasonably required in connection with the proper performance by the Issuer, as the reporting entity, of its obligation to make available to the Noteholders, potential investors in the Notes and the competent authorities the reports and information necessary for the Issuer to fulfil the reporting requirements of Article 7 (Transparency requirements for originators, sponsors and SSPEs) of the Securitisation Regulation (and prior to the adoption of final disclosure templates in respect of the Transparency Requirements of Article 7 (Transparency requirements for originators, sponsors and SSPEs) of the Securitisation Regulation, the Issuer intends to fulfil those requirements contained in subparagraphs (a) and (e) of Article 7(l) of the Securitisation Regulation through the Monthly Reports and the Payment Date Reports, see “Description of the Reports”) and (c) following the adoption of the final disclosure templates in respect of the EU Retention and Transparency Requirements the Issuer (with the consent of the Collateral Manager) will propose in writing to the Collateral Administrator the form, content, method of distribution and timing of such reports and information. The Collateral Administrator shall consult with the Issuer and the Collateral Manager and, if it agrees (in its sole and absolute discretion) to assist the Issuer in providing such reporting on such proposed terms, shall confirm in writing to the Issuer and the Collateral Manager and shall make such information (as provided to it by the Collateral Manager and the Issuer) available (or procure that such information is made available) via a website currently located at https://sf.citidirect.com (or such other website as may be notified in writing by the Collateral Administrator to the Issuer, the Trustee and the Collateral Manager and as further notified by the Issuer to the Noteholders in accordance with Condition 16 (Notices)) which shall be accessible to any person who certifies (substantially in the form set out in the Collateral Management Agreement or such other form which may be agreed between the Issuer, the Collateral Manager and the Collateral Administrator from time to time) (which certificate may be given electronically and upon which certificate the Collateral Administrator shall be entitled to rely absolutely and without enquiry or liability) to the Collateral Administrator that it is a competent authority, a Noteholder or a potential investor in the Notes (and in such other manner as required by any competent authority (as instructed to the Collateral Administrator by the Issuer and as agreed with the Collateral Administrator)). If the Collateral Administrator does not agree on the terms of reporting or, in the reasonable opinion of the Issuer (acting on the advice of the Collateral Manager), the Collateral Administrator is or will be unable or unwilling to provide such reporting, the Issuer (with the consent of the Collateral Manager) shall be entitled to appoint another entity to make the relevant information available for the purposes of Article 7 (Transparency requirements for originators, sponsors and SSPEs) of the Securitisation Regulation.""",
        {"entities": [(1680, 3053, "Conditional"),
                      (3055, 3581, "Conditional")]}
    ),
    (
        """The Issuer may be deemed to be a “covered fund” under the Volcker Rule and, in such circumstances, in the absence of regulatory relief, the provisions of the Volcker Rule and its related regulatory provisions, will severely limit the ability of U.S. “banking entities” and non-U.S. affiliates of U.S. banking institutions to hold an ownership interest in the Issuer or enter into financial transactions with the Issuer. If the Issuer is deemed to be a “covered fund”, this could significantly impair the marketability and liquidity of the Refinancing Notes.""",
        {"entities": [(420, 556, "Conditional")]}
    ),
    (
        """BASED UPON INTERPRETIVE GUIDANCE PROVIDED FROM A DIVISION OF THE U.S. COMMODITY FUTURES TRADING COMMISSION (THE “CFTC”), THE ISSUER IS NOT EXPECTED TO BE TREATED AS A COMMODITY POOL AND AS SUCH, THE ISSUER (OR THE COLLATERAL MANAGER ON THE ISSUER’S BEHALF) MAY ENTER INTO ONE OR MORE HEDGE AGREEMENTS (OR ANY OTHER AGREEMENT THAT WOULD FALL WITHIN THE DEFINITION OF “SWAP” AS SET OUT IN THE CEA (AS DEFINED BELOW)) FOLLOWING RECEIPT OF LEGAL ADVICE FROM REPUTABLE COUNSEL TO THE EFFECT THAT NONE OF THE ISSUER, ITS DIRECTORS OR OFFICERS, OR THE COLLATERAL MANAGER OR ANY OF ITS DIRECTORS, OFFICERS OR EMPLOYEES, SHOULD BE REQUIRED TO REGISTER WITH THE CFTC AS EITHER A “COMMODITY POOL OPERATOR” (AS SUCH TERM IS DEFINED IN THE U.S. COMMODITY EXCHANGE ACT OF 1936, AS AMENDED (THE “CEA”) AND CFTC REGULATIONS IN RESPECT OF THE ISSUER. IN THE EVENT THAT TRADING OR ENTERING INTO ONE OR MORE HEDGE AGREEMENTS WOULD RESULT IN THE ISSUER’S ACTIVITIES FALLING WITHIN THE DEFINITION OF A “COMMODITY POOL”, THE COLLATERAL MANAGER WOULD EITHER SEEK TO UTILIZE ANY AVAILABLE EXEMPTIONS FROM REGISTRATION AS A COMMODITY POOL OPERATOR (A “CPO”) OR REGISTER AS A CPO. UTILIZING ANY SUCH EXEMPTION FROM REGISTRATION MAY IMPOSE ADDITIONAL COSTS ON THE COLLATERAL MANAGER, AND MAY SIGNIFICANTLY LIMIT ITS ABILITY TO ENGAGE IN HEDGING ACTIVITIES ON BEHALF OF THE ISSUER. IF THE COLLATERAL MANAGER IS REQUIRED TO REGISTER AS A CPO/CTA, IT WILL BECOME SUBJECT TO NUMEROUS REPORTING AND OTHER REQUIREMENTS AND IT IS EXPECTED THAT IT WILL INCUR SIGNIFICANT ADDITIONAL COSTS IN COMPLYING WITH ITS OBLIGATIONS AS A REGISTERED CPO, WHICH COSTS ARE EXPECTED TO BE PASSED ON TO THE ISSUER AND MAY ADVERSELY AFFECT THE ISSUER’S ABILITY TO MAKE PAYMENT ON THE NOTES.""",
        {"entities": [(1353, 1737, "Conditional")]}
    ),
    (
        """Many financial institutions, including banks, continue to suffer from capitalisation issues in a regulatory environment which may increase the capital requirements for certain businesses. The bankruptcy or insolvency of a major financial institution may have an adverse effect on the Issuer, particularly if such financial institution is a grantor of a participation in an asset or is a hedge counterparty to a swap or hedge involving the Issuer, or a counterparty to a buy or sell trade that has not settled with respect to an asset. The bankruptcy, insolvency or financial distress of another financial institution may result in the""",
        {"entities": [(188, 532, "Conditional")]}
    ),
    (
        """Upon any withdrawal from the EU by the UK, and subject to agreement on (and the terms of) any future EU-UK relationship, EU laws (other than those EU laws transposed into English law (see below)) will cease to apply within the UK pursuant to the terms and timing of a future withdrawal agreement. This would be achieved by the UK ceasing to be party to the Treaty on European Union and the Treaty on the Functioning of the European Union, and by the parallel repeal of the European Communities Act 1972. The UK will cease to be a member of the EU from the date of entry into force of a withdrawal agreement or, if a withdrawal agreement has not been concluded, two years after the notification under Article 50 was served, unless the European Council, in agreement with the UK, unanimously decides to extend this period (in respect of which see below).""",
        {"entities": [(611, 851, "Conditional")]}
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
    )


]

if __name__ == "__main__":
    print(len(TEST_DATA))
