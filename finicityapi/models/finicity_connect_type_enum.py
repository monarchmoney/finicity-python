# -*- coding: utf-8 -*-

class FinicityConnectTypeEnum(object):

    """Implementation of the 'Finicity Connect Type' enum.

    TODO: type enum description here.

    Attributes:
        AGGREGATION: Aggregation Only - Used by PFM (Personal Financial
            Management) partners to grant access to a customer’s
            transactions.
        ACH: TODO: type description here.
        FIX: Fix - Used to resolve authentication errors
        LITE: Lite - Provides FI authentication and adding accounts. Allows
            for custom styling, control of the FI search experience, and does
            not end with a report generation call.
        VOA: Verification of Assets - Used by lenders to verify assets. The
            default time period of data retrieved is 6 months, so that lenders
            can reduce their liability.
        VOAHISTORY: Verification of Assets with History - Used by the GSEs to
            verify assets. This differs from normal VOA in that it uses up to
            2 years of data. voahistory
        VOI: Verification of Income - Used by lenders to verify a customer’s
            income using their bank transaction history.
        VOIETXVERIFY: TODO: type description here.
        VOIESTATEMENT: TODO: type description here.
        PAYSTATEMENT: TODO: type description here.
        ASSETSUMMARY: TODO: type description here.
        PREQUALVOA: TODO: type description here.

    """

    AGGREGATION = 'aggregation'

    ACH = 'ach'

    FIX = 'fix'

    LITE = 'lite'

    VOA = 'voa'

    VOAHISTORY = 'voahistory'

    VOI = 'voi'

    VOIE_TXVERIFY = 'voieTxVerify'

    VOIESTATEMENT = 'voieStatement'

    PAYSTATEMENT = 'payStatement'

    ASSETSUMMARY = 'assetSummary'

    PREQUALVOA = 'preQualVoa'

