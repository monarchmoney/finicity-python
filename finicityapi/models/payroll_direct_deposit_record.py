# -*- coding: utf-8 -*-


class PayrollDirectDepositRecord(object):

    """Implementation of the 'Payroll Direct Deposit Record' model.

    TODO: type model description here.

    Attributes:
        account_type_code (string): Bank account types: <br> * `Checking` <br>
            * `Saving` <br> * `Share deposit`: Credit union <br> * `Loan
            deposit`: The employee chooses an amount from their net pay to
            automatically deposit a payment into their loan account.
        amount (float): Direct deposit amount
        account_last_four (string): Last four digits of the deposit account
            number
        routing_number (string): Routing number for the deposit account

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "account_type_code":'accountTypeCode',
        "amount":'amount',
        "account_last_four":'accountLastFour',
        "routing_number":'routingNumber'
    }

    def __init__(self,
                 account_type_code=None,
                 amount=None,
                 account_last_four=None,
                 routing_number=None,
                 additional_properties = {}):
        """Constructor for the PayrollDirectDepositRecord class"""

        # Initialize members of the class
        self.account_type_code = account_type_code
        self.amount = amount
        self.account_last_four = account_last_four
        self.routing_number = routing_number

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
        account_type_code = dictionary.get('accountTypeCode')
        amount = dictionary.get('amount')
        account_last_four = dictionary.get('accountLastFour')
        routing_number = dictionary.get('routingNumber')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(account_type_code,
                   amount,
                   account_last_four,
                   routing_number,
                   dictionary)


