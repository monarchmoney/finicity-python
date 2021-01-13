# -*- coding: utf-8 -*-


class Employee(object):

    """Implementation of the 'Employee' model.

    TODO: type model description here.

    Attributes:
        name (string): The name of the employee
        address_1 (string): The first address line of the employee
        address_2 (string): The second address line of the employee
        city (string): The employee’s city
        state (string): The employee’s state
        zip (string): The employee’s zip

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "name":'name',
        "address_1":'address1',
        "address_2":'address2',
        "city":'city',
        "state":'state',
        "zip":'zip'
    }

    def __init__(self,
                 name=None,
                 address_1=None,
                 address_2=None,
                 city=None,
                 state=None,
                 zip=None,
                 additional_properties = {}):
        """Constructor for the Employee class"""

        # Initialize members of the class
        self.name = name
        self.address_1 = address_1
        self.address_2 = address_2
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
        name = dictionary.get('name')
        address_1 = dictionary.get('address1')
        address_2 = dictionary.get('address2')
        city = dictionary.get('city')
        state = dictionary.get('state')
        zip = dictionary.get('zip')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(name,
                   address_1,
                   address_2,
                   city,
                   state,
                   zip,
                   dictionary)


