# -*- coding: utf-8 -*-


class Categorization(object):

    """Implementation of the 'Categorization' model.

    Categorization Record

    Attributes:
        normalized_payee_name (string): A normalized payee, derived from the
            transaction’s description and memo fields.
        category (string): One of the values from Categories (assigned based
            on the payee name)
        best_representation (string): Combines the description and memo data
            together, removes any duplicated information from description to
            memo, and removes any numbers or special characters
        city (string): City of transaction (if available)
        state (string): State of transaction (if available)
        postal_code (string): TODO: type description here.
        country (string): Country where the transaction occurred

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "normalized_payee_name":'normalizedPayeeName',
        "category":'category',
        "best_representation":'bestRepresentation',
        "country":'country',
        "city":'city',
        "state":'state',
        "postal_code":'postalCode'
    }

    def __init__(self,
                 normalized_payee_name=None,
                 category=None,
                 best_representation=None,
                 country=None,
                 city=None,
                 state=None,
                 postal_code=None,
                 additional_properties = {}):
        """Constructor for the Categorization class"""

        # Initialize members of the class
        self.normalized_payee_name = normalized_payee_name
        self.category = category
        self.best_representation = best_representation
        self.city = city
        self.state = state
        self.postal_code = postal_code
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
        city = dictionary.get('city')
        state = dictionary.get('state')
        postal_code = dictionary.get('postalCode')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(normalized_payee_name,
                   category,
                   best_representation,
                   country,
                   city,
                   state,
                   postal_code,
                   dictionary)


