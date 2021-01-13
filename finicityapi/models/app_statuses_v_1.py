# -*- coding: utf-8 -*-

import finicityapi.models.app_status_v_1

class AppStatusesV1(object):

    """Implementation of the 'App Statuses V1' model.

    The response for the Get App Registration Status endpoint which returns an
    array of App Status objects to be able to determine their registration
    status

    Attributes:
        status (list of AppStatusV1): List of App Status's

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "status":'status'
    }

    def __init__(self,
                 status=None,
                 additional_properties = {}):
        """Constructor for the AppStatusesV1 class"""

        # Initialize members of the class
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
        status = None
        if dictionary.get('status') != None:
            status = list()
            for structure in dictionary.get('status'):
                status.append(finicityapi.models.app_status_v_1.AppStatusV1.from_dictionary(structure))

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(status,
                   dictionary)


