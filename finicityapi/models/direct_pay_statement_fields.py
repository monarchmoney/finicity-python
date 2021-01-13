# -*- coding: utf-8 -*-

import finicityapi.models.payroll_main_paystatement_fields
import finicityapi.models.payroll_employer_record
import finicityapi.models.payroll_employee_record
import finicityapi.models.payroll_earnings_record
import finicityapi.models.payroll_deductions_record
import finicityapi.models.payroll_direct_deposit_record
import finicityapi.models.payroll_monthly_income_record

class DirectPayStatementFields(object):

    """Implementation of the 'Direct Pay Statement Fields' model.

    TODO: type model description here.

    Attributes:
        payroll_data_as_of_date (string): The most recent pay date out of all
            other employment records listed on the report.
        payroll_data_retrieval_id (string): An id to identify the data
            retrieved from the payroll providers for the report.
        payroll_pay_history_id (string): An id for the income and employment
            details from a pay period.
        last_pay_period_indicator (bool): The payment history from the last
            pay period of the year. If there are 3 years of pay history, then
            the value is true. <br>  <br> * History for the most recent pay
            period of the current year. <br> * History for the last pay period
            in the previous two years.
        main_pay_statement_fields (PayrollMainPaystatementFields): Pay
            statement history details
        employer (PayrollEmployerRecord): TODO: type description here.
        employee (PayrollEmployeeRecord): TODO: type description here.
        earnings (list of PayrollEarningsRecord): TODO: type description
            here.
        deductions (list of PayrollDeductionsRecord): TODO: type description
            here.
        direct_deposits (list of PayrollDirectDepositRecord): TODO: type
            description here.
        monthly_income (PayrollMonthlyIncomeRecord): TODO: type description
            here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "payroll_data_as_of_date":'payrollDataAsOfDate',
        "payroll_data_retrieval_id":'payrollDataRetrievalId',
        "payroll_pay_history_id":'payrollPayHistoryId',
        "last_pay_period_indicator":'lastPayPeriodIndicator',
        "main_pay_statement_fields":'mainPayStatementFields',
        "employer":'employer',
        "employee":'employee',
        "deductions":'deductions',
        "direct_deposits":'directDeposits',
        "monthly_income":'monthlyIncome',
        "earnings":'earnings'
    }

    def __init__(self,
                 payroll_data_as_of_date=None,
                 payroll_data_retrieval_id=None,
                 payroll_pay_history_id=None,
                 last_pay_period_indicator=None,
                 main_pay_statement_fields=None,
                 employer=None,
                 employee=None,
                 deductions=None,
                 direct_deposits=None,
                 monthly_income=None,
                 earnings=None,
                 additional_properties = {}):
        """Constructor for the DirectPayStatementFields class"""

        # Initialize members of the class
        self.payroll_data_as_of_date = payroll_data_as_of_date
        self.payroll_data_retrieval_id = payroll_data_retrieval_id
        self.payroll_pay_history_id = payroll_pay_history_id
        self.last_pay_period_indicator = last_pay_period_indicator
        self.main_pay_statement_fields = main_pay_statement_fields
        self.employer = employer
        self.employee = employee
        self.earnings = earnings
        self.deductions = deductions
        self.direct_deposits = direct_deposits
        self.monthly_income = monthly_income

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
        payroll_data_as_of_date = dictionary.get('payrollDataAsOfDate')
        payroll_data_retrieval_id = dictionary.get('payrollDataRetrievalId')
        payroll_pay_history_id = dictionary.get('payrollPayHistoryId')
        last_pay_period_indicator = dictionary.get('lastPayPeriodIndicator')
        main_pay_statement_fields = finicityapi.models.payroll_main_paystatement_fields.PayrollMainPaystatementFields.from_dictionary(dictionary.get('mainPayStatementFields')) if dictionary.get('mainPayStatementFields') else None
        employer = finicityapi.models.payroll_employer_record.PayrollEmployerRecord.from_dictionary(dictionary.get('employer')) if dictionary.get('employer') else None
        employee = finicityapi.models.payroll_employee_record.PayrollEmployeeRecord.from_dictionary(dictionary.get('employee')) if dictionary.get('employee') else None
        deductions = None
        if dictionary.get('deductions') != None:
            deductions = list()
            for structure in dictionary.get('deductions'):
                deductions.append(finicityapi.models.payroll_deductions_record.PayrollDeductionsRecord.from_dictionary(structure))
        direct_deposits = None
        if dictionary.get('directDeposits') != None:
            direct_deposits = list()
            for structure in dictionary.get('directDeposits'):
                direct_deposits.append(finicityapi.models.payroll_direct_deposit_record.PayrollDirectDepositRecord.from_dictionary(structure))
        monthly_income = finicityapi.models.payroll_monthly_income_record.PayrollMonthlyIncomeRecord.from_dictionary(dictionary.get('monthlyIncome')) if dictionary.get('monthlyIncome') else None
        earnings = None
        if dictionary.get('earnings') != None:
            earnings = list()
            for structure in dictionary.get('earnings'):
                earnings.append(finicityapi.models.payroll_earnings_record.PayrollEarningsRecord.from_dictionary(structure))

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(payroll_data_as_of_date,
                   payroll_data_retrieval_id,
                   payroll_pay_history_id,
                   last_pay_period_indicator,
                   main_pay_statement_fields,
                   employer,
                   employee,
                   deductions,
                   direct_deposits,
                   monthly_income,
                   earnings,
                   dictionary)


