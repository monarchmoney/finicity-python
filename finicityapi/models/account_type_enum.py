# -*- coding: utf-8 -*-

class AccountTypeEnum(object):

    """Implementation of the 'Account Type' enum.

    The enumeration of supported account types

    Attributes:
        CHECKING: Standard checking
        SAVINGS: Standard savings
        CD: Certificates of deposit
        MONEYMARKET: Money Market
        CREDITCARD: Standard credit cards
        LINEOFCREDIT: Home equity,line of credit
        INVESTMENT: Generic investment (no details)
        INVESTMENTTAXDEFERRED: Generic tax-advantaged investment (no details)
        EMPLOYEESTOCKPURCHASEPLAN: ESPP, Employee Stock Ownership Plans
            (ESOP), Stock Purchase Plans
        IRA: Individual Retirement Account (not Rollover or Roth)
        401K: 401K Plan
        ROTH: Roth IRA, Roth 401K
        403B: 403B Plan
        529PLAN: 529 Plan (True value s 529)
        ROLLOVER: Rollover IRA
        UGMA: Uniform Gifts to Minors Act
        UTMA: Uniform Transfers to Minors Act
        KEOGH: Keogh Plan
        457PLAN: 457 Plan (True value is 457)
        401A: 401A Plan
        MORTGAGE: Standard Mortgages
        LOAN: Auto loans, equity loans, other loans
        STUDENTLOAN: Student Loan Account
        UNKNOWN: UNK Description

    """

    CHECKING = 'checking'

    SAVINGS = 'savings'

    CD = 'cd'

    MONEYMARKET = 'moneyMarket'

    CREDITCARD = 'creditCard'

    LINEOFCREDIT = 'lineOfCredit'

    INVESTMENT = 'investment'

    INVESTMENTTAXDEFERRED = 'investmentTaxDeferred'

    EMPLOYEESTOCKPURCHASEPLAN = 'employeeStockPurchasePlan'

    IRA = 'ira'

    401K = '401k'

    ROTH = 'roth'

    403B = '403b'

    529PLAN = '529plan'

    ROLLOVER = 'rollover'

    UGMA = 'ugma'

    UTMA = 'utma'

    KEOGH = 'keogh'

    457PLAN = '457plan'

    401A = '401a'

    MORTGAGE = 'mortgage'

    LOAN = 'loan'

    STUDENTLOAN = 'StudentLoan'

    UNKNOWN = 'Unknown'

