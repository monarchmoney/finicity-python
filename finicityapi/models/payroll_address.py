# -*- coding: utf-8 -*-


class PayrollAddress(object):

    """Implementation of the 'Payroll Address' model.

    TODO: type model description here.

    Attributes:
        address_1 (string): Employer address as stated by the employer in the
            payroll system
        city (string): Employer city as stated by the employer in the payroll
            system
        state (string): Employer state as stated by the employer in the
            payroll system
        zip (string): Employer zip code as stated by the employer in the
            payroll system

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "address_1":'address1',
        "city":'city',
        "state":'state',
        "zip":'zip'
    }

    def __init__(self,
                 address_1=None,
                 city=None,
                 state=None,
                 zip=None,
                 additional_properties = {}):
        """Constructor for the PayrollAddress class"""

        # Initialize members of the class
        self.address_1 = address_1
        self.city = city
        self.state = state
        self.zip = zip

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
        address_1 = dictionary.get('address1')
        city = dictionary.get('city')
        state = dictionary.get('state')
        zip = dictionary.get('zip')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(address_1,
                   city,
                   state,
                   zip,
                   dictionary)


