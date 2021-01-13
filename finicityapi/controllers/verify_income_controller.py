# -*- coding: utf-8 -*-

from finicityapi.api_helper import APIHelper
from finicityapi.configuration import Configuration
from finicityapi.controllers.base_controller import BaseController
from finicityapi.http.auth.custom_header_auth import CustomHeaderAuth
from finicityapi.models.generate_voi_report_response import GenerateVOIReportResponse
from finicityapi.exceptions.error_1_error_exception import Error1ErrorException

class VerifyIncomeController(BaseController):

    """A Controller to access Endpoints in the finicityapi API."""


    def generate_voi_report(self,
                            customer_id,
                            accept,
                            content_type,
                            callback_url=None,
                            body=None):
        """Does a POST request to /decisioning/v2/customers/{customerId}/voi.

        Generate a Verification of Income (VOI) report for all checking,
        savings, and money market accounts for the given customer. This
        service retrieves up to two years of transaction history for each
        account and uses this information to generate the VOI report.
        This is a premium service. The billing rate is the variable rate for
        Verification of Income under the current subscription plan. The
        billable event is the successful generation of a VOI report.
        HTTP status of 202 (Accepted) means the report is being generated.
        When the report is finished, a notification will be sent to the
        specified report callback URL, if specified.
        If no account of type of checking, savings, or money market is found,
        the service will return HTTP 400 (Bad Request).

        Args:
            customer_id (long|int): Finicity ID for the customer
            accept (string): Replace 'json' with 'xml' if preferred
            content_type (string): Replace 'json' with 'xml' if preferred
            callback_url (string, optional): The Report Listener URL to
                receive notifications (optional, must be URL-encoded).
            body (RequestConstraints, optional): TODO: type description here.
                Example: 

        Returns:
            GenerateVOIReportResponse: Response from the API. Accepted

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
        _url_path = '/decisioning/v2/customers/{customerId}/voi'
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
        return APIHelper.json_deserialize(_context.response.raw_body, GenerateVOIReportResponse.from_dictionary)
