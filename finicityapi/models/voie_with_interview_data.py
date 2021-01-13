# -*- coding: utf-8 -*-

import finicityapi.models.txverify_interview

class VOIEWithInterviewData(object):

    """Implementation of the 'VOIE With Interview Data' model.

    TODO: type model description here.

    Attributes:
        txverify_interview (list of TxverifyInterview): An array of
            txVerifyInterview objects.
        extract_earnings (bool): Field to indicate whether to extract the
            earnings on all pay statements. This is an optional field.
        extract_deductions (bool): Field to indicate whether to extract the
            deductions on all pay statements. This is an optional field.
        extract_direct_deposit (bool): Field to indicate whether to extract
            the direct deposits on all pay statements. This is an optional
            field.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "txverify_interview":'txVerifyInterview',
        "extract_earnings":'extractEarnings',
        "extract_deductions":'extractDeductions',
        "extract_direct_deposit":'extractDirectDeposit'
    }

    def __init__(self,
                 txverify_interview=None,
                 extract_earnings=True,
                 extract_deductions=False,
                 extract_direct_deposit=True,
                 additional_properties = {}):
        """Constructor for the VOIEWithInterviewData class"""

        # Initialize members of the class
        self.txverify_interview = txverify_interview
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
        txverify_interview = None
        if dictionary.get('txVerifyInterview') != None:
            txverify_interview = list()
            for structure in dictionary.get('txVerifyInterview'):
                txverify_interview.append(finicityapi.models.txverify_interview.TxverifyInterview.from_dictionary(structure))
        extract_earnings = dictionary.get("extractEarnings") if dictionary.get("extractEarnings") else True
        extract_deductions = dictionary.get("extractDeductions") if dictionary.get("extractDeductions") else False
        extract_direct_deposit = dictionary.get("extractDirectDeposit") if dictionary.get("extractDirectDeposit") else True

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(txverify_interview,
                   extract_earnings,
                   extract_deductions,
                   extract_direct_deposit,
                   dictionary)


