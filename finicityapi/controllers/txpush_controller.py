# -*- coding: utf-8 -*-

from finicityapi.api_helper import APIHelper
from finicityapi.configuration import Configuration
from finicityapi.controllers.base_controller import BaseController
from finicityapi.http.auth.custom_header_auth import CustomHeaderAuth
from finicityapi.models.create_txpush_test_transaction_response import CreateTxpushTestTransactionResponse
from finicityapi.models.txpush_subscriptions import TxpushSubscriptions

class TxpushController(BaseController):

    """A Controller to access Endpoints in the finicityapi API."""


    def create_txpush_test_transaction(self,
                                       content_type,
                                       accept,
                                       customer_id,
                                       account_id,
                                       body):
        """Does a POST request to /aggregation/v1/customers/{customerId}/accounts/{accountId}/transactions.

        Inject a transaction into the transaction list for a testing account.
        This allows an app to trigger TxPush notifications for the account in
        order to test the app’s TxPush Listener service. This causes the
        platform to send one transaction event and one account event (showing
        that the account balance has changed). This service is only supported
        for testing accounts (accounts on institution 101732).

        Args:
            content_type (string): application/json, application/xml
            accept (string): application/json, application/xml
            customer_id (long|int): The ID of the customer who owns the
                account
            account_id (long|int): The Finicity ID of the account whose events
                will be sent to the TxPUSH Listener
            body (CreateTxpushTestTransactionRequest): TODO: type description
                here. Example: 

        Returns:
            CreateTxpushTestTransactionResponse: Response from the API.
                default response

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(content_type=content_type,
                                 accept=accept,
                                 customer_id=customer_id,
                                 account_id=account_id,
                                 body=body)

        # Prepare query URL
        _url_path = '/aggregation/v1/customers/{customerId}/accounts/{accountId}/transactions'
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
            'Content-Type': content_type,
            'Accept': accept
        }

        # Prepare and execute request
        _request = self.http_client.post(_query_url, headers=_headers, parameters=APIHelper.json_serialize(body))
        CustomHeaderAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, CreateTxpushTestTransactionResponse.from_dictionary)

    def subscribe_to_txpush_notifications(self,
                                          content_type,
                                          accept,
                                          customer_id,
                                          account_id,
                                          body):
        """Does a POST request to /aggregation/v1/customers/{customerId}/accounts/{accountId}/txpush.

        Register a client app’s TxPUSH Listener to receive TxPUSH
        notifications related to the given account.
        Each call to this service will return two records, one with class
        account and one with class transaction. Account events are sent when
        values change in the account’s fields (such as balance or
        interestRate). Transaction events are sent whenever a new transaction
        is posted for the account. For institutions that do not provide TxPUSH
        services, notifications are sent as soon as Finicity finds a new
        transaction or new account data through regular aggregation
        processes.
        The listener’s URL must be secure (https) for any real-world account.
        In addition, the client’sTxPUSH Listener will need to be verified.
        HTTP and HTTPS connections are only allowed on the standard ports 80
        (HTTP) and 443 (HTTPS). The use of other ports will result with the
        call failing. For additional details on this process please see,
        TxPUSH Listener Service.

        Args:
            content_type (string): application/json, application/xml
            accept (string): application/json, application/xml
            customer_id (long|int): The Finicity ID of the customer who owns
                the account
            account_id (long|int): The Finicity ID of the account whose events
                will be sent to the TxPUSH Listener
            body (TxpushSubscriptionRequest): TODO: type description here.
                Example: 

        Returns:
            TxpushSubscriptions: Response from the API. default response

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(content_type=content_type,
                                 accept=accept,
                                 customer_id=customer_id,
                                 account_id=account_id,
                                 body=body)

        # Prepare query URL
        _url_path = '/aggregation/v1/customers/{customerId}/accounts/{accountId}/txpush'
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
            'Content-Type': content_type,
            'Accept': accept
        }

        # Prepare and execute request
        _request = self.http_client.post(_query_url, headers=_headers, parameters=APIHelper.json_serialize(body))
        CustomHeaderAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, TxpushSubscriptions.from_dictionary)

    def disable_txpush_notifications(self,
                                     customer_id,
                                     account_id):
        """Does a DELETE request to /aggregation/v1/customers/{customerId}/accounts/{accountId}/txpush.

        Delete all TxPush subscriptions with their notifications for the
        indicated account. No more notifications will be sent for account or
        transaction events.

        Args:
            customer_id (long|int): The ID of the customer who owns the
                account
            account_id (long|int): The Finicity ID of the account whose events
                will be sent to the TxPUSH Listener

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
        _url_path = '/aggregation/v1/customers/{customerId}/accounts/{accountId}/txpush'
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

    def delete_txpush_subscription(self,
                                   customer_id,
                                   subscription_id):
        """Does a DELETE request to /aggregation/v1/customers/{customerId}/subscriptions/{subscriptionId}.

        Delete a specific subscription to TxPush notifications for the
        indicated account. This could be individual deleting the account or
        transactions events. No more events will be sent for that specific
        subscription.

        Args:
            customer_id (long|int): The ID of the customer who owns the
                account
            subscription_id (long|int): The ID of the specific subscription to
                be deleted, returned from Enable TxPUSH Notifications

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
                                 subscription_id=subscription_id)

        # Prepare query URL
        _url_path = '/aggregation/v1/customers/{customerId}/subscriptions/{subscriptionId}'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, { 
            'customerId': customer_id,
            'subscriptionId': subscription_id
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
