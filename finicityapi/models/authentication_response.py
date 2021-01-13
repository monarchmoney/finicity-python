# -*- coding: utf-8 -*-


class AuthenticationResponse(object):

    """Implementation of the 'AuthenticationResponse' model.

    TODO: type model description here.

    Attributes:
        token (string): A Temporary Access Token Which Must Be Passed In The
            HTTP Header "Finicity-App-Token" On All Subsequent API Requests.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "token":'token'
    }

    def __init__(self,
                 token=None,
                 additional_properties = {}):
        """Constructor for the AuthenticationResponse class"""

        # Initialize members of the class
        self.token = token

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
        token = dictionary.get('token')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(token,
                   dictionary)


