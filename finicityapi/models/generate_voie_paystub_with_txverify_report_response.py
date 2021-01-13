# -*- coding: utf-8 -*-

import finicityapi.models.error_message
import finicityapi.models.voie_paystub_with_txverify_response_constraints

class GenerateVOIEPaystubWithTxverifyReportResponse(object):

    """Implementation of the 'Generate VOIE - Paystub (with TXVerify) Report Response' model.

    TODO: type model description here.

    Attributes:
        id (string): Finicity's report ID
        portfolio_id (string): Finicity’s portfolio ID associated with the
            consumer on the report.
        customer_id (long|int): Finicity ID for the customer
        consumer_id (string): Finicity report consumer ID (max length 32
            characters)
        consumer_ssn (string): Last 4 digits of the report consumer’s Social
            Security number
        requester_name (string): Name of Finicity partner requesting the
            report
        request_id (string): Unique requestId for this specific call request
        errors (list of ErrorMessage): TODO: type description here.
        created_date (long|int): The date the report was generated
        customer_type (string): Customer type
        constraints (VOIEPaystubWithTxverifyResponseConstraints): TODO: type
            description here.
        title (string): Title of the report
        mtype (TypeEnum): Report type
        status (string): inProgress, success, or failure

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id":'id',
        "portfolio_id":'portfolioId',
        "customer_id":'customerId',
        "consumer_id":'consumerId',
        "consumer_ssn":'consumerSsn',
        "requester_name":'requesterName',
        "request_id":'requestId',
        "created_date":'createdDate',
        "customer_type":'customerType',
        "constraints":'constraints',
        "title":'title',
        "mtype":'type',
        "status":'status',
        "errors":'errors'
    }

    def __init__(self,
                 id=None,
                 portfolio_id=None,
                 customer_id=None,
                 consumer_id=None,
                 consumer_ssn=None,
                 requester_name=None,
                 request_id=None,
                 created_date=None,
                 customer_type=None,
                 constraints=None,
                 title=None,
                 mtype=None,
                 status=None,
                 errors=None,
                 additional_properties = {}):
        """Constructor for the GenerateVOIEPaystubWithTxverifyReportResponse class"""

        # Initialize members of the class
        self.id = id
        self.portfolio_id = portfolio_id
        self.customer_id = customer_id
        self.consumer_id = consumer_id
        self.consumer_ssn = consumer_ssn
        self.requester_name = requester_name
        self.request_id = request_id
        self.errors = errors
        self.created_date = created_date
        self.customer_type = customer_type
        self.constraints = constraints
        self.title = title
        self.mtype = mtype
        self.status = status

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
        customer_id = dictionary.get('customerId')
        consumer_id = dictionary.get('consumerId')
        consumer_ssn = dictionary.get('consumerSsn')
        requester_name = dictionary.get('requesterName')
        request_id = dictionary.get('requestId')
        created_date = dictionary.get('createdDate')
        customer_type = dictionary.get('customerType')
        constraints = finicityapi.models.voie_paystub_with_txverify_response_constraints.VOIEPaystubWithTxverifyResponseConstraints.from_dictionary(dictionary.get('constraints')) if dictionary.get('constraints') else None
        title = dictionary.get('title')
        mtype = dictionary.get('type')
        status = dictionary.get('status')
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
                   customer_id,
                   consumer_id,
                   consumer_ssn,
                   requester_name,
                   request_id,
                   created_date,
                   customer_type,
                   constraints,
                   title,
                   mtype,
                   status,
                   errors,
                   dictionary)


