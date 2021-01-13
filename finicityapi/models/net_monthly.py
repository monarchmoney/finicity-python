# -*- coding: utf-8 -*-


class NetMonthly(object):

    """Implementation of the 'NetMonthly' model.

    TODO: type model description here.

    Attributes:
        month (long|int): Timestamp for the first day of this month
        net (float): Total income during the given month, across all income
            streams

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "month":'month',
        "net":'net'
    }

    def __init__(self,
                 month=None,
                 net=None,
                 additional_properties = {}):
        """Constructor for the NetMonthly class"""

        # Initialize members of the class
        self.month = month
        self.net = net

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
        month = dictionary.get('month')
        net = dictionary.get('net')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(month,
                   net,
                   dictionary)


