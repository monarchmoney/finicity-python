# -*- coding: utf-8 -*-


class PortfolioReport(object):

    """Implementation of the 'Portfolio Report' model.

    TODO: type model description here.

    Attributes:
        id (string): The Finicity report ID
        portfolio_id (string): A unique identifier that will be consistent
            across all reports created for the same customer.
        mtype (TypeEnum): Report type
        status (string): The status of the report
        created_date (long|int): The date the report was generated

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id":'id',
        "portfolio_id":'portfolioId',
        "mtype":'type',
        "status":'status',
        "created_date":'createdDate'
    }

    def __init__(self,
                 id=None,
                 portfolio_id=None,
                 mtype=None,
                 status=None,
                 created_date=None,
                 additional_properties = {}):
        """Constructor for the PortfolioReport class"""

        # Initialize members of the class
        self.id = id
        self.portfolio_id = portfolio_id
        self.mtype = mtype
        self.status = status
        self.created_date = created_date

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
        portfolio_id = dictionary.get('portfolioId')
        mtype = dictionary.get('type')
        status = dictionary.get('status')
        created_date = dictionary.get('createdDate')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(id,
                   portfolio_id,
                   mtype,
                   status,
                   created_date,
                   dictionary)


