# -*- coding: utf-8 -*-

import finicityapi.models.voie_txverify_report_income_stream

class VOIETxverifyReportAccount(object):

    """Implementation of the 'VOIE TXVerify Report Account' model.

    TODO: type model description here.

    Attributes:
        id (long|int): The generated FInicity ID of the account
        number (string): The account number from the institution (all digits
            except the last four are obfuscated)
        owner_name (string): The name(s) of the account owner(s). This field
            is optional. If no owner information is available, this field will
            not appear in the report.
        owner_address (string): The mailing address of the account owner(s).
            This field is optional. If no owner information is available, this
            field will not appear in the report.
        name (string): The account name from the institution
        mtype (string): One of the values from Account Types
        aggregation_status_code (int): The status of the most recent
            aggregation attempt (see Handling Aggregation Status Codes)
        income_streams (list of VOIETxverifyReportIncomeStream): A list of
            income stream records

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id":'id',
        "number":'number',
        "owner_name":'ownerName',
        "owner_address":'ownerAddress',
        "name":'name',
        "mtype":'type',
        "aggregation_status_code":'aggregationStatusCode',
        "income_streams":'incomeStreams'
    }

    def __init__(self,
                 id=None,
                 number=None,
                 owner_name=None,
                 owner_address=None,
                 name=None,
                 mtype=None,
                 aggregation_status_code=None,
                 income_streams=None,
                 additional_properties = {}):
        """Constructor for the VOIETxverifyReportAccount class"""

        # Initialize members of the class
        self.id = id
        self.number = number
        self.owner_name = owner_name
        self.owner_address = owner_address
        self.name = name
        self.mtype = mtype
        self.aggregation_status_code = aggregation_status_code
        self.income_streams = income_streams

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
        number = dictionary.get('number')
        owner_name = dictionary.get('ownerName')
        owner_address = dictionary.get('ownerAddress')
        name = dictionary.get('name')
        mtype = dictionary.get('type')
        aggregation_status_code = dictionary.get('aggregationStatusCode')
        income_streams = None
        if dictionary.get('incomeStreams') != None:
            income_streams = list()
            for structure in dictionary.get('incomeStreams'):
                income_streams.append(finicityapi.models.voie_txverify_report_income_stream.VOIETxverifyReportIncomeStream.from_dictionary(structure))

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(id,
                   number,
                   owner_name,
                   owner_address,
                   name,
                   mtype,
                   aggregation_status_code,
                   income_streams,
                   dictionary)


