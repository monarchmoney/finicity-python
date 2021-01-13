# -*- coding: utf-8 -*-


class VOIReportTransactionRecord(object):

    """Implementation of the 'VOI Report Transaction Record' model.

    VOI Report Transaction Record

    Attributes:
        id (long|int): The Finicity ID of the transaction
        amount (float): The total amount of the transaction. Transactions for
            deposits are positive values, withdrawals and debits are negative
            values.
        posted_date (long|int): A timestamp showing when the transaction was
            posted or cleared by the institution (see Handling Dates and
            Times)
        description (string): The description of the transaction, as provided
            by the institution (often known as payee). In the event that this
            field is left blank by the institution, Finicity will pass a value
            of “No description provided by institution”. All other values are
            provided by the institution.
        memo (string): The memo field of the transaction, as provided by the
            institution. The institution must provide either a description, a
            memo, or both. It is recommended to concatenate the two fields
            into a single value
        institution_transaction_id (string): The unique identifier given by
            the FI for each transaction.
        category (string): The categorization of the transaction.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id":'id',
        "amount":'amount',
        "posted_date":'postedDate',
        "description":'description',
        "memo":'memo',
        "institution_transaction_id":'institutionTransactionId',
        "category":'category'
    }

    def __init__(self,
                 id=None,
                 amount=None,
                 posted_date=None,
                 description=None,
                 memo=None,
                 institution_transaction_id=None,
                 category=None,
                 additional_properties = {}):
        """Constructor for the VOIReportTransactionRecord class"""

        # Initialize members of the class
        self.id = id
        self.amount = amount
        self.posted_date = posted_date
        self.description = description
        self.memo = memo
        self.institution_transaction_id = institution_transaction_id
        self.category = category

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
        amount = dictionary.get('amount')
        posted_date = dictionary.get('postedDate')
        description = dictionary.get('description')
        memo = dictionary.get('memo')
        institution_transaction_id = dictionary.get('institutionTransactionId')
        category = dictionary.get('category')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(id,
                   amount,
                   posted_date,
                   description,
                   memo,
                   institution_transaction_id,
                   category,
                   dictionary)


