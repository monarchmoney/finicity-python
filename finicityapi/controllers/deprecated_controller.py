# -*- coding: utf-8 -*-

from finicityapi.api_helper import APIHelper
from finicityapi.configuration import Configuration
from finicityapi.controllers.base_controller import BaseController
from finicityapi.http.auth.custom_header_auth import CustomHeaderAuth
from finicityapi.models.generate_connect_url_response import GenerateConnectURLResponse
from finicityapi.models.customer_accounts import CustomerAccounts
from finicityapi.models.auditable_report import AuditableReport
from finicityapi.models.add_customer_response import AddCustomerResponse
from finicityapi.models.voa_report_record import VOAReportRecord
from finicityapi.models.voie_paystub_with_txverify_report_record import VOIEPaystubWithTxverifyReportRecord
from finicityapi.models.voi_report_record import VOIReportRecord
from finicityapi.models.voa_with_income_report_record import VOAWithIncomeReportRecord
from finicityapi.models.prequalification_report_record import PrequalificationReportRecord
from finicityapi.models.pay_statement_report_record import PayStatementReportRecord
from finicityapi.models.generate_connect_email_response_multiple_borrowers import GenerateConnectEmailResponseMultipleBorrowers
from finicityapi.models.transactions_report_record import TransactionsReportRecord
from finicityapi.models.app_statuses_v_1 import AppStatusesV1
from finicityapi.models.statement_report_record import StatementReportRecord
from finicityapi.exceptions.error_1_error_exception import Error1ErrorException

