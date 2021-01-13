# -*- coding: utf-8 -*-

import finicityapi.models.interview_accounts

class TxverifyInterview(object):

    """Implementation of the 'TxVerifyInterview' model.

    TODO: type model description here.

    Attributes:
        asset_id (string): The assetId assigned to the pay statement.
        net_pay_current (float): The net pay the consumer entered during the
            interview. This is an optional field
        gross_pay_current (float): The gross pay the consumer entered during
            the interview. This is an optional field
        name (string): The name of the employer the consumer entered during
            the interview. This is an optional field
        date (long|int): The pay date the consumer entered during the
            interview. This is an optional field
        accounts (list of InterviewAccounts): An array of accounts objects
            that contain Account Interview data.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "asset_id":'assetId',
        "net_pay_current":'netPayCurrent',
        "gross_pay_current":'grossPayCurrent',
        "name":'name',
        "date":'date',
        "accounts":'accounts'
    }

    def __init__(self,
                 asset_id=None,
                 net_pay_current=None,
                 gross_pay_current=None,
                 name=None,
                 date=None,
                 accounts=None,
                 additional_properties = {}):
        """Constructor for the TxverifyInterview class"""

        # Initialize members of the class
        self.asset_id = asset_id
        self.net_pay_current = net_pay_current
        self.gross_pay_current = gross_pay_current
        self.name = name
        self.date = date
        self.accounts = accounts

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
        asset_id = dictionary.get('assetId')
        net_pay_current = dictionary.get('netPayCurrent')
        gross_pay_current = dictionary.get('grossPayCurrent')
        name = dictionary.get('name')
        date = dictionary.get('date')
        accounts = None
        if dictionary.get('accounts') != None:
            accounts = list()
            for structure in dictionary.get('accounts'):
                accounts.append(finicityapi.models.interview_accounts.InterviewAccounts.from_dictionary(structure))

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(asset_id,
                   net_pay_current,
                   gross_pay_current,
                   name,
                   date,
                   accounts,
                   dictionary)


