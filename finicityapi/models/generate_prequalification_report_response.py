# -*- coding: utf-8 -*-

import finicityapi.models.report_constraints
import finicityapi.models.error_message

class GeneratePrequalificationReportResponse(object):

    """Implementation of the 'Generate Prequalification Report Response' model.

    TODO: type model description here.

    Attributes:
        id (string): The Finicity report ID
        portfolio_id (string): A unique identifier that will be consistent
            across all reports created for the same customer.
        customer_type (string): Type of the customer
        customer_id (long|int): Finicity's customer ID
        request_id (string): Finicity indicator to track all activity
            associated with this report.
        requester_name (string): Name of Finicity partner requesting the
            report
        created_date (long|int): The date the report was generated
        title (string): Finicity's title of the report
        consumer_id (string): Finicity ID of the consumer
        consumer_ssn (string): Last 4 digits of the report consumer’s Social
            Security number
        constraints (ReportConstraints): TODO: type description here.
        mtype (TypeEnum): Type of the report
        status (string): inProgress, success, or failure
        errors (list of ErrorMessage): TODO: type description here.
        source (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id":'id',
        "portfolio_id":'portfolioId',
        "customer_type":'customerType',
        "customer_id":'customerId',
        "request_id":'requestId',
        "requester_name":'requesterName',
        "created_date":'createdDate',
        "title":'title',
        "consumer_id":'consumerId',
        "consumer_ssn":'consumerSsn',
        "mtype":'type',
        "status":'status',
        "constraints":'constraints',
        "errors":'errors',
        "source":'source'
    }

    def __init__(self,
                 id=None,
                 portfolio_id=None,
                 customer_type=None,
                 customer_id=None,
                 request_id=None,
                 requester_name=None,
                 created_date=None,
                 title=None,
                 consumer_id=None,
                 consumer_ssn=None,
                 mtype=None,
                 status=None,
                 constraints=None,
                 errors=None,
                 source=None,
                 additional_properties = {}):
        """Constructor for the GeneratePrequalificationReportResponse class"""

        # Initialize members of the class
        self.id = id
        self.portfolio_id = portfolio_id
        self.customer_type = customer_type
        self.customer_id = customer_id
        self.request_id = request_id
        self.requester_name = requester_name
        self.created_date = created_date
        self.title = title
        self.consumer_id = consumer_id
        self.consumer_ssn = consumer_ssn
        self.constraints = constraints
        self.mtype = mtype
        self.status = status
        self.errors = errors
        self.source = source

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
        customer_type = dictionary.get('customerType')
        customer_id = dictionary.get('customerId')
        request_id = dictionary.get('requestId')
        requester_name = dictionary.get('requesterName')
        created_date = dictionary.get('createdDate')
        title = dictionary.get('title')
        consumer_id = dictionary.get('consumerId')
        consumer_ssn = dictionary.get('consumerSsn')
        mtype = dictionary.get('type')
        status = dictionary.get('status')
        constraints = finicityapi.models.report_constraints.ReportConstraints.from_dictionary(dictionary.get('constraints')) if dictionary.get('constraints') else None
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
                   portfolio_id,
                   customer_type,
                   customer_id,
                   request_id,
                   requester_name,
                   created_date,
                   title,
                   consumer_id,
                   consumer_ssn,
                   mtype,
                   status,
                   constraints,
                   errors,
                   source,
                   dictionary)


