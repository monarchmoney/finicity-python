# -*- coding: utf-8 -*-


class AppRegistrationRequest(object):

    """Implementation of the 'App Registration Request' model.

    TODO: type model description here.

    Attributes:
        app_description (string): A short description of the app
        app_name (string): App Name. This will be visible to end users in the
            FI interface.
        app_url (string): App URL
        owner_address_line_1 (string): Address Line 1 for business entity that
            owns the app. Information for registration purposes only and not
            given to the end user.
        owner_address_line_2 (string): Address Line 2 for business entity that
            owns the app. Information for registration purposes only and not
            given to the end user.
        owner_city (string): City for business entity that owns the app.
            Information for registration purposes only and not given to the
            end user.
        owner_country (string): Country  for business entity that owns the
            app. Information for registration purposes only and not given to
            the end user.
        owner_name (string): Business name for business entity that owns the
            app. Information for registration purposes only and not given to
            the end user.
        owner_postal_code (string): Zip code for business entity that owns the
            app. Information for registration purposes only and not given to
            the end user.
        owner_state (string): State for business entity that owns the app.
            Information for registration purposes only and not given to the
            end user.
        image (string): App Logo. The base 64 encoded value for the logo. 1:1
            .svg file less than 50 KB

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "app_description":'appDescription',
        "app_name":'appName',
        "app_url":'appUrl',
        "owner_address_line_1":'ownerAddressLine1',
        "owner_address_line_2":'ownerAddressLine2',
        "owner_city":'ownerCity',
        "owner_country":'ownerCountry',
        "owner_name":'ownerName',
        "owner_postal_code":'ownerPostalCode',
        "owner_state":'ownerState',
        "image":'image'
    }

    def __init__(self,
                 app_description=None,
                 app_name=None,
                 app_url=None,
                 owner_address_line_1=None,
                 owner_address_line_2=None,
                 owner_city=None,
                 owner_country=None,
                 owner_name=None,
                 owner_postal_code=None,
                 owner_state=None,
                 image=None,
                 additional_properties = {}):
        """Constructor for the AppRegistrationRequest class"""

        # Initialize members of the class
        self.app_description = app_description
        self.app_name = app_name
        self.app_url = app_url
        self.owner_address_line_1 = owner_address_line_1
        self.owner_address_line_2 = owner_address_line_2
        self.owner_city = owner_city
        self.owner_country = owner_country
        self.owner_name = owner_name
        self.owner_postal_code = owner_postal_code
        self.owner_state = owner_state
        self.image = image

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
        app_description = dictionary.get('appDescription')
        app_name = dictionary.get('appName')
        app_url = dictionary.get('appUrl')
        owner_address_line_1 = dictionary.get('ownerAddressLine1')
        owner_address_line_2 = dictionary.get('ownerAddressLine2')
        owner_city = dictionary.get('ownerCity')
        owner_country = dictionary.get('ownerCountry')
        owner_name = dictionary.get('ownerName')
        owner_postal_code = dictionary.get('ownerPostalCode')
        owner_state = dictionary.get('ownerState')
        image = dictionary.get('image')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(app_description,
                   app_name,
                   app_url,
                   owner_address_line_1,
                   owner_address_line_2,
                   owner_city,
                   owner_country,
                   owner_name,
                   owner_postal_code,
                   owner_state,
                   image,
                   dictionary)


