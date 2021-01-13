# -*- coding: utf-8 -*-


class VOAReportTransaction(object):

    """Implementation of the 'VOA Report Transaction' model.

    TODO: type model description here.

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
        normalized_payee (string): A normalized payee, derived from the
            transaction's description and memo fields.
        institution_transaction_id (string): The unique identifier given by
            the FI for each transaction.
        category (string): The categorization of the transaction.
        mtype (TransactionTypeEnum): One of the values from Transaction Types
            (optional)
        security_type (string): The type of investment security (VOA only)
        symbol (string): Investment symbol (VOA only)
        commission (float): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id":'id',
        "amount":'amount',
        "posted_date":'postedDate',
        "description":'description',
        "memo":'memo',
        "normalized_payee":'normalizedPayee',
        "institution_transaction_id":'institutionTransactionId',
        "category":'category',
        "mtype":'type',
        "security_type":'securityType',
        "symbol":'symbol',
        "commission":'commission'
    }

    def __init__(self,
                 id=None,
                 amount=None,
                 posted_date=None,
                 description=None,
                 memo=None,
                 normalized_payee=None,
                 institution_transaction_id=None,
                 category=None,
                 mtype=None,
                 security_type=None,
                 symbol=None,
                 commission=None,
                 additional_properties = {}):
        """Constructor for the VOAReportTransaction class"""

        # Initialize members of the class
        self.id = id
        self.amount = amount
        self.posted_date = posted_date
        self.description = description
        self.memo = memo
        self.normalized_payee = normalized_payee
        self.institution_transaction_id = institution_transaction_id
        self.category = category
        self.mtype = mtype
        self.security_type = security_type
        self.symbol = symbol
        self.commission = commission

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
        normalized_payee = dictionary.get('normalizedPayee')
        institution_transaction_id = dictionary.get('institutionTransactionId')
        category = dictionary.get('category')
        mtype = dictionary.get('type')
        security_type = dictionary.get('securityType')
        symbol = dictionary.get('symbol')
        commission = dictionary.get('commission')

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
                   normalized_payee,
                   institution_transaction_id,
                   category,
                   mtype,
                   security_type,
                   symbol,
                   commission,
                   dictionary)


