# -*- coding: utf-8 -*-

from finicityapi.api_helper import APIHelper
from finicityapi.configuration import Configuration
from finicityapi.controllers.base_controller import BaseController
from finicityapi.http.auth.custom_header_auth import CustomHeaderAuth
from finicityapi.models.generate_connect_url_response import GenerateConnectURLResponse
from finicityapi.models.generate_v_2_connect_email_response import GenerateV2ConnectEmailResponse

class ConnectController(BaseController):

    """A Controller to access Endpoints in the finicityapi API."""


    def generate_v_2_connect_url(self,
                                 accept,
                                 body):
        """Does a POST request to /connect/v2/generate.

        No matter how you plan on implementing Finicity Connect, you’ll need
        to generate and retrieve a Finicity Connect Link.  Connect provides
        you with a complete user experience, which requires minimal work in
        integration.  
        Once you have generated the link it will only last until the
        authentication token under which it was generated expires. After that
        you will need to regenerate the Connect link under a new
        authentication token. We recommend generating a new authentication
        token when you generate a Connect link, to guarantee a full two hour
        life-span.
        Connect features:
        * Sign in, the user’s credentials and Multi-Factor Authentication
        (MFA)
        * Search for the user’s financial institutions
        * Manage the user’s accounts
        **MVS Developers**
        Use the `experience` parameter to call (per session) the Connect and
        the MVS application modules in the body of the request.
         
        You can prepopulate the consumer’s SSN (only the last 4 digits appear)
        and DOB to display on the Find employment records page at the
        beginning of the MVS payroll module. Pass the SSN and DOB values for
        the consumer in the body of the request call.

        Args:
            accept (string): application/json, application/xml
            body (GenerateV2ConnectURLRequest): Expected body to be sent with
                the request

        Returns:
            GenerateConnectURLResponse: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(accept=accept,
                                 body=body)

        # Prepare query URL
        _url_path = '/connect/v2/generate'
        _query_builder = Configuration.get_base_uri()
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'content-type': 'application/json; charset=utf-8',
            'Finicity-App-Key': Configuration.finicity_app_key,
            'Accept': accept
        }

        # Prepare and execute request
        _request = self.http_client.post(_query_url, headers=_headers, parameters=APIHelper.json_serialize(body))
        CustomHeaderAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, GenerateConnectURLResponse.from_dictionary)

    def generate_v_2_lite_connect_url(self,
                                      accept,
                                      body):
        """Does a POST request to /connect/v2/generate/lite.

        Connect Lite allows as much control of the customer experience as
        possible. Lite includes just the essential pages needed for handling
        credentials and multi-factor authentication that must be handled by
        Finicity. You would be providing the financial institution search and
        the account management pages.
        Connect Lite features:
        * Sign in, user’s credentials and Multi-Factor Authentication (MFA)
        * No user account management

        Args:
            accept (string): application/json, application/xml
            body (GenerateConnectURLRequestLiteV2): Expected body to be sent
                with the request

        Returns:
            GenerateConnectURLResponse: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(accept=accept,
                                 body=body)

        # Prepare query URL
        _url_path = '/connect/v2/generate/lite'
        _query_builder = Configuration.get_base_uri()
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'content-type': 'application/json; charset=utf-8',
            'Finicity-App-Key': Configuration.finicity_app_key,
            'Accept': accept
        }

        # Prepare and execute request
        _request = self.http_client.post(_query_url, headers=_headers, parameters=APIHelper.json_serialize(body))
        CustomHeaderAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, GenerateConnectURLResponse.from_dictionary)

    def generate_v_2_fix_connect_url(self,
                                     accept,
                                     body):
        """Does a POST request to /connect/v2/generate/fix.

        Fix provides a flow for customers to re-authenticate to their
        accounts, when the connection to the user’s financial institution is
        lost.  The connection to their accounts can stop working if the
        account password has changed, the MFA challenge has expired, or the
        token provided by the financial institution has been revoked.

        Args:
            accept (string): application/json, application/xml
            body (GenerateConnectURLRequestFixV2): Expected body to be sent
                with the request

        Returns:
            GenerateConnectURLResponse: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(accept=accept,
                                 body=body)

        # Prepare query URL
        _url_path = '/connect/v2/generate/fix'
        _query_builder = Configuration.get_base_uri()
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'content-type': 'application/json; charset=utf-8',
            'Finicity-App-Key': Configuration.finicity_app_key,
            'Accept': accept
        }

        # Prepare and execute request
        _request = self.http_client.post(_query_url, headers=_headers, parameters=APIHelper.json_serialize(body))
        CustomHeaderAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, GenerateConnectURLResponse.from_dictionary)

    def send_v_2_connect_email(self,
                               accept,
                               body):
        """Does a POST request to /connect/v2/send/email.

        Rather than adding a Connect URL link into your applications, this API
        allows you to send a Connect email to the consumer. The `experience`
        parameter refers to the type of connect experience (per session) you
        want for the customer such as, the brand color, logo, icon, and which
        credit decisioning report to generate when the Connect application
        completes.
        **Note**: Contact your Sales Account Team to set up the `experience`
        parameter.
        **MVS Developers**: Use the `experience` parameter to call (per
        session) the MVS application modules in the body of the request. When
        the consumer opens the email, they’ll click a button that opens the
        Connect application or the MVS application modules.
        You can prepopulate the consumer’s SSN (only the last 4 digits appear)
        and DOB to display on the Find employment records page at the
        beginning of the MVS payroll module. Pass the SSN and DOB values for
        the consumer in the body of the request call.

        Args:
            accept (string): application/json
            body (GenerateV2ConnectEmailRequest): Expected body to be sent
                with the request

        Returns:
            GenerateV2ConnectEmailResponse: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(accept=accept,
                                 body=body)

        # Prepare query URL
        _url_path = '/connect/v2/send/email'
        _query_builder = Configuration.get_base_uri()
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'content-type': 'application/json; charset=utf-8',
            'Finicity-App-Key': Configuration.finicity_app_key,
            'Accept': accept
        }

        # Prepare and execute request
        _request = self.http_client.post(_query_url, headers=_headers, parameters=APIHelper.json_serialize(body))
        CustomHeaderAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, GenerateV2ConnectEmailResponse.from_dictionary)

    def generate_v_2_connect_url_joint_borrower(self,
                                                accept,
                                                body):
        """Does a POST request to /connect/v2/generate/jointBorrower.

        This API generates a Connect 2.0 URL link for you to add within your
        own applications. Use the `experience` parameter to call the MVS
        application modules in the body of the request.
         
        MVS prompts for both of the borrowers to enter all their financial,
        payroll, and paystub information. The primary and joint borrower’s
        experience is all done in one session.
         
        You can prepopulate the consumer’s SSN (only the last 4 digits appear)
        and DOB to display on the Find employment records page at the
        beginning of the MVS payroll module. Pass the SSN and DOB values for
        the consumer in the body of the request call.

        Args:
            accept (string): application/json, application/xml
            body (GenerateV2ConnectURLRequestJointBorrower): Expected body to
                be sent with the request

        Returns:
            GenerateConnectURLResponse: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(accept=accept,
                                 body=body)

        # Prepare query URL
        _url_path = '/connect/v2/generate/jointBorrower'
        _query_builder = Configuration.get_base_uri()
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'content-type': 'application/json; charset=utf-8',
            'Finicity-App-Key': Configuration.finicity_app_key,
            'Accept': accept
        }

        # Prepare and execute request
        _request = self.http_client.post(_query_url, headers=_headers, parameters=APIHelper.json_serialize(body))
        CustomHeaderAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, GenerateConnectURLResponse.from_dictionary)

    def send_v_2_connect_email_joint_borrower(self,
                                              accept,
                                              body):
        """Does a POST request to /connect/v2/send/email/jointBorrower.

        Send a Connect email to at least one of the joint borrower’s email
        addresses. Use the `experience` parameter to call the MVS application
        module in the body of the request.
         
        When the consumer opens the email, MVS prompts for both of the
        borrowers to enter all their financial, payroll, and paystub
        information. The primary and joint borrower’s experience is all done
        in one session.
         
        You can prepopulate the consumer’s SSN (only the last 4 digits appear)
        and DOB to display on the Find employment records page at the
        beginning of the MVS payroll module. Pass the SSN and DOB values for
        the consumer in the body of the request call.

        Args:
            accept (string): application/json
            body (V2ConnectEmailRequestJointBorrower): Expected body to be
                sent with the request

        Returns:
            GenerateV2ConnectEmailResponse: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(accept=accept,
                                 body=body)

        # Prepare query URL
        _url_path = '/connect/v2/send/email/jointBorrower'
        _query_builder = Configuration.get_base_uri()
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'content-type': 'application/json; charset=utf-8',
            'Finicity-App-Key': Configuration.finicity_app_key,
            'Accept': accept
        }

        # Prepare and execute request
        _request = self.http_client.post(_query_url, headers=_headers, parameters=APIHelper.json_serialize(body))
        CustomHeaderAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, GenerateV2ConnectEmailResponse.from_dictionary)
