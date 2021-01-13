# -*- coding: utf-8 -*-

import finicityapi.models.report_summary

class ReportSummaries(object):

    """Implementation of the 'Report Summaries' model.

    TODO: type model description here.

    Attributes:
        reports (list of ReportSummary): Data pertaining to each report

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "reports":'reports'
    }

    def __init__(self,
                 reports=None,
                 additional_properties = {}):
        """Constructor for the ReportSummaries class"""

        # Initialize members of the class
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
        reports = None
        if dictionary.get('reports') != None:
            reports = list()
            for structure in dictionary.get('reports'):
                reports.append(finicityapi.models.report_summary.ReportSummary.from_dictionary(structure))

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(reports,
                   dictionary)


