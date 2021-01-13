# -*- coding: utf-8 -*-

import finicityapi.models.connect_oauth_options
import finicityapi.models.report_custom_fields
import finicityapi.models.connect_email_options

class GenerateConnectEmailRequestMultipleBorrowers(object):

    """Implementation of the 'Generate Connect Email Request Multiple Borrowers' model.

    TODO: type model description here.

    Attributes:
        partner_id (string): The partner id you can obtain from your Finicity
            developer dashboard
        customers (list of object): The customers' information
        redirect_uri (string): The url that customers will be redirected to
            after completing Finicity Connect.
        mtype (string): The report type you wish to have generated for you.
            Valid types include ‘voa’, ‘voi’, and ‘aggregation’
        webhook (string): The publicly available url you wish to be posted to
            when the user starts Finicity Connect, and completes, it etc. 
            This is an optional field
        webhook_content_type (string): The format of the data you wish to be
            posted to your server. Valid values are ‘application/json’ and
            ‘application/xml’ This field is optional.
        webhook_data (object): Allows additional identifiable information to
            be inserted into webhooks (value1, value2, etc.). Alternative
            naming conventions may be desired in place of value1, value2 for
            specific values (e.g. loanNumber, currentDate, etc.) This field is
            optional.
        webhook_headers (object): Headers to be included with webhook events
        institution_id (int): Institution id (required for type=lite)
        oauth_options (ConnectOauthOptions): oauthOptions for oauthEnabled
            institutions
        report_custom_fields (list of ReportCustomFields): Designate up to 5
            custom fields that you would like associated with the report upon
            generation by providing a label for the field and a value for the
            field.  Set the shown variable to true if you want the custom
            field to display in the JSON, XML, and PDF reports. Set the shown
            variable to false if you do not wish to see this field in the
            report. All custom fields will display in the Reseller Billing
            endpoint.   This is optional.
        analytics (string): Google Analytics can be used with Connect to
            provide an additional layer of transparency of end user
            engagement. This field is optional
        skip_report (bool): Boolean indicating if Connect should generate the
            report
        email (ConnectEmailOptions): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "partner_id":'partnerId',
        "customers":'customers',
        "mtype":'type',
        "redirect_uri":'redirectUri',
        "webhook":'webhook',
        "webhook_content_type":'webhookContentType',
        "webhook_data":'webhookData',
        "webhook_headers":'webhookHeaders',
        "institution_id":'institutionId',
        "oauth_options":'oauthOptions',
        "report_custom_fields":'reportCustomFields',
        "analytics":'analytics',
        "skip_report":'skipReport',
        "email":'email'
    }

    def __init__(self,
                 partner_id=None,
                 customers=None,
                 mtype=None,
                 redirect_uri=None,
                 webhook=None,
                 webhook_content_type=None,
                 webhook_data=None,
                 webhook_headers=None,
                 institution_id=None,
                 oauth_options=None,
                 report_custom_fields=None,
                 analytics=None,
                 skip_report=None,
                 email=None,
                 additional_properties = {}):
        """Constructor for the GenerateConnectEmailRequestMultipleBorrowers class"""

        # Initialize members of the class
        self.partner_id = partner_id
        self.customers = customers
        self.redirect_uri = redirect_uri
        self.mtype = mtype
        self.webhook = webhook
        self.webhook_content_type = webhook_content_type
        self.webhook_data = webhook_data
        self.webhook_headers = webhook_headers
        self.institution_id = institution_id
        self.oauth_options = oauth_options
        self.report_custom_fields = report_custom_fields
        self.analytics = analytics
        self.skip_report = skip_report
        self.email = email

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
        partner_id = dictionary.get('partnerId')
        customers = dictionary.get('customers')
        mtype = dictionary.get('type')
        redirect_uri = dictionary.get('redirectUri')
        webhook = dictionary.get('webhook')
        webhook_content_type = dictionary.get('webhookContentType')
        webhook_data = dictionary.get('webhookData')
        webhook_headers = dictionary.get('webhookHeaders')
        institution_id = dictionary.get('institutionId')
        oauth_options = finicityapi.models.connect_oauth_options.ConnectOauthOptions.from_dictionary(dictionary.get('oauthOptions')) if dictionary.get('oauthOptions') else None
        report_custom_fields = None
        if dictionary.get('reportCustomFields') != None:
            report_custom_fields = list()
            for structure in dictionary.get('reportCustomFields'):
                report_custom_fields.append(finicityapi.models.report_custom_fields.ReportCustomFields.from_dictionary(structure))
        analytics = dictionary.get('analytics')
        skip_report = dictionary.get('skipReport')
        email = finicityapi.models.connect_email_options.ConnectEmailOptions.from_dictionary(dictionary.get('email')) if dictionary.get('email') else None

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(partner_id,
                   customers,
                   mtype,
                   redirect_uri,
                   webhook,
                   webhook_content_type,
                   webhook_data,
                   webhook_headers,
                   institution_id,
                   oauth_options,
                   report_custom_fields,
                   analytics,
                   skip_report,
                   email,
                   dictionary)


