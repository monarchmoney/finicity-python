# -*- coding: utf-8 -*-


class ConnectOauthOptions(object):

    """Implementation of the 'ConnectOAuthOptions' model.

    oauthOptions for oauthEnabled institutions

    Attributes:
        enabled (bool): Indicates if OAuth institutions should be enabled for
            the session
        auto_replace (bool): If set to true, Connect will replace OAuth
            institutions based on the customer's existing accounts. e.g if the
            customer has a legacy Chase account, legacy Chase will be used
            throughout the session but if the user doesn't have a Capital One
            legacy account, OAuth Capital One will be used for the session.
        institutions (object): Provides the ability to control what
            institutions should or shouldn't be displayed to the user

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "enabled":'enabled',
        "auto_replace":'autoReplace',
        "institutions":'institutions'
    }

    def __init__(self,
                 enabled=None,
                 auto_replace=None,
                 institutions=None,
                 additional_properties = {}):
        """Constructor for the ConnectOauthOptions class"""

        # Initialize members of the class
        self.enabled = enabled
        self.auto_replace = auto_replace
        self.institutions = institutions

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
        enabled = dictionary.get('enabled')
        auto_replace = dictionary.get('autoReplace')
        institutions = dictionary.get('institutions')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(enabled,
                   auto_replace,
                   institutions,
                   dictionary)


