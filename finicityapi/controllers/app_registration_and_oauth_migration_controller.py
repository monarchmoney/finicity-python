# -*- coding: utf-8 -*-

from finicityapi.api_helper import APIHelper
from finicityapi.configuration import Configuration
from finicityapi.controllers.base_controller import BaseController
from finicityapi.http.auth.custom_header_auth import CustomHeaderAuth
from finicityapi.models.app_registration_response import AppRegistrationResponse
from finicityapi.models.customer_accounts import CustomerAccounts
from finicityapi.models.app_statuses import AppStatuses

class AppRegistrationAndOauthMigrationController(BaseController):

    """A Controller to access Endpoints in the finicityapi API."""


    def set_customer_application_id(self,
                                    customer_id,
                                    application_id):
        """Does a PUT request to /aggregation/v1/customers/{customerId}/applications/{applicationId}.

        If you have multiple applications for a single client, and you want to
        register their applications to access financial institutions using
        OAuth connections, then use this API to assign all applications to an
        existing customer.

        Args:
            customer_id (long|int): The customer's ID for the customer you
                want to assign the app for.
            application_id (long|int): Application ID you want to assign the
                customer to. This is the "applicationId" value returned from
                the Get App Registration Status endpoint

        Returns:
            void: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(customer_id=customer_id,
                                 application_id=application_id)

        # Prepare query URL
        _url_path = '/aggregation/v1/customers/{customerId}/applications/{applicationId}'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, { 
            'customerId': customer_id,
            'applicationId': application_id
        })
        _query_builder = Configuration.get_base_uri()
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'Finicity-App-Key': Configuration.finicity_app_key
        }

        # Prepare and execute request
        _request = self.http_client.put(_query_url, headers=_headers)
        CustomHeaderAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

    def app_registration(self,
                         body):
        """Does a POST request to /aggregation/v1/partners/applications.

        Register new applications to access financial institutions using OAuth
        connections.

        Args:
            body (AppRegistrationRequest): The values for the new app
                registration

        Returns:
            AppRegistrationResponse: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(body=body)

        # Prepare query URL
        _url_path = '/aggregation/v1/partners/applications'
        _query_builder = Configuration.get_base_uri()
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json',
            'content-type': 'application/json; charset=utf-8',
            'Finicity-App-Key': Configuration.finicity_app_key
        }

        # Prepare and execute request
        _request = self.http_client.post(_query_url, headers=_headers, parameters=APIHelper.json_serialize(body))
        CustomHeaderAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, AppRegistrationResponse.from_dictionary)

    def modify_app_registration(self,
                                pre_app_id,
                                body):
        """Does a PUT request to /aggregation/v1/partners/applications/{preAppId}.

        Update the field values you want to change for the registered
        applications accessing financial institutions using OAuth
        connections.

        Args:
            pre_app_id (long|int): The preAppId from the App Registration and
                Get App Registration Status endpoints
            body (ModifyAppRegistrationRequest): The values for the app
                registration modification

        Returns:
            AppRegistrationResponse: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(pre_app_id=pre_app_id,
                                 body=body)

        # Prepare query URL
        _url_path = '/aggregation/v1/partners/applications/{preAppId}'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, { 
            'preAppId': pre_app_id
        })
        _query_builder = Configuration.get_base_uri()
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json',
            'content-type': 'application/json; charset=utf-8',
            'Finicity-App-Key': Configuration.finicity_app_key
        }

        # Prepare and execute request
        _request = self.http_client.put(_query_url, headers=_headers, parameters=APIHelper.json_serialize(body))
        CustomHeaderAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, AppRegistrationResponse.from_dictionary)

    def migrate_institution_login_accounts_v_2(self,
                                               customer_id,
                                               institution_login_id):
        """Does a PUT request to /aggregation/v2/customers/{customerId}/institutionLogins/{institutionLoginId}/migration.

        The institutionLoginId parameter uses Finicity’s internal FI mapping
        to move accounts from the current FI legacy connection to the new
        OAuth FI connection.
        The API returns a list of accounts for the institution login id
        specified with an HTTP status code 200.

        Args:
            customer_id (long|int): The target customer for the account
                migration
            institution_login_id (long|int): The institutionLoginId for the
                set of accounts to be migrated from the legacy FI ID to the
                new OAuth FI ID

        Returns:
            CustomerAccounts: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(customer_id=customer_id,
                                 institution_login_id=institution_login_id)

        # Prepare query URL
        _url_path = '/aggregation/v2/customers/{customerId}/institutionLogins/{institutionLoginId}/migration'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, { 
            'customerId': customer_id,
            'institutionLoginId': institution_login_id
        })
        _query_builder = Configuration.get_base_uri()
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json',
            'Finicity-App-Key': Configuration.finicity_app_key
        }

        # Prepare and execute request
        _request = self.http_client.put(_query_url, headers=_headers)
        CustomHeaderAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, CustomerAccounts.from_dictionary)

    def get_app_registration_status_v_2(self,
                                        accept='application/json',
                                        pre_app_id=None,
                                        application_id=None,
                                        status=None,
                                        app_name=None,
                                        submitted_date=None,
                                        modified_date=None,
                                        page=1,
                                        page_size=1):
        """Does a GET request to /aggregation/v2/partners/applications.

        Get the status of your application registration to access financial
        institutions using OAuth connections.

        Args:
            accept (string, optional): application/json, application/xml
            pre_app_id (long|int, optional): Look up the status of an app by
                the preAppId
            application_id (string, optional): Look up the status of an app by
                the applicationId
            status (string, optional): Look up the status of app registration
                requests by the registration request status. Valid values P
                (For Pending), A (For Approved), R (For Rejected)
            app_name (string, optional): Look up app registration requests by
                the application name
            submitted_date (long|int, optional): Look up app registration
                requests by the date they were submitted in epoch format.
            modified_date (long|int, optional): Look up app registration
                requests by the date the request was updated. This could be
                used to determine when the app was updated to approved or
                rejected.
            page (long|int, optional): Select which page of results to return
            page_size (long|int, optional): Select how many results per page
                to return

        Returns:
            AppStatuses: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/aggregation/v2/partners/applications'
        _query_builder = Configuration.get_base_uri()
        _query_builder += _url_path
        _query_parameters = {
            'preAppId': pre_app_id,
            'applicationId': application_id,
            'status': status,
            'appName': app_name,
            'submittedDate': submitted_date,
            'modifiedDate': modified_date,
            'page': page,
            'pageSize': page_size
        }
        _query_builder = APIHelper.append_url_with_query_parameters(_query_builder,
            _query_parameters, Configuration.array_serialization)
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'Finicity-App-Key': Configuration.finicity_app_key,
            'Accept': accept
        }

        # Prepare and execute request
        _request = self.http_client.get(_query_url, headers=_headers)
        CustomHeaderAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, AppStatuses.from_dictionary)
