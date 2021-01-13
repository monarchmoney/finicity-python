# -*- coding: utf-8 -*-

import finicityapi.models.voa_with_income_report_account

class VOAWithIncomeReportInstitution(object):

    """Implementation of the 'VOA with Income Report Institution' model.

    TODO: type model description here.

    Attributes:
        id (long|int): The institution ID
        name (string): The name of the institution
        url_home_app (string): The URL of the institution’s primary home page
        accounts (list of VOAWithIncomeReportAccount): An array of accounts

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id":'id',
        "name":'name',
        "url_home_app":'urlHomeApp',
        "accounts":'accounts'
    }

    def __init__(self,
                 id=None,
                 name=None,
                 url_home_app=None,
                 accounts=None,
                 additional_properties = {}):
        """Constructor for the VOAWithIncomeReportInstitution class"""

        # Initialize members of the class
        self.id = id
        self.name = name
        self.url_home_app = url_home_app
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
        id = dictionary.get('id')
        name = dictionary.get('name')
        url_home_app = dictionary.get('urlHomeApp')
        accounts = None
        if dictionary.get('accounts') != None:
            accounts = list()
            for structure in dictionary.get('accounts'):
                accounts.append(finicityapi.models.voa_with_income_report_account.VOAWithIncomeReportAccount.from_dictionary(structure))

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(id,
                   name,
                   url_home_app,
                   accounts,
                   dictionary)


