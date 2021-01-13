# -*- coding: utf-8 -*-

from finicityapi.api_helper import APIHelper
from finicityapi.configuration import Configuration
from finicityapi.controllers.base_controller import BaseController
from finicityapi.http.auth.custom_header_auth import CustomHeaderAuth
from finicityapi.models.portfolio_summary import PortfolioSummary
from finicityapi.models.portfolio_summary_by_customer import PortfolioSummaryByCustomer
from finicityapi.exceptions.error_1_error_exception import Error1ErrorException

class GetPortfoliosController(BaseController):

    """A Controller to access Endpoints in the finicityapi API."""


    def get_portfolio_by_consumer(self,
                                  consumer_id,
                                  portfolio_id,
                                  accept,
                                  content_type):
        """Does a GET request to /decisioning/v1/consumers/{consumerId}/portfolios/{portfolioId}.

        Returns a portfolio of most recently generated report for each report
        type for a specified consumer. If there are multiple reports that were
        generated for a report type (VOA, VOI, etc), only the most recently
        generated report for the type will be returned.  
         
        HTTP 404 status means that there is no data for the consumer or
        portfolio. HTTP 200 (OK) status means that the call was successful.

        Args:
            consumer_id (string): Finicity report consumer ID (max length 32
                characters)
            portfolio_id (string): Finicity portfolio ID (Max 17 characters)
                with the portfolio version number. Using the portfolio number
                without a version number will return the most recently
                generated reports for the consumer.
            accept (string): Replace 'json' with 'xml' if preferred
            content_type (string): Replace 'json' with 'xml' if preferred

        Returns:
            PortfolioSummary: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(consumer_id=consumer_id,
                                 portfolio_id=portfolio_id,
                                 accept=accept,
                                 content_type=content_type)

        # Prepare query URL
        _url_path = '/decisioning/v1/consumers/{consumerId}/portfolios/{portfolioId}'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, { 
            'consumerId': consumer_id,
            'portfolioId': portfolio_id
        })
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
        _request = self.http_client.get(_query_url, headers=_headers)
        CustomHeaderAuth.apply(_request)
        _context = self.execute_request(_request)

        # Endpoint and global error handling using HTTP status codes.
        if _context.response.status_code == 400:
            raise Error1ErrorException('Bad Request', _context)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, PortfolioSummary.from_dictionary)

    def get_portfolio_by_customer(self,
                                  customer_id,
                                  portfolio_id,
                                  accept,
                                  content_type):
        """Does a GET request to /decisioning/v1/customers/{customerId}/portfolios/{portfolioId}.

        Returns a portfolio of most recently generated report for each report
        type for a specified customer. If there are multiple reports that were
        generated for a report type (VOA, VOI, etc), only the most recently
        generated report for the type will be returned.  
         
        HTTP 404 status means that there is no data for the customer or
        portfolio. HTTP 200 (OK) status means that the call was successful. 

        Args:
            customer_id (long|int): Finicity ID of the customer
            portfolio_id (string): Finicity portfolio ID (Max 17 characters)
                with the portfolio version number. Using the portfolio number
                without a version number will return the most recently
                generated reports for the consumer.
            accept (string): Replace 'json' with 'xml' if preferred
            content_type (string): Replace 'json' with 'xml' if preferred

        Returns:
            PortfolioSummaryByCustomer: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(customer_id=customer_id,
                                 portfolio_id=portfolio_id,
                                 accept=accept,
                                 content_type=content_type)

        # Prepare query URL
        _url_path = '/decisioning/v1/customers/{customerId}/portfolios/{portfolioId}'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, { 
            'customerId': customer_id,
            'portfolioId': portfolio_id
        })
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
        _request = self.http_client.get(_query_url, headers=_headers)
        CustomHeaderAuth.apply(_request)
        _context = self.execute_request(_request)

        # Endpoint and global error handling using HTTP status codes.
        if _context.response.status_code == 400:
            raise Error1ErrorException('Bad Request', _context)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, PortfolioSummaryByCustomer.from_dictionary)
