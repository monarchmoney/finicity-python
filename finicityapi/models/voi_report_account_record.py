# -*- coding: utf-8 -*-

import finicityapi.models.voi_report_income_stream_record
import finicityapi.models.voi_report_transaction_record

class VOIReportAccountRecord(object):

    """Implementation of the 'VOI Report Account Record' model.

    VOI Report Account Record

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
        income_streams (list of VOIReportIncomeStreamRecord): A list of income
            stream records
        misc_deposits (list of VOIReportTransactionRecord): A list of
            miscellaneous deposits

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
        "income_streams":'incomeStreams',
        "misc_deposits":'miscDeposits'
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
                 misc_deposits=None,
                 additional_properties = {}):
        """Constructor for the VOIReportAccountRecord class"""

        # Initialize members of the class
        self.id = id
        self.number = number
        self.owner_name = owner_name
        self.owner_address = owner_address
        self.name = name
        self.mtype = mtype
        self.aggregation_status_code = aggregation_status_code
        self.income_streams = income_streams
        self.misc_deposits = misc_deposits

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
                income_streams.append(finicityapi.models.voi_report_income_stream_record.VOIReportIncomeStreamRecord.from_dictionary(structure))
        misc_deposits = None
        if dictionary.get('miscDeposits') != None:
            misc_deposits = list()
            for structure in dictionary.get('miscDeposits'):
                misc_deposits.append(finicityapi.models.voi_report_transaction_record.VOIReportTransactionRecord.from_dictionary(structure))

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
                   misc_deposits,
                   dictionary)


