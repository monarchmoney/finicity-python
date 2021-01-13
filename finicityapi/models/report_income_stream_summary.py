# -*- coding: utf-8 -*-

import finicityapi.models.net_monthly
import finicityapi.models.report_income_estimate

class ReportIncomeStreamSummary(object):

    """Implementation of the 'Report Income Stream Summary' model.

    ReportIncomeStreamSummary

    Attributes:
        confidence_type (EstimateInclusionEnum): TODO: type description here.
        net_monthly (list of NetMonthly): TODO: type description here.
        income_estimate (ReportIncomeEstimate): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "confidence_type":'confidenceType',
        "net_monthly":'netMonthly',
        "income_estimate":'incomeEstimate'
    }

    def __init__(self,
                 confidence_type=None,
                 net_monthly=None,
                 income_estimate=None,
                 additional_properties = {}):
        """Constructor for the ReportIncomeStreamSummary class"""

        # Initialize members of the class
        self.confidence_type = confidence_type
        self.net_monthly = net_monthly
        self.income_estimate = income_estimate

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
        confidence_type = dictionary.get('confidenceType')
        net_monthly = None
        if dictionary.get('netMonthly') != None:
            net_monthly = list()
            for structure in dictionary.get('netMonthly'):
                net_monthly.append(finicityapi.models.net_monthly.NetMonthly.from_dictionary(structure))
        income_estimate = finicityapi.models.report_income_estimate.ReportIncomeEstimate.from_dictionary(dictionary.get('incomeEstimate')) if dictionary.get('incomeEstimate') else None

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(confidence_type,
                   net_monthly,
                   income_estimate,
                   dictionary)