class DeprecatedController(BaseController):

    """A Controller to access Endpoints in the finicityapi API."""


    def generate_connect_url_all_types(self,
                                       accept,
                                       body):
        """Does a POST request to /connect/v1/generate.

        No matter how you plan on implementing Finicity Connect, you’ll need
        to generate and retrieve a Finicity Connect Link.  You will need to
        specify what type of Finicity Connect you need depending on what will
        happen once the customer accounts and transaction data are gathered. 
        Below you’ll find how to generate the Connect link as well as where to
        specify what type of Finicity Connect you need.
        Once you have generated the link it will only last until the
        authentication token under which it was generated expires.  After that
        you will need to regenerate the Connect link under a new
        authentication token. We recommend generating a new authentication
        token when you generate a Connect link, to guarantee a full two hour
        life-span.
        Several Finicity products utilize Finicity Connect, and most products
        have their own type of Connect.  The Connect type is controlled by the
        “type” code in the call.  Many times the type also corresponds to the
        report that will be run upon completing the Connect flow.
        It is best to use the documentation for the specific use case you are
        interested in as the documentation here is a list of all the possible
        parameters you can send for this endpoint depending on the use case.
        See the following more specific documentation for your use
        case.......
        Generate Finicity Connect URL (Data and Payments)
        Generate Finicity Connect URL (Lending)
        Generate Finicity Connect URL (Lite)
        Generate Finicity Connect URL (Fix)

        Args:
            accept (string): application/json, application/xml
            body (GenerateConnectURLRequest): Expected body to be sent with
                the request

        Returns:
            GenerateConnectURLResponse: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(accept=accept,
                                 body=body)

        # Prepare query URL
        _url_path = '/connect/v1/generate'
        _query_builder = Configuration.get_base_uri()
        _query_builder += _url_path
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
        return APIHelper.json_deserialize(_context.response.raw_body, GenerateConnectURLResponse.from_dictionary)

    def migrate_institution_login_accounts_v_1(self,
                                               customer_id,
                                               institution_login_id,
                                               new_institution_id):
        """Does a PUT request to /aggregation/v1/customers/{customerId}/institutionLogins/{institutionLoginId}/institutions/{newInstitutionId}.

        This service has been replaced by version 2 call now "Migrate
        Institution Login Accounts"
        This service is to migrate accounts from legacy FI to new OAuth FI. 
        A successful API response will return a list of accounts for the given
        institution login id with an http status code as 200.

        Args:
            customer_id (long|int): Finicity’s ID of the customer for the
                institutionLoginId of accounts
            institution_login_id (long|int): Finicity's institutionLoginId for
                the set of accounts to be migrated
            new_institution_id (long|int): New OAuth FI ID where accounts 
                will be migrated

        Returns:
            CustomerAccounts: Response from the API. default response

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(customer_id=customer_id,
                                 institution_login_id=institution_login_id,
                                 new_institution_id=new_institution_id)

        # Prepare query URL
        _url_path = '/aggregation/v1/customers/{customerId}/institutionLogins/{institutionLoginId}/institutions/{newInstitutionId}'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, { 
            'customerId': customer_id,
            'institutionLoginId': institution_login_id,
            'newInstitutionId': new_institution_id
        })
        _query_builder = Configuration.get_base_uri()
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json',
            'Finicity-App-Key': Configuration.finicity_app_key
        }

        # Prepare and execute request
        _request = self.http_client.put(_query_url, headers=_headers)
        CustomHeaderAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, CustomerAccounts.from_dictionary)

    def get_report_by_customer(self,
                               customer_id,
                               report_id,
                               accept,
                               content_type,
                               on_behalf_of=None,
                               purpose=None):
        """Does a GET request to /decisioning/v1/customers/{customerId}/reports/{reportId}.

        Get a report that has been generated by calling one of the Generate
        Report services.
        The report's status field will contain inProgress, failure, or
        success. If the status shows inProgress, the client app should wait 20
        seconds and then call again to see if the report is finished.
        See Permissible Purpose Codes for a list of permissible purposes for
        retrieving a report.

        Args:
            customer_id (long|int): Finicity’s ID of the customer
            report_id (string): Finicity’s ID of the report
            accept (string): Replace 'json' with 'xml' if preferred
            content_type (string): Replace 'json' with 'xml' if preferred
            on_behalf_of (string, optional): The name of the entity you are
                retrieving the report on behalf of.
            purpose (string, optional): 2-digit code from Permissible Purpose
                Codes, specifying the reason for retrieving this report.

        Returns:
            AuditableReport: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(customer_id=customer_id,
                                 report_id=report_id,
                                 accept=accept,
                                 content_type=content_type)

        # Prepare query URL
        _url_path = '/decisioning/v1/customers/{customerId}/reports/{reportId}'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, { 
            'customerId': customer_id,
            'reportId': report_id
        })
        _query_builder = Configuration.get_base_uri()
        _query_builder += _url_path
        _query_parameters = {
            'onBehalfOf': on_behalf_of,
            'purpose': purpose
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
        _request = self.http_client.get(_query_url, headers=_headers)
        CustomHeaderAuth.apply(_request)
        _context = self.execute_request(_request)

        # Endpoint and global error handling using HTTP status codes.
        if _context.response.status_code == 400:
            raise Error1ErrorException('Bad Request', _context)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, AuditableReport.from_dictionary)

    def get_report_by_consumer(self,
                               consumer_id,
                               report_id,
                               accept,
                               content_type,
                               on_behalf_of=None,
                               purpose=None):
        """Does a GET request to /decisioning/v1/consumers/{consumerId}/reports/{reportId}.

        Get a report that has been generated by calling one of the Generate
        Report services.
        The report's status field will contain inProgress, failure, or
        success. If the status shows inProgress, the client app should wait 20
        seconds and then call again to see if the report is finished.
        See Permissible Purpose Codes for a list of permissible purposes for
        retrieving a report.

        Args:
            consumer_id (string): Finicity’s ID of the consumer (UUID with max
                length 32 characters)
            report_id (string): Finicity’s ID of the report (UUID with max
                length 32 characters)
            accept (string): Replace 'json' with 'xml' if preferred
            content_type (string): Replace 'json' with 'xml' if preferred
            on_behalf_of (string, optional): The name of the entity you are
                retrieving the report on behalf of.
            purpose (string, optional): 2-digit code from Permissible Purpose
                Codes, specifying the reason for retrieving this report.

        Returns:
            AuditableReport: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(consumer_id=consumer_id,
                                 report_id=report_id,
                                 accept=accept,
                                 content_type=content_type)

        # Prepare query URL
        _url_path = '/decisioning/v1/consumers/{consumerId}/reports/{reportId}'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, { 
            'consumerId': consumer_id,
            'reportId': report_id
        })
        _query_builder = Configuration.get_base_uri()
        _query_builder += _url_path
        _query_parameters = {
            'onBehalfOf': on_behalf_of,
            'purpose': purpose
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
        _request = self.http_client.get(_query_url, headers=_headers)
        CustomHeaderAuth.apply(_request)
        _context = self.execute_request(_request)

        # Endpoint and global error handling using HTTP status codes.
        if _context.response.status_code == 400:
            raise Error1ErrorException('Bad Request', _context)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, AuditableReport.from_dictionary)

    def add_testing_customer_v_1(self,
                                 content_type,
                                 accept,
                                 body):
        """Does a POST request to /aggregation/v1/customers/testing.

        Enroll a testing customer. A testing customer may only register
        accounts with FinBank institutions.

        Args:
            content_type (string): application/json, application/xml
            accept (string): application/json, application/xml
            body (AddCustomerRequest): The Fields For The New Testing
                Customer

        Returns:
            AddCustomerResponse: Response from the API. default response

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(content_type=content_type,
                                 accept=accept,
                                 body=body)

        # Prepare query URL
        _url_path = '/aggregation/v1/customers/testing'
        _query_builder = Configuration.get_base_uri()
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'Finicity-App-Key': Configuration.finicity_app_key,
            'Content-Type': content_type,
            'Accept': accept
        }

        # Prepare and execute request
        _request = self.http_client.post(_query_url, headers=_headers, parameters=APIHelper.json_serialize(body))
        CustomHeaderAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, AddCustomerResponse.from_dictionary)

    def get_voa_report_by_consumer(self,
                                   consumer_id,
                                   report_id,
                                   accept,
                                   content_type,
                                   on_behalf_of=None,
                                   purpose=None):
        """Does a GET request to /decisioning/v1/consumers/{consumerId}/reports/{reportId}.

        Get a report that has been generated by calling one of the Generate
        Report services.
        The report's status field will contain inProgress, failure, or
        success. If the status shows inProgress, the client app should wait 20
        seconds and then call again to see if the report is finished.
        See Permissible Purpose Codes for a list of permissible purposes for
        retrieving a report.

        Args:
            consumer_id (string): Finicity’s ID of the consumer (UUID with max
                length 32 characters)
            report_id (string): Finicity’s ID of the report
            accept (string): Replace 'json' with 'xml' if preferred
            content_type (string): Replace 'json' with 'xml' if preferred
            on_behalf_of (string, optional): The name of the entity you are
                retrieving the report on behalf of.
            purpose (string, optional): 2-digit code from Permissible Purpose
                Codes, specifying the reason for retrieving this report.

        Returns:
            VOAReportRecord: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(consumer_id=consumer_id,
                                 report_id=report_id,
                                 accept=accept,
                                 content_type=content_type)

        # Prepare query URL
        _url_path = '/decisioning/v1/consumers/{consumerId}/reports/{reportId}'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, { 
            'consumerId': consumer_id,
            'reportId': report_id
        })
        _query_builder = Configuration.get_base_uri()
        _query_builder += _url_path
        _query_parameters = {
            'onBehalfOf': on_behalf_of,
            'purpose': purpose
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
        _request = self.http_client.get(_query_url, headers=_headers)
        CustomHeaderAuth.apply(_request)
        _context = self.execute_request(_request)

        # Endpoint and global error handling using HTTP status codes.
        if _context.response.status_code == 400:
            raise Error1ErrorException('Bad Request', _context)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, VOAReportRecord.from_dictionary)

    def get_voie_txverify_report_by_customer(self,
                                             customer_id,
                                             report_id,
                                             accept,
                                             content_type,
                                             on_behalf_of=None,
                                             purpose=None):
        """Does a GET request to /decisioning/v1/customers/{customerId}/reports/{reportId}.

        Get a report that has been generated by calling one of the Generate
        Report services.
        The report's status field will contain inProgress, failure, or
        success. If the status shows inProgress, the client app should wait 20
        seconds and then call again to see if the report is finished.
        See Permissible Purpose Codes for a list of permissible purposes for
        retrieving a report.

        Args:
            customer_id (long|int): Finicity’s ID of the customer
            report_id (string): Finicity’s ID of the report
            accept (string): Replace 'json' with 'xml' if preferred
            content_type (string): Replace 'json' with 'xml' if preferred
            on_behalf_of (string, optional): The name of the entity you are
                retrieving the report on behalf of.
            purpose (string, optional): 2-digit code from Permissible Purpose
                Codes, specifying the reason for retrieving this report.

        Returns:
            VOIEPaystubWithTxverifyReportRecord: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(customer_id=customer_id,
                                 report_id=report_id,
                                 accept=accept,
                                 content_type=content_type)

        # Prepare query URL
        _url_path = '/decisioning/v1/customers/{customerId}/reports/{reportId}'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, { 
            'customerId': customer_id,
            'reportId': report_id
        })
        _query_builder = Configuration.get_base_uri()
        _query_builder += _url_path
        _query_parameters = {
            'onBehalfOf': on_behalf_of,
            'purpose': purpose
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
        _request = self.http_client.get(_query_url, headers=_headers)
        CustomHeaderAuth.apply(_request)
        _context = self.execute_request(_request)

        # Endpoint and global error handling using HTTP status codes.
        if _context.response.status_code == 400:
            raise Error1ErrorException('Bad Request', _context)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, VOIEPaystubWithTxverifyReportRecord.from_dictionary)

    def get_voi_report_by_consumer(self,
                                   consumer_id,
                                   report_id,
                                   accept,
                                   content_type,
                                   on_behalf_of=None,
                                   purpose=None):
        """Does a GET request to /decisioning/v1/consumers/{consumerId}/reports/{reportId}.

        Get a report that has been generated by calling one of the Generate
        Report services.
        The report's status field will contain inProgress, failure, or
        success. If the status shows inProgress, the client app should wait 20
        seconds and then call again to see if the report is finished.
        See Permissible Purpose Codes for a list of permissible purposes for
        retrieving a report.

        Args:
            consumer_id (string): Finicity’s ID of the consumer (UUID with max
                length 32 characters)
            report_id (string): Finicity’s ID of the report
            accept (string): Replace 'json' with 'xml' if preferred
            content_type (string): Replace 'json' with 'xml' if preferred
            on_behalf_of (string, optional): The name of the entity you are
                retrieving the report on behalf of.
            purpose (string, optional): 2-digit code from Permissible Purpose
                Codes, specifying the reason for retrieving this report.

        Returns:
            VOIReportRecord: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(consumer_id=consumer_id,
                                 report_id=report_id,
                                 accept=accept,
                                 content_type=content_type)

        # Prepare query URL
        _url_path = '/decisioning/v1/consumers/{consumerId}/reports/{reportId}'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, { 
            'consumerId': consumer_id,
            'reportId': report_id
        })
        _query_builder = Configuration.get_base_uri()
        _query_builder += _url_path
        _query_parameters = {
            'onBehalfOf': on_behalf_of,
            'purpose': purpose
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
        _request = self.http_client.get(_query_url, headers=_headers)
        CustomHeaderAuth.apply(_request)
        _context = self.execute_request(_request)

        # Endpoint and global error handling using HTTP status codes.
        if _context.response.status_code == 400:
            raise Error1ErrorException('Bad Request', _context)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, VOIReportRecord.from_dictionary)

    def get_voi_report_by_customer(self,
                                   customer_id,
                                   report_id,
                                   accept,
                                   content_type,
                                   on_behalf_of=None,
                                   purpose=None):
        """Does a GET request to /decisioning/v1/customers/{customerId}/reports/{reportId}.

        Get a report that has been generated by calling one of the Generate
        Report services.
        The report's status field will contain inProgress, failure, or
        success. If the status shows inProgress, the client app should wait 20
        seconds and then call again to see if the report is finished.
        See Permissible Purpose Codes for a list of permissible purposes for
        retrieving a report.

        Args:
            customer_id (long|int): Finicity’s ID of the customer
            report_id (string): Finicity’s ID of the report (UUID with max
                length 32 characters)
            accept (string): Replace 'json' with 'xml' if preferred
            content_type (string): Replace 'json' with 'xml' if preferred
            on_behalf_of (string, optional): The name of the entity you are
                retrieving the report on behalf of.
            purpose (string, optional): 2-digit code from Permissible Purpose
                Codes, specifying the reason for retrieving this report.

        Returns:
            VOIReportRecord: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(customer_id=customer_id,
                                 report_id=report_id,
                                 accept=accept,
                                 content_type=content_type)

        # Prepare query URL
        _url_path = '/decisioning/v1/customers/{customerId}/reports/{reportId}'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, { 
            'customerId': customer_id,
            'reportId': report_id
        })
        _query_builder = Configuration.get_base_uri()
        _query_builder += _url_path
        _query_parameters = {
            'onBehalfOf': on_behalf_of,
            'purpose': purpose
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
        _request = self.http_client.get(_query_url, headers=_headers)
        CustomHeaderAuth.apply(_request)
        _context = self.execute_request(_request)

        # Endpoint and global error handling using HTTP status codes.
        if _context.response.status_code == 400:
            raise Error1ErrorException('Bad Request', _context)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, VOIReportRecord.from_dictionary)

    def get_voa_with_income_report_by_consumer(self,
                                               consumer_id,
                                               report_id,
                                               accept,
                                               content_type,
                                               on_behalf_of=None,
                                               purpose=None):
        """Does a GET request to /decisioning/v1/consumers/{consumerId}/reports/{reportId}.

        Get a report that has been generated by calling one of the Generate
        Report services.
        The report's status field will contain inProgress, failure, or
        success. If the status shows inProgress, the client app should wait 20
        seconds and then call again to see if the report is finished.
        See Permissible Purpose Codes for a list of permissible purposes for
        retrieving a report.

        Args:
            consumer_id (string): Finicity’s ID of the consumer (UUID with max
                length 32 characters)
            report_id (string): Finicity’s ID of the report
            accept (string): Replace 'json' with 'xml' if preferred
            content_type (string): Replace 'json' with 'xml' if preferred
            on_behalf_of (string, optional): The name of the entity you are
                retrieving the report on behalf of.
            purpose (string, optional): 2-digit code from Permissible Purpose
                Codes, specifying the reason for retrieving this report.

        Returns:
            VOAWithIncomeReportRecord: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(consumer_id=consumer_id,
                                 report_id=report_id,
                                 accept=accept,
                                 content_type=content_type)

        # Prepare query URL
        _url_path = '/decisioning/v1/consumers/{consumerId}/reports/{reportId}'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, { 
            'consumerId': consumer_id,
            'reportId': report_id
        })
        _query_builder = Configuration.get_base_uri()
        _query_builder += _url_path
        _query_parameters = {
            'onBehalfOf': on_behalf_of,
            'purpose': purpose
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
        _request = self.http_client.get(_query_url, headers=_headers)
        CustomHeaderAuth.apply(_request)
        _context = self.execute_request(_request)

        # Endpoint and global error handling using HTTP status codes.
        if _context.response.status_code == 400:
            raise Error1ErrorException('Bad Request', _context)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, VOAWithIncomeReportRecord.from_dictionary)

    def get_voa_with_income_report_by_customer(self,
                                               customer_id,
                                               report_id,
                                               accept,
                                               content_type,
                                               on_behalf_of=None,
                                               purpose=None):
        """Does a GET request to /decisioning/v1/customers/{customerId}/reports/{reportId}.

        Get a report that has been generated by calling one of the Generate
        Report services.
        The report's status field will contain inProgress, failure, or
        success. If the status shows inProgress, the client app should wait 20
        seconds and then call again to see if the report is finished.
        See Permissible Purpose Codes for a list of permissible purposes for
        retrieving a report.

        Args:
            customer_id (long|int): Finicity’s ID of the customer
            report_id (string): Finicity’s ID of the report
            accept (string): Replace 'json' with 'xml' if preferred
            content_type (string): Replace 'json' with 'xml' if preferred
            on_behalf_of (string, optional): The name of the entity you are
                retrieving the report on behalf of.
            purpose (string, optional): 2-digit code from Permissible Purpose
                Codes, specifying the reason for retrieving this report.

        Returns:
            VOAWithIncomeReportRecord: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(customer_id=customer_id,
                                 report_id=report_id,
                                 accept=accept,
                                 content_type=content_type)

        # Prepare query URL
        _url_path = '/decisioning/v1/customers/{customerId}/reports/{reportId}'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, { 
            'customerId': customer_id,
            'reportId': report_id
        })
        _query_builder = Configuration.get_base_uri()
        _query_builder += _url_path
        _query_parameters = {
            'onBehalfOf': on_behalf_of,
            'purpose': purpose
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
        _request = self.http_client.get(_query_url, headers=_headers)
        CustomHeaderAuth.apply(_request)
        _context = self.execute_request(_request)

        # Endpoint and global error handling using HTTP status codes.
        if _context.response.status_code == 400:
            raise Error1ErrorException('Bad Request', _context)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, VOAWithIncomeReportRecord.from_dictionary)

    def get_prequalification_voa_report_by_customer(self,
                                                    customer_id,
                                                    report_id,
                                                    accept,
                                                    content_type,
                                                    on_behalf_of=None,
                                                    purpose=None):
        """Does a GET request to /decisioning/v1/customers/{customerId}/reports/{reportId}.

        Get a report that has been generated by calling one of the Generate
        Report services.
        The report's status field will contain inProgress, failure, or
        success. If the status shows inProgress, the client app should wait 20
        seconds and then call again to see if the report is finished.
        See Permissible Purpose Codes for a list of permissible purposes for
        retrieving a report.

        Args:
            customer_id (long|int): Finicity’s ID of the customer
            report_id (string): Finicity’s ID of the report
            accept (string): Replace 'json' with 'xml' if preferred
            content_type (string): Replace 'json' with 'xml' if preferred
            on_behalf_of (string, optional): The name of the entity you are
                retrieving the report on behalf of.
            purpose (string, optional): 2-digit code from Permissible Purpose
                Codes, specifying the reason for retrieving this report.

        Returns:
            PrequalificationReportRecord: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(customer_id=customer_id,
                                 report_id=report_id,
                                 accept=accept,
                                 content_type=content_type)

        # Prepare query URL
        _url_path = '/decisioning/v1/customers/{customerId}/reports/{reportId}'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, { 
            'customerId': customer_id,
            'reportId': report_id
        })
        _query_builder = Configuration.get_base_uri()
        _query_builder += _url_path
        _query_parameters = {
            'onBehalfOf': on_behalf_of,
            'purpose': purpose
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
        _request = self.http_client.get(_query_url, headers=_headers)
        CustomHeaderAuth.apply(_request)
        _context = self.execute_request(_request)

        # Endpoint and global error handling using HTTP status codes.
        if _context.response.status_code == 400:
            raise Error1ErrorException('Bad Request', _context)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, PrequalificationReportRecord.from_dictionary)

    def get_prequalification_report_by_consumer(self,
                                                consumer_id,
                                                report_id,
                                                accept,
                                                content_type,
                                                on_behalf_of=None,
                                                purpose=None):
        """Does a GET request to /decisioning/v1/consumers/{consumerId}/reports/{reportId}.

        Get a report that has been generated by calling one of the Generate
        Report services.
        The report's status field will contain inProgress, failure, or
        success. If the status shows inProgress, the client app should wait 20
        seconds and then call again to see if the report is finished.
        See Permissible Purpose Codes for a list of permissible purposes for
        retrieving a report.

        Args:
            consumer_id (string): Finicity’s ID of the consumer (UUID with max
                length 32 characters)
            report_id (string): Finicity’s ID of the report
            accept (string): Replace 'json' with 'xml' if preferred
            content_type (string): Replace 'json' with 'xml' if preferred
            on_behalf_of (string, optional): The name of the entity you are
                retrieving the report on behalf of.
            purpose (string, optional): 2-digit code from Permissible Purpose
                Codes, specifying the reason for retrieving this report.

        Returns:
            PrequalificationReportRecord: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(consumer_id=consumer_id,
                                 report_id=report_id,
                                 accept=accept,
                                 content_type=content_type)

        # Prepare query URL
        _url_path = '/decisioning/v1/consumers/{consumerId}/reports/{reportId}'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, { 
            'consumerId': consumer_id,
            'reportId': report_id
        })
        _query_builder = Configuration.get_base_uri()
        _query_builder += _url_path
        _query_parameters = {
            'onBehalfOf': on_behalf_of,
            'purpose': purpose
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
        _request = self.http_client.get(_query_url, headers=_headers)
        CustomHeaderAuth.apply(_request)
        _context = self.execute_request(_request)

        # Endpoint and global error handling using HTTP status codes.
        if _context.response.status_code == 400:
            raise Error1ErrorException('Bad Request', _context)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, PrequalificationReportRecord.from_dictionary)

    def get_pay_statement_by_consumer(self,
                                      consumer_id,
                                      report_id,
                                      accept,
                                      content_type,
                                      on_behalf_of=None,
                                      purpose=None):
        """Does a GET request to /decisioning/v1/consumers/{consumerId}/reports/{reportId}.

        Get a report that has been generated by calling one of the Generate
        Report services.
        The report's status field will contain inProgress, failure, or
        success. If the status shows inProgress, the client app should wait 20
        seconds and then call again to see if the report is finished.
        See Permissible Purpose Codes for a list of permissible purposes for
        retrieving a report.

        Args:
            consumer_id (string): Finicity’s ID of the consumer (UUID with max
                length 32 characters)
            report_id (string): Finicity’s ID of the report
            accept (string): Replace 'json' with 'xml' if preferred
            content_type (string): Replace 'json' with 'xml' if preferred
            on_behalf_of (string, optional): The name of the entity you are
                retrieving the report on behalf of.
            purpose (string, optional): 2-digit code from Permissible Purpose
                Codes, specifying the reason for retrieving this report.

        Returns:
            PayStatementReportRecord: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(consumer_id=consumer_id,
                                 report_id=report_id,
                                 accept=accept,
                                 content_type=content_type)

        # Prepare query URL
        _url_path = '/decisioning/v1/consumers/{consumerId}/reports/{reportId}'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, { 
            'consumerId': consumer_id,
            'reportId': report_id
        })
        _query_builder = Configuration.get_base_uri()
        _query_builder += _url_path
        _query_parameters = {
            'onBehalfOf': on_behalf_of,
            'purpose': purpose
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
        _request = self.http_client.get(_query_url, headers=_headers)
        CustomHeaderAuth.apply(_request)
        _context = self.execute_request(_request)

        # Endpoint and global error handling using HTTP status codes.
        if _context.response.status_code == 400:
            raise Error1ErrorException('Bad Request', _context)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, PayStatementReportRecord.from_dictionary)

    def get_voa_report_by_customer(self,
                                   customer_id,
                                   report_id,
                                   accept,
                                   content_type,
                                   on_behalf_of=None,
                                   purpose=None):
        """Does a GET request to /decisioning/v1/customers/{customerId}/reports/{reportId}.

        Get a report that has been generated by calling one of the Generate
        Report services.
        The report's status field will contain inProgress, failure, or
        success. If the status shows inProgress, the client app should wait 20
        seconds and then call again to see if the report is finished.
        See Permissible Purpose Codes for a list of permissible purposes for
        retrieving a report.

        Args:
            customer_id (long|int): Finicity’s ID of the customer
            report_id (string): Finicity’s ID of the report
            accept (string): Replace 'json' with 'xml' if preferred
            content_type (string): Replace 'json' with 'xml' if preferred
            on_behalf_of (string, optional): The name of the entity you are
                retrieving the report on behalf of.
            purpose (string, optional): 2-digit code from Permissible Purpose
                Codes, specifying the reason for retrieving this report.

        Returns:
            VOAReportRecord: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(customer_id=customer_id,
                                 report_id=report_id,
                                 accept=accept,
                                 content_type=content_type)

        # Prepare query URL
        _url_path = '/decisioning/v1/customers/{customerId}/reports/{reportId}'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, { 
            'customerId': customer_id,
            'reportId': report_id
        })
        _query_builder = Configuration.get_base_uri()
        _query_builder += _url_path
        _query_parameters = {
            'onBehalfOf': on_behalf_of,
            'purpose': purpose
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
        _request = self.http_client.get(_query_url, headers=_headers)
        CustomHeaderAuth.apply(_request)
        _context = self.execute_request(_request)

        # Endpoint and global error handling using HTTP status codes.
        if _context.response.status_code == 400:
            raise Error1ErrorException('Bad Request', _context)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, VOAReportRecord.from_dictionary)

    def get_voie_txverify_report_by_consumer(self,
                                             consumer_id,
                                             report_id,
                                             accept,
                                             content_type,
                                             on_behalf_of=None,
                                             purpose=None):
        """Does a GET request to /decisioning/v1/consumers/{consumerId}/reports/{reportId}.

        Get a report that has been generated by calling one of the Generate
        Report services.
        The report's status field will contain inProgress, failure, or
        success. If the status shows inProgress, the client app should wait 20
        seconds and then call again to see if the report is finished.
        See Permissible Purpose Codes for a list of permissible purposes for
        retrieving a report.

        Args:
            consumer_id (string): Finicity’s ID of the consumer (UUID with max
                length 32 characters)
            report_id (string): Finicity’s ID of the report
            accept (string): Replace 'json' with 'xml' if preferred
            content_type (string): Replace 'json' with 'xml' if preferred
            on_behalf_of (string, optional): The name of the entity you are
                retrieving the report on behalf of.
            purpose (string, optional): 2-digit code from Permissible Purpose
                Codes, specifying the reason for retrieving this report.

        Returns:
            VOIEPaystubWithTxverifyReportRecord: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(consumer_id=consumer_id,
                                 report_id=report_id,
                                 accept=accept,
                                 content_type=content_type)

        # Prepare query URL
        _url_path = '/decisioning/v1/consumers/{consumerId}/reports/{reportId}'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, { 
            'consumerId': consumer_id,
            'reportId': report_id
        })
        _query_builder = Configuration.get_base_uri()
        _query_builder += _url_path
        _query_parameters = {
            'onBehalfOf': on_behalf_of,
            'purpose': purpose
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
        _request = self.http_client.get(_query_url, headers=_headers)
        CustomHeaderAuth.apply(_request)
        _context = self.execute_request(_request)

        # Endpoint and global error handling using HTTP status codes.
        if _context.response.status_code == 400:
            raise Error1ErrorException('Bad Request', _context)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, VOIEPaystubWithTxverifyReportRecord.from_dictionary)

    def get_pay_statement_extraction_by_customer(self,
                                                 customer_id,
                                                 report_id,
                                                 accept,
                                                 content_type,
                                                 on_behalf_of=None,
                                                 purpose=None):
        """Does a GET request to /decisioning/v1/customers/{customerId}/reports/{reportId}.

        Get a report that has been generated by calling one of the Generate
        Report services.
        The report's status field will contain inProgress, failure, or
        success. If the status shows inProgress, the client app should wait 20
        seconds and then call again to see if the report is finished.
        See Permissible Purpose Codes for a list of permissible purposes for
        retrieving a report.

        Args:
            customer_id (long|int): Finicity’s ID of the customer
            report_id (string): Finicity’s ID of the report
            accept (string): Replace 'json' with 'xml' if preferred
            content_type (string): Replace 'json' with 'xml' if preferred
            on_behalf_of (string, optional): The name of the entity you are
                retrieving the report on behalf of.
            purpose (string, optional): 2-digit code from Permissible Purpose
                Codes, specifying the reason for retrieving this report.

        Returns:
            PayStatementReportRecord: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(customer_id=customer_id,
                                 report_id=report_id,
                                 accept=accept,
                                 content_type=content_type)

        # Prepare query URL
        _url_path = '/decisioning/v1/customers/{customerId}/reports/{reportId}'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, { 
            'customerId': customer_id,
            'reportId': report_id
        })
        _query_builder = Configuration.get_base_uri()
        _query_builder += _url_path
        _query_parameters = {
            'onBehalfOf': on_behalf_of,
            'purpose': purpose
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
        _request = self.http_client.get(_query_url, headers=_headers)
        CustomHeaderAuth.apply(_request)
        _context = self.execute_request(_request)

        # Endpoint and global error handling using HTTP status codes.
        if _context.response.status_code == 400:
            raise Error1ErrorException('Bad Request', _context)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, PayStatementReportRecord.from_dictionary)

    def add_customer_v_1(self,
                         accept,
                         content_type,
                         body):
        """Does a POST request to /aggregation/v1/customers/active.

        This version 1 service has been replaced with version 2
        Enroll an active customer, which is the actual owner of one or more
        real-world accounts. This is a billable customer.
        This service is not available from the Test Drive. Calls to this
        service before enrolling in a paid plan will return HTTP 429 (Too Many
        Requests).

        Args:
            accept (string): application/json, application/xml
            content_type (string): application/json, application/xml
            body (AddCustomerRequest): The Fields For The New Customer

        Returns:
            AddCustomerResponse: Response from the API. default response

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
        _url_path = '/aggregation/v1/customers/active'
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
        _request = self.http_client.post(_query_url, headers=_headers, parameters=APIHelper.json_serialize(body))
        CustomHeaderAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, AddCustomerResponse.from_dictionary)

    def generate_connect_url_data_and_payments_connect(self,
                                                       accept,
                                                       body):
        """Does a POST request to /connect/v1/generate.

        No matter how you plan on implementing Finicity Connect, you’ll need
        to generate and retrieve a Finicity Connect Link.  You will need to
        specify what type of Finicity Connect you need depending on what will
        happen once the customer accounts and transaction data are gathered. 
        Below you’ll find how to generate the Connect link as well as where to
        specify what type of Finicity Connect you need.
        Once you have generated the link it will only last until the
        authentication token under which it was generated expires.  After that
        you will need to regenerate the Connect link under a new
        authentication token. We recommend generating a new authentication
        token when you generate a Connect link, to guarantee a full two hour
        life-span.
        Several Finicity products utilize Finicity Connect, and most products
        have their own type of Connect.  The Connect type is controlled by the
        “type” code in the call.  
        See the specific documentation for the types to see more details on
        the flow. This documentation gives the applicable implementation
        details for the following types......
        - ach
        - aggregation

        Args:
            accept (string): application/json, application/xml
            body (GenerateConnectURLRequestDataAndPayments): Expected body to
                be sent with the request

        Returns:
            GenerateConnectURLResponse: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(accept=accept,
                                 body=body)

        # Prepare query URL
        _url_path = '/connect/v1/generate'
        _query_builder = Configuration.get_base_uri()
        _query_builder += _url_path
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
        return APIHelper.json_deserialize(_context.response.raw_body, GenerateConnectURLResponse.from_dictionary)

    def generate_connect_url_lending(self,
                                     accept,
                                     body):
        """Does a POST request to /connect/v1/generate.

        No matter how you plan on implementing Finicity Connect, you’ll need
        to generate and retrieve a Finicity Connect Link.  You will need to
        specify what type of Finicity Connect you need depending on what will
        happen once the customer accounts and transaction data are gathered. 
        Below you’ll find how to generate the Connect link as well as where to
        specify what type of Finicity Connect you need.
        Once you have generated the link it will only last until the
        authentication token under which it was generated expires.  After that
        you will need to regenerate the Connect link under a new
        authentication token. We recommend generating a new authentication
        token when you generate a Connect link, to guarantee a full two hour
        life-span.
        Several Finicity products utilize Finicity Connect, and most products
        have their own type of Connect.  The Connect type is controlled by the
        “type” code in the call. For lending, each type signifies a report
        that will be generated as part of the connect flow unless otherwise
        specified.
        See the specific documentation for the types to see more details on
        the flow. This documentation gives the applicable implementation
        details for the following types......
        - voa
        - voahistory
        - voi
        - voieTxVerify
        - voieStatement
        - payStatement
        - assetSummary
        - preQualVoa

        Args:
            accept (string): application/json, application/xml
            body (GenerateConnectURLRequestLending): Expected body to be sent
                with the request

        Returns:
            GenerateConnectURLResponse: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(accept=accept,
                                 body=body)

        # Prepare query URL
        _url_path = '/connect/v1/generate'
        _query_builder = Configuration.get_base_uri()
        _query_builder += _url_path
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
        return APIHelper.json_deserialize(_context.response.raw_body, GenerateConnectURLResponse.from_dictionary)

    def generate_connect_url_lite(self,
                                  accept,
                                  body):
        """Does a POST request to /connect/v1/generate.

        No matter how you plan on implementing Finicity Connect, you’ll need
        to generate and retrieve a Finicity Connect Link.  You will need to
        specify what type of Finicity Connect you need depending on what will
        happen once the customer accounts and transaction data are gathered. 
        Below you’ll find how to generate the Connect link as well as where to
        specify what type of Finicity Connect you need.
        Once you have generated the link it will only last until the
        authentication token under which it was generated expires.  After that
        you will need to regenerate the Connect link under a new
        authentication token. We recommend generating a new authentication
        token when you generate a Connect link, to guarantee a full two hour
        life-span.
        Several Finicity products utilize Finicity Connect, and most products
        have their own type of Connect.  The Connect type is controlled by the
        “type” code in the call.  
        See the specific documentation for the types to see more details on
        the flow. This documentation gives the applicable implementation
        details for the following types......
        - lite

        Args:
            accept (string): application/json, application/xml
            body (GenerateConnectURLRequestLite): Expected body to be sent
                with the request

        Returns:
            GenerateConnectURLResponse: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(accept=accept,
                                 body=body)

        # Prepare query URL
        _url_path = '/connect/v1/generate'
        _query_builder = Configuration.get_base_uri()
        _query_builder += _url_path
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
        return APIHelper.json_deserialize(_context.response.raw_body, GenerateConnectURLResponse.from_dictionary)

    def generate_connect_url_fix(self,
                                 accept,
                                 body):
        """Does a POST request to /connect/v1/generate.

        No matter how you plan on implementing Finicity Connect, you’ll need
        to generate and retrieve a Finicity Connect Link.  You will need to
        specify what type of Finicity Connect you need depending on what will
        happen once the customer accounts and transaction data are gathered. 
        Below you’ll find how to generate the Connect link as well as where to
        specify what type of Finicity Connect you need.
        Once you have generated the link it will only last until the
        authentication token under which it was generated expires.  After that
        you will need to regenerate the Connect link under a new
        authentication token. We recommend generating a new authentication
        token when you generate a Connect link, to guarantee a full two hour
        life-span.
        Several Finicity products utilize Finicity Connect, and most products
        have their own type of Connect.  The Connect type is controlled by the
        “type” code in the call.  
        See the specific documentation for the types to see more details on
        the flow. This documentation gives the applicable implementation
        details for the following types......
        - fix

        Args:
            accept (string): application/json, application/xml
            body (GenerateConnectURLRequestFix): Expected body to be sent with
                the request

        Returns:
            GenerateConnectURLResponse: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(accept=accept,
                                 body=body)

        # Prepare query URL
        _url_path = '/connect/v1/generate'
        _query_builder = Configuration.get_base_uri()
        _query_builder += _url_path
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
        return APIHelper.json_deserialize(_context.response.raw_body, GenerateConnectURLResponse.from_dictionary)

    def send_connect_email(self,
                           accept,
                           body):
        """Does a POST request to /connect/v1/send/email.

        A connect email sends an email to the customer which will contain a
        link to the connect flow. You will need to specify what type of
        Finicity Connect you need depending on what will happen once the
        customer accounts and transaction data are gathered. 
        Several Finicity products utilize Finicity Connect, and most products
        have their own type of Connect.  The Connect type is controlled by the
        “type” code in the call.  Many times the type also corresponds to the
        report that will be run upon completing the Connect flow.
        For Send Connect Email service it does not support the types
        aggregation, lite and fix.
        See the endpoint Generate Finicity Connect URL (Lending) for
        additional details on a non email implementation.

        Args:
            accept (string): application/json
            body (GenerateConnectEmailRequest): Expected body to be sent with
                the request

        Returns:
            GenerateConnectEmailResponseMultipleBorrowers: Response from the
                API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(accept=accept,
                                 body=body)

        # Prepare query URL
        _url_path = '/connect/v1/send/email'
        _query_builder = Configuration.get_base_uri()
        _query_builder += _url_path
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
        return APIHelper.json_deserialize(_context.response.raw_body, GenerateConnectEmailResponseMultipleBorrowers.from_dictionary)

    def get_transactions_report_by_customer(self,
                                            customer_id,
                                            report_id,
                                            accept,
                                            content_type,
                                            on_behalf_of=None,
                                            purpose=None):
        """Does a GET request to /decisioning/v1/customers/{customerId}/reports/{reportId}.

        Get a report that has been generated by calling one of the Generate
        Report services.
        The report's status field will contain inProgress, failure, or
        success. If the status shows inProgress, the client app should wait 20
        seconds and then call again to see if the report is finished.
        See Permissible Purpose Codes for a list of permissible purposes for
        retrieving a report.

        Args:
            customer_id (long|int): Finicity’s ID of the customer
            report_id (string): Finicity’s ID of the report (UUID with max
                length 32 characters)
            accept (string): Replace 'json' with 'xml' if preferred
            content_type (string): Replace 'json' with 'xml' if preferred
            on_behalf_of (string, optional): The name of the entity you are
                retrieving the report on behalf of.
            purpose (string, optional): 2-digit code from Permissible Purpose
                Codes, specifying the reason for retrieving this report.

        Returns:
            TransactionsReportRecord: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(customer_id=customer_id,
                                 report_id=report_id,
                                 accept=accept,
                                 content_type=content_type)

        # Prepare query URL
        _url_path = '/decisioning/v1/customers/{customerId}/reports/{reportId}'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, { 
            'customerId': customer_id,
            'reportId': report_id
        })
        _query_builder = Configuration.get_base_uri()
        _query_builder += _url_path
        _query_parameters = {
            'onBehalfOf': on_behalf_of,
            'purpose': purpose
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
        _request = self.http_client.get(_query_url, headers=_headers)
        CustomHeaderAuth.apply(_request)
        _context = self.execute_request(_request)

        # Endpoint and global error handling using HTTP status codes.
        if _context.response.status_code == 400:
            raise Error1ErrorException('Bad Request', _context)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, TransactionsReportRecord.from_dictionary)

    def get_transactions_report_by_consumer(self,
                                            consumer_id,
                                            report_id,
                                            accept,
                                            content_type,
                                            on_behalf_of=None,
                                            purpose=None):
        """Does a GET request to /decisioning/v1/consumers/{consumerId}/reports/{reportId}.

        Get a report that has been generated by calling one of the Generate
        Report services.
        The report's status field will contain inProgress, failure, or
        success. If the status shows inProgress, the client app should wait 20
        seconds and then call again to see if the report is finished.
        See Permissible Purpose Codes for a list of permissible purposes for
        retrieving a report.

        Args:
            consumer_id (string): Finicity’s ID of the consumer (UUID with max
                length 32 characters)
            report_id (string): Finicity’s ID of the report
            accept (string): JSON or  XML
            content_type (string): JSON or  XML
            on_behalf_of (string, optional): The name of the entity you are
                retrieving the report on behalf of.
            purpose (string, optional): 2-digit code from Permissible Purpose
                Codes, specifying the reason for retrieving this report.

        Returns:
            TransactionsReportRecord: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(consumer_id=consumer_id,
                                 report_id=report_id,
                                 accept=accept,
                                 content_type=content_type)

        # Prepare query URL
        _url_path = '/decisioning/v1/consumers/{consumerId}/reports/{reportId}'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, { 
            'consumerId': consumer_id,
            'reportId': report_id
        })
        _query_builder = Configuration.get_base_uri()
        _query_builder += _url_path
        _query_parameters = {
            'onBehalfOf': on_behalf_of,
            'purpose': purpose
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
        _request = self.http_client.get(_query_url, headers=_headers)
        CustomHeaderAuth.apply(_request)
        _context = self.execute_request(_request)

        # Endpoint and global error handling using HTTP status codes.
        if _context.response.status_code == 400:
            raise Error1ErrorException('Bad Request', _context)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, TransactionsReportRecord.from_dictionary)

    def get_app_registration_status_v_1(self):
        """Does a GET request to /aggregation/v1/partners/applications.

        Get the status of your application registration to access FI's with
        OAuth connections.

        Returns:
            AppStatusesV1: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/aggregation/v1/partners/applications'
        _query_builder = Configuration.get_base_uri()
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json',
            'Finicity-App-Key': Configuration.finicity_app_key
        }

        # Prepare and execute request
        _request = self.http_client.get(_query_url, headers=_headers)
        CustomHeaderAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, AppStatusesV1.from_dictionary)

    def get_statement_report_by_customer(self,
                                         customer_id,
                                         report_id,
                                         accept,
                                         content_type,
                                         on_behalf_of=None,
                                         purpose=None):
        """Does a GET request to /decisioning/v1/customers/{customerId}/reports/{reportId}.

        Get a report that has been generated by calling one of the Generate
        Report services.
        The report's status field will contain inProgress, failure, or
        success. If the status shows inProgress, the client app should wait 20
        seconds and then call again to see if the report is finished.
        See Permissible Purpose Codes for a list of permissible purposes for
        retrieving a report.

        Args:
            customer_id (long|int): Finicity’s ID of the customer
            report_id (string): Finicity’s ID of the report
            accept (string): Replace 'json' with 'xml' if preferred
            content_type (string): Replace 'json' with 'xml' if preferred
            on_behalf_of (string, optional): The name of the entity you are
                retrieving the report on behalf of.
            purpose (string, optional): 2-digit code from Permissible Purpose
                Codes, specifying the reason for retrieving this report.

        Returns:
            StatementReportRecord: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(customer_id=customer_id,
                                 report_id=report_id,
                                 accept=accept,
                                 content_type=content_type)

        # Prepare query URL
        _url_path = '/decisioning/v1/customers/{customerId}/reports/{reportId}'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, { 
            'customerId': customer_id,
            'reportId': report_id
        })
        _query_builder = Configuration.get_base_uri()
        _query_builder += _url_path
        _query_parameters = {
            'onBehalfOf': on_behalf_of,
            'purpose': purpose
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
        _request = self.http_client.get(_query_url, headers=_headers)
        CustomHeaderAuth.apply(_request)
        _context = self.execute_request(_request)

        # Endpoint and global error handling using HTTP status codes.
        if _context.response.status_code == 400:
            raise Error1ErrorException('Bad Request', _context)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, StatementReportRecord.from_dictionary)

    def get_statement_report_by_consumer(self,
                                         consumer_id,
                                         report_id,
                                         accept,
                                         content_type,
                                         on_behalf_of=None,
                                         purpose=None):
        """Does a GET request to /decisioning/v1/consumers/{consumerId}/reports/{reportId}.

        Get a report that has been generated by calling one of the Generate
        Report services.
        The report's status field will contain inProgress, failure, or
        success. If the status shows inProgress, the client app should wait 20
        seconds and then call again to see if the report is finished.
        See Permissible Purpose Codes for a list of permissible purposes for
        retrieving a report.

        Args:
            consumer_id (string): Finicity’s ID of the consumer (UUID with max
                length 32 characters)
            report_id (string): Finicity’s ID of the report
            accept (string): Replace 'json' with 'xml' if preferred
            content_type (string): Replace 'json' with 'xml' if preferred
            on_behalf_of (string, optional): The name of the entity you are
                retrieving the report on behalf of.
            purpose (string, optional): 2-digit code from Permissible Purpose
                Codes, specifying the reason for retrieving this report.

        Returns:
            StatementReportRecord: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(consumer_id=consumer_id,
                                 report_id=report_id,
                                 accept=accept,
                                 content_type=content_type)

        # Prepare query URL
        _url_path = '/decisioning/v1/consumers/{consumerId}/reports/{reportId}'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, { 
            'consumerId': consumer_id,
            'reportId': report_id
        })
        _query_builder = Configuration.get_base_uri()
        _query_builder += _url_path
        _query_parameters = {
            'onBehalfOf': on_behalf_of,
            'purpose': purpose
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
        _request = self.http_client.get(_query_url, headers=_headers)
        CustomHeaderAuth.apply(_request)
        _context = self.execute_request(_request)

        # Endpoint and global error handling using HTTP status codes.
        if _context.response.status_code == 400:
            raise Error1ErrorException('Bad Request', _context)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, StatementReportRecord.from_dictionary)
