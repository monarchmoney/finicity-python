# -*- coding: utf-8 -*-

from finicityapi.api_helper import APIHelper
from finicityapi.configuration import Configuration
from finicityapi.controllers.base_controller import BaseController
from finicityapi.http.auth.custom_header_auth import CustomHeaderAuth
from finicityapi.models.customer_accounts import CustomerAccounts
from finicityapi.models.customer_account import CustomerAccount

class AccountsController(BaseController):

    """A Controller to access Endpoints in the finicityapi API."""


    def delete_customer_accounts_by_institution_login(self,
                                                      customer_id,
                                                      institution_login_id):
        """Does a DELETE request to /aggregation/v1/customers/{customerId}/institutionLogins/{institutionLoginId}.

        Remove the specified set of accounts by institution login id from the
        Finicity system.
        (Note that the request and response are the same for JSON and XML
        clients.)

        Args:
            customer_id (long|int): The ID of the customer whose accounts are
                to be deleted
            institution_login_id (long|int): The Finicity ID of the
                Institution Login for the set of accounts to be deleted

        Returns:
            void: Response from the API. default response

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
        _url_path = '/aggregation/v1/customers/{customerId}/institutionLogins/{institutionLoginId}'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, { 
            'customerId': customer_id,
            'institutionLoginId': institution_login_id
        })
        _query_builder = Configuration.get_base_uri()
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'Finicity-App-Key': Configuration.finicity_app_key
        }

        # Prepare and execute request
        _request = self.http_client.delete(_query_url, headers=_headers)
        CustomHeaderAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

    def refresh_customer_accounts_by_institution_login(self,
                                                       content_length,
                                                       accept,
                                                       customer_id,
                                                       institution_login_id):
        """Does a POST request to /aggregation/v1/customers/{customerId}/institutionLogins/{institutionLoginId}/accounts.

        Refresh account and transaction data for all accounts associated with
        a given institutionLoginId with a connection to the institution.
        Client apps are not permitted to automate calls to the Refresh
        services. Active accounts are automatically refreshed by Finicity once
        per day. Because many financial institutions only post transactions
        once per day, calling Refresh repeatedly is usually a waste of
        resources and is not recommended.
        Apps may call Refresh services for a specific customer when there is a
        specific business case for the need of data that is up to date as of
        the moment. Please discuss with your account manager and systems
        engineer for further clarification.
        The recommended timeout setting for this request is 120 seconds in
        order to receive a response. However you can terminate the connection
        after making the call the operation will still complete. You will have
        to pull the account records to check for an updated aggregation
        attempt date to know when the refresh is complete.

        Args:
            content_length (int): Must be 0 (this request has no body)
            accept (string): application/json, application/xml
            customer_id (string): The ID of the customer who owns the
                accounts
            institution_login_id (string): The institution login ID from the
                account records

        Returns:
            CustomerAccounts: Response from the API. default response

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(content_length=content_length,
                                 accept=accept,
                                 customer_id=customer_id,
                                 institution_login_id=institution_login_id)

        # Prepare query URL
        _url_path = '/aggregation/v1/customers/{customerId}/institutionLogins/{institutionLoginId}/accounts'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, { 
            'customerId': customer_id,
            'institutionLoginId': institution_login_id
        })
        _query_builder = Configuration.get_base_uri()
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'Finicity-App-Key': Configuration.finicity_app_key,
            'Content-Length': content_length,
            'Accept': accept,
            'interactive': False
        }

        # Prepare and execute request
        _request = self.http_client.post(_query_url, headers=_headers)
        CustomHeaderAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, CustomerAccounts.from_dictionary)

    def get_customer_accounts_by_institution_login(self,
                                                   accept,
                                                   customer_id,
                                                   institution_login_id):
        """Does a GET request to /aggregation/v1/customers/{customerId}/institutionLogins/{institutionLoginId}/accounts.

        Get details for all accounts associated with the given institution
        login. All accounts returned are accessible by a single set of
        credentials on a single institution.

        Args:
            accept (string): application/json, application/xml
            customer_id (long|int): Finicity ID for the customer whose
                accounts are to be retrieved
            institution_login_id (long|int): The institution login ID (from
                the account record)

        Returns:
            CustomerAccounts: Response from the API. default response

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(accept=accept,
                                 customer_id=customer_id,
                                 institution_login_id=institution_login_id)

        # Prepare query URL
        _url_path = '/aggregation/v1/customers/{customerId}/institutionLogins/{institutionLoginId}/accounts'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, { 
            'customerId': customer_id,
            'institutionLoginId': institution_login_id
        })
        _query_builder = Configuration.get_base_uri()
        _query_builder += _url_path
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
        return APIHelper.json_deserialize(_context.response.raw_body, CustomerAccounts.from_dictionary)

    def get_customer_account(self,
                             accept,
                             customer_id,
                             account_id):
        """Does a GET request to /aggregation/v1/customers/{customerId}/accounts/{accountId}.

        Get details for the specified account.

        Args:
            accept (string): application/json, application/xml
            customer_id (long|int): The ID of the customer who owns the
                account
            account_id (long|int): Finicity’s ID of the account to be
                retrieved

        Returns:
            CustomerAccount: Response from the API. default response

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(accept=accept,
                                 customer_id=customer_id,
                                 account_id=account_id)

        # Prepare query URL
        _url_path = '/aggregation/v1/customers/{customerId}/accounts/{accountId}'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, { 
            'customerId': customer_id,
            'accountId': account_id
        })
        _query_builder = Configuration.get_base_uri()
        _query_builder += _url_path
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
        return APIHelper.json_deserialize(_context.response.raw_body, CustomerAccount.from_dictionary)

    def delete_customer_account(self,
                                customer_id,
                                account_id):
        """Does a DELETE request to /aggregation/v1/customers/{customerId}/accounts/{accountId}.

        Remove the specified account from Finicity Aggregation.

        Args:
            customer_id (long|int): The ID of the customer who owns the
                account
            account_id (long|int): Finicity’s ID of the account to be deleted

        Returns:
            void: Response from the API. default response

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(customer_id=customer_id,
                                 account_id=account_id)

        # Prepare query URL
        _url_path = '/aggregation/v1/customers/{customerId}/accounts/{accountId}'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, { 
            'customerId': customer_id,
            'accountId': account_id
        })
        _query_builder = Configuration.get_base_uri()
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'Finicity-App-Key': Configuration.finicity_app_key
        }

        # Prepare and execute request
        _request = self.http_client.delete(_query_url, headers=_headers)
        CustomHeaderAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

    def get_customer_accounts(self,
                              accept,
                              customer_id,
                              status=None):
        """Does a GET request to /aggregation/v1/customers/{customerId}/accounts.

        Get details for all accounts owned by the specified customer.

        Args:
            accept (string): application/json, application/xml
            customer_id (long|int): The ID of the customer whose accounts are
                to be retrieved
            status (string, optional): append, ?status=pending, to return
                accounts in active and pending status. Pending accounts were
                discovered but not activated and will not have transactions or
                have balance updates

        Returns:
            CustomerAccounts: Response from the API. default response

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(accept=accept,
                                 customer_id=customer_id)

        # Prepare query URL
        _url_path = '/aggregation/v1/customers/{customerId}/accounts'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, { 
            'customerId': customer_id
        })
        _query_builder = Configuration.get_base_uri()
        _query_builder += _url_path
        _query_parameters = {
            'status': status
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
        return APIHelper.json_deserialize(_context.response.raw_body, CustomerAccounts.from_dictionary)

    def get_customer_accounts_by_institution(self,
                                             accept,
                                             customer_id,
                                             institution_id):
        """Does a GET request to /aggregation/v1/customers/{customerId}/institutions/{institutionId}/accounts.

        Get details for all active accounts owned by the specified customer at
        the specified institution.

        Args:
            accept (string): application/json, application/xml
            customer_id (long|int): The ID of the customer who owns the
                account
            institution_id (long|int): Finicity’s ID of the institution

        Returns:
            CustomerAccounts: Response from the API. default response

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(accept=accept,
                                 customer_id=customer_id,
                                 institution_id=institution_id)

        # Prepare query URL
        _url_path = '/aggregation/v1/customers/{customerId}/institutions/{institutionId}/accounts'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, { 
            'customerId': customer_id,
            'institutionId': institution_id
        })
        _query_builder = Configuration.get_base_uri()
        _query_builder += _url_path
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
        return APIHelper.json_deserialize(_context.response.raw_body, CustomerAccounts.from_dictionary)

    def load_historic_transactions_for_customer_account(self,
                                                        content_length,
                                                        accept,
                                                        customer_id,
                                                        account_id):
        """Does a POST request to /aggregation/v1/customers/{customerId}/accounts/{accountId}/transactions/historic.

        Connect to the account’s financial institution and load up to 24
        months of historic transactions for the account. Length of history
        varies by institution.
        This is a premium service. The billable event is a call to this
        service specifying a customerId that has not been seen before by this
        service. (If this service is called multiple times with the same
        customerId, to load transactions from multiple accounts, only one
        billable event has occurred.)
        HTTP status of 204 means historic transactions have been loaded
        successfully. The transactions are now available by calling Get
        Customer Account Transactions.
        HTTP status of 203 means the response contains an MFA challenge.
        Contact your Account Manager or Systems Engineers to determine the
        best route to handle this HTTP status code.
        The recommended timeout setting for this request is 180 seconds in
        order to receive a response. However you can terminate the connection
        after making the call the operation will still complete. You will have
        to pull the account records to check for an updated aggregation
        attempt date to know when the refresh is complete.
        This service usually requires the HTTP header Content-Length: 0
        because it is a POST request with no request body.
        The date range sent to the institution is calculated from the
        account’s createdDate. This means that calling this service a second
        time for the same account normally will not add any new transactions
        for the account. For this reason, a second call to this service for a
        known accountId will usually return immediately with HTTP 204.
        In a few specific scenarios, it may be desirable to force a second
        connection to the institution for a known accountId. Some examples
        are:
        - The institution’s policy has changed, making more transactions
        available.
        - Finicity has now added a longer transaction history support for the
        institution.
        - The first call encountered an error, and the resulting Aggregation
        Ticket has now been fixed by the Finicity Support Team.
        In these cases, the POST request can contain the parameter force=true
        in the request body to force the second connection.

        Args:
            content_length (int): Must be 0 (this request has no body)
            accept (string): application/json, application/xml
            customer_id (long|int): The ID Of the customer who owns the
                account
            account_id (long|int): The Finicity ID of the account to pull
                transaction history for

        Returns:
            void: Response from the API. default response

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(content_length=content_length,
                                 accept=accept,
                                 customer_id=customer_id,
                                 account_id=account_id)

        # Prepare query URL
        _url_path = '/aggregation/v1/customers/{customerId}/accounts/{accountId}/transactions/historic'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, { 
            'customerId': customer_id,
            'accountId': account_id
        })
        _query_builder = Configuration.get_base_uri()
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'Finicity-App-Key': Configuration.finicity_app_key,
            'Content-Length': content_length,
            'Accept': accept
        }

        # Prepare and execute request
        _request = self.http_client.post(_query_url, headers=_headers)
        CustomHeaderAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

    def refresh_customer_accounts(self,
                                  content_length,
                                  accept,
                                  customer_id):
        """Does a POST request to /aggregation/v1/customers/{customerId}/accounts.

        Refresh account and transaction data for all accounts associated with
        a given customerId with a connection to the institution.
        Client apps are not permitted to automate calls to the Refresh
        services. Active accounts are automatically refreshed by Finicity once
        per day. Because many financial institutions only post transactions
        once per day, calling Refresh repeatedly is usually a waste of
        resources and is not recommended.
        Apps may call Refresh services for a specific customer when there is a
        specific business case for the need of data that is up to date as of
        the moment. Please discuss with your account manager and systems
        engineer for further clarification.
        The recommended timeout setting for this request is 120 seconds in
        order to receive a response. However you can terminate the connection
        after making the call the operation will still complete. You will have
        to pull the account records to check for an updated aggregation
        attempt date to know when the refresh is complete.

        Args:
            content_length (int): Must be 0 (this request has no body)
            accept (string): application/json, application/xml
            customer_id (string): The ID of the customer who owns the accounts
                to be refreshed

        Returns:
            CustomerAccounts: Response from the API. default response

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(content_length=content_length,
                                 accept=accept,
                                 customer_id=customer_id)

        # Prepare query URL
        _url_path = '/aggregation/v1/customers/{customerId}/accounts'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, { 
            'customerId': customer_id
        })
        _query_builder = Configuration.get_base_uri()
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'Finicity-App-Key': Configuration.finicity_app_key,
            'Content-Length': content_length,
            'Accept': accept
        }

        # Prepare and execute request
        _request = self.http_client.post(_query_url, headers=_headers)
        CustomHeaderAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, CustomerAccounts.from_dictionary)
