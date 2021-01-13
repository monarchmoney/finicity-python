# -*- coding: utf-8 -*-

import finicityapi.models.report_custom_field

class TransactionReportConstraints(object):

    """Implementation of the 'Transaction Report Constraints' model.

    TODO: type model description here.

    Attributes:
        account_ids (list of string): Specific accountIds to be included in
            the new report.
        from_date (long|int): The fromDate parameter is an Epoch Timestamp (in
            seconds), such as “1494449017”.  Without this parameter, the
            report defaults to 6 months if available. Example:
            ?fromDate={fromDate} If included, the epoch timestamp should be 10
            digits long and be within two years of the present day. Extending
            the epoch timestamp beyond 10 digits will default back to six
            months of data.  This query is optional
        to_date (long|int): The ending timestamp for the date range. The value
            must be greater than fromDate. See Handling Dates and Times.
        include_pending (bool): True: Include pending transactions in the
            report. False: Set by default.
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
        "account_ids":'accountIds',
        "from_date":'fromDate',
        "to_date":'toDate',
        "include_pending":'includePending',
        "report_custom_fields":'reportCustomFields'
    }

    def __init__(self,
                 account_ids=None,
                 from_date=None,
                 to_date=None,
                 include_pending=None,
                 report_custom_fields=None,
                 additional_properties = {}):
        """Constructor for the TransactionReportConstraints class"""

        # Initialize members of the class
        self.account_ids = account_ids
        self.from_date = from_date
        self.to_date = to_date
        self.include_pending = include_pending
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
        account_ids = dictionary.get('accountIds')
        from_date = dictionary.get('fromDate')
        to_date = dictionary.get('toDate')
        include_pending = dictionary.get('includePending')
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
        return cls(account_ids,
                   from_date,
                   to_date,
                   include_pending,
                   report_custom_fields,
                   dictionary)


