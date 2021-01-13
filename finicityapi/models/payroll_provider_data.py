# -*- coding: utf-8 -*-


class PayrollProviderData(object):

    """Implementation of the 'Payroll Provider Data' model.

    TODO: type model description here.

    Attributes:
        payroll_data_retrieval_id (string): An id to identify the data
            retrieved from the payroll providers for the report.
        employer_names (list of string): An array of employer names that the
            consumer submitted after completing the Connect application.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "payroll_data_retrieval_id":'payrollDataRetrievalId',
        "employer_names":'employerNames'
    }

    def __init__(self,
                 payroll_data_retrieval_id=None,
                 employer_names=None,
                 additional_properties = {}):
        """Constructor for the PayrollProviderData class"""

        # Initialize members of the class
        self.payroll_data_retrieval_id = payroll_data_retrieval_id
        self.employer_names = employer_names

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
        payroll_data_retrieval_id = dictionary.get('payrollDataRetrievalId')
        employer_names = dictionary.get('employerNames')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(payroll_data_retrieval_id,
                   employer_names,
                   dictionary)


