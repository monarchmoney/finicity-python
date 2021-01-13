# -*- coding: utf-8 -*-

import finicityapi.models.report_constraints

class ReportSummary(object):

    """Implementation of the 'Report Summary' model.

    TODO: type model description here.

    Attributes:
        id (string): The Finicity report ID
        consumer_id (string): Finicity ID for the consumer
        consumer_ssn (string): Last 4 digits of the report consumer's Social
            Security number
        requester_name (string): Name of Finicity partner requesting the
            report
        request_id (string): The unique requestId for this specific call
            request
        constraints (ReportConstraints): TODO: type description here.
        mtype (TypeEnum): Report type
        status (string): inProgress, success, or failure
        created_date (long|int): The date the report was generated

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id":'id',
        "consumer_id":'consumerId',
        "consumer_ssn":'consumerSsn',
        "requester_name":'requesterName',
        "request_id":'requestId',
        "constraints":'constraints',
        "mtype":'type',
        "status":'status',
        "created_date":'createdDate'
    }

    def __init__(self,
                 id=None,
                 consumer_id=None,
                 consumer_ssn=None,
                 requester_name=None,
                 request_id=None,
                 constraints=None,
                 mtype=None,
                 status=None,
                 created_date=None,
                 additional_properties = {}):
        """Constructor for the ReportSummary class"""

        # Initialize members of the class
        self.id = id
        self.consumer_id = consumer_id
        self.consumer_ssn = consumer_ssn
        self.requester_name = requester_name
        self.request_id = request_id
        self.constraints = constraints
        self.mtype = mtype
        self.status = status
        self.created_date = created_date

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
        consumer_id = dictionary.get('consumerId')
        consumer_ssn = dictionary.get('consumerSsn')
        requester_name = dictionary.get('requesterName')
        request_id = dictionary.get('requestId')
        constraints = finicityapi.models.report_constraints.ReportConstraints.from_dictionary(dictionary.get('constraints')) if dictionary.get('constraints') else None
        mtype = dictionary.get('type')
        status = dictionary.get('status')
        created_date = dictionary.get('createdDate')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(id,
                   consumer_id,
                   consumer_ssn,
                   requester_name,
                   request_id,
                   constraints,
                   mtype,
                   status,
                   created_date,
                   dictionary)


