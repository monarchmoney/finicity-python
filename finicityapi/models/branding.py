# -*- coding: utf-8 -*-


class Branding(object):

    """Implementation of the 'Branding' model.

    All assets are SVGs so can be slightly resized without any issues.

    Attributes:
        logo (string): File path of the institution's logo.  For white
            backgrounds designed at 375 x 72, has built in spacing around it
            to normalize brand sizing.
        alternate_logo (string): File path of the instiitution's alternate
            logo.  For colored backgrounds designed at 375 x 72 has built in
            spacing around it to normalize brand sizing
        icon (string): File path of the Institution's icon.  For search
            results designed at 40 x 40
        primary_color (string): Hex code for the Institution's primary color.
        title (string): File path of institution name logo.  For popular banks
            designed at 160 x 72

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "logo":'logo',
        "alternate_logo":'alternateLogo',
        "icon":'icon',
        "primary_color":'primaryColor',
        "title":'title'
    }

    def __init__(self,
                 logo=None,
                 alternate_logo=None,
                 icon=None,
                 primary_color=None,
                 title=None,
                 additional_properties = {}):
        """Constructor for the Branding class"""

        # Initialize members of the class
        self.logo = logo
        self.alternate_logo = alternate_logo
        self.icon = icon
        self.primary_color = primary_color
        self.title = title

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
        logo = dictionary.get('logo')
        alternate_logo = dictionary.get('alternateLogo')
        icon = dictionary.get('icon')
        primary_color = dictionary.get('primaryColor')
        title = dictionary.get('title')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(logo,
                   alternate_logo,
                   icon,
                   primary_color,
                   title,
                   dictionary)


