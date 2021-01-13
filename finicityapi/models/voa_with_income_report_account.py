# -*- coding: utf-8 -*-

import finicityapi.models.voa_with_income_report_transaction
import finicityapi.models.asset_summary
import finicityapi.models.account_detail

class VOAWithIncomeReportAccount(object):

    """Implementation of the 'VOA with Income Report Account' model.

    TODO: type model description here.

    Attributes:
        id (long|int): The generated FInicity ID of the account
        number (string): The account number from the institution (all digits
            except the last four are obfuscated)
        owner_name (string): The name(s) of the account owner(s). This field
            is optional. If no owner information is available, this field will
            not appear in the report.
        owner_address (string): The mailing address of the account owner(s).
            This field is optional. If no owner information is available, this
            field will not appear in the report.
        name (string): The account name from the institution
        mtype (string): One of the values from Account Types
        available_balance (float): The available balance for the account
        aggregation_status_code (int): The status of the most recent
            aggregation attempt (see Handling Aggregation Status Codes)
        balance (float): The cleared balance of the account as-of balanceDate
        balance_date (long|int): A timestamp showing when the balance was
            captured (see Handling Dates and Times)
        average_monthly_balance (float): The average monthly balance of this
            account
        transactions (list of VOAWithIncomeReportTransaction): An array of
            transactions belonging to the account.
        asset (AssetSummary): An asset record for the account
        details (AccountDetail): A details record for the account

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id":'id',
        "number":'number',
        "owner_name":'ownerName',
        "owner_address":'ownerAddress',
        "name":'name',
        "mtype":'type',
        "available_balance":'availableBalance',
        "aggregation_status_code":'aggregationStatusCode',
        "balance":'balance',
        "balance_date":'balanceDate',
        "average_monthly_balance":'averageMonthlyBalance',
        "transactions":'transactions',
        "asset":'asset',
        "details":'details'
    }

    def __init__(self,
                 id=None,
                 number=None,
                 owner_name=None,
                 owner_address=None,
                 name=None,
                 mtype=None,
                 available_balance=None,
                 aggregation_status_code=None,
                 balance=None,
                 balance_date=None,
                 average_monthly_balance=None,
                 transactions=None,
                 asset=None,
                 details=None,
                 additional_properties = {}):
        """Constructor for the VOAWithIncomeReportAccount class"""

        # Initialize members of the class
        self.id = id
        self.number = number
        self.owner_name = owner_name
        self.owner_address = owner_address
        self.name = name
        self.mtype = mtype
        self.available_balance = available_balance
        self.aggregation_status_code = aggregation_status_code
        self.balance = balance
        self.balance_date = balance_date
        self.average_monthly_balance = average_monthly_balance
        self.transactions = transactions
        self.asset = asset
        self.details = details

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
        number = dictionary.get('number')
        owner_name = dictionary.get('ownerName')
        owner_address = dictionary.get('ownerAddress')
        name = dictionary.get('name')
        mtype = dictionary.get('type')
        available_balance = dictionary.get('availableBalance')
        aggregation_status_code = dictionary.get('aggregationStatusCode')
        balance = dictionary.get('balance')
        balance_date = dictionary.get('balanceDate')
        average_monthly_balance = dictionary.get('averageMonthlyBalance')
        transactions = None
        if dictionary.get('transactions') != None:
            transactions = list()
            for structure in dictionary.get('transactions'):
                transactions.append(finicityapi.models.voa_with_income_report_transaction.VOAWithIncomeReportTransaction.from_dictionary(structure))
        asset = finicityapi.models.asset_summary.AssetSummary.from_dictionary(dictionary.get('asset')) if dictionary.get('asset') else None
        details = finicityapi.models.account_detail.AccountDetail.from_dictionary(dictionary.get('details')) if dictionary.get('details') else None

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(id,
                   number,
                   owner_name,
                   owner_address,
                   name,
                   mtype,
                   available_balance,
                   aggregation_status_code,
                   balance,
                   balance_date,
                   average_monthly_balance,
                   transactions,
                   asset,
                   details,
                   dictionary)


