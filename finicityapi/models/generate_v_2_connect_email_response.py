# -*- coding: utf-8 -*-

import finicityapi.models.connect_v_2_email_options

class GenerateV2ConnectEmailResponse(object):

    """Implementation of the 'Generate V2 Connect Email Response' model.

    The response from the send email endpoint.

    Attributes:
        link (string): The URL generated to send a Connect email
        email_config (ConnectV2EmailOptions): The configuration used to
            generate the Connect email.

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
        """Constructor for the GenerateV2ConnectEmailResponse class"""

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
        email_config = finicityapi.models.connect_v_2_email_options.ConnectV2EmailOptions.from_dictionary(dictionary.get('emailConfig')) if dictionary.get('emailConfig') else None

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(link,
                   email_config,
                   dictionary)


