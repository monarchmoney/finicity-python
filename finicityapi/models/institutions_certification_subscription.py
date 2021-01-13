# -*- coding: utf-8 -*-


class InstitutionsCertificationSubscription(object):

    """Implementation of the 'Institutions Certification Subscription' model.

    The institutions certification subscription details

    Attributes:
        partner_id (string): The Finicity Partner ID
        webhook_url (string): The url to which the webhook events will be
            sent
        created_at (string): The date the subscription was created
        updated_at (string): The date the subscription was last updated

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "partner_id":'partnerId',
        "webhook_url":'webhookUrl',
        "created_at":'createdAt',
        "updated_at":'updatedAt'
    }

    def __init__(self,
                 partner_id=None,
                 webhook_url=None,
                 created_at=None,
                 updated_at=None,
                 additional_properties = {}):
        """Constructor for the InstitutionsCertificationSubscription class"""

        # Initialize members of the class
        self.partner_id = partner_id
        self.webhook_url = webhook_url
        self.created_at = created_at
        self.updated_at = updated_at

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
        webhook_url = dictionary.get('webhookUrl')
        created_at = dictionary.get('createdAt')
        updated_at = dictionary.get('updatedAt')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(partner_id,
                   webhook_url,
                   created_at,
                   updated_at,
                   dictionary)


