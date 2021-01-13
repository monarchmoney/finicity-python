# -*- coding: utf-8 -*-

import finicityapi.models.asset_summary
import finicityapi.models.account_detail

class PrequalificationReportAccount(object):

    """Implementation of the 'Prequalification Report Account' model.

    TODO: type model description here.

    Attributes:
        id (long|int): The generated FInicity ID of the account
        number (string): The account number from the institution (last four
            digits are shown)
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
        asset (AssetSummary): An asset record for the account
        details (AccountDetail): A details record for the account
        tot_number_days_since_most_recent_insufficient_funds_fee_debit_tx_accou
            nt (long|int): The total number of days since the most recent
            insufficient funds fee for the account
        tot_number_insufficient_funds_fee_debit_tx_over_6_months_account
            (long|int): The total number of  insufficient funds fees for the
            account over six months

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
        "asset":'asset',
        "details":'details',
        "tot_number_days_since_most_recent_insufficient_funds_fee_debit_tx_account":'totNumberDaysSinceMostRecentInsufficientFundsFeeDebitTxAccount',
        "tot_number_insufficient_funds_fee_debit_tx_over_6_months_account":'totNumberInsufficientFundsFeeDebitTxOver6MonthsAccount'
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
                 asset=None,
                 details=None,
                 tot_number_days_since_most_recent_insufficient_funds_fee_debit_tx_account=None,
                 tot_number_insufficient_funds_fee_debit_tx_over_6_months_account=None,
                 additional_properties = {}):
        """Constructor for the PrequalificationReportAccount class"""

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
        self.asset = asset
        self.details = details
        self.tot_number_days_since_most_recent_insufficient_funds_fee_debit_tx_account = tot_number_days_since_most_recent_insufficient_funds_fee_debit_tx_account
        self.tot_number_insufficient_funds_fee_debit_tx_over_6_months_account = tot_number_insufficient_funds_fee_debit_tx_over_6_months_account

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
        asset = finicityapi.models.asset_summary.AssetSummary.from_dictionary(dictionary.get('asset')) if dictionary.get('asset') else None
        details = finicityapi.models.account_detail.AccountDetail.from_dictionary(dictionary.get('details')) if dictionary.get('details') else None
        tot_number_days_since_most_recent_insufficient_funds_fee_debit_tx_account = dictionary.get('totNumberDaysSinceMostRecentInsufficientFundsFeeDebitTxAccount')
        tot_number_insufficient_funds_fee_debit_tx_over_6_months_account = dictionary.get('totNumberInsufficientFundsFeeDebitTxOver6MonthsAccount')

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
                   asset,
                   details,
                   tot_number_days_since_most_recent_insufficient_funds_fee_debit_tx_account,
                   tot_number_insufficient_funds_fee_debit_tx_over_6_months_account,
                   dictionary)


