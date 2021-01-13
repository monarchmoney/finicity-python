# -*- coding: utf-8 -*-

import finicityapi.models.content
import finicityapi.models.sort

class InvoiceBillingResponse(object):

    """Implementation of the 'Invoice Billing Response' model.

    TODO: type model description here.

    Attributes:
        content (list of Content): TODO: type description here.
        pageable (string): TODO: type description here.
        total_pages (int): TODO: type description here.
        total_elements (int): TODO: type description here.
        last (bool): TODO: type description here.
        size (int): TODO: type description here.
        number (int): TODO: type description here.
        sort (Sort): TODO: type description here.
        number_of_elements (int): TODO: type description here.
        first (bool): TODO: type description here.
        empty (bool): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "content":'content',
        "pageable":'pageable',
        "total_pages":'totalPages',
        "total_elements":'totalElements',
        "last":'last',
        "size":'size',
        "number":'number',
        "sort":'sort',
        "number_of_elements":'numberOfElements',
        "first":'first',
        "empty":'empty'
    }

    def __init__(self,
                 content=None,
                 pageable=None,
                 total_pages=None,
                 total_elements=None,
                 last=None,
                 size=None,
                 number=None,
                 sort=None,
                 number_of_elements=None,
                 first=None,
                 empty=None,
                 additional_properties = {}):
        """Constructor for the InvoiceBillingResponse class"""

        # Initialize members of the class
        self.content = content
        self.pageable = pageable
        self.total_pages = total_pages
        self.total_elements = total_elements
        self.last = last
        self.size = size
        self.number = number
        self.sort = sort
        self.number_of_elements = number_of_elements
        self.first = first
        self.empty = empty

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
        content = None
        if dictionary.get('content') != None:
            content = list()
            for structure in dictionary.get('content'):
                content.append(finicityapi.models.content.Content.from_dictionary(structure))
        pageable = dictionary.get('pageable')
        total_pages = dictionary.get('totalPages')
        total_elements = dictionary.get('totalElements')
        last = dictionary.get('last')
        size = dictionary.get('size')
        number = dictionary.get('number')
        sort = finicityapi.models.sort.Sort.from_dictionary(dictionary.get('sort')) if dictionary.get('sort') else None
        number_of_elements = dictionary.get('numberOfElements')
        first = dictionary.get('first')
        empty = dictionary.get('empty')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(content,
                   pageable,
                   total_pages,
                   total_elements,
                   last,
                   size,
                   number,
                   sort,
                   number_of_elements,
                   first,
                   empty,
                   dictionary)


