# -*- coding: utf-8 -*-

import finicityapi.models.employer
import finicityapi.models.employee
import finicityapi.models.pay_stat
import finicityapi.models.deduction
import finicityapi.models.direct_deposit
import finicityapi.models.paystub_monthly_income_record
import finicityapi.models.voie_txverify_report_institution

class VOIETxverifyPayStatement(object):

    """Implementation of the 'VOIE TXVerify Pay Statement' model.

    TODO: type model description here.

    Attributes:
        pay_period (string): The pay period of the pay statement.
        billable (bool): This will display true if the pay statement is
            billable. If a pay statement has been digitized previously, this
            will display as false as it will not be billable.
        asset_id (string): The asset ID of the stored pay statement
        pay_date (long|int): The listed pay date for the pay statement.
        start_date (long|int): The beginning of the pay period.
        end_date (long|int): The end of the pay period.
        net_pay_current (float): The total pay after deductions for the
            employee for the current pay period.
        net_pay_ytd (float): The total accumulation of pay after deductions
            for the employee for the current pay year.
        gross_pay_current (float): The total pay before deductions for the
            employee for the current pay period.
        gross_pay_ytd (float): The total accumulation of pay before deductions
            for the employee for the current pay year.
        payroll_provider (string): The payroll provider extracted from the pay
            statement.
        match_type (PayStatementMatchTypesEnum): This denotes the match type
            associated with the pay statement.
        employer (Employer): Information pertaining to the employer
        employee (Employee): Information pertaining to the employee
        pay_stat (list of PayStat): Information pertaining to the earnings on
            the pay statement
        deductions (list of Deduction): Information pertaining to the
            deductions on the pay statement
        direct_deposits (list of DirectDeposit): Information pertaining to the
            direct deposits on the pay statement
        monthly_income (PaystubMonthlyIncomeRecord): TODO: type description
            here.
        institutions (list of VOIETxverifyReportInstitution): TODO: type
            description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "pay_period":'payPeriod',
        "billable":'billable',
        "asset_id":'assetId',
        "pay_date":'payDate',
        "start_date":'startDate',
        "end_date":'endDate',
        "net_pay_current":'netPayCurrent',
        "net_pay_ytd":'netPayYTD',
        "gross_pay_current":'grossPayCurrent',
        "gross_pay_ytd":'grossPayYTD',
        "payroll_provider":'payrollProvider',
        "match_type":'matchType',
        "employer":'employer',
        "employee":'employee',
        "pay_stat":'payStat',
        "deductions":'deductions',
        "direct_deposits":'directDeposits',
        "monthly_income":'monthlyIncome',
        "institutions":'institutions'
    }

    def __init__(self,
                 pay_period=None,
                 billable=None,
                 asset_id=None,
                 pay_date=None,
                 start_date=None,
                 end_date=None,
                 net_pay_current=None,
                 net_pay_ytd=None,
                 gross_pay_current=None,
                 gross_pay_ytd=None,
                 payroll_provider=None,
                 match_type=None,
                 employer=None,
                 employee=None,
                 pay_stat=None,
                 deductions=None,
                 direct_deposits=None,
                 monthly_income=None,
                 institutions=None,
                 additional_properties = {}):
        """Constructor for the VOIETxverifyPayStatement class"""

        # Initialize members of the class
        self.pay_period = pay_period
        self.billable = billable
        self.asset_id = asset_id
        self.pay_date = pay_date
        self.start_date = start_date
        self.end_date = end_date
        self.net_pay_current = net_pay_current
        self.net_pay_ytd = net_pay_ytd
        self.gross_pay_current = gross_pay_current
        self.gross_pay_ytd = gross_pay_ytd
        self.payroll_provider = payroll_provider
        self.match_type = match_type
        self.employer = employer
        self.employee = employee
        self.pay_stat = pay_stat
        self.deductions = deductions
        self.direct_deposits = direct_deposits
        self.monthly_income = monthly_income
        self.institutions = institutions

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
        pay_period = dictionary.get('payPeriod')
        billable = dictionary.get('billable')
        asset_id = dictionary.get('assetId')
        pay_date = dictionary.get('payDate')
        start_date = dictionary.get('startDate')
        end_date = dictionary.get('endDate')
        net_pay_current = dictionary.get('netPayCurrent')
        net_pay_ytd = dictionary.get('netPayYTD')
        gross_pay_current = dictionary.get('grossPayCurrent')
        gross_pay_ytd = dictionary.get('grossPayYTD')
        payroll_provider = dictionary.get('payrollProvider')
        match_type = dictionary.get('matchType')
        employer = finicityapi.models.employer.Employer.from_dictionary(dictionary.get('employer')) if dictionary.get('employer') else None
        employee = finicityapi.models.employee.Employee.from_dictionary(dictionary.get('employee')) if dictionary.get('employee') else None
        pay_stat = None
        if dictionary.get('payStat') != None:
            pay_stat = list()
            for structure in dictionary.get('payStat'):
                pay_stat.append(finicityapi.models.pay_stat.PayStat.from_dictionary(structure))
        deductions = None
        if dictionary.get('deductions') != None:
            deductions = list()
            for structure in dictionary.get('deductions'):
                deductions.append(finicityapi.models.deduction.Deduction.from_dictionary(structure))
        direct_deposits = None
        if dictionary.get('directDeposits') != None:
            direct_deposits = list()
            for structure in dictionary.get('directDeposits'):
                direct_deposits.append(finicityapi.models.direct_deposit.DirectDeposit.from_dictionary(structure))
        monthly_income = finicityapi.models.paystub_monthly_income_record.PaystubMonthlyIncomeRecord.from_dictionary(dictionary.get('monthlyIncome')) if dictionary.get('monthlyIncome') else None
        institutions = None
        if dictionary.get('institutions') != None:
            institutions = list()
            for structure in dictionary.get('institutions'):
                institutions.append(finicityapi.models.voie_txverify_report_institution.VOIETxverifyReportInstitution.from_dictionary(structure))

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(pay_period,
                   billable,
                   asset_id,
                   pay_date,
                   start_date,
                   end_date,
                   net_pay_current,
                   net_pay_ytd,
                   gross_pay_current,
                   gross_pay_ytd,
                   payroll_provider,
                   match_type,
                   employer,
                   employee,
                   pay_stat,
                   deductions,
                   direct_deposits,
                   monthly_income,
                   institutions,
                   dictionary)


