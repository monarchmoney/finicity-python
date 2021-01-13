# -*- coding: utf-8 -*-


class PayrollEarningsRecord(object):

    """Implementation of the 'Payroll Earnings Record' model.

    TODO: type model description here.

    Attributes:
        name (string): **Earning names**: <br> * `basePayAmount` <br> *
            `overtimePayAmount` * `bonusPayAmount` <br> * `otherPayAmount`:
            pay not categorized, such as commission, car allowances, and
            more.
        mtype (string): Names: `base`, `overtime`, `bonus`, `other`
        rate (float): This field is only populated if `type` is `base`. It’s
            the regular pay rate from the payroll provider.
        amount (float): Earnings amount for each earning type
        amount_ytd (float): The year-to-date total amount for each earning
            type. <br>  <br>**Note**: This field is only included in pay
            histories from the last pay period of the year where
            `lastPayPeriodIndicator` = true.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "name":'name',
        "mtype":'type',
        "rate":'rate',
        "amount":'amount',
        "amount_ytd":'amountYTD'
    }

    def __init__(self,
                 name=None,
                 mtype=None,
                 rate=None,
                 amount=None,
                 amount_ytd=None,
                 additional_properties = {}):
        """Constructor for the PayrollEarningsRecord class"""

        # Initialize members of the class
        self.name = name
        self.mtype = mtype
        self.rate = rate
        self.amount = amount
        self.amount_ytd = amount_ytd

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
        name = dictionary.get('name')
        mtype = dictionary.get('type')
        rate = dictionary.get('rate')
        amount = dictionary.get('amount')
        amount_ytd = dictionary.get('amountYTD')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(name,
                   mtype,
                   rate,
                   amount,
                   amount_ytd,
                   dictionary)


