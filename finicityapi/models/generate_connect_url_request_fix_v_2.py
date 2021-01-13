# -*- coding: utf-8 -*-


class GenerateConnectURLRequestFixV2(object):

    """Implementation of the 'Generate Connect URL Request (fix) - V2' model.

    TODO: type model description here.

    Attributes:
        partner_id (string): The partner id you can obtain from your Finicity
            developer dashboard
        customer_id (string): Finicity’s customer ID. Obtained from the Add
            Customer call.
        institution_login_id (int): The institutionLoginId for the account
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
        experience (string): The `experience` field allows you to customize:
            <br> * **Brand**: color and logo <br> * **Icon**: displayed on the
            Share your data page <br>      <br>**Note**: The Finicity sales
            engineers (SE) help you set up a default experience for your
            company when you migrate to Connect 2. For each additional
            experience you create thereafter, they’ll give you a unique ID.
            See [Generate 2.0 Connect URL APIs](
            https://docs.finicity.com/migrate-to-connect-web-sdk-2-0/#migrate-c
            onnect-web-sdk-1) <br>  <br>**Experience values options**: <br> *
            **default**: your default experience <br> * **unique ID**: the
            code for a different experience <br> * **not defined**: If you
            don’t pass the experience parameter, then Connect’s out of the box
            default experience (add accounts but no branding) is used. <br>

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "partner_id":'partnerId',
        "customer_id":'customerId',
        "institution_login_id":'institutionLoginId',
        "redirect_uri":'redirectUri',
        "webhook":'webhook',
        "webhook_content_type":'webhookContentType',
        "webhook_data":'webhookData',
        "webhook_headers":'webhookHeaders',
        "experience":'experience'
    }

    def __init__(self,
                 partner_id=None,
                 customer_id=None,
                 institution_login_id=None,
                 redirect_uri=None,
                 webhook=None,
                 webhook_content_type='application/json',
                 webhook_data=None,
                 webhook_headers=None,
                 experience=None,
                 additional_properties = {}):
        """Constructor for the GenerateConnectURLRequestFixV2 class"""

        # Initialize members of the class
        self.partner_id = partner_id
        self.customer_id = customer_id
        self.institution_login_id = institution_login_id
        self.redirect_uri = redirect_uri
        self.webhook = webhook
        self.webhook_content_type = webhook_content_type
        self.webhook_data = webhook_data
        self.webhook_headers = webhook_headers
        self.experience = experience

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
        institution_login_id = dictionary.get('institutionLoginId')
        redirect_uri = dictionary.get('redirectUri')
        webhook = dictionary.get('webhook')
        webhook_content_type = dictionary.get("webhookContentType") if dictionary.get("webhookContentType") else 'application/json'
        webhook_data = dictionary.get('webhookData')
        webhook_headers = dictionary.get('webhookHeaders')
        experience = dictionary.get('experience')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(partner_id,
                   customer_id,
                   institution_login_id,
                   redirect_uri,
                   webhook,
                   webhook_content_type,
                   webhook_data,
                   webhook_headers,
                   experience,
                   dictionary)


