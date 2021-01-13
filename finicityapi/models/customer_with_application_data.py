# -*- coding: utf-8 -*-


class CustomerWithApplicationData(object):

    """Implementation of the 'Customer With Application Data' model.

    The finicity customer record

    Attributes:
        id (string): Finicity’s ID for the customer
        username (string): The username associated with the customer
        first_name (string): The first name associated with the customer
        last_name (string): The last name associated with the customer
        mtype (CustomerTypeEnum): active or testing
        created_date (string): The date the customer was created
        application_id (string): The application id of the application
            assigned to the customer
        application_name (string): The application name of the application
            assigned to the customer

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id":'id',
        "username":'username',
        "first_name":'firstName',
        "last_name":'lastName',
        "mtype":'type',
        "created_date":'createdDate',
        "application_id":'applicationId',
        "application_name":'applicationName'
    }

    def __init__(self,
                 id=None,
                 username=None,
                 first_name=None,
                 last_name=None,
                 mtype=None,
                 created_date=None,
                 application_id=None,
                 application_name=None,
                 additional_properties = {}):
        """Constructor for the CustomerWithApplicationData class"""

        # Initialize members of the class
        self.id = id
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.mtype = mtype
        self.created_date = created_date
        self.application_id = application_id
        self.application_name = application_name

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
        first_name = dictionary.get('firstName')
        last_name = dictionary.get('lastName')
        mtype = dictionary.get('type')
        created_date = dictionary.get('createdDate')
        application_id = dictionary.get('applicationId')
        application_name = dictionary.get('applicationName')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(id,
                   username,
                   first_name,
                   last_name,
                   mtype,
                   created_date,
                   application_id,
                   application_name,
                   dictionary)


