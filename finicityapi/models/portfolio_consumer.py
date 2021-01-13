# -*- coding: utf-8 -*-

import finicityapi.models.birthday

class PortfolioConsumer(object):

    """Implementation of the 'Portfolio Consumer' model.

    TODO: type model description here.

    Attributes:
        id (string): Finicity ID of the consumer (UUID with max length 32
            characters)
        first_name (string): The consumer first name(s) / given name(s)
        last_name (string): The consumer last name(s) / surname(s)
        customer_id (long|int): Finicity's ID of the customer
        ssn (string): The consumer’s 9-digit Social Security number (may
            include separators: nnn-nn-nnnn)
        birthday (Birthday): The consumer birth date
        suffix (string): The consumer suffix

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id":'id',
        "first_name":'firstName',
        "last_name":'lastName',
        "customer_id":'customerId',
        "ssn":'ssn',
        "birthday":'birthday',
        "suffix":'suffix'
    }

    def __init__(self,
                 id=None,
                 first_name=None,
                 last_name=None,
                 customer_id=None,
                 ssn=None,
                 birthday=None,
                 suffix=None,
                 additional_properties = {}):
        """Constructor for the PortfolioConsumer class"""

        # Initialize members of the class
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.customer_id = customer_id
        self.ssn = ssn
        self.birthday = birthday
        self.suffix = suffix

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
        id = dictionary.get('id')
        first_name = dictionary.get('firstName')
        last_name = dictionary.get('lastName')
        customer_id = dictionary.get('customerId')
        ssn = dictionary.get('ssn')
        birthday = finicityapi.models.birthday.Birthday.from_dictionary(dictionary.get('birthday')) if dictionary.get('birthday') else None
        suffix = dictionary.get('suffix')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(id,
                   first_name,
                   last_name,
                   customer_id,
                   ssn,
                   birthday,
                   suffix,
                   dictionary)


