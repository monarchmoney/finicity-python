# -*- coding: utf-8 -*-

import finicityapi.models.report_custom_field_1

class Content(object):

    """Implementation of the 'Content' model.

    TODO: type model description here.

    Attributes:
        reseller (string): TODO: type description here.
        reseller_provider (string): TODO: type description here.
        platform_provider (string): TODO: type description here.
        customer_id (int): TODO: type description here.
        consumer_id (string): TODO: type description here.
        consumer_ssn (string): TODO: type description here.
        first_name (string): TODO: type description here.
        last_name (string): TODO: type description here.
        last_four_report_id (string): TODO: type description here.
        created_date (int): TODO: type description here.
        report_type (string): TODO: type description here.
        report_custom_fields (list of ReportCustomField1): TODO: type
            description here.
        status (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "customer_id":'customerId',
        "consumer_id":'consumerId',
        "consumer_ssn":'consumerSsn',
        "first_name":'firstName',
        "last_name":'lastName',
        "last_four_report_id":'lastFourReportId',
        "created_date":'createdDate',
        "report_type":'reportType',
        "report_custom_fields":'reportCustomFields',
        "reseller":'reseller',
        "reseller_provider":'resellerProvider',
        "platform_provider":'platformProvider',
        "status":'status'
    }

    def __init__(self,
                 customer_id=None,
                 consumer_id=None,
                 consumer_ssn=None,
                 first_name=None,
                 last_name=None,
                 last_four_report_id=None,
                 created_date=None,
                 report_type=None,
                 report_custom_fields=None,
                 reseller=None,
                 reseller_provider=None,
                 platform_provider=None,
                 status=None,
                 additional_properties = {}):
        """Constructor for the Content class"""

        # Initialize members of the class
        self.reseller = reseller
        self.reseller_provider = reseller_provider
        self.platform_provider = platform_provider
        self.customer_id = customer_id
        self.consumer_id = consumer_id
        self.consumer_ssn = consumer_ssn
        self.first_name = first_name
        self.last_name = last_name
        self.last_four_report_id = last_four_report_id
        self.created_date = created_date
        self.report_type = report_type
        self.report_custom_fields = report_custom_fields
        self.status = status

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
        customer_id = dictionary.get('customerId')
        consumer_id = dictionary.get('consumerId')
        consumer_ssn = dictionary.get('consumerSsn')
        first_name = dictionary.get('firstName')
        last_name = dictionary.get('lastName')
        last_four_report_id = dictionary.get('lastFourReportId')
        created_date = dictionary.get('createdDate')
        report_type = dictionary.get('reportType')
        report_custom_fields = None
        if dictionary.get('reportCustomFields') != None:
            report_custom_fields = list()
            for structure in dictionary.get('reportCustomFields'):
                report_custom_fields.append(finicityapi.models.report_custom_field_1.ReportCustomField1.from_dictionary(structure))
        reseller = dictionary.get('reseller')
        reseller_provider = dictionary.get('resellerProvider')
        platform_provider = dictionary.get('platformProvider')
        status = dictionary.get('status')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(customer_id,
                   consumer_id,
                   consumer_ssn,
                   first_name,
                   last_name,
                   last_four_report_id,
                   created_date,
                   report_type,
                   report_custom_fields,
                   reseller,
                   reseller_provider,
                   platform_provider,
                   status,
                   dictionary)


