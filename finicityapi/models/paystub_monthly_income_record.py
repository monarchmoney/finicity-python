# -*- coding: utf-8 -*-


class PaystubMonthlyIncomeRecord(object):

    """Implementation of the 'Paystub Monthly Income Record' model.

    TODO: type model description here.

    Attributes:
        estimated_monthly_base_pay (float): The estimated monthly base pay
            amount for the employment from the paystub, calculated by
            Finicity.
        estimated_monthly_overtime_pay (float): The estimated monthly overtime
            pay amount for the employment from the paystub, calculated by
            Finicity.
        estimated_monthly_bonus_pay (float): The estimated monthly bonus pay
            amount for the employment from the paystub, calculated by
            Finicity.
        estimated_monthly_commission_pay (float): The estimated commission
            bonus pay amount for the employment from the paystub, calculated
            by Finicity.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "estimated_monthly_base_pay":'estimatedMonthlyBasePay',
        "estimated_monthly_overtime_pay":'estimatedMonthlyOvertimePay',
        "estimated_monthly_bonus_pay":'estimatedMonthlyBonusPay',
        "estimated_monthly_commission_pay":'estimatedMonthlyCommissionPay'
    }

    def __init__(self,
                 estimated_monthly_base_pay=None,
                 estimated_monthly_overtime_pay=None,
                 estimated_monthly_bonus_pay=None,
                 estimated_monthly_commission_pay=None,
                 additional_properties = {}):
        """Constructor for the PaystubMonthlyIncomeRecord class"""

        # Initialize members of the class
        self.estimated_monthly_base_pay = estimated_monthly_base_pay
        self.estimated_monthly_overtime_pay = estimated_monthly_overtime_pay
        self.estimated_monthly_bonus_pay = estimated_monthly_bonus_pay
        self.estimated_monthly_commission_pay = estimated_monthly_commission_pay

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
        estimated_monthly_base_pay = dictionary.get('estimatedMonthlyBasePay')
        estimated_monthly_overtime_pay = dictionary.get('estimatedMonthlyOvertimePay')
        estimated_monthly_bonus_pay = dictionary.get('estimatedMonthlyBonusPay')
        estimated_monthly_commission_pay = dictionary.get('estimatedMonthlyCommissionPay')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(estimated_monthly_base_pay,
                   estimated_monthly_overtime_pay,
                   estimated_monthly_bonus_pay,
                   estimated_monthly_commission_pay,
                   dictionary)


