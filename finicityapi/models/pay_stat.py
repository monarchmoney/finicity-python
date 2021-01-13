# -*- coding: utf-8 -*-


class PayStat(object):

    """Implementation of the 'Pay Stat' model.

    TODO: type model description here.

    Attributes:
        name (string): The normalized category of the earnings with a number
            appended. The number is the will be the iterating number of the
            type’s occurrence starting at one.
        mtype (string): Categorization based on the earning line’s
            description.
        description (string): The earnings line’s pay type description
        rate (float): The earning line’s pay rate.
        units (float): The unit by which you multiply the rate to get the
            total paid out to the employee for the specified earning line.
            This is typically used for hourly employees.
        amount_current (float): The amount for the earning line paid out to
            the employee for the specified pay period.
        amount_ytd (float): The amount for the earning line being paid out to
            the employee for the current pay year.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "name":'name',
        "mtype":'type',
        "description":'description',
        "rate":'rate',
        "units":'units',
        "amount_current":'amountCurrent',
        "amount_ytd":'amountYTD'
    }

    def __init__(self,
                 name=None,
                 mtype=None,
                 description=None,
                 rate=None,
                 units=None,
                 amount_current=None,
                 amount_ytd=None,
                 additional_properties = {}):
        """Constructor for the PayStat class"""

        # Initialize members of the class
        self.name = name
        self.mtype = mtype
        self.description = description
        self.rate = rate
        self.units = units
        self.amount_current = amount_current
        self.amount_ytd = amount_ytd

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
        mtype = dictionary.get('type')
        description = dictionary.get('description')
        rate = dictionary.get('rate')
        units = dictionary.get('units')
        amount_current = dictionary.get('amountCurrent')
        amount_ytd = dictionary.get('amountYTD')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(name,
                   mtype,
                   description,
                   rate,
                   units,
                   amount_current,
                   amount_ytd,
                   dictionary)


