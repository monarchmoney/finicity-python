# -*- coding: utf-8 -*-


class AssetSummary(object):

    """Implementation of the 'Asset Summary' model.

    TODO: type model description here.

    Attributes:
        mtype (string): checking / savings / moneyMarket / cd / investment*
        current_balance (float): Current balance of the account
        two_month_average (float): Two month average daily balance of the
            account
        six_month_average (float): Six month average daily balance of the
            account
        beginning_balance (float): Beginning balance of account per the time
            period in the report

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "mtype":'type',
        "current_balance":'currentBalance',
        "two_month_average":'twoMonthAverage',
        "six_month_average":'sixMonthAverage',
        "beginning_balance":'beginningBalance'
    }

    def __init__(self,
                 mtype=None,
                 current_balance=None,
                 two_month_average=None,
                 six_month_average=None,
                 beginning_balance=None,
                 additional_properties = {}):
        """Constructor for the AssetSummary class"""

        # Initialize members of the class
        self.mtype = mtype
        self.current_balance = current_balance
        self.two_month_average = two_month_average
        self.six_month_average = six_month_average
        self.beginning_balance = beginning_balance

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
        mtype = dictionary.get('type')
        current_balance = dictionary.get('currentBalance')
        two_month_average = dictionary.get('twoMonthAverage')
        six_month_average = dictionary.get('sixMonthAverage')
        beginning_balance = dictionary.get('beginningBalance')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(mtype,
                   current_balance,
                   two_month_average,
                   six_month_average,
                   beginning_balance,
                   dictionary)


