# -*- coding: utf-8 -*-


class BankAccountStatementV2Response(object):

    """Implementation of the 'BankAccountStatement_V2Response' model.

    TODO: type model description here.

    Attributes:
        id (string): TODO: type description here.
        as_of_date (int): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id":'id',
        "as_of_date":'asOfDate'
    }

    def __init__(self,
                 id=None,
                 as_of_date=None,
                 additional_properties = {}):
        """Constructor for the BankAccountStatementV2Response class"""

        # Initialize members of the class
        self.id = id
        self.as_of_date = as_of_date

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
        as_of_date = dictionary.get('asOfDate')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(id,
                   as_of_date,
                   dictionary)


