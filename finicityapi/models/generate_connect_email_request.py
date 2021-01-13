# -*- coding: utf-8 -*-

import finicityapi.models.report_custom_fields
import finicityapi.models.connect_email_options

class GenerateConnectEmailRequest(object):

    """Implementation of the 'Generate Connect Email Request' model.

    TODO: type model description here.

    Attributes:
        partner_id (string): The partner id you can obtain from your Finicity
            developer dashboard
        customer_id (string): Finicity’s customer ID. Obtained from the Add
            Customer call.
        consumer_id (string): Finicity’s consumer ID. Obtained from the Create
            Consumer call. <br> *Required for any connect type that generate a
            report*
        mtype (FinicityConnectTypeEnum): The type of connect flow you want for
            the customer/consumer. Email does not support types aggregation,
            lite and fix. See Finicity Connect Type For Definitions.
        skip_report (bool): Boolean indicating if Connect should generate the
            report at the end of the flow
        from_date (string): The `fromDate` param is an Epoch Timestamp (in
            seconds), such as “1494449017”. Without this param, the report
            defaults to 6 months if available. If included, the epoch
            timestamp should be 10 digits long, and be within two years of the
            present day. Extending the epoch timestamp beyond 10 digits will
            default back to six months of data. This is an optional field for
            use with only “voa” Connect type. The fromDate param should not be
            used with the “voi” Connect type.
        paystubs (string): Enter the value 2 here if the consumer needs to
            upload the 2 most recent pay statements. Applicable only for VOIE
            products.
        redirect_uri (string): The url that customers will be redirected to
            after completing Finicity Connect. <br> *Required unless Connect
            is embedded inside your application. (iframe)*
        webhook (string): The publicly available URL you wish to be notified
            with events as the user progresses through the application. See
            [Connect Webhook
            Event](https://docs-new.finicitydev.com/connect-webhooks/) for
            event details.
        webhook_content_type (string): The Content Type The Webhooks Events
            Will Be Sent In. Supported Types `application/json` and
            `application/xml`
        webhook_data (object): Allows additional identifiable information to
            be inserted into the payload of connect webhook events. See this
            article for
            [Details](https://docs-new.finicitydev.com/connect-custom-webhook-d
            ata-and-headers/).
        webhook_headers (object): Allows additional identifiable information
            to be included as headers of connect webhook event. See this
            article for
            [Details](https://docs-new.finicitydev.com/connect-custom-webhook-d
            ata-and-headers/).
        institution_settings (object): Advanced options for configuration of
            which institutions to display in. See this article for
            [Details](https://docs-new.finicitydev.com/connect-institutions-opt
            ions/)
        report_custom_fields (list of ReportCustomFields): Designate up to 5
            custom fields that you would like associated with the report upon
            generation by providing a label for the field and a value for the
            field.  Set the shown variable to true if you want the custom
            field to display in the JSON, XML, and PDF reports. Set the shown
            variable to false if you do not wish to see this field in the
            report. All custom fields will display in the Reseller Billing
            endpoint.   This is optional.
        analytics (string): Google Analytics or Adobe Analytics can be used
            with Connect to provide an additional layer of transparency of end
            user engagement. This is optional.
        email (ConnectEmailOptions): Customizable email details

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "partner_id":'partnerId',
        "customer_id":'customerId',
        "mtype":'type',
        "email":'email',
        "consumer_id":'consumerId',
        "skip_report":'skipReport',
        "from_date":'fromDate',
        "paystubs":'paystubs',
        "redirect_uri":'redirectUri',
        "webhook":'webhook',
        "webhook_content_type":'webhookContentType',
        "webhook_data":'webhookData',
        "webhook_headers":'webhookHeaders',
        "institution_settings":'institutionSettings',
        "report_custom_fields":'reportCustomFields',
        "analytics":'analytics'
    }

    def __init__(self,
                 partner_id=None,
                 customer_id=None,
                 mtype=None,
                 email=None,
                 consumer_id=None,
                 skip_report=False,
                 from_date=None,
                 paystubs=None,
                 redirect_uri=None,
                 webhook=None,
                 webhook_content_type='application/json',
                 webhook_data=None,
                 webhook_headers=None,
                 institution_settings=None,
                 report_custom_fields=None,
                 analytics=None,
                 additional_properties = {}):
        """Constructor for the GenerateConnectEmailRequest class"""

        # Initialize members of the class
        self.partner_id = partner_id
        self.customer_id = customer_id
        self.consumer_id = consumer_id
        self.mtype = mtype
        self.skip_report = skip_report
        self.from_date = from_date
        self.paystubs = paystubs
        self.redirect_uri = redirect_uri
        self.webhook = webhook
        self.webhook_content_type = webhook_content_type
        self.webhook_data = webhook_data
        self.webhook_headers = webhook_headers
        self.institution_settings = institution_settings
        self.report_custom_fields = report_custom_fields
        self.analytics = analytics
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
        customer_id = dictionary.get('customerId')
        mtype = dictionary.get('type')
        email = finicityapi.models.connect_email_options.ConnectEmailOptions.from_dictionary(dictionary.get('email')) if dictionary.get('email') else None
        consumer_id = dictionary.get('consumerId')
        skip_report = dictionary.get("skipReport") if dictionary.get("skipReport") else False
        from_date = dictionary.get('fromDate')
        paystubs = dictionary.get('paystubs')
        redirect_uri = dictionary.get('redirectUri')
        webhook = dictionary.get('webhook')
        webhook_content_type = dictionary.get("webhookContentType") if dictionary.get("webhookContentType") else 'application/json'
        webhook_data = dictionary.get('webhookData')
        webhook_headers = dictionary.get('webhookHeaders')
        institution_settings = dictionary.get('institutionSettings')
        report_custom_fields = None
        if dictionary.get('reportCustomFields') != None:
            report_custom_fields = list()
            for structure in dictionary.get('reportCustomFields'):
                report_custom_fields.append(finicityapi.models.report_custom_fields.ReportCustomFields.from_dictionary(structure))
        analytics = dictionary.get('analytics')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(partner_id,
                   customer_id,
                   mtype,
                   email,
                   consumer_id,
                   skip_report,
                   from_date,
                   paystubs,
                   redirect_uri,
                   webhook,
                   webhook_content_type,
                   webhook_data,
                   webhook_headers,
                   institution_settings,
                   report_custom_fields,
                   analytics,
                   dictionary)


