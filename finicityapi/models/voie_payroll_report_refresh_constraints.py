# -*- coding: utf-8 -*-

import finicityapi.models.payroll_provider_refresh_data
import finicityapi.models.report_custom_field

class VOIEPayrollReportRefreshConstraints(object):

    """Implementation of the 'VOIE - Payroll Report Refresh Constraints' model.

    TODO: type model description here.

    Attributes:
        payroll_provider_data (list of PayrollProviderRefreshData): TODO: type
            description here.
        report_custom_fields (list of ReportCustomField): Designate up to 5
            custom fields that you would like associated with the report upon
            generation by providing a label for the field and a value for the
            field. Set the shown variable to true if you want the custom field
            to display in the PDF reports. Set the shown variable to false to
            limit seeing the variable to JSON, XML report but not in the PDF
            report. All custom fields will display in the Reseller Billing
            endpoint.  This is optional.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "payroll_provider_data":'payrollProviderData',
        "report_custom_fields":'reportCustomFields'
    }

    def __init__(self,
                 payroll_provider_data=None,
                 report_custom_fields=None,
                 additional_properties = {}):
        """Constructor for the VOIEPayrollReportRefreshConstraints class"""

        # Initialize members of the class
        self.payroll_provider_data = payroll_provider_data
        self.report_custom_fields = report_custom_fields

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
        payroll_provider_data = None
        if dictionary.get('payrollProviderData') != None:
            payroll_provider_data = list()
            for structure in dictionary.get('payrollProviderData'):
                payroll_provider_data.append(finicityapi.models.payroll_provider_refresh_data.PayrollProviderRefreshData.from_dictionary(structure))
        report_custom_fields = None
        if dictionary.get('reportCustomFields') != None:
            report_custom_fields = list()
            for structure in dictionary.get('reportCustomFields'):
                report_custom_fields.append(finicityapi.models.report_custom_field.ReportCustomField.from_dictionary(structure))

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(payroll_provider_data,
                   report_custom_fields,
                   dictionary)


