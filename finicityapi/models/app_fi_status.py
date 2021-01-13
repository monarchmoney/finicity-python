# -*- coding: utf-8 -*-


class AppFIStatus(object):

    """Implementation of the 'App FI Status' model.

    The registration status fields for each specific OAuth financial
    institution

    Attributes:
        id (long|int): The finicity financial institution id
        abbrv_name (string): The applications abbreviated name
        logo_url (string): Logo URL for stored logo file
        decryption_key_activated (bool): Status of decryption keys for
            financial institution app registration
        created_date (long|int): Creation date of app's financial institution
            registration
        last_modified_date (long|int): Last modified date of the app's
            financial institution registration
        status (bool): App registered for specific FI what status is true.
            False indicates registration is still pending.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id":'id',
        "decryption_key_activated":'decryptionKeyActivated',
        "created_date":'createdDate',
        "last_modified_date":'lastModifiedDate',
        "status":'status',
        "abbrv_name":'abbrvName',
        "logo_url":'logoUrl'
    }

    def __init__(self,
                 id=None,
                 decryption_key_activated=None,
                 created_date=None,
                 last_modified_date=None,
                 status=None,
                 abbrv_name=None,
                 logo_url=None,
                 additional_properties = {}):
        """Constructor for the AppFIStatus class"""

        # Initialize members of the class
        self.id = id
        self.abbrv_name = abbrv_name
        self.logo_url = logo_url
        self.decryption_key_activated = decryption_key_activated
        self.created_date = created_date
        self.last_modified_date = last_modified_date
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
        id = dictionary.get('id')
        decryption_key_activated = dictionary.get('decryptionKeyActivated')
        created_date = dictionary.get('createdDate')
        last_modified_date = dictionary.get('lastModifiedDate')
        status = dictionary.get('status')
        abbrv_name = dictionary.get('abbrvName')
        logo_url = dictionary.get('logoUrl')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(id,
                   decryption_key_activated,
                   created_date,
                   last_modified_date,
                   status,
                   abbrv_name,
                   logo_url,
                   dictionary)


