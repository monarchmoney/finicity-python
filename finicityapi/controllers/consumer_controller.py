# -*- coding: utf-8 -*-

from finicityapi.api_helper import APIHelper
from finicityapi.configuration import Configuration
from finicityapi.controllers.base_controller import BaseController
from finicityapi.http.auth.custom_header_auth import CustomHeaderAuth
from finicityapi.models.consumer import Consumer
from finicityapi.models.create_consumer_response import CreateConsumerResponse
from finicityapi.exceptions.error_1_error_exception import Error1ErrorException

class ConsumerController(BaseController):

    """A Controller to access Endpoints in the finicityapi API."""


    def get_consumer_for_customer(self,
                                  customer_id,
                                  accept,
                                  content_type):
        """Does a GET request to /decisioning/v1/customers/{customerId}/consumer.

        Get the details of a consumer record.
        If the service is successful, HTTP 200 (Accepted) will be returned. If
        the customer does not exist, the service will return HTTP 404 (Not
        Found)

        Args:
            customer_id (long|int): Finicity’s ID of the customer
            accept (string): Replace 'json' with 'xml' if preferred
            content_type (string): Replace 'json' with 'xml' if preferred

        Returns:
            Consumer: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(customer_id=customer_id,
                                 accept=accept,
                                 content_type=content_type)

        # Prepare query URL
        _url_path = '/decisioning/v1/customers/{customerId}/consumer'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, { 
            'customerId': customer_id
        })
        _query_builder = Configuration.get_base_uri()
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'Finicity-App-Key': Configuration.finicity_app_key,
            'Accept': accept,
            'Content-Type': content_type
        }

        # Prepare and execute request
        _request = self.http_client.get(_query_url, headers=_headers)
        CustomHeaderAuth.apply(_request)
        _context = self.execute_request(_request)

        # Endpoint and global error handling using HTTP status codes.
        if _context.response.status_code == 404:
            raise Error1ErrorException('Bad Request', _context)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, Consumer.from_dictionary)

    def create_consumer(self,
                        customer_id,
                        body,
                        accept,
                        content_type):
        """Does a POST request to /decisioning/v1/customers/{customerId}/consumer.

        Create a consumer record associated with the given customer. A
        consumer persists as the owner of any reports that are generated, even
        after the original customer is deleted from the system. A consumer
        must be created for the given customer before calling any of the
        Generate Report services.
        If a consumer already exists for this customer, this service will
        return HTTP 409 (Conflict). If the consumer is successfully created,
        the service will return HTTP 201 (Created).

        Args:
            customer_id (long|int): Finicity’s ID for the customer
            body (CreateConsumerRequest): TODO: type description here.
                Example: 
            accept (string): Replace 'json' with 'xml' if preferred
            content_type (string): Replace 'json' with 'xml' if preferred

        Returns:
            CreateConsumerResponse: Response from the API. Created

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(customer_id=customer_id,
                                 body=body,
                                 accept=accept,
                                 content_type=content_type)

        # Prepare query URL
        _url_path = '/decisioning/v1/customers/{customerId}/consumer'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, { 
            'customerId': customer_id
        })
        _query_builder = Configuration.get_base_uri()
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'Finicity-App-Key': Configuration.finicity_app_key,
            'Accept': accept,
            'Content-Type': content_type
        }

        # Prepare and execute request
        _request = self.http_client.post(_query_url, headers=_headers, parameters=APIHelper.json_serialize(body))
        CustomHeaderAuth.apply(_request)
        _context = self.execute_request(_request)

        # Endpoint and global error handling using HTTP status codes.
        if _context.response.status_code == 404:
            raise Error1ErrorException('Bad Request', _context)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, CreateConsumerResponse.from_dictionary)

    def get_consumer(self,
                     consumer_id,
                     accept,
                     content_type):
        """Does a GET request to /decisioning/v1/consumers/{consumerId}.

        Get the details of a consumer record. If the service successfully
        retrieves the consumer record, HTTP 200 will be returned. If the
        consumer does not exist, the service will return HTTP 404.

        Args:
            consumer_id (string): Finicity’s ID of the consumer (UUID with max
                length 32 characters)
            accept (string): Replace 'json' with 'xml' if preferred
            content_type (string): Replace 'json' with 'xml' if preferred

        Returns:
            Consumer: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(consumer_id=consumer_id,
                                 accept=accept,
                                 content_type=content_type)

        # Prepare query URL
        _url_path = '/decisioning/v1/consumers/{consumerId}'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, { 
            'consumerId': consumer_id
        })
        _query_builder = Configuration.get_base_uri()
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'Finicity-App-Key': Configuration.finicity_app_key,
            'Accept': accept,
            'Content-Type': content_type
        }

        # Prepare and execute request
        _request = self.http_client.get(_query_url, headers=_headers)
        CustomHeaderAuth.apply(_request)
        _context = self.execute_request(_request)

        # Endpoint and global error handling using HTTP status codes.
        if _context.response.status_code == 404:
            raise Error1ErrorException('Bad Request', _context)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, Consumer.from_dictionary)

    def modify_consumer(self,
                        consumer_id,
                        body,
                        accept,
                        content_type):
        """Does a PUT request to /decisioning/v1/consumers/{consumerId}.

        Modify the details for an existing consumer. All fields are required
        for a consumer record, but individual fields for this call are
        optional because fields that are not specified will be left
        unchanged.
        If the service is successful, HTTP 204 (No Content) will be returned.
        If the consumer does not exist, the service will return HTTP 404.

        Args:
            consumer_id (string): Finicity ID of the consumer (UUID with max
                length 32 characters)
            body (ModifyConsumerRequest): Consumer details
            accept (string): Replace 'json' with 'xml' if preferred
            content_type (string): Replace 'json' with 'xml' if preferred

        Returns:
            void: Response from the API. No Content

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(consumer_id=consumer_id,
                                 body=body,
                                 accept=accept,
                                 content_type=content_type)

        # Prepare query URL
        _url_path = '/decisioning/v1/consumers/{consumerId}'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, { 
            'consumerId': consumer_id
        })
        _query_builder = Configuration.get_base_uri()
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'Finicity-App-Key': Configuration.finicity_app_key,
            'Accept': accept,
            'Content-Type': content_type
        }

        # Prepare and execute request
        _request = self.http_client.put(_query_url, headers=_headers, parameters=APIHelper.json_serialize(body))
        CustomHeaderAuth.apply(_request)
        _context = self.execute_request(_request)

        # Endpoint and global error handling using HTTP status codes.
        if _context.response.status_code == 404:
            raise Error1ErrorException('Bad Request', _context)
        self.validate_response(_context)
