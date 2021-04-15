# -*- coding: utf-8 -*-
import copy

import finicityapi.models.customer_account_detail
import finicityapi.models.customer_account_position


class CustomerAccount(object):

    """Implementation of the 'Customer Account' model.

    A customer account represents a bank account such as a checking or savings
    that the customer has added via the Connect interface

    Attributes:
        id (long|int): The generated FInicity ID of the account
        number (string): The account number from the institution (all digits
            except the last four are obfuscated)
        real_account_number_last_4 (int): The last 4 digits of the ACH account
            number
        name (string): The account name from the institution
        balance (float): The cleared balance of the account as-of balanceDate
        mtype (AccountTypeEnum): One of the values from Account Types
        aggregation_status_code (int): The status of the most recent
            aggregation attempt (see Handling Aggregation Status Codes). This
            will not be present until you have run your first aggregation for
            the account.
        status (string): pending during account discovery, always active
            following successful account activation
        customer_id (long|int): The Finicity ID of the customer associated
            with this account
        institution_id (long|int): The Finicity ID of the institution for this
            account
        balance_date (long|int): A timestamp showing when the balance was
            captured (see Handling Dates and Times)
        aggregation_success_date (long|int): A timestamp showing the last
            successful aggregation of the account (see Handling Dates and
            Times). This will not be present until you have run your first
            aggregation for the account.
        aggregation_attempt_date (long|int): A timestamp showing the last
            aggregation attempt, whether successful or not (see Handling Dates
            and Times). This will not be present until you have run your first
            aggregation for the account.
        created_date (long|int): A timestamp showing when the account was
            added to the Finicity system (see Handling Dates and Times)
        currency (string): The currency of the account
        last_transaction_date (long|int): The date of the latest transaction
            on the account (see Handling Dates and Times). This will not be
            present until you have run your first aggregation for the
            account.
        institution_login_id (long|int): The institution login ID (see
            Institution Logins)
        detail (CustomerAccountDetail): Additional Account Details
        position (list of CustomerAccountPosition): Investment holdings
        display_position (int): Display position of the account at the
            financial institution 1 being the top listed account

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
        "display_position":'displayPosition',
        "real_account_number_last_4":'realAccountNumberLast4',
        "aggregation_status_code":'aggregationStatusCode',
        "aggregation_success_date":'aggregationSuccessDate',
        "aggregation_attempt_date":'aggregationAttemptDate',
        "last_transaction_date":'lastTransactionDate',
        "detail":'detail',
        "position":'position'
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
                 real_account_number_last_4=None,
                 aggregation_status_code=None,
                 aggregation_success_date=None,
                 aggregation_attempt_date=None,
                 last_transaction_date=None,
                 detail=None,
                 position=None,
                 additional_properties = {},
                 json_data=None):
        """Constructor for the CustomerAccount class"""

        # Initialize members of the class
        self.id = id
        self.number = number
        self.real_account_number_last_4 = real_account_number_last_4
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
        self.detail = detail
        self.position = position
        self.display_position = display_position

        # Add additional model properties to the instance
        self.additional_properties = additional_properties

        # Store original response
        self.json_data = json_data

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

        json_data = copy.deepcopy(dictionary)

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
        real_account_number_last_4 = dictionary.get('realAccountNumberLast4')
        aggregation_status_code = dictionary.get('aggregationStatusCode')
        aggregation_success_date = dictionary.get('aggregationSuccessDate')
        aggregation_attempt_date = dictionary.get('aggregationAttemptDate')
        last_transaction_date = dictionary.get('lastTransactionDate')
        detail = finicityapi.models.customer_account_detail.CustomerAccountDetail.from_dictionary(dictionary.get('detail')) if dictionary.get('detail') else None
        position = None
        if dictionary.get('position') != None:
            position = list()
            for structure in dictionary.get('position'):
                position.append(finicityapi.models.customer_account_position.CustomerAccountPosition.from_dictionary(structure))

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
                   real_account_number_last_4,
                   aggregation_status_code,
                   aggregation_success_date,
                   aggregation_attempt_date,
                   last_transaction_date,
                   detail,
                   position,
                   dictionary,
                   json_data=json_data)
