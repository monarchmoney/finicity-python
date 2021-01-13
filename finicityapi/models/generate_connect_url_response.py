# -*- coding: utf-8 -*-


class GenerateConnectURLResponse(object):

    """Implementation of the 'Generate Connect URL Response' model.

    Response from create url call

    Attributes:
        link (string): The generated Connect URL

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "link":'link'
    }

    def __init__(self,
                 link=None,
                 additional_properties = {}):
        """Constructor for the GenerateConnectURLResponse class"""

        # Initialize members of the class
        self.link = link

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

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(link,
                   dictionary)


