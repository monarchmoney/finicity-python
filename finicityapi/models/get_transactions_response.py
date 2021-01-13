# -*- coding: utf-8 -*-

import finicityapi.models.transaction

class GetTransactionsResponse(object):

    """Implementation of the 'Get Transactions Response' model.

    TODO: type model description here.

    Attributes:
        found (string): Total number of records matching search criteria
        displaying (string): Number of records in this response
        more_available (bool): true if this response does not contain the last
            record in the result set
        from_date (string): Value of the fromDate request parameter that
            generated this response
        to_date (string): Value of the toDate request parameter that generated
            this response
        sort (string): Value of the sort request parameter that generated this
            response
        transactions (list of Transaction): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "found":'found',
        "displaying":'displaying',
        "more_available":'moreAvailable',
        "from_date":'fromDate',
        "to_date":'toDate',
        "sort":'sort',
        "transactions":'transactions'
    }

    def __init__(self,
                 found=None,
                 displaying=None,
                 more_available=None,
                 from_date=None,
                 to_date=None,
                 sort=None,
                 transactions=None,
                 additional_properties = {}):
        """Constructor for the GetTransactionsResponse class"""

        # Initialize members of the class
        self.found = found
        self.displaying = displaying
        self.more_available = more_available
        self.from_date = from_date
        self.to_date = to_date
        self.sort = sort
        self.transactions = transactions

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
        found = dictionary.get('found')
        displaying = dictionary.get('displaying')
        more_available = dictionary.get('moreAvailable')
        from_date = dictionary.get('fromDate')
        to_date = dictionary.get('toDate')
        sort = dictionary.get('sort')
        transactions = None
        if dictionary.get('transactions') != None:
            transactions = list()
            for structure in dictionary.get('transactions'):
                transactions.append(finicityapi.models.transaction.Transaction.from_dictionary(structure))

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(found,
                   displaying,
                   more_available,
                   from_date,
                   to_date,
                   sort,
                   transactions,
                   dictionary)


