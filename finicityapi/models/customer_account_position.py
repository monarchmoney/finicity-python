# -*- coding: utf-8 -*-


class CustomerAccountPosition(object):

    """Implementation of the 'Customer Account Position' model.

    Details for investment account holdings

    Attributes:
        id (long|int): The id of the investment position
        description (string): The description of the holding
        cusip_no (long|int): Cusip number for the investment holding
        symbol (string): The symbol of the investment holding
        quantity (float): The quantity of investment holdings
        current_price (float): The current price of the investment holding
        fund_name (string): The fund name for the investment holding
        security_name (string): The security name for the investment holding
        transaction_type (string): The transaction type of the holding. Cash,
            Margin, POSSTOCK, Etc
        market_value (float): The market value of the holding
        cost_basis (float): The cost basis of the holding
        units (float): The # of units of the holding
        unit_price (float): The unit price of the holding
        status (string): The status of the holding
        current_price_date (long|int): The latest date the price date was
            updated. In epoch time.
        inv_security_type (string): The investment holding security type

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id":'id',
        "description":'description',
        "cusip_no":'cusipNo',
        "symbol":'symbol',
        "quantity":'quantity',
        "current_price":'currentPrice',
        "fund_name":'fundName',
        "security_name":'securityName',
        "transaction_type":'transactionType',
        "market_value":'marketValue',
        "cost_basis":'costBasis',
        "units":'units',
        "unit_price":'unitPrice',
        "status":'status',
        "current_price_date":'currentPriceDate',
        "inv_security_type":'invSecurityType'
    }

    def __init__(self,
                 id=None,
                 description=None,
                 cusip_no=None,
                 symbol=None,
                 quantity=None,
                 current_price=None,
                 fund_name=None,
                 security_name=None,
                 transaction_type=None,
                 market_value=None,
                 cost_basis=None,
                 units=None,
                 unit_price=None,
                 status=None,
                 current_price_date=None,
                 inv_security_type=None,
                 additional_properties = {}):
        """Constructor for the CustomerAccountPosition class"""

        # Initialize members of the class
        self.id = id
        self.description = description
        self.cusip_no = cusip_no
        self.symbol = symbol
        self.quantity = quantity
        self.current_price = current_price
        self.fund_name = fund_name
        self.security_name = security_name
        self.transaction_type = transaction_type
        self.market_value = market_value
        self.cost_basis = cost_basis
        self.units = units
        self.unit_price = unit_price
        self.status = status
        self.current_price_date = current_price_date
        self.inv_security_type = inv_security_type

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
        description = dictionary.get('description')
        cusip_no = dictionary.get('cusipNo')
        symbol = dictionary.get('symbol')
        quantity = dictionary.get('quantity')
        current_price = dictionary.get('currentPrice')
        fund_name = dictionary.get('fundName')
        security_name = dictionary.get('securityName')
        transaction_type = dictionary.get('transactionType')
        market_value = dictionary.get('marketValue')
        cost_basis = dictionary.get('costBasis')
        units = dictionary.get('units')
        unit_price = dictionary.get('unitPrice')
        status = dictionary.get('status')
        current_price_date = dictionary.get('currentPriceDate')
        inv_security_type = dictionary.get('invSecurityType')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(id,
                   description,
                   cusip_no,
                   symbol,
                   quantity,
                   current_price,
                   fund_name,
                   security_name,
                   transaction_type,
                   market_value,
                   cost_basis,
                   units,
                   unit_price,
                   status,
                   current_price_date,
                   inv_security_type,
                   dictionary)


