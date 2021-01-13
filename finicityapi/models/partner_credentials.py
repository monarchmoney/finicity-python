# -*- coding: utf-8 -*-


class PartnerCredentials(object):

    """Implementation of the 'Partner Credentials' model.

    TODO: type model description here.

    Attributes:
        partner_id (string): Partner ID From Developer Portal
        partner_secret (string): Partner Secret From Developer Portal

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "partner_id":'partnerId',
        "partner_secret":'partnerSecret'
    }

    def __init__(self,
                 partner_id=None,
                 partner_secret=None,
                 additional_properties = {}):
        """Constructor for the PartnerCredentials class"""

        # Initialize members of the class
        self.partner_id = partner_id
        self.partner_secret = partner_secret

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
        partner_id = dictionary.get('partnerId')
        partner_secret = dictionary.get('partnerSecret')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(partner_id,
                   partner_secret,
                   dictionary)


