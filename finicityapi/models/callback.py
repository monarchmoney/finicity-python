# -*- coding: utf-8 -*-


class Callback(object):

    """Implementation of the 'Callback' model.

    TODO: type model description here.

    Attributes:
        callback_url (string): The callback url for the events
        content_type (string): The content type for the body of the events

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "callback_url":'callbackUrl',
        "content_type":'contentType'
    }

    def __init__(self,
                 callback_url=None,
                 content_type=None,
                 additional_properties = {}):
        """Constructor for the Callback class"""

        # Initialize members of the class
        self.callback_url = callback_url
        self.content_type = content_type

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
        content_type = dictionary.get('contentType')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(callback_url,
                   content_type,
                   dictionary)


