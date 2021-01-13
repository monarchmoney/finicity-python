# -*- coding: utf-8 -*-


class OptionalConsumerInfo(object):

    """Implementation of the 'Optional Consumer Info' model.

    TODO: type model description here.

    Attributes:
        ssn (string): (MVS-optional) The full SSN without hyphens that matches
            the consumer’s SSN.
        dob (string): (MVS-optional) The consumer’s date of birth is in Unix
            epoch time (in seconds).  The timestamp is UTC at the start of day
            of birth. <br>   <br> **Example**: If the DOB is 1/1/1980, then
            the timestamp passed is 315576000. <br>   <br> **Note**: DOB’s
            prior to 1970 result in a negative timestamp; this is acceptable.
            To avoid errors, the DOB and consumer’s DOB must match.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "ssn":'ssn',
        "dob":'dob'
    }

    def __init__(self,
                 ssn=None,
                 dob=None,
                 additional_properties = {}):
        """Constructor for the OptionalConsumerInfo class"""

        # Initialize members of the class
        self.ssn = ssn
        self.dob = dob

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
        dob = dictionary.get('dob')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(ssn,
                   dob,
                   dictionary)


