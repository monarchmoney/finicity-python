# -*- coding: utf-8 -*-


class ModifyCustomerRequest(object):

    """Implementation of the 'Modify Customer Request' model.

    The fields to be modified for a customer record

    Attributes:
        first_name (string): The first name associated with the customer
        last_name (string): The last name associated with the customer

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "first_name":'firstName',
        "last_name":'lastName'
    }

    def __init__(self,
                 first_name=None,
                 last_name=None,
                 additional_properties = {}):
        """Constructor for the ModifyCustomerRequest class"""

        # Initialize members of the class
        self.first_name = first_name
        self.last_name = last_name

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
        first_name = dictionary.get('firstName')
        last_name = dictionary.get('lastName')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(first_name,
                   last_name,
                   dictionary)


