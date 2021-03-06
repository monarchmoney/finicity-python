# -*- coding: utf-8 -*-

from finicityapi.api_helper import APIHelper
import finicityapi.exceptions.api_exception

class Error1ErrorException(finicityapi.exceptions.api_exception.APIException):
    def __init__(self, reason, context):
        """Constructor for the Error1ErrorException class

        Args:
            reason (string): The reason (or error message) for the Exception
                to be raised.
            context (HttpContext):  The HttpContext of the API call.

        """
        super(Error1ErrorException, self).__init__(reason, context)
        dictionary = APIHelper.json_deserialize(self.context.response.raw_body)
        if isinstance(dictionary, dict):
            self.unbox(dictionary)

    def unbox(self, dictionary):
        """Populates the properties of this object by extracting them from a dictionary.

        Args:
            dictionary (dictionary): A dictionary representation of the object as
            obtained from the deserialization of the server's response. The keys
            MUST match property names in the API description.

        """
        self.code = dictionary.get('code')
        self.message = dictionary.get('message')
        self.asset_id = dictionary.get('assetId')
