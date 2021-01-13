# -*- coding: utf-8 -*-


class SubscriptionRecord(object):

    """Implementation of the 'Subscription Record' model.

    TxPush subscription details

    Attributes:
        id (long|int): Unique subscription identifier
        account_id (long|int): The Finicity account Id for the subscription
        mtype (string): Event subscription type. account or transaction
        callback_url (string): The url for the events
        signing_key (string): Signing key for events

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id":'id',
        "account_id":'accountId',
        "mtype":'type',
        "callback_url":'callbackUrl',
        "signing_key":'signingKey'
    }

    def __init__(self,
                 id=None,
                 account_id=None,
                 mtype=None,
                 callback_url=None,
                 signing_key=None,
                 additional_properties = {}):
        """Constructor for the SubscriptionRecord class"""

        # Initialize members of the class
        self.id = id
        self.account_id = account_id
        self.mtype = mtype
        self.callback_url = callback_url
        self.signing_key = signing_key

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
        account_id = dictionary.get('accountId')
        mtype = dictionary.get('type')
        callback_url = dictionary.get('callbackUrl')
        signing_key = dictionary.get('signingKey')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(id,
                   account_id,
                   mtype,
                   callback_url,
                   signing_key,
                   dictionary)


