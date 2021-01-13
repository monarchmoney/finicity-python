# -*- coding: utf-8 -*-

import finicityapi.models.voie_payroll_report_constraints
import finicityapi.models.direct_pay_statement_fields
import finicityapi.models.error_message

class VOIEPayrollReportRecord(object):

    """Implementation of the 'VOIE - Payroll Report Record' model.

    TODO: type model description here.

    Attributes:
        id (string): Finicity's report ID
        portfolio_id (string): Finicity’s portfolio ID associated with the
            consumer on the report.
        gse_enabled (bool): Finicity internal use only
        customer_type (string): Customer type
        customer_id (long|int): Finicity ID for the customer
        request_id (string): Unique requestId for this specific call request
        consumer_id (string): Finicity report consumer ID (max length 32
            characters)
        consumer_ssn (string): Last 4 digits of the report consumer’s Social
            Security number
        requester_name (string): Name of Finicity partner requesting the
            report
        mtype (TypeEnum): Report type
        status (string): inProgress, success, or failure
        created_date (long|int): The date the report was generated
        title (string): Title of the report
        constraints (VOIEPayrollReportConstraints): TODO: type description
            here.
        direct_pay_statements (list of DirectPayStatementFields): Direct pay
            statement fields.
        errors (list of ErrorMessage): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id":'id',
        "portfolio_id":'portfolioId',
        "gse_enabled":'gseEnabled',
        "customer_type":'customerType',
        "customer_id":'customerId',
        "request_id":'requestId',
        "consumer_id":'consumerId',
        "consumer_ssn":'consumerSsn',
        "requester_name":'requesterName',
        "mtype":'type',
        "status":'status',
        "created_date":'createdDate',
        "title":'title',
        "constraints":'constraints',
        "direct_pay_statements":'directPayStatements',
        "errors":'errors'
    }

    def __init__(self,
                 id=None,
                 portfolio_id=None,
                 gse_enabled=True,
                 customer_type=None,
                 customer_id=None,
                 request_id=None,
                 consumer_id=None,
                 consumer_ssn=None,
                 requester_name=None,
                 mtype=None,
                 status=None,
                 created_date=None,
                 title=None,
                 constraints=None,
                 direct_pay_statements=None,
                 errors=None,
                 additional_properties = {}):
        """Constructor for the VOIEPayrollReportRecord class"""

        # Initialize members of the class
        self.id = id
        self.portfolio_id = portfolio_id
        self.gse_enabled = gse_enabled
        self.customer_type = customer_type
        self.customer_id = customer_id
        self.request_id = request_id
        self.consumer_id = consumer_id
        self.consumer_ssn = consumer_ssn
        self.requester_name = requester_name
        self.mtype = mtype
        self.status = status
        self.created_date = created_date
        self.title = title
        self.constraints = constraints
        self.direct_pay_statements = direct_pay_statements
        self.errors = errors

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
        portfolio_id = dictionary.get('portfolioId')
        gse_enabled = dictionary.get("gseEnabled") if dictionary.get("gseEnabled") else True
        customer_type = dictionary.get('customerType')
        customer_id = dictionary.get('customerId')
        request_id = dictionary.get('requestId')
        consumer_id = dictionary.get('consumerId')
        consumer_ssn = dictionary.get('consumerSsn')
        requester_name = dictionary.get('requesterName')
        mtype = dictionary.get('type')
        status = dictionary.get('status')
        created_date = dictionary.get('createdDate')
        title = dictionary.get('title')
        constraints = finicityapi.models.voie_payroll_report_constraints.VOIEPayrollReportConstraints.from_dictionary(dictionary.get('constraints')) if dictionary.get('constraints') else None
        direct_pay_statements = None
        if dictionary.get('directPayStatements') != None:
            direct_pay_statements = list()
            for structure in dictionary.get('directPayStatements'):
                direct_pay_statements.append(finicityapi.models.direct_pay_statement_fields.DirectPayStatementFields.from_dictionary(structure))
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
                   portfolio_id,
                   gse_enabled,
                   customer_type,
                   customer_id,
                   request_id,
                   consumer_id,
                   consumer_ssn,
                   requester_name,
                   mtype,
                   status,
                   created_date,
                   title,
                   constraints,
                   direct_pay_statements,
                   errors,
                   dictionary)


