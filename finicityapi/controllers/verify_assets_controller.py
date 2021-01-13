# -*- coding: utf-8 -*-

from finicityapi.api_helper import APIHelper
from finicityapi.configuration import Configuration
from finicityapi.controllers.base_controller import BaseController
from finicityapi.http.auth.custom_header_auth import CustomHeaderAuth
from finicityapi.models.generate_voa_report_response import GenerateVOAReportResponse
from finicityapi.models.generate_voa_with_income_report_response import GenerateVOAWithIncomeReportResponse
from finicityapi.models.generate_prequalification_report_response import GeneratePrequalificationReportResponse
from finicityapi.models.generate_asset_summary_report_response import GenerateAssetSummaryReportResponse
from finicityapi.exceptions.error_1_error_exception import Error1ErrorException

class VerifyAssetsController(BaseController):

    """A Controller to access Endpoints in the finicityapi API."""


    def generate_voa_report(self,
                            customer_id,
                            accept,
                            content_type,
                            callback_url=None,
                            from_date=None,
                            body=None):
        """Does a POST request to /decisioning/v2/customers/{customerId}/voa.

        Generate a Verification of Assets (VOA) report for all checking,
        savings, money market, and investment accounts for the given customer.
        This service retrieves up to six months of transaction history for
        each account and uses this information to generate the VOA report.
        This is a premium service. The billing rate is the variable rate for
        Verification of Assets under the current subscription plan. The
        billable event is the successful generation of a VOA report.
        HTTP status of 202 (Accepted) means the report is being generated.
        When the report is finished, a notification will be sent to the
        specified report callback URL, if specified.
        If no account of type of checking, savings, money market, or
        investment is found, the service will return HTTP 400 (Bad Request).

        Args:
            customer_id (long|int): Finicity ID for the customer
            accept (string): Replace 'json' with 'xml' if preferred
            content_type (string): Replace 'json' with 'xml' if preferred
            callback_url (string, optional): The Report Listener URL to
                receive notifications (optional, must be URL-encoded).
            from_date (long|int, optional): The fromDate parameter is an Epoch
                Timestamp (in seconds), such as '1494449017'. Without this
                parameter, the report defaults to 61 days if available.
                Example: ?fromDate={fromDate}. If included, the epoch
                timestamp should be 10 digits long and be within six months of
                the present day. Extending the epoch timestamp beyond 10
                digits will default back to six months of data. This query is
                optional
            body (RequestConstraints, optional): TODO: type description here.
                Example: 

        Returns:
            GenerateVOAReportResponse: Response from the API. Accepted

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
        _url_path = '/decisioning/v2/customers/{customerId}/voa'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, { 
            'customerId': customer_id
        })
        _query_builder = Configuration.get_base_uri()
        _query_builder += _url_path
        _query_parameters = {
            'callbackUrl': callback_url,
            'fromDate': from_date
        }
        _query_builder = APIHelper.append_url_with_query_parameters(_query_builder,
            _query_parameters, Configuration.array_serialization)
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
        if _context.response.status_code == 400:
            raise Error1ErrorException('Bad Request', _context)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, GenerateVOAReportResponse.from_dictionary)

    def generate_voa_with_income_report(self,
                                        customer_id,
                                        accept,
                                        content_type,
                                        callback_url=None,
                                        from_date=None,
                                        body=None):
        """Does a POST request to /decisioning/v2/customers/{customerId}/voaHistory.

        Generate a Verification of Assets with GSE Income View (VOAHistory)
        report for all checking, savings, money market, and investment
        accounts for the given customer. This service retrieves up to 24
        months of transaction history for each account and uses this
        information to generate the VOAHistory report.
        This is a premium service. The billing rate is the variable rate for
        Verification of Assets under the current subscription plan. The
        billable event is the successful generation of a VOAhistory report.
        A report consumer must be created for the given customer before
        calling Generate VOAHistory Report (see Report Consumers).
        After making this call, the client app may wait for a notification to
        be sent to the Report Listener Service, or it may enter a loop, which
        should wait 20 seconds and then call the service Get Report to see if
        the report is finished. While the report is being generated, Get
        Report will return a minimal report with status inProgress. The loop
        should repeat every 20 seconds until Get Report returns a different
        status.
        If using the listener service, the following format must be followed
        and the webhook must respond to the Finicity API with a 200 series
        code:
        https://api.finicity.com/decisioning/v2/customers/[customerId]/voaHisto
        ry?callbackUrl=[webhookUrl]
        HTTP status of 202 (Accepted) means the report is being generated.
        When the report is finished, a notification will be sent to the
        specified report callback URL, if specified.
        If no account of type of checking, savings, money market, or
        investment is found, the service will return HTTP 400 (Bad Request).

        Args:
            customer_id (long|int): Finicity Id of the customer
            accept (string): Replace 'json' with 'xml' if preferred
            content_type (string): Replace 'json' with 'xml' if preferred
            callback_url (string, optional): The Report Listener URL to
                receive notifications (optional, must be URL-encoded).
            from_date (long|int, optional): The fromDate parameter is an Epoch
                Timestamp (in seconds), such as ?1494449017?. Without this
                parameter, the report defaults to 61 days if available. This
                will limit the amount of credit and debit transactions
                included in the report up to the date specified, but will not
                limit the amount of income stream transactions. The income
                stream transactions are all included, up to 24 months, to help
                the lender and GSE's have the full history to validate income.
                Example: ?fromDate={fromDate}If included, the epoch timestamp
                should be 10 digits long and be within two years of the
                present day. Extending the epoch timestamp beyond 10 digits
                will default back to 2 years of data. This query is optional.
            body (RequestConstraints, optional): TODO: type description here.
                Example: 

        Returns:
            GenerateVOAWithIncomeReportResponse: Response from the API.
                Accepted

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
        _url_path = '/decisioning/v2/customers/{customerId}/voaHistory'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, { 
            'customerId': customer_id
        })
        _query_builder = Configuration.get_base_uri()
        _query_builder += _url_path
        _query_parameters = {
            'callbackUrl': callback_url,
            'fromDate': from_date
        }
        _query_builder = APIHelper.append_url_with_query_parameters(_query_builder,
            _query_parameters, Configuration.array_serialization)
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
        if _context.response.status_code == 400:
            raise Error1ErrorException('Bad Request', _context)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, GenerateVOAWithIncomeReportResponse.from_dictionary)

    def generate_prequalification_report(self,
                                         customer_id,
                                         accept,
                                         content_type,
                                         callback_url=None,
                                         body=None):
        """Does a POST request to /decisioning/v2/customers/{customerId}/preQualVoa.

        Generate a Prequalification Report (preQualVoa) for all checking,
        savings, money market, and investment accounts for the given customer.
        This service retrieves account and owner information as well as the
        number of NSFs for any account that is a checking account for the
        customer. 
        This is a premium service. The billing rate is billed per report for
        the Prequalification report. 
        After making this call, the client app may wait for a notification to
        be sent to the Report Listener Service, or it may enter a loop, which
        should wait 20 seconds and then call the service Get Report to see if
        the report is finished. While the report is being generated, Get
        Report will return a minimal report with status inProgress. The loop
        should repeat every 20 seconds until Get Report returns a different
        status.
        If using the listener service, the following format must be followed
        and the webhook must respond to the Finicity API with a 200 series
        code:
        https://api.finicity.com/decisioning/v2/customers/[customerId]/preQualV
        oa?callbackUrl=[webhookUrl]
        HTTP status of 202 (Accepted) means the report is being generated.
        When the report is finished, a notification will be sent to the
        specified report callback URL, if specified.
        If no account type of checking, savings, money market, or investment
        is found, the service will return HTTP 400 (Bad Request).

        Args:
            customer_id (long|int): Finicity's ID of the customer
            accept (string): Replace 'json' with 'xml' if preferred
            content_type (string): Replace 'json' with 'xml' if preferred
            callback_url (string, optional): The Report Listener URL to
                receive notifications (optional, must be URL-encoded).
            body (RequestConstraints, optional): TODO: type description here.
                Example: 

        Returns:
            GeneratePrequalificationReportResponse: Response from the API.
                Accepted

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
        _url_path = '/decisioning/v2/customers/{customerId}/preQualVoa'
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
            'Finicity-App-Key': Configuration.finicity_app_key,
            'Accept': accept,
            'Content-Type': content_type
        }

        # Prepare and execute request
        _request = self.http_client.post(_query_url, headers=_headers, parameters=APIHelper.json_serialize(body))
        CustomHeaderAuth.apply(_request)
        _context = self.execute_request(_request)

        # Endpoint and global error handling using HTTP status codes.
        if _context.response.status_code == 400:
            raise Error1ErrorException('Bad Request', _context)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, GeneratePrequalificationReportResponse.from_dictionary)

    def generate_asset_summary_report(self,
                                      customer_id,
                                      accept,
                                      content_type,
                                      callback_url=None,
                                      body=None):
        """Does a POST request to /decisioning/v2/customers/{customerId}/assetSummary.

        Generate Asset Summary report (assetSummary) for all checking,
        savings, money market, and investment accounts for the given customer.
        This service retrieves account and owner information as well as the
        number of NSFs for any account that is a checking account for the
        customer. 
        This is a premium service. The billing rate is billed per report for
        the Asset Summary report. 
        After making this call, the client app may wait for a notification to
        be sent to the Report Listener Service, or it may enter a loop, which
        should wait 20 seconds and then call the service Get Report to see if
        the report is finished. While the report is being generated, Get
        Report will return a minimal report with status inProgress. The loop
        should repeat every 20 seconds until Get Report returns a different
        status.
        If using the listener service, the following format must be followed
        and the webhook must respond to the Finicity API with a 200 series
        code:
        https://api.finicity.com/decisioning/v2/customers/[customerId]/assetSum
        mary?callbackUrl=[webhookUrl]
        HTTP status of 202 (Accepted) means the report is being generated.
        When the report is finished, a notification will be sent to the
        specified report callback URL, if specified.
        If no account type of checking, savings, money market, or investment
        is found, the service will return HTTP 400 (Bad Request).

        Args:
            customer_id (long|int): Finicity's ID of the customer
            accept (string): Replace 'json' with 'xml' if preferred
            content_type (string): Replace 'json' with 'xml' if preferred
            callback_url (string, optional): The Report Listener URL to
                receive notifications (optional, must be URL-encoded).
            body (RequestConstraints, optional): TODO: type description here.
                Example: 

        Returns:
            GenerateAssetSummaryReportResponse: Response from the API.
                Accepted

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
        _url_path = '/decisioning/v2/customers/{customerId}/assetSummary'
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
            'Finicity-App-Key': Configuration.finicity_app_key,
            'Accept': accept,
            'Content-Type': content_type
        }

        # Prepare and execute request
        _request = self.http_client.post(_query_url, headers=_headers, parameters=APIHelper.json_serialize(body))
        CustomHeaderAuth.apply(_request)
        _context = self.execute_request(_request)

        # Endpoint and global error handling using HTTP status codes.
        if _context.response.status_code == 400:
            raise Error1ErrorException('Bad Request', _context)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, GenerateAssetSummaryReportResponse.from_dictionary)
