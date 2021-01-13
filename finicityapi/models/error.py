# -*- coding: utf-8 -*-


class Error(object):

    """Implementation of the 'error' model.

    TODO: type model description here.

    Attributes:
        error_code (string): TODO: type description here.
        error_message (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "error_code":'errorCode',
        "error_message":'errorMessage'
    }

    def __init__(self,
                 error_code=None,
                 error_message=None,
                 additional_properties = {}):
        """Constructor for the Error class"""

        # Initialize members of the class
        self.error_code = error_code
        self.error_message = error_message

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
        error_code = dictionary.get('errorCode')
        error_message = dictionary.get('errorMessage')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(error_code,
                   error_message,
                   dictionary)


