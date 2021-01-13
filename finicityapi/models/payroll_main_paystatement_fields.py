# -*- coding: utf-8 -*-


class PayrollMainPaystatementFields(object):

    """Implementation of the 'Payroll Main Paystatement Fields' model.

    TODO: type model description here.

    Attributes:
        pay_date (long|int): Pay date for a pay period
        start_date (long|int): Start date for a pay period
        end_date (long|int): End date for a pay period
        pay_period_hours (int): The sum total of the number of hours worked
            each week for a pay period.
        gross_pay_amount (float): Gross pay amount for a pay period
        gross_pay_ytd (float): The year-to-date (YTD) gross pay amount for an
            employer. <br>  <br>**Note**: This field is only included in the
            pay histories from the last period of the year where
            `lastPayPeriodIndicator` = true.
        net_pay_amount (float): Net pay amount for a pay period
        net_pay_ytd (float): The YTD net pay amount for an employer. <br> 
            <br>**Note**: This field is only included in the pay histories
            from the last period of the year where `lastPayPeriodIndicator` =
            true.
        payroll_provider (string): The name of the payroll provider where the
            data was retrieved.
        pay_frequency (string): The pay frequency: <br> * Monthly <br> *
            Semimonthly <br> * Weekly <br> * Biweekly <br> * Daily <br> *
            Biweekly odd <br> * Biweekly even <br> * Quarterly <br> * Annually
            <br> * Semiannually <br> * Every 2.6 weeks <br> * Every 4 weeks
            <br> * Every 5.2 weeks
        pay_type (string): The pay type is `salary`, `hourly`, or `daily`.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "pay_date":'payDate',
        "start_date":'startDate',
        "end_date":'endDate',
        "pay_period_hours":'payPeriodHours',
        "gross_pay_amount":'grossPayAmount',
        "gross_pay_ytd":'grossPayYTD',
        "net_pay_amount":'netPayAmount',
        "net_pay_ytd":'netPayYTD',
        "payroll_provider":'payrollProvider',
        "pay_frequency":'payFrequency',
        "pay_type":'payType'
    }

    def __init__(self,
                 pay_date=None,
                 start_date=None,
                 end_date=None,
                 pay_period_hours=None,
                 gross_pay_amount=None,
                 gross_pay_ytd=None,
                 net_pay_amount=None,
                 net_pay_ytd=None,
                 payroll_provider=None,
                 pay_frequency=None,
                 pay_type=None,
                 additional_properties = {}):
        """Constructor for the PayrollMainPaystatementFields class"""

        # Initialize members of the class
        self.pay_date = pay_date
        self.start_date = start_date
        self.end_date = end_date
        self.pay_period_hours = pay_period_hours
        self.gross_pay_amount = gross_pay_amount
        self.gross_pay_ytd = gross_pay_ytd
        self.net_pay_amount = net_pay_amount
        self.net_pay_ytd = net_pay_ytd
        self.payroll_provider = payroll_provider
        self.pay_frequency = pay_frequency
        self.pay_type = pay_type

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
        pay_date = dictionary.get('payDate')
        start_date = dictionary.get('startDate')
        end_date = dictionary.get('endDate')
        pay_period_hours = dictionary.get('payPeriodHours')
        gross_pay_amount = dictionary.get('grossPayAmount')
        gross_pay_ytd = dictionary.get('grossPayYTD')
        net_pay_amount = dictionary.get('netPayAmount')
        net_pay_ytd = dictionary.get('netPayYTD')
        payroll_provider = dictionary.get('payrollProvider')
        pay_frequency = dictionary.get('payFrequency')
        pay_type = dictionary.get('payType')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(pay_date,
                   start_date,
                   end_date,
                   pay_period_hours,
                   gross_pay_amount,
                   gross_pay_ytd,
                   net_pay_amount,
                   net_pay_ytd,
                   payroll_provider,
                   pay_frequency,
                   pay_type,
                   dictionary)


