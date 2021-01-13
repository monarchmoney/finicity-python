# -*- coding: utf-8 -*-


class AddCustomerRequest(object):

    """Implementation of the 'Add Customer Request' model.

    Request Structure For The Add Customer Endpoint and Add Testing Customer
    Endpoint

    Attributes:
        username (string): The customer’s username, assigned by the partner (a
            unique identifier), following these rules: minimum 6 characters
            maximum 255 characters any mix of uppercase, lowercase, numeric,
            and non-alphabet special characters ! @ . # $ % & * _ – + the use
            of email in this field is discouraged it is recommended to use a
            unique non-email identifier Use of special characters may result
            in an error (e.g. í, ü, etc.)
        first_name (string): The customer’s first name(s) / given name(s)
            (optional)
        last_name (string): The customer’s last name(s) / surname(s)
            (optional)
        application_id (string): The application Id for the app the partner
            would like to assign the customer to. This cannot be changed once
            set. Only applicable in cases of partners with multiple registered
            applications. If the partner only has one app this can be omitted.
            This value comes from the "applicationId" from the Get App
            Registration Status endpoint

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "username":'username',
        "first_name":'firstName',
        "last_name":'lastName',
        "application_id":'applicationId'
    }

    def __init__(self,
                 username=None,
                 first_name=None,
                 last_name=None,
                 application_id=None,
                 additional_properties = {}):
        """Constructor for the AddCustomerRequest class"""

        # Initialize members of the class
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.application_id = application_id

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
        username = dictionary.get('username')
        first_name = dictionary.get('firstName')
        last_name = dictionary.get('lastName')
        application_id = dictionary.get('applicationId')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(username,
                   first_name,
                   last_name,
                   application_id,
                   dictionary)


