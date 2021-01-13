# -*- coding: utf-8 -*-

import finicityapi.models.child_institution

class CertifiedInstitution(object):

    """Implementation of the 'Certified Institution' model.

    TODO: type model description here.

    Attributes:
        name (string): Institution's name
        id (long|int): Institution's Id
        voa (bool): VOA Certification
        voi (bool): VOI Certification
        state_agg (bool): State Agg Certification
        ach (bool): ACH Certification
        trans_agg (bool): Trans Agg Certification
        aha (bool): AHA Certification
        child_institutions (list of ChildInstitution): TODO: type description
            here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "name":'name',
        "id":'id',
        "voa":'voa',
        "voi":'voi',
        "state_agg":'stateAgg',
        "ach":'ach',
        "trans_agg":'transAgg',
        "aha":'aha',
        "child_institutions":'childInstitutions'
    }

    def __init__(self,
                 name=None,
                 id=None,
                 voa=None,
                 voi=None,
                 state_agg=None,
                 ach=None,
                 trans_agg=None,
                 aha=None,
                 child_institutions=None,
                 additional_properties = {}):
        """Constructor for the CertifiedInstitution class"""

        # Initialize members of the class
        self.name = name
        self.id = id
        self.voa = voa
        self.voi = voi
        self.state_agg = state_agg
        self.ach = ach
        self.trans_agg = trans_agg
        self.aha = aha
        self.child_institutions = child_institutions

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
        name = dictionary.get('name')
        id = dictionary.get('id')
        voa = dictionary.get('voa')
        voi = dictionary.get('voi')
        state_agg = dictionary.get('stateAgg')
        ach = dictionary.get('ach')
        trans_agg = dictionary.get('transAgg')
        aha = dictionary.get('aha')
        child_institutions = None
        if dictionary.get('childInstitutions') != None:
            child_institutions = list()
            for structure in dictionary.get('childInstitutions'):
                child_institutions.append(finicityapi.models.child_institution.ChildInstitution.from_dictionary(structure))

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(name,
                   id,
                   voa,
                   voi,
                   state_agg,
                   ach,
                   trans_agg,
                   aha,
                   child_institutions,
                   dictionary)


