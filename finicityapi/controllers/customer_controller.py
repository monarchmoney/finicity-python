# -*- coding: utf-8 -*-

from finicityapi.api_helper import APIHelper
from finicityapi.configuration import Configuration
from finicityapi.controllers.base_controller import BaseController
from finicityapi.http.auth.custom_header_auth import CustomHeaderAuth
from finicityapi.models.customer import Customer
from finicityapi.models.get_customers_response import GetCustomersResponse
from finicityapi.models.add_customer_response import AddCustomerResponse
from finicityapi.models.customer_with_application_data import CustomerWithApplicationData

class CustomerController(BaseController):

    """A Controller to access Endpoints in the finicityapi API."""


    def get_customer(self,
                     content_length,
                     accept,
                     customer_id):
        """Does a GET request to /aggregation/v1/customers/{customerId}.

        Get the details for the specified customer. The service will return
        HTTP 200 upon a successful call. If the customer does not exist, the
        service will return HTTP 404.

        Args:
            content_length (string): Must be 0 (this request has no body)
            accept (string): application/json, application/xml
            customer_id (long|int): Finicity’s ID of the customer

        Returns:
            Customer: Response from the API. default response

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
        _url_path = '/aggregation/v1/customers/{customerId}'
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
        _request = self.http_client.get(_query_url, headers=_headers)
        CustomHeaderAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, Customer.from_dictionary)

    def modify_customer(self,
                        content_type,
                        customer_id,
                        body):
        """Does a PUT request to /aggregation/v1/customers/{customerId}.

        Modify the details for an enrolled customer. You must specify either
        the first name, the last name, or both in the request.
        If the service is successful, HTTP 204 (No Content) will be returned.

        Args:
            content_type (string): application/json, application/xml
            customer_id (long|int): Finicity ‘s ID of the customer to modify
            body (ModifyCustomerRequest): The information to be modified for
                the customer

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
                                 customer_id=customer_id,
                                 body=body)

        # Prepare query URL
        _url_path = '/aggregation/v1/customers/{customerId}'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, { 
            'customerId': customer_id
        })
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
        CustomHeaderAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

    def delete_customer(self,
                        customer_id):
        """Does a DELETE request to /aggregation/v1/customers/{customerId}.

        Completely remove a customer from the system. This will remove the
        customer and all associated accounts and transactions.
        (Note that the request and response is the same for JSON or XML
        clients.)
        Use this service carefully! It will not pause for confirmation before
        performing the operation!
        Success: HTTP 204 (No Content)

        Args:
            customer_id (long|int): Finicity’s ID of the customer to delete

        Returns:
            void: Response from the API. default response

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(customer_id=customer_id)

        # Prepare query URL
        _url_path = '/aggregation/v1/customers/{customerId}'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, { 
            'customerId': customer_id
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

    def get_customers(self,
                      accept,
                      search=None,
                      username=None,
                      start=1,
                      limit=25,
                      mtype=None):
        """Does a GET request to /aggregation/v1/customers.

        Find all customers enrolled by the current partner, where the search
        text is found in the customer’s username or any combination of
        firstName and lastName fields. If no search text is provided, return
        all customers.
        Valid values for type are testing, active.
        If the value of moreAvailable in the response is true, you can
        retrieve the next page of results by increasing the value of the start
        parameter in your next request:
          …&start=6&limit=5

        Args:
            accept (string): application/json, application/xml
            search (string, optional): The text you wish to match. Leave this
                empty if you wish to return all customers. Must be URL-encoded
                (see Handling Spaces in Queries)
            username (string, optional): Username for exact match. (Will
                return 0 or 1 records.)
            start (long|int, optional): Starting index for this page of
                results. The default value is 1.
            limit (long|int, optional): Maximum number of entries for this
                page of results. The default value is 25.
            mtype (string, optional): One of the values testing or active to
                return only customers of that type, or leave empty to return
                all customers.

        Returns:
            GetCustomersResponse: Response from the API. default response

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(accept=accept)

        # Prepare query URL
        _url_path = '/aggregation/v1/customers'
        _query_builder = Configuration.get_base_uri()
        _query_builder += _url_path
        _query_parameters = {
            'search': search,
            'username': username,
            'start': start,
            'limit': limit,
            'type': mtype
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
        return APIHelper.json_deserialize(_context.response.raw_body, GetCustomersResponse.from_dictionary)

    def add_customer(self,
                     accept,
                     content_type,
                     body):
        """Does a POST request to /aggregation/v2/customers/active.

        This is a version 2 service that replaces version 1. The new version
        supports passing an applicationId for assigning applicationId's to
        customers if a partner has more than one registered app.
        Enroll an active customer, which is the actual owner of one or more
        real-world accounts. This is a billable customer.
        This service is not available from the Test Drive. Calls to this
        service before enrolling in a paid plan will return HTTP 429 (Too Many
        Requests).

        Args:
            accept (string): application/json, application/xml
            content_type (string): application/json, application/xml
            body (AddCustomerRequest): The Fields For The New Customer

        Returns:
            AddCustomerResponse: Response from the API. default response

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(accept=accept,
                                 content_type=content_type,
                                 body=body)

        # Prepare query URL
        _url_path = '/aggregation/v2/customers/active'
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
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, AddCustomerResponse.from_dictionary)

    def add_testing_customer(self,
                             accept,
                             content_type,
                             body):
        """Does a POST request to /aggregation/v2/customers/testing.

        This is a version 2 service that replaces version 1. The new version
        supports passing an applicationId for assigning applicationId's to
        customers if a partner has more than one registered app.
        Enroll a testing customer that is available for Test Drive accounts.
        For using testing customers when testing Finbank OAuth register a test
        application with your systems engineer or account manager. You would
        then use that testing applicationId for the creating of any testing
        customers. Testing customers can only be assigned to testing OAuth
        applications and Testing customers can only add accounts to Finbank
        OAuth for testing OAuth implementation as well as other Finbank
        testing institutions.

        Args:
            accept (string): application/json, application/xml
            content_type (string): application/json, application/xml
            body (AddCustomerRequest): The Fields For The New Customer

        Returns:
            AddCustomerResponse: Response from the API. default response

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(accept=accept,
                                 content_type=content_type,
                                 body=body)

        # Prepare query URL
        _url_path = '/aggregation/v2/customers/testing'
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
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, AddCustomerResponse.from_dictionary)

    def get_customer_with_application_data(self,
                                           accept,
                                           customer_id):
        """Does a GET request to /aggregation/v1/customers/{customerId}/application.

        Get the details for the specified customer with additional details
        that includes the OAuth application info. The service will return HTTP
        200 upon a successful call. If the customer does not exist, the
        service will return HTTP 404.

        Args:
            accept (string): application/json, application/xml
            customer_id (long|int): Finicity’s ID of the customer

        Returns:
            CustomerWithApplicationData: Response from the API. default
                response

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
        _url_path = '/aggregation/v1/customers/{customerId}/application'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, { 
            'customerId': customer_id
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
        return APIHelper.json_deserialize(_context.response.raw_body, CustomerWithApplicationData.from_dictionary)
