# -*- coding: utf-8 -*-


class TxpushSubscriptionRequest(object):

    """Implementation of the 'TxPush Subscription Request' model.

    TODO: type model description here.

    Attributes:
        callback_url (string): The TxPUSH Listener URL to receive TxPUSH
            notifications (must use https protocol for any real-world
            account)

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "callback_url":'callbackUrl'
    }

    def __init__(self,
                 callback_url=None,
                 additional_properties = {}):
        """Constructor for the TxpushSubscriptionRequest class"""

        # Initialize members of the class
        self.callback_url = callback_url

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
        callback_url = dictionary.get('callbackUrl')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(callback_url,
                   dictionary)


