# -*- coding: utf-8 -*-


class CreateTxpushTestTransactionRequest(object):

    """Implementation of the 'Create TxPush Test Transaction Request' model.

    Create a text transaction for TxPush testing

    Attributes:
        amount (float): The amount of the transaction
        description (string): The description of the transaction
        status (string): active or pending (optional)
        posted_date (long|int): An optional timestamp for the transaction’s
            posted date value for this transaction (see Handling Dates and
            Times). Timestamp must be no more than 6 months from the current
            date.
        transaction_date (long|int): An optional timestamp for the
            transaction’s posted date value for this transaction (see Handling
            Dates and Times)

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "amount":'amount',
        "description":'description',
        "posted_date":'postedDate',
        "transaction_date":'transactionDate',
        "status":'status'
    }

    def __init__(self,
                 amount=None,
                 description=None,
                 posted_date=None,
                 transaction_date=None,
                 status='active',
                 additional_properties = {}):
        """Constructor for the CreateTxpushTestTransactionRequest class"""

        # Initialize members of the class
        self.amount = amount
        self.description = description
        self.status = status
        self.posted_date = posted_date
        self.transaction_date = transaction_date

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
        amount = dictionary.get('amount')
        description = dictionary.get('description')
        posted_date = dictionary.get('postedDate')
        transaction_date = dictionary.get('transactionDate')
        status = dictionary.get("status") if dictionary.get("status") else 'active'

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(amount,
                   description,
                   posted_date,
                   transaction_date,
                   status,
                   dictionary)


