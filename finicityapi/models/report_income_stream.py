# -*- coding: utf-8 -*-

import finicityapi.models.cadence_details
import finicityapi.models.net_monthly
import finicityapi.models.report_transaction

class ReportIncomeStream(object):

    """Implementation of the 'Report Income Stream' model.

    TODO: type model description here.

    Attributes:
        id (string): Finicity’s income stream ID
        name (string): A human-readable name based on the normalizedPayee name
            of the transactions for this income stream
        status (StatusEnum): active or inactive
        estimate_inclusion (EstimateInclusionEnum): TODO: type description
            here.
        confidence (int): Level of confidence that the deposit stream
            represents income (example: 85%)
        cadence (CadenceDetails): TODO: type description here.
        net_monthly (list of NetMonthly): A list of net monthly records. One
            instance for each complete calendar month in the report
        net_annual (float): Sum of all values in netMonthlyIncome over the
            previous 12 months
        projected_net_annual (float): Projected net income over the next 12
            months, across all income streams, based on netAnnualIncome
        estimated_gross_annual (float): Before-tax gross annual income
            (estimated from netAnnual) across all income stream in the past 12
            months
        projected_gross_annual (float): Projected gross income over the next
            12 months, across all active income streams, based on
            projectedNetAnnual
        average_monthly_income_net (float): Monthly average amount over the
            previous 24 months
        transactions (list of ReportTransaction): A list of transaction
            records

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id":'id',
        "name":'name',
        "status":'status',
        "estimate_inclusion":'estimateInclusion',
        "confidence":'confidence',
        "cadence":'cadence',
        "net_monthly":'netMonthly',
        "net_annual":'netAnnual',
        "projected_net_annual":'projectedNetAnnual',
        "estimated_gross_annual":'estimatedGrossAnnual',
        "projected_gross_annual":'projectedGrossAnnual',
        "average_monthly_income_net":'averageMonthlyIncomeNet',
        "transactions":'transactions'
    }

    def __init__(self,
                 id=None,
                 name=None,
                 status=None,
                 estimate_inclusion=None,
                 confidence=None,
                 cadence=None,
                 net_monthly=None,
                 net_annual=None,
                 projected_net_annual=None,
                 estimated_gross_annual=None,
                 projected_gross_annual=None,
                 average_monthly_income_net=None,
                 transactions=None,
                 additional_properties = {}):
        """Constructor for the ReportIncomeStream class"""

        # Initialize members of the class
        self.id = id
        self.name = name
        self.status = status
        self.estimate_inclusion = estimate_inclusion
        self.confidence = confidence
        self.cadence = cadence
        self.net_monthly = net_monthly
        self.net_annual = net_annual
        self.projected_net_annual = projected_net_annual
        self.estimated_gross_annual = estimated_gross_annual
        self.projected_gross_annual = projected_gross_annual
        self.average_monthly_income_net = average_monthly_income_net
        self.transactions = transactions

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
        name = dictionary.get('name')
        status = dictionary.get('status')
        estimate_inclusion = dictionary.get('estimateInclusion')
        confidence = dictionary.get('confidence')
        cadence = finicityapi.models.cadence_details.CadenceDetails.from_dictionary(dictionary.get('cadence')) if dictionary.get('cadence') else None
        net_monthly = None
        if dictionary.get('netMonthly') != None:
            net_monthly = list()
            for structure in dictionary.get('netMonthly'):
                net_monthly.append(finicityapi.models.net_monthly.NetMonthly.from_dictionary(structure))
        net_annual = dictionary.get('netAnnual')
        projected_net_annual = dictionary.get('projectedNetAnnual')
        estimated_gross_annual = dictionary.get('estimatedGrossAnnual')
        projected_gross_annual = dictionary.get('projectedGrossAnnual')
        average_monthly_income_net = dictionary.get('averageMonthlyIncomeNet')
        transactions = None
        if dictionary.get('transactions') != None:
            transactions = list()
            for structure in dictionary.get('transactions'):
                transactions.append(finicityapi.models.report_transaction.ReportTransaction.from_dictionary(structure))

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(id,
                   name,
                   status,
                   estimate_inclusion,
                   confidence,
                   cadence,
                   net_monthly,
                   net_annual,
                   projected_net_annual,
                   estimated_gross_annual,
                   projected_gross_annual,
                   average_monthly_income_net,
                   transactions,
                   dictionary)


