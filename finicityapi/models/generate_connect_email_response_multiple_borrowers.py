# -*- coding: utf-8 -*-


class GenerateConnectEmailResponseMultipleBorrowers(object):

    """Implementation of the 'Generate Connect Email Response Multiple borrowers' model.

    TODO: type model description here.

    Attributes:
        links (list of string): The URL generated to send a Connect email
        email_config (object): The configuration used to generate the Connect
            email.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "links":'links',
        "email_config":'emailConfig'
    }

    def __init__(self,
                 links=None,
                 email_config=None,
                 additional_properties = {}):
        """Constructor for the GenerateConnectEmailResponseMultipleBorrowers class"""

        # Initialize members of the class
        self.links = links
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
        links = dictionary.get('links')
        email_config = dictionary.get('emailConfig')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(links,
                   email_config,
                   dictionary)


