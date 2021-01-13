# -*- coding: utf-8 -*-

class StatusEnum(object):

    """Implementation of the 'Status' enum.

    TODO: type enum description here.

    Attributes:
        ACTIVE: "active” means that the most-recent deposit occurred as
            expected by the cadence and the next expected date is still in the
            future.
        INACTIVE: "inactive" means that the deposit has not occurred in the
            expected cadence or has not occurred recently

    """

    ACTIVE = 'ACTIVE'

    INACTIVE = 'INACTIVE'

