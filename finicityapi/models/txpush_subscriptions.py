# -*- coding: utf-8 -*-

import finicityapi.models.subscription_record

class TxpushSubscriptions(object):

    """Implementation of the 'TxPush Subscriptions' model.

    TODO: type model description here.

    Attributes:
        subscriptions (list of SubscriptionRecord): TODO: type description
            here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "subscriptions":'subscriptions'
    }

    def __init__(self,
                 subscriptions=None,
                 additional_properties = {}):
        """Constructor for the TxpushSubscriptions class"""

        # Initialize members of the class
        self.subscriptions = subscriptions

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
        subscriptions = None
        if dictionary.get('subscriptions') != None:
            subscriptions = list()
            for structure in dictionary.get('subscriptions'):
                subscriptions.append(finicityapi.models.subscription_record.SubscriptionRecord.from_dictionary(structure))

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(subscriptions,
                   dictionary)


