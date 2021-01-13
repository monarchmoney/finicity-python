# -*- coding: utf-8 -*-

import finicityapi.models.certified_institution

class GetCertifiedInstitutionsResponse(object):

    """Implementation of the 'Get Certified Institutions Response' model.

    TODO: type model description here.

    Attributes:
        found (int): Total number of results found
        displaying (int): Displaying count
        more_available (bool): Indicates if there are more institutions to
            display that match the parameters
        created_date (int): Date the request was created
        institutions (list of CertifiedInstitution): Results

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "found":'found',
        "displaying":'displaying',
        "more_available":'moreAvailable',
        "created_date":'createdDate',
        "institutions":'institutions'
    }

    def __init__(self,
                 found=None,
                 displaying=None,
                 more_available=None,
                 created_date=None,
                 institutions=None,
                 additional_properties = {}):
        """Constructor for the GetCertifiedInstitutionsResponse class"""

        # Initialize members of the class
        self.found = found
        self.displaying = displaying
        self.more_available = more_available
        self.created_date = created_date
        self.institutions = institutions

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
        found = dictionary.get('found')
        displaying = dictionary.get('displaying')
        more_available = dictionary.get('moreAvailable')
        created_date = dictionary.get('createdDate')
        institutions = None
        if dictionary.get('institutions') != None:
            institutions = list()
            for structure in dictionary.get('institutions'):
                institutions.append(finicityapi.models.certified_institution.CertifiedInstitution.from_dictionary(structure))

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(found,
                   displaying,
                   more_available,
                   created_date,
                   institutions,
                   dictionary)


