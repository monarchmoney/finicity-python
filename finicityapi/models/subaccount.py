# -*- coding: utf-8 -*-


class Subaccount(object):

    """Implementation of the 'Subaccount' model.

    TODO: type model description here.

    Attributes:
        subaccount_number (string): TODO: type description here.
        subaccount_name (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "subaccount_number":'subaccountNumber',
        "subaccount_name":'subaccountName'
    }

    def __init__(self,
                 subaccount_number=None,
                 subaccount_name=None,
                 additional_properties = {}):
        """Constructor for the Subaccount class"""

        # Initialize members of the class
        self.subaccount_number = subaccount_number
        self.subaccount_name = subaccount_name

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
        subaccount_number = dictionary.get('subaccountNumber')
        subaccount_name = dictionary.get('subaccountName')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(subaccount_number,
                   subaccount_name,
                   dictionary)


