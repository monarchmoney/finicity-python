# -*- coding: utf-8 -*-


class Sort(object):

    """Implementation of the 'Sort' model.

    TODO: type model description here.

    Attributes:
        sorted (bool): TODO: type description here.
        unsorted (bool): TODO: type description here.
        empty (bool): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "sorted":'sorted',
        "unsorted":'unsorted',
        "empty":'empty'
    }

    def __init__(self,
                 sorted=None,
                 unsorted=None,
                 empty=None,
                 additional_properties = {}):
        """Constructor for the Sort class"""

        # Initialize members of the class
        self.sorted = sorted
        self.unsorted = unsorted
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
        sorted = dictionary.get('sorted')
        unsorted = dictionary.get('unsorted')
        empty = dictionary.get('empty')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(sorted,
                   unsorted,
                   empty,
                   dictionary)


