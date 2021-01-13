# -*- coding: utf-8 -*-

class ReportTransactionPayStatementMatchTypesEnum(object):

    """Implementation of the 'Report Transaction Pay Statement Match Types' enum.

    Pay Statement matches found at the transaction level

    Attributes:
        DATE: The transaction date matched the date on the pay statement
        NET_AMOUNT: The transaction amount matched the net pay amount on the
            pay statement
        INTERVIEW_AMOUNT: The transaction amount matched the net pay amount
            the consumer entered during the Connect interview process.
        LESS_THAN_NET_PAY: The transaction amount was less than the net pay
            amount on the pay statement
        EMPLOYER_NAME: The transaction description included a match to the
            employer name that was on the pay statement
        INCOME_STREAM_PAYCHECK: The income stream type was paycheck
        DIRECT_DEPOSIT_AMOUNT: The transaction amount matched the direct
            deposit amount on the pay statement
        PAYROLL_PROVIDER: The transaction description included a match to the
            payroll provider name that was on the pay statement

    """

    DATE = 'DATE'

    NET_AMOUNT = 'NET_AMOUNT'

    INTERVIEW_AMOUNT = 'INTERVIEW_AMOUNT'

    LESS_THAN_NET_PAY = 'LESS_THAN_NET_PAY'

    EMPLOYER_NAME = 'EMPLOYER_NAME'

    INCOME_STREAM_PAYCHECK = 'INCOME_STREAM_PAYCHECK'

    DIRECT_DEPOSIT_AMOUNT = 'DIRECT_DEPOSIT_AMOUNT'

    PAYROLL_PROVIDER = 'PAYROLL_PROVIDER'

