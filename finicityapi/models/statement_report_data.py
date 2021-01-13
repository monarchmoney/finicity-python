# -*- coding: utf-8 -*-


class StatementReportData(object):

    """Implementation of the 'Statement Report Data' model.

    TODO: type model description here.

    Attributes:
        account_id (long|int): Specify the account to retrieve the statement
            for and display in the report.
        index (long|int): Index of statement to retrieve (default is 1,
            maximum is 6)

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "account_id":'accountId',
        "index":'index'
    }

    def __init__(self,
                 account_id=None,
                 index=None,
                 additional_properties = {}):
        """Constructor for the StatementReportData class"""

        # Initialize members of the class
        self.account_id = account_id
        self.index = index

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
        account_id = dictionary.get('accountId')
        index = dictionary.get('index')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(account_id,
                   index,
                   dictionary)


