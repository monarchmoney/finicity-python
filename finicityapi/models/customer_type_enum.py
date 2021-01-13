# -*- coding: utf-8 -*-

class CustomerTypeEnum(object):

    """Implementation of the 'Customer Type' enum.

    The type of Finicity Customer

    Attributes:
        ACTIVE: An active customer is a billable customer that can add real
            institution accounts
        TESTING: A testing customer is a non billable customer that is limited
            to only adding account for finbank type institutions

    """

    ACTIVE = 'active'

    TESTING = 'testing'

