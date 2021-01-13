# -*- coding: utf-8 -*-


class GenerateConnectURLRequestFix(object):

    """Implementation of the 'Generate Connect URL Request (fix)' model.

    TODO: type model description here.

    Attributes:
        partner_id (string): The partner id you can obtain from your Finicity
            developer dashboard
        customer_id (string): Finicity’s customer ID. Obtained from the Add
            Customer call.
        mtype (FinicityConnectTypeEnum): The type of connect flow you want for
            the customer/consumer. See Finicity Connect Type For Definitions.
        institution_login_id (string): The institutionLoginId for the account
            record. Used in type “fix” in order to pull up a fix flow for a
            specific set of accounts under one institutionLoginId. If none is
            given then the fix flow will give an account management dashboard
            and attempt to have the customer fix all accounts in turn.
        redirect_uri (string): The url that customers will be redirected to
            after completing Finicity Connect. <br> *Required unless Connect
            is embedded inside your application. (iframe)*
        webhook (string): The publicly available URL you wish to be notified
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
            which institutions to display in. See this article for
            [Details](https://docs.finicity.com/connect-institution-settings/)
                    analytics (string): Google Analytics or Adobe Analytics can be used
            with Connect to provide an additional layer of transparency of end
            user engagement. This is optional.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "partner_id":'partnerId',
        "customer_id":'customerId',
        "mtype":'type',
        "institution_login_id":'institutionLoginId',
        "redirect_uri":'redirectUri',
        "webhook":'webhook',
        "webhook_content_type":'webhookContentType',
        "webhook_data":'webhookData',
        "webhook_headers":'webhookHeaders',
        "institution_settings":'institutionSettings',
        "analytics":'analytics'
    }

    def __init__(self,
                 partner_id=None,
                 customer_id=None,
                 mtype=None,
                 institution_login_id=None,
                 redirect_uri=None,
                 webhook=None,
                 webhook_content_type='application/json',
                 webhook_data=None,
                 webhook_headers=None,
                 institution_settings=None,
                 analytics=None,
                 additional_properties = {}):
        """Constructor for the GenerateConnectURLRequestFix class"""

        # Initialize members of the class
        self.partner_id = partner_id
        self.customer_id = customer_id
        self.mtype = mtype
        self.institution_login_id = institution_login_id
        self.redirect_uri = redirect_uri
        self.webhook = webhook
        self.webhook_content_type = webhook_content_type
        self.webhook_data = webhook_data
        self.webhook_headers = webhook_headers
        self.institution_settings = institution_settings
        self.analytics = analytics

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
        institution_login_id = dictionary.get('institutionLoginId')
        redirect_uri = dictionary.get('redirectUri')
        webhook = dictionary.get('webhook')
        webhook_content_type = dictionary.get("webhookContentType") if dictionary.get("webhookContentType") else 'application/json'
        webhook_data = dictionary.get('webhookData')
        webhook_headers = dictionary.get('webhookHeaders')
        institution_settings = dictionary.get('institutionSettings')
        analytics = dictionary.get('analytics')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(partner_id,
                   customer_id,
                   mtype,
                   institution_login_id,
                   redirect_uri,
                   webhook,
                   webhook_content_type,
                   webhook_data,
                   webhook_headers,
                   institution_settings,
                   analytics,
                   dictionary)


