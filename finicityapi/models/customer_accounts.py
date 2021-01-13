# -*- coding: utf-8 -*-

import finicityapi.models.customer_account

class CustomerAccounts(object):

    """Implementation of the 'Customer Accounts' model.

    The response to calls to refresh accounts or get customer accounts is a
    list of account in the "accounts" array. A customer account represents a
    bank account such as a checking or savings that the customer has added via
    the Connect interface

    Attributes:
        accounts (list of CustomerAccount): List of customer accounts

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "accounts":'accounts'
    }

    def __init__(self,
                 accounts=None,
                 additional_properties = {}):
        """Constructor for the CustomerAccounts class"""

        # Initialize members of the class
        self.accounts = accounts

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
        accounts = None
        if dictionary.get('accounts') != None:
            accounts = list()
            for structure in dictionary.get('accounts'):
                accounts.append(finicityapi.models.customer_account.CustomerAccount.from_dictionary(structure))

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(accounts,
                   dictionary)

