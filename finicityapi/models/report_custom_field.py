# -*- coding: utf-8 -*-


class ReportCustomField(object):

    """Implementation of the 'Report Custom Field' model.

    TODO: type model description here.

    Attributes:
        label (string): The name of the custom field
        value (string): The value of the custom field
        shown (bool): The shown variable designates whether the custom field
            will display on the PDF report. When shown is true, the custom
            field will show on the PDF.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "label":'label',
        "value":'value',
        "shown":'shown'
    }

    def __init__(self,
                 label=None,
                 value=None,
                 shown=None,
                 additional_properties = {}):
        """Constructor for the ReportCustomField class"""

        # Initialize members of the class
        self.label = label
        self.value = value
        self.shown = shown

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
        label = dictionary.get('label')
        value = dictionary.get('value')
        shown = dictionary.get('shown')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(label,
                   value,
                   shown,
                   dictionary)


