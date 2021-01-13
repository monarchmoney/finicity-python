# -*- coding: utf-8 -*-

import finicityapi.models.customer

class GetCustomersResponse(object):

    """Implementation of the 'Get Customers Response' model.

    Response For Get Customers Endpoint

    Attributes:
        found (int): Total number of records matching search criteria
        displaying (int): Number of records in this response
        more_available (bool): true if this response does not contain the last
            record in the result set
        customers (list of Customer): List of customer records

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "found":'found',
        "displaying":'displaying',
        "more_available":'moreAvailable',
        "customers":'customers'
    }

    def __init__(self,
                 found=None,
                 displaying=None,
                 more_available=None,
                 customers=None,
                 additional_properties = {}):
        """Constructor for the GetCustomersResponse class"""

        # Initialize members of the class
        self.found = found
        self.displaying = displaying
        self.more_available = more_available
        self.customers = customers

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
        customers = None
        if dictionary.get('customers') != None:
            customers = list()
            for structure in dictionary.get('customers'):
                customers.append(finicityapi.models.customer.Customer.from_dictionary(structure))

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(found,
                   displaying,
                   more_available,
                   customers,
                   dictionary)


