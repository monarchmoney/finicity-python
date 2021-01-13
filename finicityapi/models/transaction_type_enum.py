# -*- coding: utf-8 -*-

class TransactionTypeEnum(object):

    """Implementation of the 'Transaction Type' enum.

    If provided by the institution, the following values may be returned in
    the field of a record:

    Attributes:
        ATM: ATM debit or credit (depends on signage of amount)
        CASH: Cash withdrawal
        CHECK: Check
        CREDIT: Generic credit
        DEBIT: Generic debit
        DEPOSIT: Deposit
        DIRECTDEBIT: Merchant initiated debit
        DIRECTDEPOSIT: Direct deposit
        DIVIDEND: Dividend
        FEE: Institution fee
        INTEREST: Interest earned or paid (depends on signage of amount)
        OTHER: Type is not known or doesn’t match types available in this
            list
        PAYMENT: Electronic payment
        POINTOFSALE: Point of sale debit or credit (depends on signage of
            amount)
        REPEATPAYMENT: Repeating payment/standing order
        SERVICECHARGE: Service charge
        TRANSFER: Transfer

    """

    ATM = 'atm'

    CASH = 'cash'

    CHECK = 'check'

    CREDIT = 'credit'

    DEBIT = 'debit'

    DEPOSIT = 'deposit'

    DIRECTDEBIT = 'directDebit'

    DIRECTDEPOSIT = 'directDeposit'

    DIVIDEND = 'dividend'

    FEE = 'fee'

    INTEREST = 'interest'

    OTHER = 'other'

    PAYMENT = 'payment'

    POINTOFSALE = 'pointOfSale'

    REPEATPAYMENT = 'repeatPayment'

    SERVICECHARGE = 'serviceCharge'

    TRANSFER = 'transfer'

