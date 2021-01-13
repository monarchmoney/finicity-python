# -*- coding: utf-8 -*-


class AppRegistrationResponse(object):

    """Implementation of the 'App Registration Response' model.

    TODO: type model description here.

    Attributes:
        pre_app_id (long|int): An identifier to track the application
            registration request
        status (string): The status of the app registration request. When
            submitted starts as P for pending.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "pre_app_id":'preAppId',
        "status":'status'
    }

    def __init__(self,
                 pre_app_id=None,
                 status=None,
                 additional_properties = {}):
        """Constructor for the AppRegistrationResponse class"""

        # Initialize members of the class
        self.pre_app_id = pre_app_id
        self.status = status

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
        pre_app_id = dictionary.get('preAppId')
        status = dictionary.get('status')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(pre_app_id,
                   status,
                   dictionary)


