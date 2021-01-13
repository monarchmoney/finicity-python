# -*- coding: utf-8 -*-

import finicityapi.models.error_message
import finicityapi.models.report_constraints
import finicityapi.models.prequalification_report_institution
import finicityapi.models.asset_summary

class PrequalificationReportRecord(object):

    """Implementation of the 'Prequalification Report Record' model.

    TODO: type model description here.

    Attributes:
        id (string): Finicity's report ID
        customer_id (long|int): Finicity ID for the customer
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
        gse_enabled (bool): Finicity Internal Use Only
        consolidated_available_balance (float): Sum of Available Balance for
            all of the accounts included in the report
        portfolio_id (string): Finicity’s portfolio ID associated with the
            consumer on the report.
        consumer_id (string): Finicity report consumer ID (max length 32
            characters)
        consumer_ssn (string): Last 4 digits of the report consumer’s Social
            Security number
        institutions (list of PrequalificationReportInstitution): A list of
            institution records, including information about the individual
            accounts used in this report
        assets (AssetSummary): TODO: type description here.

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
        "customer_type":'customerType',
        "title":'title',
        "start_date":'startDate',
        "end_date":'endDate',
        "days":'days',
        "seasoned":'seasoned',
        "gse_enabled":'gseEnabled',
        "consolidated_available_balance":'consolidatedAvailableBalance',
        "portfolio_id":'portfolioId',
        "consumer_id":'consumerId',
        "consumer_ssn":'consumerSsn',
        "institutions":'institutions',
        "assets":'assets',
        "errors":'errors',
        "constraints":'constraints',
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
                 customer_type=None,
                 title=None,
                 start_date=None,
                 end_date=None,
                 days=None,
                 seasoned=None,
                 gse_enabled=None,
                 consolidated_available_balance=None,
                 portfolio_id=None,
                 consumer_id=None,
                 consumer_ssn=None,
                 institutions=None,
                 assets=None,
                 errors=None,
                 constraints=None,
                 source=None,
                 additional_properties = {}):
        """Constructor for the PrequalificationReportRecord class"""

        # Initialize members of the class
        self.id = id
        self.customer_id = customer_id
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
        self.consolidated_available_balance = consolidated_available_balance
        self.portfolio_id = portfolio_id
        self.consumer_id = consumer_id
        self.consumer_ssn = consumer_ssn
        self.institutions = institutions
        self.assets = assets

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
        customer_type = dictionary.get('customerType')
        title = dictionary.get('title')
        start_date = dictionary.get('startDate')
        end_date = dictionary.get('endDate')
        days = dictionary.get('days')
        seasoned = dictionary.get('seasoned')
        gse_enabled = dictionary.get('gseEnabled')
        consolidated_available_balance = dictionary.get('consolidatedAvailableBalance')
        portfolio_id = dictionary.get('portfolioId')
        consumer_id = dictionary.get('consumerId')
        consumer_ssn = dictionary.get('consumerSsn')
        institutions = None
        if dictionary.get('institutions') != None:
            institutions = list()
            for structure in dictionary.get('institutions'):
                institutions.append(finicityapi.models.prequalification_report_institution.PrequalificationReportInstitution.from_dictionary(structure))
        assets = finicityapi.models.asset_summary.AssetSummary.from_dictionary(dictionary.get('assets')) if dictionary.get('assets') else None
        errors = None
        if dictionary.get('errors') != None:
            errors = list()
            for structure in dictionary.get('errors'):
                errors.append(finicityapi.models.error_message.ErrorMessage.from_dictionary(structure))
        constraints = finicityapi.models.report_constraints.ReportConstraints.from_dictionary(dictionary.get('constraints')) if dictionary.get('constraints') else None
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
                   customer_type,
                   title,
                   start_date,
                   end_date,
                   days,
                   seasoned,
                   gse_enabled,
                   consolidated_available_balance,
                   portfolio_id,
                   consumer_id,
                   consumer_ssn,
                   institutions,
                   assets,
                   errors,
                   constraints,
                   source,
                   dictionary)


