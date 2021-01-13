# -*- coding: utf-8 -*-


class PayStatementReportData(object):

    """Implementation of the 'Pay Statement Report Data' model.

    TODO: type model description here.

    Attributes:
        asset_ids (list of string): The list of pay statement asset IDs.
        extract_earnings (bool): Field to indicate whether to extract the
            earnings on all pay statements.
        extract_deductions (bool): Field to indicate whether to extract the
            deductions on all pay statements.
        extract_direct_deposit (bool): Field to indicate whether to extract
            the direct deposits on all pay statements.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "asset_ids":'assetIds',
        "extract_earnings":'extractEarnings',
        "extract_deductions":'extractDeductions',
        "extract_direct_deposit":'extractDirectDeposit'
    }

    def __init__(self,
                 asset_ids=None,
                 extract_earnings=True,
                 extract_deductions=False,
                 extract_direct_deposit=True,
                 additional_properties = {}):
        """Constructor for the PayStatementReportData class"""

        # Initialize members of the class
        self.asset_ids = asset_ids
        self.extract_earnings = extract_earnings
        self.extract_deductions = extract_deductions
        self.extract_direct_deposit = extract_direct_deposit

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
        asset_ids = dictionary.get('assetIds')
        extract_earnings = dictionary.get("extractEarnings") if dictionary.get("extractEarnings") else True
        extract_deductions = dictionary.get("extractDeductions") if dictionary.get("extractDeductions") else False
        extract_direct_deposit = dictionary.get("extractDirectDeposit") if dictionary.get("extractDirectDeposit") else True

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(asset_ids,
                   extract_earnings,
                   extract_deductions,
                   extract_direct_deposit,
                   dictionary)


