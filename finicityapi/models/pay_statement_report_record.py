# -*- coding: utf-8 -*-

import finicityapi.models.error_message
import finicityapi.models.pay_statement_constraints
import finicityapi.models.voie_pay_statement

class PayStatementReportRecord(object):

    """Implementation of the 'Pay Statement Report Record' model.

    TODO: type model description here.

    Attributes:
        id (string): Report id
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
        constraints (PayStatementConstraints): TODO: type description here.
        source (string): TODO: type description here.
        customer_type (string): Customer type
        title (string): Title of the report
        start_date (long|int): The postedDate of the earliest transaction
            analyzed for this report
        end_date (long|int): The postedDate of the latest transaction analyzed
            for this report
        portfolio_id (string): Finicity’s portfolio ID associated with the
            consumer on the report.
        gse_enabled (bool): TODO: type description here.
        report_style (string): TODO: type description here.
        number_of_billable_assets (int): Total number of billable pay
            statements included in the report
        asset_ids (list of string): TODO: type description here.
        pay_statement_txverify_dao_list (list of VOIEPayStatement): Extracted
            pay statement details

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
        "start_date":'startDate',
        "end_date":'endDate',
        "portfolio_id":'portfolioId',
        "gse_enabled":'gseEnabled',
        "report_style":'reportStyle',
        "number_of_billable_assets":'numberOfBillableAssets',
        "asset_ids":'assetIds',
        "pay_statement_txverify_dao_list":'payStatementTxVerifyDaoList',
        "errors":'errors',
        "source":'source'
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
                 start_date=None,
                 end_date=None,
                 portfolio_id=None,
                 gse_enabled=None,
                 report_style=None,
                 number_of_billable_assets=None,
                 asset_ids=None,
                 pay_statement_txverify_dao_list=None,
                 errors=None,
                 source=None,
                 additional_properties = {}):
        """Constructor for the PayStatementReportRecord class"""

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
        self.source = source
        self.customer_type = customer_type
        self.title = title
        self.start_date = start_date
        self.end_date = end_date
        self.portfolio_id = portfolio_id
        self.gse_enabled = gse_enabled
        self.report_style = report_style
        self.number_of_billable_assets = number_of_billable_assets
        self.asset_ids = asset_ids
        self.pay_statement_txverify_dao_list = pay_statement_txverify_dao_list

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
        constraints = finicityapi.models.pay_statement_constraints.PayStatementConstraints.from_dictionary(dictionary.get('constraints')) if dictionary.get('constraints') else None
        customer_type = dictionary.get('customerType')
        title = dictionary.get('title')
        start_date = dictionary.get('startDate')
        end_date = dictionary.get('endDate')
        portfolio_id = dictionary.get('portfolioId')
        gse_enabled = dictionary.get('gseEnabled')
        report_style = dictionary.get('reportStyle')
        number_of_billable_assets = dictionary.get('numberOfBillableAssets')
        asset_ids = dictionary.get('assetIds')
        pay_statement_txverify_dao_list = None
        if dictionary.get('payStatementTxVerifyDaoList') != None:
            pay_statement_txverify_dao_list = list()
            for structure in dictionary.get('payStatementTxVerifyDaoList'):
                pay_statement_txverify_dao_list.append(finicityapi.models.voie_pay_statement.VOIEPayStatement.from_dictionary(structure))
        errors = None
        if dictionary.get('errors') != None:
            errors = list()
            for structure in dictionary.get('errors'):
                errors.append(finicityapi.models.error_message.ErrorMessage.from_dictionary(structure))
        source = dictionary.get('source')

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
                   start_date,
                   end_date,
                   portfolio_id,
                   gse_enabled,
                   report_style,
                   number_of_billable_assets,
                   asset_ids,
                   pay_statement_txverify_dao_list,
                   errors,
                   source,
                   dictionary)


