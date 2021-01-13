# -*- coding: utf-8 -*-


class DirectDeposit(object):

    """Implementation of the 'Direct Deposit' model.

    TODO: type model description here.

    Attributes:
        financial_institution_name (string): The name of the financial
            institution that the deposit was made to.
        account_type (string): The type of account the deposit was made to.
        amount_current (float): The amount of the deposit.
        account_last_four (string): The last four numbers of the account the
            deposit went into.
        description (string): The description associated with the direct
            deposit.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "financial_institution_name":'financialInstitutionName',
        "account_type":'accountType',
        "amount_current":'amountCurrent',
        "account_last_four":'accountLastFour',
        "description":'description'
    }

    def __init__(self,
                 financial_institution_name=None,
                 account_type=None,
                 amount_current=None,
                 account_last_four=None,
                 description=None,
                 additional_properties = {}):
        """Constructor for the DirectDeposit class"""

        # Initialize members of the class
        self.financial_institution_name = financial_institution_name
        self.account_type = account_type
        self.amount_current = amount_current
        self.account_last_four = account_last_four
        self.description = description

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
        financial_institution_name = dictionary.get('financialInstitutionName')
        account_type = dictionary.get('accountType')
        amount_current = dictionary.get('amountCurrent')
        account_last_four = dictionary.get('accountLastFour')
        description = dictionary.get('description')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(financial_institution_name,
                   account_type,
                   amount_current,
                   account_last_four,
                   description,
                   dictionary)


