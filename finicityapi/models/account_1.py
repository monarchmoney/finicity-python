# -*- coding: utf-8 -*-


class Account1(object):

    """Implementation of the 'Account1' model.

    TODO: type model description here.

    Attributes:
        id (string): TODO: type description here.
        number (string): TODO: type description here.
        name (string): TODO: type description here.
        balance (float): TODO: type description here.
        mtype (string): TODO: type description here.
        status (string): TODO: type description here.
        customer_id (string): TODO: type description here.
        institution_id (string): TODO: type description here.
        balance_date (int): TODO: type description here.
        created_date (int): TODO: type description here.
        currency (string): TODO: type description here.
        institution_login_id (int): TODO: type description here.
        display_position (int): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id":'id',
        "number":'number',
        "name":'name',
        "balance":'balance',
        "mtype":'type',
        "status":'status',
        "customer_id":'customerId',
        "institution_id":'institutionId',
        "balance_date":'balanceDate',
        "created_date":'createdDate',
        "currency":'currency',
        "institution_login_id":'institutionLoginId',
        "display_position":'displayPosition'
    }

    def __init__(self,
                 id=None,
                 number=None,
                 name=None,
                 balance=None,
                 mtype=None,
                 status=None,
                 customer_id=None,
                 institution_id=None,
                 balance_date=None,
                 created_date=None,
                 currency=None,
                 institution_login_id=None,
                 display_position=None,
                 additional_properties = {}):
        """Constructor for the Account1 class"""

        # Initialize members of the class
        self.id = id
        self.number = number
        self.name = name
        self.balance = balance
        self.mtype = mtype
        self.status = status
        self.customer_id = customer_id
        self.institution_id = institution_id
        self.balance_date = balance_date
        self.created_date = created_date
        self.currency = currency
        self.institution_login_id = institution_login_id
        self.display_position = display_position

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
        number = dictionary.get('number')
        name = dictionary.get('name')
        balance = dictionary.get('balance')
        mtype = dictionary.get('type')
        status = dictionary.get('status')
        customer_id = dictionary.get('customerId')
        institution_id = dictionary.get('institutionId')
        balance_date = dictionary.get('balanceDate')
        created_date = dictionary.get('createdDate')
        currency = dictionary.get('currency')
        institution_login_id = dictionary.get('institutionLoginId')
        display_position = dictionary.get('displayPosition')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(id,
                   number,
                   name,
                   balance,
                   mtype,
                   status,
                   customer_id,
                   institution_id,
                   balance_date,
                   created_date,
                   currency,
                   institution_login_id,
                   display_position,
                   dictionary)


