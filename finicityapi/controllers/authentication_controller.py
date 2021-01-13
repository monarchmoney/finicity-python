# -*- coding: utf-8 -*-

from finicityapi.api_helper import APIHelper
from finicityapi.configuration import Configuration
from finicityapi.controllers.base_controller import BaseController
from finicityapi.models.authentication_response import AuthenticationResponse

class AuthenticationController(BaseController):

    """A Controller to access Endpoints in the finicityapi API."""


    def modify_partner_secret(self,
                              content_type,
                              body):
        """Does a PUT request to /aggregation/v2/partners/authentication.

        Change the partner secret that is used to authenticate this partner.
        The secret does not expire, but can be changed by calling Modify
        Partner Secret. A valid partner secret may contain upper- and
        lowercase characters, numbers, and the characters !, @, #, $, %, &, *,
        _, -, +. It must include at least one number and at least one letter,
        and its length should be between 12 and 255 characters.

        Args:
            content_type (string): application/json
            body (ModifyPartnerCredentials): Partner ID and Partner Secret
                From Developer Portal Along With A Value For The New Partner
                Secret

        Returns:
            void: Response from the API. default response

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(content_type=content_type,
                                 body=body)

        # Prepare query URL
        _url_path = '/aggregation/v2/partners/authentication'
        _query_builder = Configuration.get_base_uri()
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'Finicity-App-Key': Configuration.finicity_app_key,
            'Content-Type': content_type
        }

        # Prepare and execute request
        _request = self.http_client.put(_query_url, headers=_headers, parameters=APIHelper.json_serialize(body))
        _context = self.execute_request(_request)
        self.validate_response(_context)

    def partner_authentication(self,
                               content_type,
                               accept,
                               body):
        """Does a POST request to /aggregation/v2/partners/authentication.

        Partner ID and Partner Secret: Sends to the Partner Authentication
        service to obtain a token for accessing the APIs.
        •The token is valid for two hours and is required on all calls to the
        Finicity APIs
        •As a best practice, use a single token for all calls. Assign a
        timestamp for each token, and then check the current timestamp before
        making any calls. If the token is greater than 90 minutes, generate a
        new one.
        Finicity-App-Key: Required on all calls to the Finicity APIs to
        identify your application.
        After five failed attempts to authenticate, your account is locked.
        Contact support@finicity.com to get help resetting your account.

        Args:
            content_type (string): application/json
            accept (string): application/json
            body (PartnerCredentials): Partner ID and Partner Secret From
                Developer Portal

        Returns:
            AuthenticationResponse: Response from the API. default response

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(content_type=content_type,
                                 accept=accept,
                                 body=body)

        # Prepare query URL
        _url_path = '/aggregation/v2/partners/authentication'
        _query_builder = Configuration.get_base_uri()
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'Finicity-App-Key': Configuration.finicity_app_key,
            'Content-Type': content_type,
            'Accept': accept
        }

        # Prepare and execute request
        _request = self.http_client.post(_query_url, headers=_headers, parameters=APIHelper.json_serialize(body))
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, AuthenticationResponse.from_dictionary)
