# -*- coding: utf-8 -*-


class StorePayStatementResponse(object):

    """Implementation of the 'Store Pay Statement Response' model.

    TODO: type model description here.

    Attributes:
        asset_id (string): The asset ID of the stored pay statement

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "asset_id":'assetId'
    }

    def __init__(self,
                 asset_id=None,
                 additional_properties = {}):
        """Constructor for the StorePayStatementResponse class"""

        # Initialize members of the class
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
        asset_id = dictionary.get('assetId')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(asset_id,
                   dictionary)


