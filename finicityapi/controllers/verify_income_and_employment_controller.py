# -*- coding: utf-8 -*-

from finicityapi.api_helper import APIHelper
from finicityapi.configuration import Configuration
from finicityapi.controllers.base_controller import BaseController
from finicityapi.http.auth.custom_header_auth import CustomHeaderAuth
from finicityapi.models.generate_pay_statement_report_response import GeneratePayStatementReportResponse
from finicityapi.models.generate_voie_paystub_with_txverify_report_response import GenerateVOIEPaystubWithTxverifyReportResponse
from finicityapi.models.refresh_voie_payroll_report_response import RefreshVOIEPayrollReportResponse
from finicityapi.exceptions.error_1_error_exception import Error1ErrorException

class VerifyIncomeAndEmploymentController(BaseController):

    """A Controller to access Endpoints in the finicityapi API."""


    def generate_pay_statement_report(self,
                                      customer_id,
                                      accept,
                                      content_type,
                                      body,
                                      callback_url=None):
        """Does a POST request to /decisioning/v2/customers/{customerId}/payStatement.

        Generate Pay Statement Extraction Report for the given customer. This
        service accepts asset IDs of the stored pay statements to generate a
        Pay Statement Extraction Report. 
        This is a premium service. The billing rate is the variable rate for
        Pay Statement Extraction Report under the current subscription plan.
        The billable event is the successful generation of a Pay Statement
        Extraction Report.
        The service returns immediately with status HTTP 202 (Accepted) if
        successful. When finished, a notification will be sent to the
        specified report callback URL, if specified.
        After making this call, the client app may wait for a notification to
        be sent to the Report Listener Service, or it may enter a loop, which
        should wait 20 seconds and then call the service Get Report to see if
        the report is finished. While the report is being generated, Get
        Report will return a minimal report including status inProgress. The
        loop should repeat every 20 seconds until Get Report returns a
        different status.
        The service will return HTTP 400 (Bad Request) if the asset ID does
        not exist within Finicity?s system.

        Args:
            customer_id (long|int): Finicity ID of the customer
            accept (string): Replace 'json' with 'xml' if preferred
            content_type (string): Replace 'json' with 'xml' if preferred
            body (PayStatementConstraints): TODO: type description here.
                Example: 
            callback_url (string, optional): The Report Listener URL to
                receive notifications (optional, must be URL-encoded).

        Returns:
            GeneratePayStatementReportResponse: Response from the API.
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
                                 content_type=content_type,
                                 body=body)

        # Prepare query URL
        _url_path = '/decisioning/v2/customers/{customerId}/payStatement'
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
        return APIHelper.json_deserialize(_context.response.raw_body, GeneratePayStatementReportResponse.from_dictionary)

    def generate_voie_paystub_with_txverify_report(self,
                                                   customer_id,
                                                   accept,
                                                   content_type,
                                                   body,
                                                   callback_url=None):
        """Does a POST request to /decisioning/v2/customers/{customerId}/voieTxVerify/withInterview.

        Generate a VOIE - Paystub (with TXVerify) with Interview report for
        all checking and savings under the given customer. This service
        retrieves up to two years of transaction history for the given
        accounts. It then uses this information as well as the provided
        paystubs to generate the VOIE TXVerify report.
        This is a premium service. The billing rate is the variable rate for
        VOIE TXVerify under the current subscription plan. The billable event
        is the successful generation of a VOIE TXVerify Report.
        The service returns immediately with status HTTP 202 (Accepted). When
        finished, a notification will be sent to the specified report callback
        URL, if specified.
        After making this call, the client app may wait for a notification to
        be sent to the Report Listener Service, or it may enter a loop, which
        should wait 20 seconds and then call the service Get Report to see if
        the report is finished. While the report is being generated, Get
        Report will return a minimal report including status inProgress. The
        loop should repeat every 20 seconds until Get Report returns a
        different status.
        When the call cannot be processed due to invalid input, the service
        will return HTTP 400 (Bad Request).

        Args:
            customer_id (long|int): Finicity ID for the customer
            accept (string): application/json or application/xml
            content_type (string): application/json or application/xml
            body (VOIETxverifyConstraints): TODO: type description here.
                Example: 
            callback_url (string, optional): The Report Listener URL to
                receive notifications (optional, must be URL-encoded).

        Returns:
            GenerateVOIEPaystubWithTxverifyReportResponse: Response from the
                API. Accepted

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(customer_id=customer_id,
                                 accept=accept,
                                 content_type=content_type,
                                 body=body)

        # Prepare query URL
        _url_path = '/decisioning/v2/customers/{customerId}/voieTxVerify/withInterview'
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
        return APIHelper.json_deserialize(_context.response.raw_body, GenerateVOIEPaystubWithTxverifyReportResponse.from_dictionary)

    def refresh_voie_payroll_report(self,
                                    customer_id,
                                    accept,
                                    content_type,
                                    body,
                                    callback_url=None):
        """Does a POST request to /decisioning/v2/customers/{customerId}/voiePayrollProvider.

        The VOIE – Payroll report generates when the customer completes
        Connect. Lenders, who commonly use this report for pre-close
        verification employment check, can refresh this report by passing the
        consumer’s SSN, DOB, and the `reportId` from the first VOIE – Payroll
        report they received.
         
        We’ll refresh this report and update any new pay histories since the
        first report generated, including borrower’s employment status as
        active or not.
         
        Note: Lenders can only refresh this report one time in a 60-day period
        starting from the date of the first report. Any further report
        refreshes will incur additional charges.
         
        The service immediately returns the status HTTP 202 (accepted). A
        notification gets sent to the report callback URL, if specified.
         
        After the call is made, the client’s application can wait for a
        notification sent by the Report Listener Service. Or it may enter a
        loop, which waits about 20 seconds and then calls the service, Get
        Report to check if the report is finished.
         
        While the report’s generating, Get Report returns a minimal report
        with a status of InProgress.  The loop repeats every 20 seconds until
        Get Report returns a different status.

        Args:
            customer_id (long|int): Finicity ID for the customer
            accept (string): application/json
            content_type (string): application/json
            body (VOIEPayrollReportRefreshConstraints): TODO: type description
                here. Example: 
            callback_url (string, optional): The Report Listener URL to
                receive notifications (optional, must be URL-encoded).

        Returns:
            RefreshVOIEPayrollReportResponse: Response from the API. Accepted

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(customer_id=customer_id,
                                 accept=accept,
                                 content_type=content_type,
                                 body=body)

        # Prepare query URL
        _url_path = '/decisioning/v2/customers/{customerId}/voiePayrollProvider'
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
        return APIHelper.json_deserialize(_context.response.raw_body, RefreshVOIEPayrollReportResponse.from_dictionary)
