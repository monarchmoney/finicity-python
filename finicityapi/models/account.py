# -*- coding: utf-8 -*-


class Account(object):

    """Implementation of the 'Account' model.

    TODO: type model description here.

    Attributes:
        id (string): TODO: type description here.
        number (string): TODO: type description here.
        name (string): TODO: type description here.
        balance (float): TODO: type description here.
        mtype (string): TODO: type description here.
        aggregation_status_code (int): TODO: type description here.
        status (string): TODO: type description here.
        customer_id (string): TODO: type description here.
        institution_id (string): TODO: type description here.
        balance_date (int): TODO: type description here.
        aggregation_success_date (int): TODO: type description here.
        aggregation_attempt_date (int): TODO: type description here.
        created_date (int): TODO: type description here.
        currency (string): TODO: type description here.
        last_transaction_date (int): TODO: type description here.
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
        "created_date":'createdDate',
        "currency":'currency',
        "institution_login_id":'institutionLoginId',
        "display_position":'displayPosition',
        "aggregation_status_code":'aggregationStatusCode',
        "balance_date":'balanceDate',
        "aggregation_success_date":'aggregationSuccessDate',
        "aggregation_attempt_date":'aggregationAttemptDate',
        "last_transaction_date":'lastTransactionDate'
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
                 created_date=None,
                 currency=None,
                 institution_login_id=None,
                 display_position=None,
                 aggregation_status_code=None,
                 balance_date=None,
                 aggregation_success_date=None,
                 aggregation_attempt_date=None,
                 last_transaction_date=None,
                 additional_properties = {}):
        """Constructor for the Account class"""

        # Initialize members of the class
        self.id = id
        self.number = number
        self.name = name
        self.balance = balance
        self.mtype = mtype
        self.aggregation_status_code = aggregation_status_code
        self.status = status
        self.customer_id = customer_id
        self.institution_id = institution_id
        self.balance_date = balance_date
        self.aggregation_success_date = aggregation_success_date
        self.aggregation_attempt_date = aggregation_attempt_date
        self.created_date = created_date
        self.currency = currency
        self.last_transaction_date = last_transaction_date
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
        created_date = dictionary.get('createdDate')
        currency = dictionary.get('currency')
        institution_login_id = dictionary.get('institutionLoginId')
        display_position = dictionary.get('displayPosition')
        aggregation_status_code = dictionary.get('aggregationStatusCode')
        balance_date = dictionary.get('balanceDate')
        aggregation_success_date = dictionary.get('aggregationSuccessDate')
        aggregation_attempt_date = dictionary.get('aggregationAttemptDate')
        last_transaction_date = dictionary.get('lastTransactionDate')

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
                   created_date,
                   currency,
                   institution_login_id,
                   display_position,
                   aggregation_status_code,
                   balance_date,
                   aggregation_success_date,
                   aggregation_attempt_date,
                   last_transaction_date,
                   dictionary)


