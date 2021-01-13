# -*- coding: utf-8 -*-

import finicityapi.models.connect_email_options

class GenerateConnectEmailResponse(object):

    """Implementation of the 'Generate Connect Email Response' model.

    Response from create url call

    Attributes:
        link (string): The generated Connect URL
        email_config (ConnectEmailOptions): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "link":'link',
        "email_config":'emailConfig'
    }

    def __init__(self,
                 link=None,
                 email_config=None,
                 additional_properties = {}):
        """Constructor for the GenerateConnectEmailResponse class"""

        # Initialize members of the class
        self.link = link
        self.email_config = email_config

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
        link = dictionary.get('link')
        email_config = finicityapi.models.connect_email_options.ConnectEmailOptions.from_dictionary(dictionary.get('emailConfig')) if dictionary.get('emailConfig') else None

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(link,
                   email_config,
                   dictionary)


