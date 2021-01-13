# -*- coding: utf-8 -*-


class AccountDetail(object):

    """Implementation of the 'Account Detail' model.

    TODO: type model description here.

    Attributes:
        interest_margin_balance (float): Only available for investment
            accounts. Net interest earned after deducting interest paid out
        available_cash_balance (float): Only available for investment
            accounts. Amount available for cash withdrawal
        vested_balance (float): Only available for investment accounts. Vested
            amount in account
        current_loan_balance (float): Only available for investment accounts.
            Current loan balance
        available_balance_amount (float): The available balance for the
            account

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "interest_margin_balance":'interestMarginBalance',
        "available_cash_balance":'availableCashBalance',
        "vested_balance":'vestedBalance',
        "current_loan_balance":'currentLoanBalance',
        "available_balance_amount":'availableBalanceAmount'
    }

    def __init__(self,
                 interest_margin_balance=None,
                 available_cash_balance=None,
                 vested_balance=None,
                 current_loan_balance=None,
                 available_balance_amount=None,
                 additional_properties = {}):
        """Constructor for the AccountDetail class"""

        # Initialize members of the class
        self.interest_margin_balance = interest_margin_balance
        self.available_cash_balance = available_cash_balance
        self.vested_balance = vested_balance
        self.current_loan_balance = current_loan_balance
        self.available_balance_amount = available_balance_amount

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
        interest_margin_balance = dictionary.get('interestMarginBalance')
        available_cash_balance = dictionary.get('availableCashBalance')
        vested_balance = dictionary.get('vestedBalance')
        current_loan_balance = dictionary.get('currentLoanBalance')
        available_balance_amount = dictionary.get('availableBalanceAmount')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(interest_margin_balance,
                   available_cash_balance,
                   vested_balance,
                   current_loan_balance,
                   available_balance_amount,
                   dictionary)


