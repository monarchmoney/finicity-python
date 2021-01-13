# -*- coding: utf-8 -*-


class Categorization1(object):

    """Implementation of the 'Categorization1' model.

    TODO: type model description here.

    Attributes:
        normalized_payee_name (string): TODO: type description here.
        category (string): TODO: type description here.
        best_representation (string): TODO: type description here.
        country (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "normalized_payee_name":'normalizedPayeeName',
        "category":'category',
        "best_representation":'bestRepresentation',
        "country":'country'
    }

    def __init__(self,
                 normalized_payee_name=None,
                 category=None,
                 best_representation=None,
                 country=None,
                 additional_properties = {}):
        """Constructor for the Categorization1 class"""

        # Initialize members of the class
        self.normalized_payee_name = normalized_payee_name
        self.category = category
        self.best_representation = best_representation
        self.country = country

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
        normalized_payee_name = dictionary.get('normalizedPayeeName')
        category = dictionary.get('category')
        best_representation = dictionary.get('bestRepresentation')
        country = dictionary.get('country')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(normalized_payee_name,
                   category,
                   best_representation,
                   country,
                   dictionary)


