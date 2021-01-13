# -*- coding: utf-8 -*-

import finicityapi.models.branding

class InstitutionBrandingResponse(object):

    """Implementation of the 'Institution Branding Response' model.

    TODO: type model description here.

    Attributes:
        branding (Branding): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "branding":'branding'
    }

    def __init__(self,
                 branding=None,
                 additional_properties = {}):
        """Constructor for the InstitutionBrandingResponse class"""

        # Initialize members of the class
        self.branding = branding

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
        branding = finicityapi.models.branding.Branding.from_dictionary(dictionary.get('branding')) if dictionary.get('branding') else None

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(branding,
                   dictionary)


