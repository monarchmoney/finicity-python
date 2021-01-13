# -*- coding: utf-8 -*-


class InstitutionsCertificationSubscriptionRequest(object):

    """Implementation of the 'Institutions Certification Subscription Request' model.

    TODO: type model description here.

    Attributes:
        webhook_url (string): Webhook URL to send the notifications to

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "webhook_url":'webhookUrl'
    }

    def __init__(self,
                 webhook_url=None,
                 additional_properties = {}):
        """Constructor for the InstitutionsCertificationSubscriptionRequest class"""

        # Initialize members of the class
        self.webhook_url = webhook_url

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
        webhook_url = dictionary.get('webhookUrl')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(webhook_url,
                   dictionary)


