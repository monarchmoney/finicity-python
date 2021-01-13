# -*- coding: utf-8 -*-

import finicityapi.models.birthday

class Consumer(object):

    """Implementation of the 'Consumer' model.

    TODO: type model description here.

    Attributes:
        id (string): Finicity ID of the consumer (UUID with max length 32
            characters)
        first_name (string): The consumer first name(s) / given name(s)
        last_name (string): The consumer last name(s) / surname(s)
        customer_id (long|int): Finicity's ID of the customer
        address (string): The consumer’s street address
        city (string): The consumer’s city
        state (string): The consumer’s state
        zip (string): The consumer’s ZIP code
        phone (string): The consumer’s phone number
        ssn (string): The consumer’s 9-digit Social Security number (may
            include separators: nnn-nn-nnnn)
        birthday (Birthday): The consumer birth date
        email (string): The consumer’s email address
        created_date (long|int): Consumer created date
        suffix (string): The consumer suffix

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id":'id',
        "first_name":'firstName',
        "last_name":'lastName',
        "customer_id":'customerId',
        "address":'address',
        "city":'city',
        "state":'state',
        "zip":'zip',
        "phone":'phone',
        "ssn":'ssn',
        "birthday":'birthday',
        "email":'email',
        "created_date":'createdDate',
        "suffix":'suffix'
    }

    def __init__(self,
                 id=None,
                 first_name=None,
                 last_name=None,
                 customer_id=None,
                 address=None,
                 city=None,
                 state=None,
                 zip=None,
                 phone=None,
                 ssn=None,
                 birthday=None,
                 email=None,
                 created_date=None,
                 suffix=None,
                 additional_properties = {}):
        """Constructor for the Consumer class"""

        # Initialize members of the class
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.customer_id = customer_id
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.phone = phone
        self.ssn = ssn
        self.birthday = birthday
        self.email = email
        self.created_date = created_date
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
        address = dictionary.get('address')
        city = dictionary.get('city')
        state = dictionary.get('state')
        zip = dictionary.get('zip')
        phone = dictionary.get('phone')
        ssn = dictionary.get('ssn')
        birthday = finicityapi.models.birthday.Birthday.from_dictionary(dictionary.get('birthday')) if dictionary.get('birthday') else None
        email = dictionary.get('email')
        created_date = dictionary.get('createdDate')
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
                   address,
                   city,
                   state,
                   zip,
                   phone,
                   ssn,
                   birthday,
                   email,
                   created_date,
                   suffix,
                   dictionary)


