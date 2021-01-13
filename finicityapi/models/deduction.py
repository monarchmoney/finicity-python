# -*- coding: utf-8 -*-


class Deduction(object):

    """Implementation of the 'Deduction' model.

    TODO: type model description here.

    Attributes:
        name (string): The normalized category of the deductions in the format
            [type][number]. The number is the will be the iterating number of
            the type’s occurrence starting at one.
        description (string): The deduction line’s deduction type description
        amount_current (float): The amount for the deduction line deducted
            from employee’s pay for the specified pay period.
        amount_ytd (string): The amount for the deduction line being deducted
            from the employee’s pay for the current pay year.
        mtype (string): Categorization based on the deduction line’s
            description.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "name":'name',
        "description":'description',
        "amount_current":'amountCurrent',
        "amount_ytd":'amountYTD',
        "mtype":'type'
    }

    def __init__(self,
                 name=None,
                 description=None,
                 amount_current=None,
                 amount_ytd=None,
                 mtype=None,
                 additional_properties = {}):
        """Constructor for the Deduction class"""

        # Initialize members of the class
        self.name = name
        self.description = description
        self.amount_current = amount_current
        self.amount_ytd = amount_ytd
        self.mtype = mtype

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
        description = dictionary.get('description')
        amount_current = dictionary.get('amountCurrent')
        amount_ytd = dictionary.get('amountYTD')
        mtype = dictionary.get('type')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(name,
                   description,
                   amount_current,
                   amount_ytd,
                   mtype,
                   dictionary)


