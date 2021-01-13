# -*- coding: utf-8 -*-


class ErrorMessage(object):

    """Implementation of the 'ErrorMessage' model.

    TODO: type model description here.

    Attributes:
        code (int): Error code
        message (string): Error message
        asset_id (string): Finicity's asset ID

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "code":'code',
        "message":'message',
        "asset_id":'assetId'
    }

    def __init__(self,
                 code=None,
                 message=None,
                 asset_id=None,
                 additional_properties = {}):
        """Constructor for the ErrorMessage class"""

        # Initialize members of the class
        self.code = code
        self.message = message
        self.asset_id = asset_id

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
        code = dictionary.get('code')
        message = dictionary.get('message')
        asset_id = dictionary.get('assetId')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(code,
                   message,
                   asset_id,
                   dictionary)


