# -*- coding: utf-8 -*-

import finicityapi.models.error_message
import finicityapi.models.voie_paystub_with_txverify_response_constraints
import finicityapi.models.voie_txverify_pay_statement
import finicityapi.models.voie_txverify_report_institution

class VOIEPaystubWithTxverifyReportRecord(object):

    """Implementation of the 'VOIE - Paystub with TXVerify Report Record' model.

    TODO: type model description here.

    Attributes:
        id (string): Finicity's report ID
        customer_id (long|int): Finicity ID for the customer
        consumer_id (string): Finicity report consumer ID (max length 32
            characters)
        consumer_ssn (string): Last 4 digits of the report consumer’s Social
            Security number
        requester_name (string): Name of Finicity partner requesting the
            report
        request_id (string): Unique requestId for this specific call request
        mtype (TypeEnum): Report type
        status (string): inProgress, success, or failure
        errors (list of ErrorMessage): TODO: type description here.
        created_date (long|int): The date the report was generated
        constraints (VOIEPaystubWithTxverifyResponseConstraints): TODO: type
            description here.
        customer_type (string): Customer type
        title (string): Title of the report
        portfolio_id (string): Finicity’s portfolio ID associated with the
            consumer on the report.
        number_of_billable_assets (int): Total number of billable pay
            statements included in the report
        report_style (string): One of the styles of VOIE: voieWithInterview,
            voieWithReport, voieWithStatement
        asset_ids (list of string): The pay statements included in the report
        pay_statements (list of VOIETxverifyPayStatement): Pay statement
            details
        institutions (list of VOIETxverifyReportInstitution): Institution
            details

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id":'id',
        "customer_id":'customerId',
        "consumer_id":'consumerId',
        "consumer_ssn":'consumerSsn',
        "requester_name":'requesterName',
        "request_id":'requestId',
        "mtype":'type',
        "status":'status',
        "created_date":'createdDate',
        "constraints":'constraints',
        "customer_type":'customerType',
        "title":'title',
        "portfolio_id":'portfolioId',
        "number_of_billable_assets":'numberOfBillableAssets',
        "report_style":'reportStyle',
        "asset_ids":'assetIds',
        "pay_statements":'payStatements',
        "institutions":'institutions',
        "errors":'errors'
    }

    def __init__(self,
                 id=None,
                 customer_id=None,
                 consumer_id=None,
                 consumer_ssn=None,
                 requester_name=None,
                 request_id=None,
                 mtype=None,
                 status=None,
                 created_date=None,
                 constraints=None,
                 customer_type=None,
                 title=None,
                 portfolio_id=None,
                 number_of_billable_assets=None,
                 report_style=None,
                 asset_ids=None,
                 pay_statements=None,
                 institutions=None,
                 errors=None,
                 additional_properties = {}):
        """Constructor for the VOIEPaystubWithTxverifyReportRecord class"""

        # Initialize members of the class
        self.id = id
        self.customer_id = customer_id
        self.consumer_id = consumer_id
        self.consumer_ssn = consumer_ssn
        self.requester_name = requester_name
        self.request_id = request_id
        self.mtype = mtype
        self.status = status
        self.errors = errors
        self.created_date = created_date
        self.constraints = constraints
        self.customer_type = customer_type
        self.title = title
        self.portfolio_id = portfolio_id
        self.number_of_billable_assets = number_of_billable_assets
        self.report_style = report_style
        self.asset_ids = asset_ids
        self.pay_statements = pay_statements
        self.institutions = institutions

        # Add additional model properties to the instance
        self.additional_properties = additional_properties


    @classmethod
    def from_dictionary(cls,
                        dictionary):
        """Creates an instance of this model from a dictionary

        Args:
            dictionary (dictionary): A dictionary representation of the object as
            obtained from the deserialization of the server's response. The keys
            MUST match property names in the API description.

        Returns:
            object: An instance of this structure class.

        """
        if dictionary is None:
            return None

        # Extract variables from the dictionary
        id = dictionary.get('id')
        customer_id = dictionary.get('customerId')
        consumer_id = dictionary.get('consumerId')
        consumer_ssn = dictionary.get('consumerSsn')
        requester_name = dictionary.get('requesterName')
        request_id = dictionary.get('requestId')
        mtype = dictionary.get('type')
        status = dictionary.get('status')
        created_date = dictionary.get('createdDate')
        constraints = finicityapi.models.voie_paystub_with_txverify_response_constraints.VOIEPaystubWithTxverifyResponseConstraints.from_dictionary(dictionary.get('constraints')) if dictionary.get('constraints') else None
        customer_type = dictionary.get('customerType')
        title = dictionary.get('title')
        portfolio_id = dictionary.get('portfolioId')
        number_of_billable_assets = dictionary.get('numberOfBillableAssets')
        report_style = dictionary.get('reportStyle')
        asset_ids = dictionary.get('assetIds')
        pay_statements = None
        if dictionary.get('payStatements') != None:
            pay_statements = list()
            for structure in dictionary.get('payStatements'):
                pay_statements.append(finicityapi.models.voie_txverify_pay_statement.VOIETxverifyPayStatement.from_dictionary(structure))
        institutions = None
        if dictionary.get('institutions') != None:
            institutions = list()
            for structure in dictionary.get('institutions'):
                institutions.append(finicityapi.models.voie_txverify_report_institution.VOIETxverifyReportInstitution.from_dictionary(structure))
        errors = None
        if dictionary.get('errors') != None:
            errors = list()
            for structure in dictionary.get('errors'):
                errors.append(finicityapi.models.error_message.ErrorMessage.from_dictionary(structure))

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(id,
                   customer_id,
                   consumer_id,
                   consumer_ssn,
                   requester_name,
                   request_id,
                   mtype,
                   status,
                   created_date,
                   constraints,
                   customer_type,
                   title,
                   portfolio_id,
                   number_of_billable_assets,
                   report_style,
                   asset_ids,
                   pay_statements,
                   institutions,
                   errors,
                   dictionary)


