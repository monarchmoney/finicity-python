# -*- coding: utf-8 -*-

from finicityapi.api_helper import APIHelper
from finicityapi.configuration import Configuration
from finicityapi.controllers.base_controller import BaseController
from finicityapi.http.auth.custom_header_auth import CustomHeaderAuth
from finicityapi.models.loan_payment_details import LoanPaymentDetails

class LiabilitiesController(BaseController):

    """A Controller to access Endpoints in the finicityapi API."""


    def get_loan_payment_details(self,
                                 accept,
                                 customer_id,
                                 account_id):
        """Does a GET request to /aggregation/v1/customers/{customerId}/accounts/{accountId}/loanDetails.

        This will return loan payment details of customer for account. Only
        applies to loan type accounts.

        Args:
            accept (string): application/json, application/xml
            customer_id (long|int): ID of the customer
            account_id (long|int): The Finicity ID of the account

        Returns:
            LoanPaymentDetails: Response from the API. default response

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
        _url_path = '/aggregation/v1/customers/{customerId}/accounts/{accountId}/loanDetails'
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
        return APIHelper.json_deserialize(_context.response.raw_body, LoanPaymentDetails.from_dictionary)
