# -*- coding: utf-8 -*-


class InstitutionAddress(object):

    """Implementation of the 'Institution Address' model.

    The address for the financial institution

    Attributes:
        city (string): The city of the institution’s headquarters
        state (string): Two-letter code for the state of the institution’s
            headquarters
        country (string): The country of the institution’s headquarters
        postal_code (string): The postal code of the institution’s
            headquarters
        address_line_1 (string): Address information for the institution’s
            headquarters
        address_line_2 (string): Address information for the institution’s
            headquarters

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "city":'city',
        "state":'state',
        "country":'country',
        "postal_code":'postalCode',
        "address_line_1":'addressLine1',
        "address_line_2":'addressLine2'
    }

    def __init__(self,
                 city=None,
                 state=None,
                 country=None,
                 postal_code=None,
                 address_line_1=None,
                 address_line_2=None,
                 additional_properties = {}):
        """Constructor for the InstitutionAddress class"""

        # Initialize members of the class
        self.city = city
        self.state = state
        self.country = country
        self.postal_code = postal_code
        self.address_line_1 = address_line_1
        self.address_line_2 = address_line_2

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
        city = dictionary.get('city')
        state = dictionary.get('state')
        country = dictionary.get('country')
        postal_code = dictionary.get('postalCode')
        address_line_1 = dictionary.get('addressLine1')
        address_line_2 = dictionary.get('addressLine2')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(city,
                   state,
                   country,
                   postal_code,
                   address_line_1,
                   address_line_2,
                   dictionary)


