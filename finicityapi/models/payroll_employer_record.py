# -*- coding: utf-8 -*-

import finicityapi.models.payroll_address

class PayrollEmployerRecord(object):

    """Implementation of the 'Payroll Employer Record' model.

    TODO: type model description here.

    Attributes:
        name (string): Name of the employer as stated by the employer in the
            payroll system.
        legal_entity_id (string): Employer identification number (EIN)
        original_hire_date (long|int): The original hired date of an employee
            at the company.
        latest_hire_date (long|int): If an employee leaves the company and
            returns later, then the employer states the latest hire date at
            the company.
        employment_end_date (long|int): The date an employee ended their
            employment at the company.
        address (list of PayrollAddress): Array of addresses
        employment_status_code (string): Status codes: `A` - Active, `T` -
            Terminated, `L` - Leave
        employment_status_name (string): Status name: `Active`, `Terminated`,
            or `Leave`
        work_level_code (string): The abbreviate code for the employment level
            names (workLevelName) that we receive from the employer.
        work_level_name (string): The employment level name is whatever we
            receive from the employer, such as full time, part time, temp,
            contractor, and more.
        position_title (string): Employee job title

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "name":'name',
        "legal_entity_id":'legalEntityId',
        "original_hire_date":'originalHireDate',
        "latest_hire_date":'latestHireDate',
        "employment_end_date":'employmentEndDate',
        "address":'address',
        "employment_status_code":'employmentStatusCode',
        "employment_status_name":'employmentStatusName',
        "work_level_code":'workLevelCode',
        "work_level_name":'workLevelName',
        "position_title":'positionTitle'
    }

    def __init__(self,
                 name=None,
                 legal_entity_id=None,
                 original_hire_date=None,
                 latest_hire_date=None,
                 employment_end_date=None,
                 address=None,
                 employment_status_code=None,
                 employment_status_name=None,
                 work_level_code=None,
                 work_level_name=None,
                 position_title=None,
                 additional_properties = {}):
        """Constructor for the PayrollEmployerRecord class"""

        # Initialize members of the class
        self.name = name
        self.legal_entity_id = legal_entity_id
        self.original_hire_date = original_hire_date
        self.latest_hire_date = latest_hire_date
        self.employment_end_date = employment_end_date
        self.address = address
        self.employment_status_code = employment_status_code
        self.employment_status_name = employment_status_name
        self.work_level_code = work_level_code
        self.work_level_name = work_level_name
        self.position_title = position_title

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
        name = dictionary.get('name')
        legal_entity_id = dictionary.get('legalEntityId')
        original_hire_date = dictionary.get('originalHireDate')
        latest_hire_date = dictionary.get('latestHireDate')
        employment_end_date = dictionary.get('employmentEndDate')
        address = None
        if dictionary.get('address') != None:
            address = list()
            for structure in dictionary.get('address'):
                address.append(finicityapi.models.payroll_address.PayrollAddress.from_dictionary(structure))
        employment_status_code = dictionary.get('employmentStatusCode')
        employment_status_name = dictionary.get('employmentStatusName')
        work_level_code = dictionary.get('workLevelCode')
        work_level_name = dictionary.get('workLevelName')
        position_title = dictionary.get('positionTitle')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(name,
                   legal_entity_id,
                   original_hire_date,
                   latest_hire_date,
                   employment_end_date,
                   address,
                   employment_status_code,
                   employment_status_name,
                   work_level_code,
                   work_level_name,
                   position_title,
                   dictionary)


