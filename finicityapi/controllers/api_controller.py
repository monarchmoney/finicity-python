# -*- coding: utf-8 -*-

from finicityapi.api_helper import APIHelper
from finicityapi.configuration import Configuration
from finicityapi.controllers.base_controller import BaseController
from finicityapi.http.auth.custom_header_auth import CustomHeaderAuth
from finicityapi.models.invoice_billing_response import InvoiceBillingResponse

class APIController(BaseController):

    """A Controller to access Endpoints in the finicityapi API."""


    def get_asset_by_customer_id(self,
                                 customer_id,
                                 asset_id):
        """Does a GET request to //aggregation/v1/customers/{customerId}/assets/{assetId}.

        Retrieve a binary file with the given assetId. The returned content
        type is always application/octet-stream. If the service successfully
        retrieves the asset, HTTP 200 (OK) will be returned. If the asset
        doesn’t exist, HTTP 404 (Not Found) will be returned. If you would
        like to see an error message on the return, include application/json
        or application/xml in your desired format for the Accept header.

        Args:
            customer_id (string): TODO: type description here. Example: 
            asset_id (string): TODO: type description here. Example: 

        Returns:
            void: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(customer_id=customer_id,
                                 asset_id=asset_id)

        # Prepare query URL
        _url_path = '//aggregation/v1/customers/{customerId}/assets/{assetId}'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, { 
            'customerId': customer_id,
            'assetId': asset_id
        })
        _query_builder = Configuration.get_base_uri()
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'Finicity-App-Key': Configuration.finicity_app_key
        }

        # Prepare and execute request
        _request = self.http_client.get(_query_url, headers=_headers)
        CustomHeaderAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

    def invoice_billing_endpoint(self,
                                 accept,
                                 partner_id,
                                 start_date,
                                 end_date,
                                 view_testing_reports,
                                 size=None,
                                 page=None):
        """Does a GET request to /decisioning/v1/partners/{partnerId}/billing/reseller.

        Partners would like the capability to see the reports generated for a
        specific date range as well as the custom fields associated with the
        report. This will allow partners to determine which branches have
        generated specific reports to better bill those branches

        Args:
            accept (string): Replace 'json' with 'xml' if preferred
            partner_id (string): Partner ID From Developer Portal
            start_date (string): The earliest date to be analyzed in this
                report. This is required.  Note: The range between startDate
                and endDate must be 31 days or less.
            end_date (string): The latest date to be analyzed in this report.
                This is required.
            view_testing_reports (string): Designate as true to only display
                testing reports in the response. By default, this is false.
            size (string, optional): The size of the results returned per
                page. By default, this is 100 results per page and can be no
                more than 1000 results per page. This is optional.
            page (string, optional): The page to be viewed. Zero based index.
                This is optional. Default 0.

        Returns:
            InvoiceBillingResponse: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(accept=accept,
                                 partner_id=partner_id,
                                 start_date=start_date,
                                 end_date=end_date,
                                 view_testing_reports=view_testing_reports)

        # Prepare query URL
        _url_path = '/decisioning/v1/partners/{partnerId}/billing/reseller'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, { 
            'partnerId': partner_id
        })
        _query_builder = Configuration.get_base_uri()
        _query_builder += _url_path
        _query_parameters = {
            'startDate': start_date,
            'endDate': end_date,
            'viewTestingReports': view_testing_reports,
            'size': size,
            'page': page
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
        return APIHelper.json_deserialize(_context.response.raw_body, InvoiceBillingResponse.from_dictionary)
