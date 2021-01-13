# -*- coding: utf-8 -*-


class InstitutionOptionsTest(object):

    """Implementation of the 'Institution Options Test' model.

    TODO: type model description here.

    Attributes:
        institution_id (TypeEnum): The institutionId

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "institution_id":'institutionId'
    }

    def __init__(self,
                 institution_id=None,
                 additional_properties = {}):
        """Constructor for the InstitutionOptionsTest class"""

        # Initialize members of the class
        self.institution_id = institution_id

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
        institution_id = dictionary.get('institutionId')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(institution_id,
                   dictionary)


