# -*- coding: utf-8 -*-

import finicityapi.models.optional_consumer_info

class Borrowers(object):

    """Implementation of the 'Borrowers' model.

    TODO: type model description here.

    Attributes:
        customer_id (string): Customer ID from the [Add Customer API](
            https://api-reference.finicity.com/#/rest/api-endpoints/customer/ad
            d-customer)
        consumer_id (string): Consumer ID from the [Create Consumer API](
            https://api-reference.finicity.com/#/rest/api-endpoints/consumer/cr
            eate-consumer)
        mtype (BorrowerTypeEnum): (MVS) Borrower type: `primary` or
            `jointBorrower`
        optional_consumer_info (OptionalConsumerInfo): (MVS-Optional) Optional
            consumer information such as the consumer’s SSN and DOB. Use to
            prepopulate the consumer’s SSN (only the last 4 digits appear) and
            DOB on the Find employment records page at the beginning of the
            MVS payroll module.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "customer_id":'customerId',
        "consumer_id":'consumerId',
        "mtype":'type',
        "optional_consumer_info":'optionalConsumerInfo'
    }

    def __init__(self,
                 customer_id=None,
                 consumer_id=None,
                 mtype=None,
                 optional_consumer_info=None,
                 additional_properties = {}):
        """Constructor for the Borrowers class"""

        # Initialize members of the class
        self.customer_id = customer_id
        self.consumer_id = consumer_id
        self.mtype = mtype
        self.optional_consumer_info = optional_consumer_info

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
        customer_id = dictionary.get('customerId')
        consumer_id = dictionary.get('consumerId')
        mtype = dictionary.get('type')
        optional_consumer_info = finicityapi.models.optional_consumer_info.OptionalConsumerInfo.from_dictionary(dictionary.get('optionalConsumerInfo')) if dictionary.get('optionalConsumerInfo') else None

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(customer_id,
                   consumer_id,
                   mtype,
                   optional_consumer_info,
                   dictionary)


