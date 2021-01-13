# -*- coding: utf-8 -*-


class LoanPaymentDetails(object):

    """Implementation of the 'Loan Payment Details' model.

    The loan payment details for the customer account

    Attributes:
        loan_number (string): The number of the specific loan under the
            account.
        loan_payment_number (string): The payment number given by the
            institution. This number is typically for manual payments. This is
            not an ACH payment number.
        loan_payment_address (string): The payment address to send manual
            payments to

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "loan_number":'loanNumber',
        "loan_payment_number":'loanPaymentNumber',
        "loan_payment_address":'loanPaymentAddress'
    }

    def __init__(self,
                 loan_number=None,
                 loan_payment_number=None,
                 loan_payment_address=None,
                 additional_properties = {}):
        """Constructor for the LoanPaymentDetails class"""

        # Initialize members of the class
        self.loan_number = loan_number
        self.loan_payment_number = loan_payment_number
        self.loan_payment_address = loan_payment_address

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
        loan_number = dictionary.get('loanNumber')
        loan_payment_number = dictionary.get('loanPaymentNumber')
        loan_payment_address = dictionary.get('loanPaymentAddress')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(loan_number,
                   loan_payment_number,
                   loan_payment_address,
                   dictionary)


