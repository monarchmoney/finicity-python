# -*- coding: utf-8 -*-


class ConnectV2EmailOptions(object):

    """Implementation of the 'Connect V2 Email Options' model.

    The parameter definitions used to configure the Connect email's sent to
    customers.

    Attributes:
        to (string): The email address for the customer receiving the Connect
            email.
        support_phone (string): (Optional) The support phone number listed in
            the email.
        subject (string): (Optional) The subject line of the email. The
            default is Verify your Financial Information.
        first_name (string): (Optional) The first name of the customer or both
            names of the customers for joint borrowers. Example: Marvin and
            Jenny.
        institution_name (string): (Optional) The name of your company.
        institution_address (string): (Optional) The institution address
            appears in the footer of the email.
        signature (list of string): (Optional) Add a signature to the email.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "to":'to',
        "support_phone":'supportPhone',
        "subject":'subject',
        "first_name":'firstName',
        "institution_name":'institutionName',
        "institution_address":'institutionAddress',
        "signature":'signature'
    }

    def __init__(self,
                 to=None,
                 support_phone=None,
                 subject=None,
                 first_name=None,
                 institution_name=None,
                 institution_address=None,
                 signature=None,
                 additional_properties = {}):
        """Constructor for the ConnectV2EmailOptions class"""

        # Initialize members of the class
        self.to = to
        self.support_phone = support_phone
        self.subject = subject
        self.first_name = first_name
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
                   institution_name,
                   institution_address,
                   signature,
                   dictionary)


