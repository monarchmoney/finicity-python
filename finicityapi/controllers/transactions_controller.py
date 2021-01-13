# -*- coding: utf-8 -*-

from finicityapi.api_helper import APIHelper
from finicityapi.configuration import Configuration
from finicityapi.controllers.base_controller import BaseController
from finicityapi.http.auth.custom_header_auth import CustomHeaderAuth
from finicityapi.models.transaction import Transaction
from finicityapi.models.get_transactions_response import GetTransactionsResponse
from finicityapi.models.generate_transactions_report_response import GenerateTransactionsReportResponse

class TransactionsController(BaseController):

    """A Controller to access Endpoints in the finicityapi API."""


    def get_customer_transaction(self,
                                 accept,
                                 customer_id,
                                 transaction_id):
        """Does a GET request to /aggregation/v2/customers/{customerId}/transactions/{transactionId}.

        Get details for the specified transaction.

        Args:
            accept (string): application/json, application/xml
            customer_id (string): Finicity ID for the customer whose
                transactions are to be retrieved
            transaction_id (string): The transaction to be retrieved

        Returns:
            Transaction: Response from the API. default response

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(accept=accept,
                                 customer_id=customer_id,
                                 transaction_id=transaction_id)

        # Prepare query URL
        _url_path = '/aggregation/v2/customers/{customerId}/transactions/{transactionId}'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, { 
            'customerId': customer_id,
            'transactionId': transaction_id
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
        return APIHelper.json_deserialize(_context.response.raw_body, Transaction.from_dictionary)

    def get_customer_transactions_all(self,
                                      accept,
                                      customer_id,
                                      from_date,
                                      to_date,
                                      start=1,
                                      limit=1000,
                                      sort='desc',
                                      include_pending=False):
        """Does a GET request to /aggregation/v3/customers/{customerId}/transactions.

        Get all transactions available for this customer within the given date
        range, across all accounts. This service supports paging and sorting
        by transactionDate (or postedDate if no transaction date is provided),
        with a maximum of 1000 transactions per request.
        Standard consumer aggregation provides up to 180 days of transactions
        prior to the date each account was added to the Finicity system. To
        access older transactions, you must first call the service Load
        Historic Transactions for Account.
        There is no limit for the size of the window between fromDate and
        toDate; however, the maximum number of transactions returned in one
        page is 1000.
        If the value of moreAvailable in the response is true, you can
        retrieve the next page of results by increasing the value of the start
        parameter in your next request:
          …&start=6&limit=5

        Args:
            accept (string): application/json, application/xml
            customer_id (long|int): The ID of the customer whose transactions
                are to be retrieved
            from_date (long|int): Starting timestamp for the date range
                (required) (see Handling Dates and Times)
            to_date (long|int): Ending timestamp for the date range (required,
                must be greater than fromDate) (see Handling Dates and Times)
            start (long|int, optional): Starting index for this page of
                results
            limit (long|int, optional): Maximum number of entries for this
                page of results (max is 1000)
            sort (string, optional): Sort order: asc for ascending order
                (oldest transactions are on page 1), descfor descending order
                (newest transactions are on page 1).
            include_pending (bool, optional): true to include pending
                transactions if available.

        Returns:
            GetTransactionsResponse: Response from the API. default response

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(accept=accept,
                                 customer_id=customer_id,
                                 from_date=from_date,
                                 to_date=to_date)

        # Prepare query URL
        _url_path = '/aggregation/v3/customers/{customerId}/transactions'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, { 
            'customerId': customer_id
        })
        _query_builder = Configuration.get_base_uri()
        _query_builder += _url_path
        _query_parameters = {
            'fromDate': from_date,
            'toDate': to_date,
            'start': start,
            'limit': limit,
            'sort': sort,
            'includePending': include_pending
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
        return APIHelper.json_deserialize(_context.response.raw_body, GetTransactionsResponse.from_dictionary)

    def get_customer_account_transactions(self,
                                          accept,
                                          customer_id,
                                          account_id,
                                          from_date,
                                          to_date,
                                          start=1,
                                          limit=1000,
                                          sort='desc',
                                          include_pending=False):
        """Does a GET request to /aggregation/v3/customers/{customerId}/accounts/{accountId}/transactions.

        Get all transactions available for this customer account within the
        given date range. This service supports paging and sorting by
        transactionDate (or postedDate if no transaction date is provided),
        with a maximum of 1000 transactions per request.
        Standard consumer aggregation provides up to 180 days of transactions
        prior to the date each account was added to the Finicity system. To
        access older transactions, you must first call the Cash Flow
        Verification service Load Historic Transactions for Account.
        There is no limit for the size of the window between fromDate and
        toDate; however, the maximum number of transactions returned in one
        page is 1000.
        If the value of moreAvailable in the response is true, you can
        retrieve the next page of results by increasing the value of the start
        parameter in your next request:
        …&start=6&limit=5

        Args:
            accept (string): application/json, application/xml
            customer_id (long|int): The ID of the customer whose transactions
                are to be retrieved
            account_id (string): Finicity’s ID of the account whose
                transactions are to be retrieved
            from_date (long|int): Starting timestamp for the date range
                (required) (see Handling Dates and Times)
            to_date (long|int): Ending timestamp for the date range (required,
                must be greater than fromDate) (see Handling Dates and Times)
            start (long|int, optional): Starting index for this page of
                results
            limit (long|int, optional): Maximum number of entries for this
                page of results (max is 1000)
            sort (string, optional): Sort order: asc for ascending order
                (oldest transactions are on page 1), descfor descending order
                (newest transactions are on page 1).
            include_pending (bool, optional): true to include pending
                transactions if available.

        Returns:
            GetTransactionsResponse: Response from the API. default response

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(accept=accept,
                                 customer_id=customer_id,
                                 account_id=account_id,
                                 from_date=from_date,
                                 to_date=to_date)

        # Prepare query URL
        _url_path = '/aggregation/v3/customers/{customerId}/accounts/{accountId}/transactions'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, { 
            'customerId': customer_id,
            'accountId': account_id
        })
        _query_builder = Configuration.get_base_uri()
        _query_builder += _url_path
        _query_parameters = {
            'fromDate': from_date,
            'toDate': to_date,
            'start': start,
            'limit': limit,
            'sort': sort,
            'includePending': include_pending
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
        return APIHelper.json_deserialize(_context.response.raw_body, GetTransactionsResponse.from_dictionary)

    def generate_transactions_report(self,
                                     accept,
                                     callback_url,
                                     customer_id,
                                     body,
                                     from_date,
                                     to_date,
                                     include_pending):
        """Does a POST request to /decisioning/v2/customers/{customerId}/transactions.

        Generate a Transaction Report for specified accounts under the given
        customer. This service retrieves up to 24 months of transaction
        history for the given customer. It then uses this information to
        generate the Transaction Report. 
        The service returns immediately with status HTTP 202 (Accepted). When
        finished, a notification will be sent to the specified report callback
        URL, if specified.
        This is a premium service. A billable event will be created upon the
        successful generation of the Transactions Report. 
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
        There cannot be more than 24 months between fromDate and toDate.

        Args:
            accept (string): JSON or XML output.
            callback_url (string): The Report Listener URL to receive
                notifications (optional, must be URL-encoded)
            customer_id (long|int): ID of the customer
            body (GenerateTransactionsReportConstraints): TODO: type
                description here. Example: 
            from_date (long|int): The `fromDate` param is an Epoch Timestamp
                (in seconds).  It must be 10 digits long and within two years
                of the present day.    Example: ?fromDate=1494449017.   If
                fromDate is not used or it’s longer than 10 digits, the
                transaction report history defaults to 24 months of data.   
                (Optional)
            to_date (long|int): The ending timestamp for the date range. The
                value must be greater than fromDate. See Handling Dates and
                Times.
            include_pending (bool): True: Include pending transactions in the
                report. False: Set by default.

        Returns:
            GenerateTransactionsReportResponse: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(accept=accept,
                                 callback_url=callback_url,
                                 customer_id=customer_id,
                                 body=body,
                                 from_date=from_date,
                                 to_date=to_date,
                                 include_pending=include_pending)

        # Prepare query URL
        _url_path = '/decisioning/v2/customers/{customerId}/transactions'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, { 
            'customerId': customer_id
        })
        _query_builder = Configuration.get_base_uri()
        _query_builder += _url_path
        _query_parameters = {
            'callbackUrl': callback_url,
            'fromDate': from_date,
            'toDate': to_date,
            'includePending': include_pending
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
        return APIHelper.json_deserialize(_context.response.raw_body, GenerateTransactionsReportResponse.from_dictionary)
