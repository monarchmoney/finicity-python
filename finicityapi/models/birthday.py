# -*- coding: utf-8 -*-


class Birthday(object):

    """Implementation of the 'Birthday' model.

    The consumer birth date

    Attributes:
        year (int): The birthday 4-digit year
        month (int): The birthday 2-digit month (01 is January)
        day_of_month (int): The birthday 2-digit day-of-month

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "year":'year',
        "month":'month',
        "day_of_month":'dayOfMonth'
    }

    def __init__(self,
                 year=None,
                 month=None,
                 day_of_month=None,
                 additional_properties = {}):
        """Constructor for the Birthday class"""

        # Initialize members of the class
        self.year = year
        self.month = month
        self.day_of_month = day_of_month

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
        year = dictionary.get('year')
        month = dictionary.get('month')
        day_of_month = dictionary.get('dayOfMonth')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(year,
                   month,
                   day_of_month,
                   dictionary)


