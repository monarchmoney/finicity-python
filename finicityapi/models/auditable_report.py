# -*- coding: utf-8 -*-

import finicityapi.models.error_message
import finicityapi.models.report_constraints
import finicityapi.models.report_institution

class AuditableReport(object):

    """Implementation of the 'AuditableReport' model.

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
        constraints (ReportConstraints): TODO: type description here.
        source (string): TODO: type description here.
        customer_type (string): Customer type
        title (string): Title of the report
        start_date (long|int): The postedDate of the earliest transaction
            analyzed for this report
        end_date (long|int): The postedDate of the latest transaction analyzed
            for this report
        days (long|int): Number of days covered by the report
        seasoned (bool): This will display true if the report covers more than
            180 days
        gse_enabled (bool): TODO: type description here.
        portfolio_id (string): Finicity’s portfolio ID associated with the
            consumer on the report.
        consolidated_available_balance (float): TODO: type description here.
        institutions (list of ReportInstitution): A list of institution
            records, including information about the individual accounts used
            in this report

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id":'id',
        "customer_id":'customerId',
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
        "days":'days',
        "seasoned":'seasoned',
        "gse_enabled":'gseEnabled',
        "portfolio_id":'portfolioId',
        "consolidated_available_balance":'consolidatedAvailableBalance',
        "institutions":'institutions',
        "consumer_id":'consumerId',
        "consumer_ssn":'consumerSsn',
        "errors":'errors',
        "source":'source'
    }

    def __init__(self,
                 id=None,
                 customer_id=None,
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
                 days=None,
                 seasoned=None,
                 gse_enabled=None,
                 portfolio_id=None,
                 consolidated_available_balance=None,
                 institutions=None,
                 consumer_id=None,
                 consumer_ssn=None,
                 errors=None,
                 source=None,
                 additional_properties = {}):
        """Constructor for the AuditableReport class"""

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
        self.days = days
        self.seasoned = seasoned
        self.gse_enabled = gse_enabled
        self.portfolio_id = portfolio_id
        self.consolidated_available_balance = consolidated_available_balance
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
        requester_name = dictionary.get('requesterName')
        request_id = dictionary.get('requestId')
        mtype = dictionary.get('type')
        status = dictionary.get('status')
        created_date = dictionary.get('createdDate')
        constraints = finicityapi.models.report_constraints.ReportConstraints.from_dictionary(dictionary.get('constraints')) if dictionary.get('constraints') else None
        customer_type = dictionary.get('customerType')
        title = dictionary.get('title')
        start_date = dictionary.get('startDate')
        end_date = dictionary.get('endDate')
        days = dictionary.get('days')
        seasoned = dictionary.get('seasoned')
        gse_enabled = dictionary.get('gseEnabled')
        portfolio_id = dictionary.get('portfolioId')
        consolidated_available_balance = dictionary.get('consolidatedAvailableBalance')
        institutions = None
        if dictionary.get('institutions') != None:
            institutions = list()
            for structure in dictionary.get('institutions'):
                institutions.append(finicityapi.models.report_institution.ReportInstitution.from_dictionary(structure))
        consumer_id = dictionary.get('consumerId')
        consumer_ssn = dictionary.get('consumerSsn')
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
                   days,
                   seasoned,
                   gse_enabled,
                   portfolio_id,
                   consolidated_available_balance,
                   institutions,
                   consumer_id,
                   consumer_ssn,
                   errors,
                   source,
                   dictionary)


