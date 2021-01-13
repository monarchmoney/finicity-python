# -*- coding: utf-8 -*-


class PayrollDeductionsRecord(object):

    """Implementation of the 'Payroll Deductions Record' model.

    TODO: type model description here.

    Attributes:
        name (string): Deduction name types: <br> * `Federal tax`: Federal tax
            withholdings <br> * `State tax`: State tax withholdings <br> *
            `Local tax`: Local tax withholdings <br> * `Social Security tax`:
            Social security tax withholdings <br> * `Medicare tax`: Medicare
            tax withholdings <br> * `SUI SDI VPDI tax`: SUI SDI VPDI tax <br>
            * `Retirement deductions`: Retirement withholdings <br> * `Benefit
            deductions`: Medical/Health benefits withholdings, such as
            medical, dental, vision insurance <br> * `Garnishment deductions`:
            Garnishment withholdings, such as bankruptcy, student loan, state
            garnishments, tax levy garnishments, child support <br> * `Other
            deductions`: Any other or uncommon withholdings, pension plan,
            stock plans.
        amount (float): The amount associated with each deduction.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "name":'name',
        "amount":'amount'
    }

    def __init__(self,
                 name=None,
                 amount=None,
                 additional_properties = {}):
        """Constructor for the PayrollDeductionsRecord class"""

        # Initialize members of the class
        self.name = name
        self.amount = amount

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
        name = dictionary.get('name')
        amount = dictionary.get('amount')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(name,
                   amount,
                   dictionary)


