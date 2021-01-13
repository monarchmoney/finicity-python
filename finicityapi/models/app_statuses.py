# -*- coding: utf-8 -*-

import finicityapi.models.app_status

class AppStatuses(object):

    """Implementation of the 'App Statuses' model.

    The response for the Get App Registration Status endpoint which returns an
    array of App Status objects to be able to determine their registration
    status. This is version 2 of this response.

    Attributes:
        total_records (long|int): Total number of applications in query
        total_pages (long|int): Total number of pages in application query for
            size of results per page
        page_number (long|int): The page number returned as per the
            application query
        number_of_records_per_page (long|int): The number of records per page
            as per the application query
        applications (list of AppStatus): List of applications with their
            status information

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "total_records":'totalRecords',
        "total_pages":'totalPages',
        "page_number":'pageNumber',
        "number_of_records_per_page":'numberOfRecordsPerPage',
        "applications":'applications'
    }

    def __init__(self,
                 total_records=None,
                 total_pages=None,
                 page_number=None,
                 number_of_records_per_page=None,
                 applications=None,
                 additional_properties = {}):
        """Constructor for the AppStatuses class"""

        # Initialize members of the class
        self.total_records = total_records
        self.total_pages = total_pages
        self.page_number = page_number
        self.number_of_records_per_page = number_of_records_per_page
        self.applications = applications

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
        total_records = dictionary.get('totalRecords')
        total_pages = dictionary.get('totalPages')
        page_number = dictionary.get('pageNumber')
        number_of_records_per_page = dictionary.get('numberOfRecordsPerPage')
        applications = None
        if dictionary.get('applications') != None:
            applications = list()
            for structure in dictionary.get('applications'):
                applications.append(finicityapi.models.app_status.AppStatus.from_dictionary(structure))

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(total_records,
                   total_pages,
                   page_number,
                   number_of_records_per_page,
                   applications,
                   dictionary)


