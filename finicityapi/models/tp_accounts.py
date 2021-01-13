# -*- coding: utf-8 -*-

import finicityapi.models.account

class TpAccounts(object):

    """Implementation of the 'TpAccounts' model.

    TODO: type model description here.

    Attributes:
        accounts (list of Account): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "accounts":'accounts'
    }

    def __init__(self,
                 accounts=None,
                 additional_properties = {}):
        """Constructor for the TpAccounts class"""

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
                accounts.append(finicityapi.models.account.Account.from_dictionary(structure))

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(accounts,
                   dictionary)


