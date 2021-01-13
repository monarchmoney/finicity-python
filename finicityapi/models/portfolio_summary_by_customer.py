# -*- coding: utf-8 -*-

import finicityapi.models.portfolio_report

class PortfolioSummaryByCustomer(object):

    """Implementation of the 'Portfolio Summary By Customer' model.

    TODO: type model description here.

    Attributes:
        portfolio_id (string): A unique identifier that will be consistent
            across all reports created for the same customer.
        reports (list of PortfolioReport): A list of reports in the portfolio

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "portfolio_id":'portfolioId',
        "reports":'reports'
    }

    def __init__(self,
                 portfolio_id=None,
                 reports=None,
                 additional_properties = {}):
        """Constructor for the PortfolioSummaryByCustomer class"""

        # Initialize members of the class
        self.portfolio_id = portfolio_id
        self.reports = reports

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
        portfolio_id = dictionary.get('portfolioId')
        reports = None
        if dictionary.get('reports') != None:
            reports = list()
            for structure in dictionary.get('reports'):
                reports.append(finicityapi.models.portfolio_report.PortfolioReport.from_dictionary(structure))

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(portfolio_id,
                   reports,
                   dictionary)


