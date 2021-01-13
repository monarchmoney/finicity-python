# -*- coding: utf-8 -*-

import finicityapi.models.transactions_report_transaction

class TransactionsReportAccount(object):

    """Implementation of the 'Transactions Report Account' model.

    The fields used for the Transaction History Report (CRA products).

    Attributes:
        id (long|int): The Finicity account ID.
        name (string): The account name from the financial institution.
        number (string): The account number from the financial institution
            (obfuscated).
        mtype (AccountTypeEnum): All Types: checking, savings, loan, mortgage,
            credit card, CD, MM, investment, and more.
        aggregation_status_code (int): The status of the most recent
            aggregation attempt for this account. Note: non-zero means the
            account was not accessed successfully for this report, and
            additional fields for this account may not be reliable.
        balance (float): The cleared balance of the account as-of
            balanceDate.
        balance_date (long|int): A timestamp showing when the balance was
            captured.
        transactions (list of TransactionsReportTransaction): A list of
            transactions associated with the account.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id":'id',
        "name":'name',
        "number":'number',
        "mtype":'type',
        "aggregation_status_code":'aggregationStatusCode',
        "balance":'balance',
        "balance_date":'balanceDate',
        "transactions":'transactions'
    }

    def __init__(self,
                 id=None,
                 name=None,
                 number=None,
                 mtype=None,
                 aggregation_status_code=None,
                 balance=None,
                 balance_date=None,
                 transactions=None,
                 additional_properties = {}):
        """Constructor for the TransactionsReportAccount class"""

        # Initialize members of the class
        self.id = id
        self.name = name
        self.number = number
        self.mtype = mtype
        self.aggregation_status_code = aggregation_status_code
        self.balance = balance
        self.balance_date = balance_date
        self.transactions = transactions

        # Add additional model properties to the instance
        self.additional_properties = additional_properties


    @classmethod
    def from_dictionary(cls,
                        dictionary):
        """Creates an instance of this model from a dictionary

        Args:
            dictionary (dictionary): A dictionary representation of the object as
            obtained from the deserialization of the server's response. The keys
            MUST match property names in the API description.

        Returns:
            object: An instance of this structure class.

        """
        if dictionary is None:
            return None

        # Extract variables from the dictionary
        id = dictionary.get('id')
        name = dictionary.get('name')
        number = dictionary.get('number')
        mtype = dictionary.get('type')
        aggregation_status_code = dictionary.get('aggregationStatusCode')
        balance = dictionary.get('balance')
        balance_date = dictionary.get('balanceDate')
        transactions = None
        if dictionary.get('transactions') != None:
            transactions = list()
            for structure in dictionary.get('transactions'):
                transactions.append(finicityapi.models.transactions_report_transaction.TransactionsReportTransaction.from_dictionary(structure))

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(id,
                   name,
                   number,
                   mtype,
                   aggregation_status_code,
                   balance,
                   balance_date,
                   transactions,
                   dictionary)


