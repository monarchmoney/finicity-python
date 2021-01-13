# -*- coding: utf-8 -*-

import finicityapi.models.portfolio_consumer
import finicityapi.models.portfolio_report

class PortfolioSummary(object):

    """Implementation of the 'Portfolio Summary' model.

    TODO: type model description here.

    Attributes:
        portfolio_id (string): A unique identifier that will be consistent
            across all reports created for the same customer.
        consumer (PortfolioConsumer): Information pertaining to the consumer
        reports (list of PortfolioReport): A list of reports in the portfolio

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "portfolio_id":'portfolioId',
        "consumer":'consumer',
        "reports":'reports'
    }

    def __init__(self,
                 portfolio_id=None,
                 consumer=None,
                 reports=None,
                 additional_properties = {}):
        """Constructor for the PortfolioSummary class"""

        # Initialize members of the class
        self.portfolio_id = portfolio_id
        self.consumer = consumer
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
        consumer = finicityapi.models.portfolio_consumer.PortfolioConsumer.from_dictionary(dictionary.get('consumer')) if dictionary.get('consumer') else None
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
                   consumer,
                   reports,
                   dictionary)


