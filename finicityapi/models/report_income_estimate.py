# -*- coding: utf-8 -*-


class ReportIncomeEstimate(object):

    """Implementation of the 'Report Income Estimate' model.

    Report Income Estimate

    Attributes:
        net_annual (float): TODO: type description here.
        projected_net_annual (float): TODO: type description here.
        estimated_gross_annual (float): TODO: type description here.
        projected_gross_annual (float): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "net_annual":'netAnnual',
        "projected_net_annual":'projectedNetAnnual',
        "estimated_gross_annual":'estimatedGrossAnnual',
        "projected_gross_annual":'projectedGrossAnnual'
    }

    def __init__(self,
                 net_annual=None,
                 projected_net_annual=None,
                 estimated_gross_annual=None,
                 projected_gross_annual=None,
                 additional_properties = {}):
        """Constructor for the ReportIncomeEstimate class"""

        # Initialize members of the class
        self.net_annual = net_annual
        self.projected_net_annual = projected_net_annual
        self.estimated_gross_annual = estimated_gross_annual
        self.projected_gross_annual = projected_gross_annual

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
        net_annual = dictionary.get('netAnnual')
        projected_net_annual = dictionary.get('projectedNetAnnual')
        estimated_gross_annual = dictionary.get('estimatedGrossAnnual')
        projected_gross_annual = dictionary.get('projectedGrossAnnual')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(net_annual,
                   projected_net_annual,
                   estimated_gross_annual,
                   projected_gross_annual,
                   dictionary)


