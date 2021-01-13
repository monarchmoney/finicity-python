# -*- coding: utf-8 -*-

import finicityapi.models.payroll_address

class PayrollEmployeeRecord(object):

    """Implementation of the 'Payroll Employee Record' model.

    TODO: type model description here.

    Attributes:
        name (string): Full name of the employee: first, middle (if stated),
            and last name.
        given_name (string): First name of employee
        middle_name (string): Middle name of employee, if stated
        family_name (string): Last name of employee
        address (list of PayrollAddress): Array of addresses

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "name":'name',
        "given_name":'givenName',
        "middle_name":'middleName',
        "family_name":'familyName',
        "address":'address'
    }

    def __init__(self,
                 name=None,
                 given_name=None,
                 middle_name=None,
                 family_name=None,
                 address=None,
                 additional_properties = {}):
        """Constructor for the PayrollEmployeeRecord class"""

        # Initialize members of the class
        self.name = name
        self.given_name = given_name
        self.middle_name = middle_name
        self.family_name = family_name
        self.address = address

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
        given_name = dictionary.get('givenName')
        middle_name = dictionary.get('middleName')
        family_name = dictionary.get('familyName')
        address = None
        if dictionary.get('address') != None:
            address = list()
            for structure in dictionary.get('address'):
                address.append(finicityapi.models.payroll_address.PayrollAddress.from_dictionary(structure))

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(name,
                   given_name,
                   middle_name,
                   family_name,
                   address,
                   dictionary)


