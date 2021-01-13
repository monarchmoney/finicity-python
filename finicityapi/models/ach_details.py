# -*- coding: utf-8 -*-


class ACHDetails(object):

    """Implementation of the 'ACH Details' model.

    The routing and account number information to initiate ACH transfers

    Attributes:
        routing_number (string): The routing number of the financial
            institution for this specific customers account
        real_account_number (string): The account number for initiating ACH
            transfers for this account

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "routing_number":'routingNumber',
        "real_account_number":'realAccountNumber'
    }

    def __init__(self,
                 routing_number=None,
                 real_account_number=None,
                 additional_properties = {}):
        """Constructor for the ACHDetails class"""

        # Initialize members of the class
        self.routing_number = routing_number
        self.real_account_number = real_account_number

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
        routing_number = dictionary.get('routingNumber')
        real_account_number = dictionary.get('realAccountNumber')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(routing_number,
                   real_account_number,
                   dictionary)


