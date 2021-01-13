# -*- coding: utf-8 -*-

from finicityapi.api_helper import APIHelper
from finicityapi.configuration import Configuration
from finicityapi.controllers.base_controller import BaseController
from finicityapi.http.auth.custom_header_auth import CustomHeaderAuth
from finicityapi.models.institution import Institution
from finicityapi.models.get_institutions_response import GetInstitutionsResponse
from finicityapi.models.get_certified_institutions_response import GetCertifiedInstitutionsResponse
from finicityapi.models.institutions_certification_subscription_response import InstitutionsCertificationSubscriptionResponse
from finicityapi.models.institutions_certification_subscription import InstitutionsCertificationSubscription
from finicityapi.models.institution_branding_response import InstitutionBrandingResponse
from finicityapi.exceptions.api_exception import APIException

class InstitutionsController(BaseController):

    """A Controller to access Endpoints in the finicityapi API."""


    def get_institution(self,
                        accept,
                        institution_id):
        """Does a GET request to /institution/v2/institutions/{institutionId}.

        Get details for the specified institution

        Args:
            accept (string): application/json, application/xml
            institution_id (long|int): Finicity’s ID of the institution to
                retrieve

        Returns:
            Institution: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(accept=accept,
                                 institution_id=institution_id)

        # Prepare query URL
        _url_path = '/institution/v2/institutions/{institutionId}'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, { 
            'institutionId': institution_id
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
        return APIHelper.json_deserialize(_context.response.raw_body, Institution.from_dictionary)

    def get_institutions(self,
                         accept,
                         search=None,
                         start=1,
                         limit=25):
        """Does a GET request to /institution/v2/institutions.

        Use this call to search all Financial Institutions (FI) the Finicity
        has connections with and supports.
        Return all financial institutions that contain the search text in the
        institution’s name, urlHomeApp, or urlLogonApp fields.
        To get a list of all FI’s, leave the search parameter out of the call.
        If the search query is left blank, the API will return an error.
        If the value of moreAvailable in the response is true, you can
        retrieve the next page of results by increasing the value of the start
        parameter in your next request:
        1st Request
        …….start=1&limit=25 (First 25 from list 1-25)
        2nd Request
        …….start=2&limit=25 (Next 25 from list 26-50)

        Args:
            accept (string): application/json, application/xml
            search (string, optional): Text to match, or omit the search
                parameter.  Must be URL-encoded (see Handling Spaces in
                Queries)
            start (int, optional): Starting index for this page of results.
                This defaults to 1.
            limit (int, optional): Maximum number of entries for this page of
                results. This defaults to 25. Limits the number of results
                returned to 1000.

        Returns:
            GetInstitutionsResponse: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(accept=accept)

        # Prepare query URL
        _url_path = '/institution/v2/institutions'
        _query_builder = Configuration.get_base_uri()
        _query_builder += _url_path
        _query_parameters = {
            'search': search,
            'start': start,
            'limit': limit
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
        return APIHelper.json_deserialize(_context.response.raw_body, GetInstitutionsResponse.from_dictionary)

    def get_certified_institutions(self,
                                   accept,
                                   search,
                                   start=1,
                                   limit=25,
                                   mtype=None):
        """Does a GET request to /institution/v2/certifiedInstitutions.

        Search for institutions by certified product

        Args:
            accept (string): application/json, application/xml
            search (string): Text to match, or * to return all supported
                institutions.
            start (int, optional): Starting index for this page of results
                (ignored if returning all institutions). This will default to
                1.
            limit (int, optional): Maximum number of entries for this page of
                results (ignored if returning all institutions). This will
                default to 25. Limits the number of results returned to 1000.
            mtype (string, optional): Allowed types: voa, voi, state_agg, ach,
                aha

        Returns:
            GetCertifiedInstitutionsResponse: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(accept=accept,
                                 search=search)

        # Prepare query URL
        _url_path = '/institution/v2/certifiedInstitutions'
        _query_builder = Configuration.get_base_uri()
        _query_builder += _url_path
        _query_parameters = {
            'search': search,
            'start': start,
            'limit': limit,
            'type': mtype
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
        return APIHelper.json_deserialize(_context.response.raw_body, GetCertifiedInstitutionsResponse.from_dictionary)

    def get_certified_institutions_with_rssd(self,
                                             accept,
                                             search,
                                             start,
                                             limit,
                                             mtype):
        """Does a GET request to /institution/v2/certifiedInstitutions/rssd.

        Get Certified Institution List w/RSSD

        Args:
            accept (string): application/json, application/xml
            search (string): Search term, * returns all institutions
            start (int): Page (Default: 1)
            limit (int): Limits the number of results returned (max: 1000)
            mtype (string): product types trans_agg, voa, voi, state_agg, ach,
                aha

        Returns:
            GetCertifiedInstitutionsResponse: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(accept=accept,
                                 search=search,
                                 start=start,
                                 limit=limit,
                                 mtype=mtype)

        # Prepare query URL
        _url_path = '/institution/v2/certifiedInstitutions/rssd'
        _query_builder = Configuration.get_base_uri()
        _query_builder += _url_path
        _query_parameters = {
            'search': search,
            'start': start,
            'limit': limit,
            'type': mtype
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
        return APIHelper.json_deserialize(_context.response.raw_body, GetCertifiedInstitutionsResponse.from_dictionary)

    def enable_institutions_certification_subscription(self,
                                                       accept,
                                                       content_type,
                                                       body):
        """Does a PUT request to /institution/v2/institutions/subscription.

        Subscription to a webhook service to return changes in certification
        status for financial institutions as they happen. Webhook
        example.......
        {
          "name": "FinBank",
          "id": 101722,
          "changes": {
            "voi": true,
            "voa": false
          }
        }

        Args:
            accept (string): application/json, application/xml
            content_type (string): application/json, application/xml
            body (InstitutionsCertificationSubscriptionRequest): TODO: type
                description here. Example: 

        Returns:
            InstitutionsCertificationSubscriptionResponse: Response from the
                API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(accept=accept,
                                 content_type=content_type,
                                 body=body)

        # Prepare query URL
        _url_path = '/institution/v2/institutions/subscription'
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
        _request = self.http_client.put(_query_url, headers=_headers, parameters=APIHelper.json_serialize(body))
        CustomHeaderAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, InstitutionsCertificationSubscriptionResponse.from_dictionary)

    def get_institutions_certification_subscription(self,
                                                    accept):
        """Does a GET request to /institution/v2/institutions/subscription.

        Service to retrieve Institutions Certification Subscription details

        Args:
            accept (string): application/json, application/xml

        Returns:
            InstitutionsCertificationSubscription: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(accept=accept)

        # Prepare query URL
        _url_path = '/institution/v2/institutions/subscription'
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
        return APIHelper.json_deserialize(_context.response.raw_body, InstitutionsCertificationSubscription.from_dictionary)

    def delete_institutions_certification_subscription(self):
        """Does a DELETE request to /institution/v2/institutions/subscription.

        Delete subscription to a webhook services for certification status
        changes

        Returns:
            void: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/institution/v2/institutions/subscription'
        _query_builder = Configuration.get_base_uri()
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'Finicity-App-Key': Configuration.finicity_app_key
        }

        # Prepare and execute request
        _request = self.http_client.delete(_query_url, headers=_headers)
        CustomHeaderAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

    def get_institution_branding(self,
                                 accept,
                                 id):
        """Does a GET request to /institution/v2/institutions/{id}/branding.

        This endpoint returns the branding information for an Institution
        given the `id`

        Args:
            accept (string): Replace 'json' with 'xml' if preferred
            id (int): ID of the institution

        Returns:
            InstitutionBrandingResponse: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(accept=accept,
                                 id=id)

        # Prepare query URL
        _url_path = '/institution/v2/institutions/{id}/branding'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, { 
            'id': id
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

        # Endpoint and global error handling using HTTP status codes.
        if _context.response.status_code == 404:
            raise APIException('The requested entity was not found', _context)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, InstitutionBrandingResponse.from_dictionary)
