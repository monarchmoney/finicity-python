# -*- coding: utf-8 -*-


class PayrollProviderRefreshData(object):

    """Implementation of the 'Payroll Provider Refresh Data' model.

    TODO: type model description here.

    Attributes:
        ssn (string): The full SSN without hyphens that matches the consumer’s
            SSN.
        date_of_birth (string): The consumer’s date of birth in YYYY-MM-DD
            format.
        report_id (string): The `reportId` of the original VOIE Payroll
            report.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "ssn":'ssn',
        "date_of_birth":'dateOfBirth',
        "report_id":'reportId'
    }

    def __init__(self,
                 ssn=None,
                 date_of_birth=None,
                 report_id=None,
                 additional_properties = {}):
        """Constructor for the PayrollProviderRefreshData class"""

        # Initialize members of the class
        self.ssn = ssn
        self.date_of_birth = date_of_birth
        self.report_id = report_id

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
        ssn = dictionary.get('ssn')
        date_of_birth = dictionary.get('dateOfBirth')
        report_id = dictionary.get('reportId')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(ssn,
                   date_of_birth,
                   report_id,
                   dictionary)


