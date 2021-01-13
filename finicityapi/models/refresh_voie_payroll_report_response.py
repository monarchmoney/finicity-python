# -*- coding: utf-8 -*-

import finicityapi.models.error_message
import finicityapi.models.payroll_report_refresh_response_constraints

class RefreshVOIEPayrollReportResponse(object):

    """Implementation of the 'Refresh VOIE - Payroll Report Response' model.

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
        constraints (PayrollReportRefreshResponseConstraints): TODO: type
            description here.
        customer_type (string): Customer type
        title (string): Title of the report
        portfolio_id (string): Finicity’s portfolio ID associated with the
            consumer on the report.

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
                 errors=None,
                 additional_properties = {}):
        """Constructor for the RefreshVOIEPayrollReportResponse class"""

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
        constraints = finicityapi.models.payroll_report_refresh_response_constraints.PayrollReportRefreshResponseConstraints.from_dictionary(dictionary.get('constraints')) if dictionary.get('constraints') else None
        customer_type = dictionary.get('customerType')
        title = dictionary.get('title')
        portfolio_id = dictionary.get('portfolioId')
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
                   errors,
                   dictionary)


