# -*- coding: utf-8 -*-

from finicityapi.api_helper import APIHelper
from finicityapi.configuration import Configuration
from finicityapi.controllers.base_controller import BaseController
from finicityapi.http.auth.custom_header_auth import CustomHeaderAuth
from finicityapi.models.account_owner_v_1 import AccountOwnerV1

class AccountOwnerController(BaseController):

    """A Controller to access Endpoints in the finicityapi API."""


    def get_account_owner(self,
                          accept,
                          customer_id,
                          account_id):
        """Does a GET request to /aggregation/v1/customers/{customerId}/accounts/{accountId}/owner.

        Return the account owner’s name and address.
        This is a premium service. The billable event is a successful call to
        this service.
        HTTP status of 200 means the account owner’s name and address were
        retrieved successfully.
        HTTP status of 203 means the response contains an MFA challenge in XML
        or JSON format. Contact your Account Manager or Systems Engineers to
        determine the best route to handle this HTTP status code.
        This service retrieves account data from the institution. This usually
        returns quickly, but in some scenarios may take a few minutes to
        complete. In the event of a timeout condition, please retry the call.

        Args:
            accept (string): application/json, application/xml
            customer_id (long|int): Finicity’s ID for the customer
            account_id (long|int): Finicity’s ID of the account

        Returns:
            AccountOwnerV1: Response from the API. default response

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
        _url_path = '/aggregation/v1/customers/{customerId}/accounts/{accountId}/owner'
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
        return APIHelper.json_deserialize(_context.response.raw_body, AccountOwnerV1.from_dictionary)
