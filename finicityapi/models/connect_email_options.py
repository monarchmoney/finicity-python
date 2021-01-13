# -*- coding: utf-8 -*-


class ConnectEmailOptions(object):

    """Implementation of the 'Connect Email Options' model.

    Customizable email details

    Attributes:
        to (string): The email address you wish to receive the email
        support_phone (string): Phone number that will be listed for support
            in the email. This field is optional. This is also available in
            the Finicity Developer Portal.
        subject (string): The “subject” line that will appear in user’s
            inboxes. Defaults to ‘Verify your Financial Information’ This
            field is optional.
        first_name (string): The first name of the customer that will appear
            in the email This field is optional.
        brand_color (string): The header color in the email. Defaults to dark
            blue This field is optional. This is also available in the
            Finicity Developer Portal.
        brand_logo (string): A valid url that points to the logo you want to
            appear in the email. For optimal display, should have dimensions
            no greater than 110 pixels tall and 300 pixels wide This field is
            optional. This is also available in the Finicity Developer
            Portal.
        institution_name (string): The name of your company that will appear
            in the email This field is optional. This is also available in the
            Finicity Developer Portal.
        institution_address (string): Address that will appear in the footer
            of the email This field is optional. This is also available in the
            Finicity Developer Portal.
        signature (list of string): Signature can be applied. In xml a
            separate line in signature is delineated by each tag. In json this
            is simply an array, e.g. “signature”: This field is optional.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "to":'to',
        "support_phone":'supportPhone',
        "subject":'subject',
        "first_name":'firstName',
        "brand_color":'brandColor',
        "brand_logo":'brandLogo',
        "institution_name":'institutionName',
        "institution_address":'institutionAddress',
        "signature":'signature'
    }

    def __init__(self,
                 to=None,
                 support_phone=None,
                 subject=None,
                 first_name=None,
                 brand_color=None,
                 brand_logo=None,
                 institution_name=None,
                 institution_address=None,
                 signature=None,
                 additional_properties = {}):
        """Constructor for the ConnectEmailOptions class"""

        # Initialize members of the class
        self.to = to
        self.support_phone = support_phone
        self.subject = subject
        self.first_name = first_name
        self.brand_color = brand_color
        self.brand_logo = brand_logo
        self.institution_name = institution_name
        self.institution_address = institution_address
        self.signature = signature

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
        to = dictionary.get('to')
        support_phone = dictionary.get('supportPhone')
        subject = dictionary.get('subject')
        first_name = dictionary.get('firstName')
        brand_color = dictionary.get('brandColor')
        brand_logo = dictionary.get('brandLogo')
        institution_name = dictionary.get('institutionName')
        institution_address = dictionary.get('institutionAddress')
        signature = dictionary.get('signature')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(to,
                   support_phone,
                   subject,
                   first_name,
                   brand_color,
                   brand_logo,
                   institution_name,
                   institution_address,
                   signature,
                   dictionary)


