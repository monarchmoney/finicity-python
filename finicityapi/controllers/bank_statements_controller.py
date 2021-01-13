# -*- coding: utf-8 -*-

from finicityapi.api_helper import APIHelper
from finicityapi.configuration import Configuration
from finicityapi.controllers.base_controller import BaseController
from finicityapi.http.auth.custom_header_auth import CustomHeaderAuth
from finicityapi.models.generate_statement_report_response import GenerateStatementReportResponse

class BankStatementsController(BaseController):

    """A Controller to access Endpoints in the finicityapi API."""


    def get_customer_account_statement(self,
                                       accept,
                                       customer_id,
                                       account_id,
                                       index=1):
        """Does a GET request to /aggregation/v1/customers/{customerId}/accounts/{accountId}/statement.

        Connect to the account’s financial institution and download the most
        recent monthly statement for the account, in PDF format. This is an
        interactive refresh, so MFA challenges may be required.
        The index parameter allows an app to request statements earlier than
        the most recent one. The default is 1, meaning the most recent
        statement. Another value such as 3 would mean to count back and
        retrieve the third most recent statement. For example, if a request is
        made in July, the most recent statement (index 1) would probably be
        for June, and the third most recent statement (index 3) would be for
        April.
        This is a premium service. The billing rate is the variable rate for
        Account Ownership Verification under the current subscription plan.
        The billable event is a successful call to this service.
        HTTP status of 200 means the statement was retrieved successfully, and
        the body of the response contains the bytes of the PDF document.
        HTTP status of 203 means the response contains an MFA challenge in XML
        or JSON format. Contact your Account Manager or Systems Engineers to
        determine the best route to handle this HTTP status code.
        The recommended timeout setting for this request is 180 seconds in
        order to receive a response.
        Statements are only available for specific account types: checking,
        savings, money market, CDs, and investments.
        Statements are not available for the following account types:
        mortgage, credit card, line of credit, loan

        Args:
            accept (string): application/pdf, application/json (the document
                will be in PDF format, but errors will be JSON)
            customer_id (long|int): Finicity ‘s ID for the customer who owns
                the account
            account_id (long|int): Finicity’s ID of the account
            index (int, optional): Index of statement to retrieve (default is
                1, maximum is 6)

        Returns:
            binary: Response from the API. default response

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
        _url_path = '/aggregation/v1/customers/{customerId}/accounts/{accountId}/statement'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, { 
            'customerId': customer_id,
            'accountId': account_id
        })
        _query_builder = Configuration.get_base_uri()
        _query_builder += _url_path
        _query_parameters = {
            'index': index
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
        _context = self.execute_request(_request, binary = True)
        self.validate_response(_context)

        # Return appropriate type
        return _context.response.raw_body

    def generate_statement_report(self,
                                  accept,
                                  customer_id,
                                  body,
                                  callback_url=None):
        """Does a POST request to /decisioning/v2/customers/{customerId}/statement.

        Generate a Statement Report report for specified accounts under the
        given customer. This report requires a consumer. 
        The service returns immediately with status HTTP 202 (Accepted). When
        finished, a notification will be sent to the specified report callback
        URL, if specified.
        This is a premium service. A billable event will be created upon the
        successful generation of the Statement Report. 
        After making this call, the client app may wait for a notification to
        be sent to the Report Listener Service, or it may enter a loop, which
        should wait 20 seconds and then call the service Get Report to see if
        the report is finished. While the report is being generated, Get
        Report will return a minimal report including status inProgress. The
        loop should repeat every 20 seconds until Get Report returns a
        different status.
        A Report Consumer must be created for the given Customer (using Create
        Report Consumer) before calling this service. If no Report Consumer
        has been created, the service will return HTTP 400 (Bad Request).

        Args:
            accept (string): Replace 'json' with 'xml' if preferred
            customer_id (long|int): ID of the customer
            body (GenerateStatementReportConstraints): TODO: type description
                here. Example: 
            callback_url (string, optional): The Report Listener URL to
                receive notifications (optional, must be URL-encoded)

        Returns:
            GenerateStatementReportResponse: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(accept=accept,
                                 customer_id=customer_id,
                                 body=body)

        # Prepare query URL
        _url_path = '/decisioning/v2/customers/{customerId}/statement'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, { 
            'customerId': customer_id
        })
        _query_builder = Configuration.get_base_uri()
        _query_builder += _url_path
        _query_parameters = {
            'callbackUrl': callback_url
        }
        _query_builder = APIHelper.append_url_with_query_parameters(_query_builder,
            _query_parameters, Configuration.array_serialization)
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
        return APIHelper.json_deserialize(_context.response.raw_body, GenerateStatementReportResponse.from_dictionary)
