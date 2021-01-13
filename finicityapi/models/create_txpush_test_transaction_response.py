# -*- coding: utf-8 -*-


class CreateTxpushTestTransactionResponse(object):

    """Implementation of the 'Create TxPush Test Transaction Response' model.

    Response for TxPush test transaction

    Attributes:
        id (long|int): The ID of the new transaction record
        created_date (long|int): A timestamp of when the transaction was added
            (see Handling Dates and Times)

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id":'id',
        "created_date":'createdDate'
    }

    def __init__(self,
                 id=None,
                 created_date=None,
                 additional_properties = {}):
        """Constructor for the CreateTxpushTestTransactionResponse class"""

        # Initialize members of the class
        self.id = id
        self.created_date = created_date

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
        created_date = dictionary.get('createdDate')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(id,
                   created_date,
                   dictionary)


