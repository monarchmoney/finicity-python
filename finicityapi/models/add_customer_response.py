# -*- coding: utf-8 -*-


class AddCustomerResponse(object):

    """Implementation of the 'Add Customer Response' model.

    The Response Structure For The Add Customer Endpoint and Add Testing
    Customer Endpoint

    Attributes:
        id (string): The ID Of The New Customer Record
        username (string): The Username Value Of The New Customer Record
        created_date (string): A Timestamp Of When The Customer Was Added (see
            Handling Dates And Times)

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id":'id',
        "username":'username',
        "created_date":'createdDate'
    }

    def __init__(self,
                 id=None,
                 username=None,
                 created_date=None,
                 additional_properties = {}):
        """Constructor for the AddCustomerResponse class"""

        # Initialize members of the class
        self.id = id
        self.username = username
        self.created_date = created_date

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
        username = dictionary.get('username')
        created_date = dictionary.get('createdDate')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(id,
                   username,
                   created_date,
                   dictionary)


