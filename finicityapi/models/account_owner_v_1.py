# -*- coding: utf-8 -*-


class AccountOwnerV1(object):

    """Implementation of the 'Account Owner v1' model.

    The account owner information for the customer account

    Attributes:
        owner_name (string): The name of the account owner. In v1 this can be
            multiple account owners in one string. This is how the source data
            is returned from the institution.
        owner_address (string): The address of the account owner

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "owner_name":'ownerName',
        "owner_address":'ownerAddress'
    }

    def __init__(self,
                 owner_name=None,
                 owner_address=None,
                 additional_properties = {}):
        """Constructor for the AccountOwnerV1 class"""

        # Initialize members of the class
        self.owner_name = owner_name
        self.owner_address = owner_address

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
        owner_name = dictionary.get('ownerName')
        owner_address = dictionary.get('ownerAddress')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(owner_name,
                   owner_address,
                   dictionary)


