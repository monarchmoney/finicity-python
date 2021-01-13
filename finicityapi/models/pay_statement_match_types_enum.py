# -*- coding: utf-8 -*-

class PayStatementMatchTypesEnum(object):

    """Implementation of the 'Pay Statement Match Types' enum.

    TODO: type enum description here.

    Attributes:
        NET_PAY_MATCH: Single transaction matching the net pay of the pay
            statement
        SPLIT_INTERVIEW_AMOUNT_SUM_TO_NET_PAY_MATCH: Multiple transactions
            matching up to the interview amounts if present
        SPLIT_DIRECT_DEPOSIT_SUM_TO_NET_PAY_MATCH: Multiple transactions that
            sum up to the net pay and match direct deposits on the pay
            statement
        SPLIT_LESS_THAN_NET_PAY_SUM_TO_NET_PAY_MATCH: Multiple transactions
            were found that do not quite sum up to the net pay amount
        PARTIAL: An inconclusive pay statement match was found
        TRANSACTION_DATE_RANGE_INVALID: No possible transactions to match to
            for pay date. This may be resolved by refreshing the report.
        NO_MATCH: None of the transactions match the pay statement

    """

    NET_PAY_MATCH = 'NET_PAY_MATCH'

    SPLIT_INTERVIEW_AMOUNT_SUM_TO_NET_PAY_MATCH = 'SPLIT_INTERVIEW_AMOUNT_SUM_TO_NET_PAY_MATCH'

    SPLIT_DIRECT_DEPOSIT_SUM_TO_NET_PAY_MATCH = 'SPLIT_DIRECT_DEPOSIT_SUM_TO_NET_PAY_MATCH'

    SPLIT_LESS_THAN_NET_PAY_SUM_TO_NET_PAY_MATCH = 'SPLIT_LESS_THAN_NET_PAY_SUM_TO_NET_PAY_MATCH'

    PARTIAL = 'PARTIAL'

    TRANSACTION_DATE_RANGE_INVALID = 'TRANSACTION_DATE_RANGE_INVALID'

    NO_MATCH = 'NO_MATCH'

