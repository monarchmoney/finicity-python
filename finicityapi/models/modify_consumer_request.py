# -*- coding: utf-8 -*-

import finicityapi.models.birthday

class ModifyConsumerRequest(object):

    """Implementation of the 'ModifyConsumerRequest' model.

    TODO: type model description here.

    Attributes:
        first_name (string): The consumer first name(s) / given name(s)
        last_name (string): The consumer last name(s) / surname(s)
        address (string): The consumer’s street address
        city (string): The consumer’s city
        state (string): The consumer’s state
        zip (string): The consumer’s ZIP code
        phone (string): The consumer’s phone number
        ssn (string): The consumer’s 9-digit Social Security number (may
            include separators: nnn-nn-nnnn)
        birthday (Birthday): The consumer birth date
        email (string): The consumer’s email address
        suffix (string): The consumer suffix
        email_address (string): The consumer’s email address

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "first_name":'firstName',
        "last_name":'lastName',
        "address":'address',
        "city":'city',
        "state":'state',
        "zip":'zip',
        "phone":'phone',
        "ssn":'ssn',
        "birthday":'birthday',
        "email":'email',
        "email_address":'emailAddress',
        "suffix":'suffix'
    }

    def __init__(self,
                 first_name=None,
                 last_name=None,
                 address=None,
                 city=None,
                 state=None,
                 zip=None,
                 phone=None,
                 ssn=None,
                 birthday=None,
                 email=None,
                 email_address=None,
                 suffix=None,
                 additional_properties = {}):
        """Constructor for the ModifyConsumerRequest class"""

        # Initialize members of the class
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.phone = phone
        self.ssn = ssn
        self.birthday = birthday
        self.email = email
        self.suffix = suffix
        self.email_address = email_address

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
        first_name = dictionary.get('firstName')
        last_name = dictionary.get('lastName')
        address = dictionary.get('address')
        city = dictionary.get('city')
        state = dictionary.get('state')
        zip = dictionary.get('zip')
        phone = dictionary.get('phone')
        ssn = dictionary.get('ssn')
        birthday = finicityapi.models.birthday.Birthday.from_dictionary(dictionary.get('birthday')) if dictionary.get('birthday') else None
        email = dictionary.get('email')
        email_address = dictionary.get('emailAddress')
        suffix = dictionary.get('suffix')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(first_name,
                   last_name,
                   address,
                   city,
                   state,
                   zip,
                   phone,
                   ssn,
                   birthday,
                   email,
                   email_address,
                   suffix,
                   dictionary)


