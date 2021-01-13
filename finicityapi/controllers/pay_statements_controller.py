# -*- coding: utf-8 -*-

from finicityapi.api_helper import APIHelper
from finicityapi.configuration import Configuration
from finicityapi.controllers.base_controller import BaseController
from finicityapi.http.auth.custom_header_auth import CustomHeaderAuth
from finicityapi.models.store_pay_statement_response import StorePayStatementResponse

class PayStatementsController(BaseController):

    """A Controller to access Endpoints in the finicityapi API."""


    def store_customer_pay_statement(self,
                                     finicity_app_key,
                                     finicity_app_token,
                                     customer_id,
                                     body):
        """Does a POST request to /aggregation/v1/customers/{customerId}/payStatements.

        Services to store a pay statement for a customer. Within the body of
        the request, the base 64 encoded value of the pay statement must be
        passed with a label.

        Args:
            finicity_app_key (string): Finicity-App-Key from Developer Portal
            finicity_app_token (string): Token returned from Partner
                Authentication
            customer_id (long|int): Finicity's ID of the customer
            body (StorePayStatementRequest): The label to be associated with
                the pay statement. These are recommended labels:  -
                lastPayPeriod – The most recent (last) pay statement. This
                label will allow the paystub to go through primary data
                extraction.  - lastPayPeriodMinusOne – The second most recent
                pay statement  - lastPayPeriodMinusTwo – The third most recent
                pay statement  - previousYearLastPayPeriod – Last pay
                statement of the previous calendar year  -
                previousYear2LastPayPeriod – Last pay statement of the
                calendar year 2 years prior  - earliestPayPeriod – The
                earliest pay statement  statement - The base 64 encoded value
                for the pay statement.

        Returns:
            StorePayStatementResponse: Response from the API. default
                response

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(finicity_app_key=finicity_app_key,
                                 finicity_app_token=finicity_app_token,
                                 customer_id=customer_id,
                                 body=body)

        # Prepare query URL
        _url_path = '/aggregation/v1/customers/{customerId}/payStatements'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, { 
            'customerId': customer_id
        })
        _query_builder = Configuration.get_base_uri()
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json',
            'content-type': 'application/json; charset=utf-8',
            'Finicity-App-Key': finicity_app_key,
            'Finicity-App-Token': finicity_app_token
        }

        # Prepare and execute request
        _request = self.http_client.post(_query_url, headers=_headers, parameters=APIHelper.json_serialize(body))
        CustomHeaderAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, StorePayStatementResponse.from_dictionary)
