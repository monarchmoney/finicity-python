# -*- coding: utf-8 -*-


class CreateConsumerResponse(object):

    """Implementation of the 'Create Consumer Response' model.

    TODO: type model description here.

    Attributes:
        id (string): Finicity ID of the consumer (UUID with max length 32
            characters)
        created_date (long|int): Consumer created date
        customer_id (long|int): Finicity?s ID of the customer

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id":'id',
        "created_date":'createdDate',
        "customer_id":'customerId'
    }

    def __init__(self,
                 id=None,
                 created_date=None,
                 customer_id=None,
                 additional_properties = {}):
        """Constructor for the CreateConsumerResponse class"""

        # Initialize members of the class
        self.id = id
        self.created_date = created_date
        self.customer_id = customer_id

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
        id = dictionary.get('id')
        created_date = dictionary.get('createdDate')
        customer_id = dictionary.get('customerId')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(id,
                   created_date,
                   customer_id,
                   dictionary)


