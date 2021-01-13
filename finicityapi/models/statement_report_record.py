# -*- coding: utf-8 -*-

import finicityapi.models.generate_statement_report_constraints

class StatementReportRecord(object):

    """Implementation of the 'Statement Report Record' model.

    TODO: type model description here.

    Attributes:
        id (string): The Finicity report ID
        gse_enabled (bool): Finicity Internal Use Only
        customer_type (string): Customer type
        customer_id (long|int): Finicity ID for the customer
        request_id (string): Unique requestId for this specific call request
        title (string): Title of the report
        consumer_id (string): Finicity report consumer ID (max length 32
            characters)
        consumer_ssn (string): Last 4 digits of the report consumer’s Social
            Security number
        requester_name (string): Name of Finicity partner requesting the
            report
        constraints (GenerateStatementReportConstraints): TODO: type
            description here.
        mtype (string): Report type
        status (string): inProgress, success, or failure
        created_date (long|int): The date the report was generated
        asset_id (string): The asset ID of the statement that was retrieved.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id":'id',
        "gse_enabled":'gseEnabled',
        "customer_type":'customerType',
        "customer_id":'customerId',
        "request_id":'requestId',
        "title":'title',
        "consumer_id":'consumerId',
        "consumer_ssn":'consumerSsn',
        "requester_name":'requesterName',
        "constraints":'constraints',
        "mtype":'type',
        "status":'status',
        "created_date":'createdDate',
        "asset_id":'assetId'
    }

    def __init__(self,
                 id=None,
                 gse_enabled=None,
                 customer_type=None,
                 customer_id=None,
                 request_id=None,
                 title=None,
                 consumer_id=None,
                 consumer_ssn=None,
                 requester_name=None,
                 constraints=None,
                 mtype=None,
                 status=None,
                 created_date=None,
                 asset_id=None,
                 additional_properties = {}):
        """Constructor for the StatementReportRecord class"""

        # Initialize members of the class
        self.id = id
        self.gse_enabled = gse_enabled
        self.customer_type = customer_type
        self.customer_id = customer_id
        self.request_id = request_id
        self.title = title
        self.consumer_id = consumer_id
        self.consumer_ssn = consumer_ssn
        self.requester_name = requester_name
        self.constraints = constraints
        self.mtype = mtype
        self.status = status
        self.created_date = created_date
        self.asset_id = asset_id

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
        gse_enabled = dictionary.get('gseEnabled')
        customer_type = dictionary.get('customerType')
        customer_id = dictionary.get('customerId')
        request_id = dictionary.get('requestId')
        title = dictionary.get('title')
        consumer_id = dictionary.get('consumerId')
        consumer_ssn = dictionary.get('consumerSsn')
        requester_name = dictionary.get('requesterName')
        constraints = finicityapi.models.generate_statement_report_constraints.GenerateStatementReportConstraints.from_dictionary(dictionary.get('constraints')) if dictionary.get('constraints') else None
        mtype = dictionary.get('type')
        status = dictionary.get('status')
        created_date = dictionary.get('createdDate')
        asset_id = dictionary.get('assetId')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(id,
                   gse_enabled,
                   customer_type,
                   customer_id,
                   request_id,
                   title,
                   consumer_id,
                   consumer_ssn,
                   requester_name,
                   constraints,
                   mtype,
                   status,
                   created_date,
                   asset_id,
                   dictionary)


