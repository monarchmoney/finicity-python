# -*- coding: utf-8 -*-


class InterviewAccounts(object):

    """Implementation of the 'Interview Accounts' model.

    TODO: type model description here.

    Attributes:
        id (long|int): The accountId of the selected account during the
            Account Interview process.
        amount (float): The customer entered value of the amount deposited
            into the account during the Account Interview process. This is an
            optional field.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id":'id',
        "amount":'amount'
    }

    def __init__(self,
                 id=None,
                 amount=None,
                 additional_properties = {}):
        """Constructor for the InterviewAccounts class"""

        # Initialize members of the class
        self.id = id
        self.amount = amount

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
        amount = dictionary.get('amount')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(id,
                   amount,
                   dictionary)


