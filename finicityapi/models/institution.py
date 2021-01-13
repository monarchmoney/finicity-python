# -*- coding: utf-8 -*-

import finicityapi.models.institution_address

class Institution(object):

    """Implementation of the 'Institution' model.

    A financial institution's Finicity registered details

    Attributes:
        id (long|int): Finicity’s institution ID
        name (string): The name of the institution
        account_type_description (string): One of the values Banking,
            Investments, Credit Cards/Accounts, Workplace Retirement,
            Mortgages and Loans, Insurance
        phone (string): The institution’s primary phone number
        url_home_app (string): The URL of the institution’s primary home page
        url_logon_app (string): The URL of the institution’s login page
        oauth_enabled (bool): Specifies if the institution is an OAuth
            institution
        url_forgot_password (string): Institution's forgot password page
        url_online_registration (string): Institution's signup page
        mclass (string): Institution's class
        special_text (string): Special instructions given to customer for
            login
        special_instructions (list of object): Instructions given to customer
            before they are sent to the institution website to login for OAuth
            insitutions. This is to help them give proper permission for data
            needed for the application.
        address (InstitutionAddress): The address for the financial
            institution
        currency (string): Institution's currency
        email (string): The institution’s primary contact email
        status (string): Institution's status. Online, Offline, Maintenance,
            Testing
        oauth_institution_id (string): The institution id of the OAuth
            institution that replaces this institution
        new_institution_id (string): The institution id of the institution
            that replaces this institution. Will be the same as
            oauthInstitutionId and will eventually replace that field.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id":'id',
        "name":'name',
        "account_type_description":'accountTypeDescription',
        "url_home_app":'urlHomeApp',
        "url_logon_app":'urlLogonApp',
        "oauth_enabled":'oauthEnabled',
        "currency":'currency',
        "status":'status',
        "phone":'phone',
        "url_forgot_password":'urlForgotPassword',
        "url_online_registration":'urlOnlineRegistration',
        "mclass":'class',
        "special_text":'specialText',
        "special_instructions":'specialInstructions',
        "address":'address',
        "email":'email',
        "oauth_institution_id":'oauthInstitutionId',
        "new_institution_id":'newInstitutionId'
    }

    def __init__(self,
                 id=None,
                 name=None,
                 account_type_description=None,
                 url_home_app=None,
                 url_logon_app=None,
                 oauth_enabled=None,
                 currency=None,
                 status=None,
                 phone=None,
                 url_forgot_password=None,
                 url_online_registration=None,
                 mclass=None,
                 special_text=None,
                 special_instructions=None,
                 address=None,
                 email=None,
                 oauth_institution_id=None,
                 new_institution_id=None,
                 additional_properties = {}):
        """Constructor for the Institution class"""

        # Initialize members of the class
        self.id = id
        self.name = name
        self.account_type_description = account_type_description
        self.phone = phone
        self.url_home_app = url_home_app
        self.url_logon_app = url_logon_app
        self.oauth_enabled = oauth_enabled
        self.url_forgot_password = url_forgot_password
        self.url_online_registration = url_online_registration
        self.mclass = mclass
        self.special_text = special_text
        self.special_instructions = special_instructions
        self.address = address
        self.currency = currency
        self.email = email
        self.status = status
        self.oauth_institution_id = oauth_institution_id
        self.new_institution_id = new_institution_id

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
        id = dictionary.get('id')
        name = dictionary.get('name')
        account_type_description = dictionary.get('accountTypeDescription')
        url_home_app = dictionary.get('urlHomeApp')
        url_logon_app = dictionary.get('urlLogonApp')
        oauth_enabled = dictionary.get('oauthEnabled')
        currency = dictionary.get('currency')
        status = dictionary.get('status')
        phone = dictionary.get('phone')
        url_forgot_password = dictionary.get('urlForgotPassword')
        url_online_registration = dictionary.get('urlOnlineRegistration')
        mclass = dictionary.get('class')
        special_text = dictionary.get('specialText')
        special_instructions = dictionary.get('specialInstructions')
        address = finicityapi.models.institution_address.InstitutionAddress.from_dictionary(dictionary.get('address')) if dictionary.get('address') else None
        email = dictionary.get('email')
        oauth_institution_id = dictionary.get('oauthInstitutionId')
        new_institution_id = dictionary.get('newInstitutionId')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(id,
                   name,
                   account_type_description,
                   url_home_app,
                   url_logon_app,
                   oauth_enabled,
                   currency,
                   status,
                   phone,
                   url_forgot_password,
                   url_online_registration,
                   mclass,
                   special_text,
                   special_instructions,
                   address,
                   email,
                   oauth_institution_id,
                   new_institution_id,
                   dictionary)


