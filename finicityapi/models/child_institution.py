# -*- coding: utf-8 -*-


class ChildInstitution(object):

    """Implementation of the 'Child Institution' model.

    TODO: type model description here.

    Attributes:
        rssd (int): The RSSD ID is a unique identifier assigned to financial
            institutions by the Federal Reserve. While the length of the RSSD
            ID varies by institution, it cannot exceed 10 numerical digits
        parent_rssd (int): The RSSD ID is a unique identifier assigned to
            financial institutions by the Federal Reserve. While the length of
            the RSSD ID varies by institution, it cannot exceed 10 numerical
            digits
        name (string): The name of the institution
        institution_id (int): Finicity’s institution ID

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "rssd":'rssd',
        "parent_rssd":'parentRSSD',
        "name":'name',
        "institution_id":'institutionId'
    }

    def __init__(self,
                 rssd=None,
                 parent_rssd=None,
                 name=None,
                 institution_id=None,
                 additional_properties = {}):
        """Constructor for the ChildInstitution class"""

        # Initialize members of the class
        self.rssd = rssd
        self.parent_rssd = parent_rssd
        self.name = name
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
        rssd = dictionary.get('rssd')
        parent_rssd = dictionary.get('parentRSSD')
        name = dictionary.get('name')
        institution_id = dictionary.get('institutionId')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(rssd,
                   parent_rssd,
                   name,
                   institution_id,
                   dictionary)


