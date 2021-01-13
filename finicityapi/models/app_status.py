# -*- coding: utf-8 -*-

import finicityapi.models.app_fi_status

class AppStatus(object):

    """Implementation of the 'App Status' model.

    The registration status fields for the application. This is version 2 of
    this object.

    Attributes:
        partner_id (string): TODO: type description here.
        pre_app_id (long|int): An identifier to track the application
            registration request
        note (string): A note on registration. Typically used to indicate
            reasons for rejected apps.
        application_id (string): The official applicationId to be used in
            customer creation and setting customer application Id services.
            This is populated after the app is in A status for approved.
        app_name (string): The App Name submitted during registration
        submitted_date (long|int): A timestamp showing when the registration
            was submitted (see Handling Dates and Times)
        modified_date (long|int): A timestamp showing when the registration
            was last modified. Typically when it was approved or rejected.
            (see Handling Dates and Times)
        status (string): The status of the app registration request. A means
            approved. P means pending which is the status when initially
            submitted or when the app is modified and awaiting approval. R
            means rejected. If it is rejected there will be a note with the
            rejected reason.
        scopes (string): Indicates scopes of data accessible to the app
        institution_details (list of AppFIStatus): A list of the registration
            status for each FI for the application

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "partner_id":'partnerId',
        "pre_app_id":'preAppId',
        "app_name":'appName',
        "submitted_date":'submittedDate',
        "modified_date":'modifiedDate',
        "status":'status',
        "note":'note',
        "application_id":'applicationId',
        "scopes":'scopes',
        "institution_details":'institutionDetails'
    }

    def __init__(self,
                 partner_id=None,
                 pre_app_id=None,
                 app_name=None,
                 submitted_date=None,
                 modified_date=None,
                 status=None,
                 note=None,
                 application_id=None,
                 scopes=None,
                 institution_details=None,
                 additional_properties = {}):
        """Constructor for the AppStatus class"""

        # Initialize members of the class
        self.partner_id = partner_id
        self.pre_app_id = pre_app_id
        self.note = note
        self.application_id = application_id
        self.app_name = app_name
        self.submitted_date = submitted_date
        self.modified_date = modified_date
        self.status = status
        self.scopes = scopes
        self.institution_details = institution_details

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
        pre_app_id = dictionary.get('preAppId')
        app_name = dictionary.get('appName')
        submitted_date = dictionary.get('submittedDate')
        modified_date = dictionary.get('modifiedDate')
        status = dictionary.get('status')
        note = dictionary.get('note')
        application_id = dictionary.get('applicationId')
        scopes = dictionary.get('scopes')
        institution_details = None
        if dictionary.get('institutionDetails') != None:
            institution_details = list()
            for structure in dictionary.get('institutionDetails'):
                institution_details.append(finicityapi.models.app_fi_status.AppFIStatus.from_dictionary(structure))

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(partner_id,
                   pre_app_id,
                   app_name,
                   submitted_date,
                   modified_date,
                   status,
                   note,
                   application_id,
                   scopes,
                   institution_details,
                   dictionary)


