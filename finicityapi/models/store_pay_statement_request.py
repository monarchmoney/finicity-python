# -*- coding: utf-8 -*-


class StorePayStatementRequest(object):

    """Implementation of the 'StorePayStatementRequest' model.

    TODO: type model description here.

    Attributes:
        label (string): The label to be associated with the pay statement.
            These are recommended labels:  lastPayPeriod - The most recent
            (last) pay statement. This label will allow the paystub to go
            through primary data extraction.  lastPayPeriodMinusOne- The
            second most recent pay statement lastPayPeriodMinusTwo - The third
            most recent pay statement previousYearLastPayPeriod - Last pay
            statement of the previous calendar year previousYear2LastPayPeriod
            - Last pay statement of the calendar year 2 years prior 
            earliestPayPeriod - The earliest pay statement
        statement (list of string): The base 64 encoded value for the pay
            statement.
        asset_id (string): TODO: type description here.
        file_type (string): TODO: type description here.
        data_available (bool): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "label":'label',
        "statement":'statement',
        "asset_id":'assetId',
        "file_type":'fileType',
        "data_available":'dataAvailable'
    }

    def __init__(self,
                 label=None,
                 statement=None,
                 asset_id=None,
                 file_type=None,
                 data_available=None,
                 additional_properties = {}):
        """Constructor for the StorePayStatementRequest class"""

        # Initialize members of the class
        self.label = label
        self.statement = statement
        self.asset_id = asset_id
        self.file_type = file_type
        self.data_available = data_available

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
        label = dictionary.get('label')
        statement = dictionary.get('statement')
        asset_id = dictionary.get('assetId')
        file_type = dictionary.get('fileType')
        data_available = dictionary.get('dataAvailable')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(label,
                   statement,
                   asset_id,
                   file_type,
                   data_available,
                   dictionary)


