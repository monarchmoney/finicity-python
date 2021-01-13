# -*- coding: utf-8 -*-


class CadenceDetails(object):

    """Implementation of the 'CadenceDetails' model.

    TODO: type model description here.

    Attributes:
        start_date (long|int): postedDate of the first deposit transaction
        stop_date (long|int): postedDate of the final deposit transaction
            (omitted if status is active)
        days (float): Number of days between the recurring deposits

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "start_date":'startDate',
        "stop_date":'stopDate',
        "days":'days'
    }

    def __init__(self,
                 start_date=None,
                 stop_date=None,
                 days=None,
                 additional_properties = {}):
        """Constructor for the CadenceDetails class"""

        # Initialize members of the class
        self.start_date = start_date
        self.stop_date = stop_date
        self.days = days

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
        start_date = dictionary.get('startDate')
        stop_date = dictionary.get('stopDate')
        days = dictionary.get('days')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(start_date,
                   stop_date,
                   days,
                   dictionary)


