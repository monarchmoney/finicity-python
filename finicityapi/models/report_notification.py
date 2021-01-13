# -*- coding: utf-8 -*-


class ReportNotification(object):

    """Implementation of the 'ReportNotification' model.

    TODO: type model description here.

    Attributes:
        consumer_id (string): Finicity’s consumer ID. This field is optional
            and may not always return.
        consumer_ssn (string): The last four of the consumer’s social security
            number. This field is optional and may not always return.
        event_name (string): The event name of the webhook. This will either
            be inProgress, failed, primaryFieldUpdate, or done.
        id (string): Finicity’s report ID
        status (string): inProgress, success, failure, or editing
        mtype (string): Finicity’s report type. This field is optional and may
            not always return.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "consumer_id":'consumerId',
        "consumer_ssn":'consumerSsn',
        "event_name":'eventName',
        "id":'id',
        "status":'status',
        "mtype":'type'
    }

    def __init__(self,
                 consumer_id=None,
                 consumer_ssn=None,
                 event_name=None,
                 id=None,
                 status=None,
                 mtype=None,
                 additional_properties = {}):
        """Constructor for the ReportNotification class"""

        # Initialize members of the class
        self.consumer_id = consumer_id
        self.consumer_ssn = consumer_ssn
        self.event_name = event_name
        self.id = id
        self.status = status
        self.mtype = mtype

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
        consumer_id = dictionary.get('consumerId')
        consumer_ssn = dictionary.get('consumerSsn')
        event_name = dictionary.get('eventName')
        id = dictionary.get('id')
        status = dictionary.get('status')
        mtype = dictionary.get('type')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(consumer_id,
                   consumer_ssn,
                   event_name,
                   id,
                   status,
                   mtype,
                   dictionary)


