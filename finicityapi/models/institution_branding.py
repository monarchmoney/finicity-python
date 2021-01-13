# -*- coding: utf-8 -*-


class InstitutionBranding(object):

    """Implementation of the 'InstitutionBranding' model.

    TODO: type model description here.

    Attributes:
        logo (string): TODO: type description here.
        alternate_logo (string): TODO: type description here.
        icon (string): TODO: type description here.
        alternate_icon (string): TODO: type description here.
        primary_color (string): TODO: type description here.
        secondary_color (string): TODO: type description here.
        gradient_color_top (string): TODO: type description here.
        gradient_color_bottom (string): TODO: type description here.
        tile (string): TODO: type description here.
        tile_small (string): TODO: type description here.
        button_text_color (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "logo":'logo',
        "icon":'icon',
        "alternate_icon":'alternateIcon',
        "primary_color":'primaryColor',
        "gradient_color_top":'gradientColorTop',
        "gradient_color_bottom":'gradientColorBottom',
        "tile":'tile',
        "button_text_color":'buttonTextColor',
        "alternate_logo":'alternateLogo',
        "secondary_color":'secondaryColor',
        "tile_small":'tileSmall'
    }

    def __init__(self,
                 logo=None,
                 icon=None,
                 alternate_icon=None,
                 primary_color=None,
                 gradient_color_top=None,
                 gradient_color_bottom=None,
                 tile=None,
                 button_text_color=None,
                 alternate_logo=None,
                 secondary_color=None,
                 tile_small=None,
                 additional_properties = {}):
        """Constructor for the InstitutionBranding class"""

        # Initialize members of the class
        self.logo = logo
        self.alternate_logo = alternate_logo
        self.icon = icon
        self.alternate_icon = alternate_icon
        self.primary_color = primary_color
        self.secondary_color = secondary_color
        self.gradient_color_top = gradient_color_top
        self.gradient_color_bottom = gradient_color_bottom
        self.tile = tile
        self.tile_small = tile_small
        self.button_text_color = button_text_color

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
        icon = dictionary.get('icon')
        alternate_icon = dictionary.get('alternateIcon')
        primary_color = dictionary.get('primaryColor')
        gradient_color_top = dictionary.get('gradientColorTop')
        gradient_color_bottom = dictionary.get('gradientColorBottom')
        tile = dictionary.get('tile')
        button_text_color = dictionary.get('buttonTextColor')
        alternate_logo = dictionary.get('alternateLogo')
        secondary_color = dictionary.get('secondaryColor')
        tile_small = dictionary.get('tileSmall')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(logo,
                   icon,
                   alternate_icon,
                   primary_color,
                   gradient_color_top,
                   gradient_color_bottom,
                   tile,
                   button_text_color,
                   alternate_logo,
                   secondary_color,
                   tile_small,
                   dictionary)


