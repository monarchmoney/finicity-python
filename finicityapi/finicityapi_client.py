# -*- coding: utf-8 -*-

from finicityapi.decorators import lazy_property
from finicityapi.configuration import Configuration
from finicityapi.controllers.deprecated_controller import DeprecatedController
from finicityapi.controllers.institutions_controller import InstitutionsController
from finicityapi.controllers.accounts_controller import AccountsController
from finicityapi.controllers.consumer_controller import ConsumerController
from finicityapi.controllers.verify_income_controller import VerifyIncomeController
from finicityapi.controllers.verify_assets_controller import VerifyAssetsController
from finicityapi.controllers.verify_income_and_employment_controller import VerifyIncomeAndEmploymentController
from finicityapi.controllers.get_portfolios_controller import GetPortfoliosController
from finicityapi.controllers.payments_controller import PaymentsController
from finicityapi.controllers.account_owner_controller import AccountOwnerController
from finicityapi.controllers.customer_controller import CustomerController
from finicityapi.controllers.txpush_controller import TxpushController
from finicityapi.controllers.bank_statements_controller import BankStatementsController
from finicityapi.controllers.transactions_controller import TransactionsController
from finicityapi.controllers.pay_statements_controller import PayStatementsController
from finicityapi.controllers.liabilities_controller import LiabilitiesController
from finicityapi.controllers.authentication_controller import AuthenticationController
from finicityapi.controllers.get_reports_by_customer_controller import GetReportsByCustomerController
from finicityapi.controllers.app_registration_and_oauth_migration_controller import AppRegistrationAndOauthMigrationController
from finicityapi.controllers.connect_controller import ConnectController
from finicityapi.controllers.get_reports_by_consumer_controller import GetReportsByConsumerController
from finicityapi.controllers.api_controller import APIController


class FinicityapiClient(object):

    config = Configuration

    @lazy_property
    def deprecated(self):
        return DeprecatedController()

    @lazy_property
    def institutions(self):
        return InstitutionsController()

    @lazy_property
    def accounts(self):
        return AccountsController()

    @lazy_property
    def consumer(self):
        return ConsumerController()

    @lazy_property
    def verify_income(self):
        return VerifyIncomeController()

    @lazy_property
    def verify_assets(self):
        return VerifyAssetsController()

    @lazy_property
    def verify_income_and_employment(self):
        return VerifyIncomeAndEmploymentController()

    @lazy_property
    def get_portfolios(self):
        return GetPortfoliosController()

    @lazy_property
    def payments(self):
        return PaymentsController()

    @lazy_property
    def account_owner(self):
        return AccountOwnerController()

    @lazy_property
    def customer(self):
        return CustomerController()

    @lazy_property
    def txpush(self):
        return TxpushController()

    @lazy_property
    def bank_statements(self):
        return BankStatementsController()

    @lazy_property
    def transactions(self):
        return TransactionsController()

    @lazy_property
    def pay_statements(self):
        return PayStatementsController()

    @lazy_property
    def liabilities(self):
        return LiabilitiesController()

    @lazy_property
    def authentication(self):
        return AuthenticationController()

    @lazy_property
    def get_reports_by_customer(self):
        return GetReportsByCustomerController()

    @lazy_property
    def app_registration_and_oauth_migration(self):
        return AppRegistrationAndOauthMigrationController()

    @lazy_property
    def connect(self):
        return ConnectController()

    @lazy_property
    def get_reports_by_consumer(self):
        return GetReportsByConsumerController()

    @lazy_property
    def client(self):
        return APIController()


    def __init__(self,
                 finicity_app_key=None,
                 finicity_app_token=None):
        if finicity_app_key is not None:
            Configuration.finicity_app_key = finicity_app_key
        if finicity_app_token is not None:
            Configuration.finicity_app_token = finicity_app_token

