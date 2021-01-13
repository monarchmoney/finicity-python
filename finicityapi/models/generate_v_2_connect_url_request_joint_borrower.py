# -*- coding: utf-8 -*-

import finicityapi.models.borrowers
import finicityapi.models.report_custom_fields

class GenerateV2ConnectURLRequestJointBorrower(object):

    """Implementation of the 'Generate V2 Connect URL Request - Joint Borrower' model.

    TODO: type model description here.

    Attributes:
        partner_id (string): The partner id you can obtain from your Finicity
            developer dashboard
        borrowers (list of Borrowers): (MVS) Array of borrowers to pass the
            primary and joint borrower’s customer and consumer IDs.
        redirect_uri (string): The url that customers will be redirected to
            after completing Finicity Connect. <br> *Required unless Connect
            is embedded inside your application. (iframe)*
        webhook (string): The publicly available URL you want to be notified
            with events as the user progresses through the application. See
            [Connect Webhook
            Event](https://docs.finicity.com/connect-webhooks/) for event
            details.
        webhook_content_type (string): The Content Type The Webhooks Events
            Will Be Sent In. Supported Types `application/json` and
            `application/xml`
        webhook_data (object): Allows additional identifiable information to
            be inserted into the payload of connect webhook events. See this
            article for
            [Details](https://docs.finicity.com/connect-custom-webhook-data-and
            -headers/).
        webhook_headers (object): Allows additional identifiable information
            to be included as headers of connect webhook event. See this
            article for
            [Details](https://docs.finicity.com/connect-custom-webhook-data-and
            -headers/).
        institution_settings (object): Advanced options for configuration of
            which institutions to display in. See [Institution
            Settings](https://docs.finicity.com/connect-institution-settings/)
                    experience (string): The `experience` field allows you to customize:
            <br> * **Brand**: color and logo <br> * **Icon**: displayed on the
            Share your data page <br> * **Popular institutions**: displayed on
            the Bank Search page <br> * **Report**: the credit decisioning
            report to send when Connect completes. <br> * **MVS modules**:
            financial, payroll, paystub <br>      <br>**Note**: The Finicity
            sales engineers (SE) help you set up a default experience for your
            company when you migrate to Connect 2.0. For each additional
            experience you create thereafter, they’ll give you a unique ID.
            See [Generate 2.0 Connect URL
            APIs](https://docs.finicity.com/migrate-to-connect-web-sdk-2-0/#mig
            rate-connect-web-sdk-1) <br>       <br>**Experience values
            options**: <br> * **default**: your default experience <br> *
            **unique ID**: the code for a different experience<br> * **not
            defined**: If you don’t pass the experience parameter, then
            Connect’s out of the box default experience (add accounts but no
            branding) is used. <br>
        from_date (long|int): The `fromDate` parameter is used when
            experiences are associated with a credit decisioning report and
            any other reports with transaction data. <br> The value is in
            epoch time and must be 10 digits. **Example**: 1494449017. <br> 
            <br>If it’s greater than 10 digits, then the `fromDate` is set to
            the credit decisioning report’s default `fromDate`.<br>  <br>For
            an experience that generates multiple reports the `fromDate` gets
            passed to the reports that support it. Although, the `fromDate`
            isn’t used in these reports:<br> * Pay Statement Extraction Report
            <br> * Statement Report <br> * Verification of Income Report  <br>
            * VOIE - Payroll Report  <br> <br>**Note**: this field isn’t used
            if you’re only collecting transaction data without a report, or
            for experiences with only reports without transaction data (like
            the ones mentioned above)..
        report_custom_fields (list of ReportCustomFields): The
            `reportCustomFields` parameter is used when experiences are
            associated with a credit decisioning report. <br>  <br>Designate
            up to 5 custom fields that you’d like associated with the report
            when it’s generated. Every custom field consists of three
            variables: `label`, `value`, and `shown`. The `shown` variable is
            true or false. <br>* **True**: (default) display the custom field
            in the PDF report. <br>  <br>* **False**: don’t display the custom
            field in the PDF report. <br>  <br>For an experience that
            generates multiple reports, the `reportCustomFields` parameter
            gets passed to all reports.<br>  <br>All custom fields display in
            the Reseller Billing endpoint.<br>

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "partner_id":'partnerId',
        "borrowers":'borrowers',
        "redirect_uri":'redirectUri',
        "webhook":'webhook',
        "webhook_content_type":'webhookContentType',
        "webhook_data":'webhookData',
        "webhook_headers":'webhookHeaders',
        "institution_settings":'institutionSettings',
        "experience":'experience',
        "from_date":'fromDate',
        "report_custom_fields":'reportCustomFields'
    }

    def __init__(self,
                 partner_id=None,
                 borrowers=None,
                 redirect_uri=None,
                 webhook=None,
                 webhook_content_type='application/json',
                 webhook_data=None,
                 webhook_headers=None,
                 institution_settings=None,
                 experience=None,
                 from_date=None,
                 report_custom_fields=None,
                 additional_properties = {}):
        """Constructor for the GenerateV2ConnectURLRequestJointBorrower class"""

        # Initialize members of the class
        self.partner_id = partner_id
        self.borrowers = borrowers
        self.redirect_uri = redirect_uri
        self.webhook = webhook
        self.webhook_content_type = webhook_content_type
        self.webhook_data = webhook_data
        self.webhook_headers = webhook_headers
        self.institution_settings = institution_settings
        self.experience = experience
        self.from_date = from_date
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
        partner_id = dictionary.get('partnerId')
        borrowers = None
        if dictionary.get('borrowers') != None:
            borrowers = list()
            for structure in dictionary.get('borrowers'):
                borrowers.append(finicityapi.models.borrowers.Borrowers.from_dictionary(structure))
        redirect_uri = dictionary.get('redirectUri')
        webhook = dictionary.get('webhook')
        webhook_content_type = dictionary.get("webhookContentType") if dictionary.get("webhookContentType") else 'application/json'
        webhook_data = dictionary.get('webhookData')
        webhook_headers = dictionary.get('webhookHeaders')
        institution_settings = dictionary.get('institutionSettings')
        experience = dictionary.get('experience')
        from_date = dictionary.get('fromDate')
        report_custom_fields = None
        if dictionary.get('reportCustomFields') != None:
            report_custom_fields = list()
            for structure in dictionary.get('reportCustomFields'):
                report_custom_fields.append(finicityapi.models.report_custom_fields.ReportCustomFields.from_dictionary(structure))

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(partner_id,
                   borrowers,
                   redirect_uri,
                   webhook,
                   webhook_content_type,
                   webhook_data,
                   webhook_headers,
                   institution_settings,
                   experience,
                   from_date,
                   report_custom_fields,
                   dictionary)


