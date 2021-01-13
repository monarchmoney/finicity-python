# -*- coding: utf-8 -*-


class TransactionsReportTransaction(object):

    """Implementation of the 'Transactions Report Transaction' model.

    The fields used in the Transactions Report Transactions record

    Attributes:
        id (long|int): The Finicity ID of the financial transaction.
        amount (float): The total amount of the transaction. Transactions for
            deposits are positive values, and withdrawals and debits are
            negative values.
        posted_date (long|int): A timestamp showing when the transaction was
            posted or cleared by the institution.
        description (string): The financial institution provides the
            description of the transaction (often known as the payee), but if
            it’s left blank, then Finicity passes the value: No description
            provided by institution.
        normalized_payee (string): A normalized payee, derived from the
            transaction's description and memo fields.
        institution_transaction_id (string): The unique identifier given by
            the financial institution for each transaction.
        category (CategoriesEnum): A value from the Categories Enumerations,
            and assigned based on the payee name.
        memo (string): The memo field of the transaction, as provided by the
            institution. The institution must provide either a description, a
            memo, or both. It is recommended to concatenate the two fields
            into a single value

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id":'id',
        "amount":'amount',
        "posted_date":'postedDate',
        "description":'description',
        "normalized_payee":'normalizedPayee',
        "institution_transaction_id":'institutionTransactionId',
        "category":'category',
        "memo":'memo'
    }

    def __init__(self,
                 id=None,
                 amount=None,
                 posted_date=None,
                 description=None,
                 normalized_payee=None,
                 institution_transaction_id=None,
                 category=None,
                 memo=None,
                 additional_properties = {}):
        """Constructor for the TransactionsReportTransaction class"""

        # Initialize members of the class
        self.id = id
        self.amount = amount
        self.posted_date = posted_date
        self.description = description
        self.normalized_payee = normalized_payee
        self.institution_transaction_id = institution_transaction_id
        self.category = category
        self.memo = memo

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
        normalized_payee = dictionary.get('normalizedPayee')
        institution_transaction_id = dictionary.get('institutionTransactionId')
        category = dictionary.get('category')
        memo = dictionary.get('memo')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(id,
                   amount,
                   posted_date,
                   description,
                   normalized_payee,
                   institution_transaction_id,
                   category,
                   memo,
                   dictionary)


