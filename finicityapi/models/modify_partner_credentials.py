# -*- coding: utf-8 -*-


class ModifyPartnerCredentials(object):

    """Implementation of the 'ModifyPartnerCredentials' model.

    TODO: type model description here.

    Attributes:
        partner_id (string): Partner ID from Developer Portal
        partner_secret (string): Partner Secret from Developer Portal
        new_partner_secret (string): The Value For The New Partner Secret To
            Be Change To

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "partner_id":'partnerId',
        "partner_secret":'partnerSecret',
        "new_partner_secret":'newPartnerSecret'
    }

    def __init__(self,
                 partner_id=None,
                 partner_secret=None,
                 new_partner_secret=None,
                 additional_properties = {}):
        """Constructor for the ModifyPartnerCredentials class"""

        # Initialize members of the class
        self.partner_id = partner_id
        self.partner_secret = partner_secret
        self.new_partner_secret = new_partner_secret

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
        new_partner_secret = dictionary.get('newPartnerSecret')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(partner_id,
                   partner_secret,
                   new_partner_secret,
                   dictionary)


