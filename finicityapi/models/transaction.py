# -*- coding: utf-8 -*-
import copy

import finicityapi.models.categorization

class Transaction(object):

    """Implementation of the 'Transaction' model.

    TODO: type model description here.

    Attributes:
        id (long|int): The Finicity ID of the transaction
        amount (float): The total amount of the transaction. Transactions for
            deposits are positive values, withdrawals and debits are negative
            values.
        account_id (long|int): The Finicity ID of the account associated with
            this transaction
        customer_id (long|int): The Finicity ID of the customer associated
            with this transaction
        status (string): One of active, pending, or shadow (see Pending
            Transactions and Shadow Transactions)
        description (string): The description of the transaction, as provided
            by the institution (often known as payee). In the event that this
            field is left blank by the institution, Finicity will pass a value
            of "No description provided by institution”. All other values are
            provided by the institution.
        memo (string): The memo field of the transaction, as provided by the
            institution. The institution must provide either a description, a
            memo, or both. It is recommended to concatenate the two fields
            into a single value
        posted_date (string): A timestamp showing when the transaction was
            posted or cleared by the institution (see Handling Dates and
            Times)
        transaction_date (string): An optional timestamp showing when the
            transaction occurred, as provided by the institution (see Handling
            Dates and Times)
        created_date (string): A timestamp showing when the transaction was
            added to the Finicity system. (See Handling Dates and Times.) This
            value usually is not interesting outside of Finicity.
        mtype (TransactionTypeEnum): TODO: type description here.
        check_num (int): The check number of the transaction, as provided by
            the institution
        escrow_amount (float): The portion of the transaction allocated to
            escrow, if available
        fee_amount (float): The portion of the transaction allocated to fee,
            if available
        interest_amount (float): The portion of the transaction allocated to
            interest, if available
        principal_amount (float): The portion of the transaction allocated to
            principal, if available
        unit_quantity (int): The number of units (e.g. individual shares) in
            the transaction, if available
        unit_value (float): The value of each unit in the transaction, if
            available
        categorization (Categorization): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id":'id',
        "amount":'amount',
        "account_id":'accountId',
        "customer_id":'customerId',
        "status":'status',
        "description":'description',
        "posted_date":'postedDate',
        "created_date":'createdDate',
        "memo":'memo',
        "transaction_date":'transactionDate',
        "mtype":'type',
        "check_num":'checkNum',
        "escrow_amount":'escrowAmount',
        "fee_amount":'feeAmount',
        "interest_amount":'interestAmount',
        "principal_amount":'principalAmount',
        "unit_quantity":'unitQuantity',
        "unit_value":'unitValue',
        "categorization":'categorization'
    }

    def __init__(self,
                 id=None,
                 amount=None,
                 account_id=None,
                 customer_id=None,
                 status=None,
                 description=None,
                 posted_date=None,
                 created_date=None,
                 memo=None,
                 transaction_date=None,
                 mtype=None,
                 check_num=None,
                 escrow_amount=None,
                 fee_amount=None,
                 interest_amount=None,
                 principal_amount=None,
                 unit_quantity=None,
                 unit_value=None,
                 categorization=None,
                 additional_properties = {},
                 json_data=None):
        """Constructor for the Transaction class"""

        # Initialize members of the class
        self.id = id
        self.amount = amount
        self.account_id = account_id
        self.customer_id = customer_id
        self.status = status
        self.description = description
        self.memo = memo
        self.posted_date = posted_date
        self.transaction_date = transaction_date
        self.created_date = created_date
        self.mtype = mtype
        self.check_num = check_num
        self.escrow_amount = escrow_amount
        self.fee_amount = fee_amount
        self.interest_amount = interest_amount
        self.principal_amount = principal_amount
        self.unit_quantity = unit_quantity
        self.unit_value = unit_value
        self.categorization = categorization

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
        amount = dictionary.get('amount')
        account_id = dictionary.get('accountId')
        customer_id = dictionary.get('customerId')
        status = dictionary.get('status')
        description = dictionary.get('description')
        posted_date = dictionary.get('postedDate')
        created_date = dictionary.get('createdDate')
        memo = dictionary.get('memo')
        transaction_date = dictionary.get('transactionDate')
        mtype = dictionary.get('type')
        check_num = dictionary.get('checkNum')
        escrow_amount = dictionary.get('escrowAmount')
        fee_amount = dictionary.get('feeAmount')
        interest_amount = dictionary.get('interestAmount')
        principal_amount = dictionary.get('principalAmount')
        unit_quantity = dictionary.get('unitQuantity')
        unit_value = dictionary.get('unitValue')
        categorization = finicityapi.models.categorization.Categorization.from_dictionary(dictionary.get('categorization')) if dictionary.get('categorization') else None

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(id,
                   amount,
                   account_id,
                   customer_id,
                   status,
                   description,
                   posted_date,
                   created_date,
                   memo,
                   transaction_date,
                   mtype,
                   check_num,
                   escrow_amount,
                   fee_amount,
                   interest_amount,
                   principal_amount,
                   unit_quantity,
                   unit_value,
                   categorization,
                   dictionary,
                   json_data=json_data)
