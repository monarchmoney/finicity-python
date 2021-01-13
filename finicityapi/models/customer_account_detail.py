# -*- coding: utf-8 -*-


class CustomerAccountDetail(object):

    """Implementation of the 'Customer Account Detail' model.

    Additional customer account details. Not all data points will return for
    each account type. You can see the account type that each data point will
    return for below. The data point are also subject to availability by the
    institution.

    Attributes:
        posted_date (long|int): (All Account Types) Most recent date of the
            following information
        available_balance_amount (float): (Checking/Savings/CD/MoneyMarket)
            and (Mortgage/Loan)  The available balance (typically the current
            balance with adjustments for any pending transactions)
        open_date (long|int): (Checking/Savings/CD/MoneyMarket) Date when
            account was opened
        period_start_date (long|int): (Checking/Savings/CD/MoneyMarket) Start
            date of period
        period_end_date (long|int): End date of period
        period_interest_rate (float): (Checking/Savings/CD/MoneyMarket) The
            APY for the current period interest rate
        period_deposit_amount (float): (Checking/Savings/CD/MoneyMarket)
            Amount deposited in period
        period_interest_amount (float): (Checking/Savings/CD/MoneyMarket)
            Interest accrued during the current period
        interest_ytd_amount (float): (Checking/Savings/CD/MoneyMarket)
            Interest accrued year-to-date
        interest_prior_ytd_amount (float): (Checking/Savings/CD/MoneyMarket)
            Interest earned in prior year
        maturity_date (long|int): (Checking/Savings/CD/MoneyMarket) Maturity
            date of account type
        interest_rate (string): (Credit Card/Line Of Credit) and
            (Mortgage/Loan) The account’s current interest rate
        credit_available_amount (float): (Credit Card/Line Of Credit) The
            available credit (typically the credit limit minus the current
            balance)
        credit_max_amount (float): (Credit Card/Line Of Credit) The account’s
            credit limit
        cash_advance_available_amount (float): (Credit Card/Line Of Credit)
            Currently available cash advance
        cash_advance_max_amount (float): (Credit Card/Line Of Credit) Maximum
            cash advance amount
        cash_advance_balance (float): (Credit Card/Line Of Credit) Balance of
            current cash advance
        cash_advance_interest_rate (float): (Credit Card/Line Of Credit)
            Interest rate for cash advances
        current_balance (float): (Credit Card/Line Of Credit) and (Investment)
            Current balance
        payment_min_amount (float): (Credit Card/Line Of Credit) and
            (Mortgage/Loan) Minimum payment due
        payment_due_date (long|int): (Credit Card/Line Of Credit) Due date for
            the next payment
        previous_balance (float): (Credit Card/Line Of Credit) Prior balance
            in last statement
        statement_start_date (long|int): (Credit Card/Line Of Credit) Start
            date of statement period
        statement_end_date (long|int): (Credit Card/Line Of Credit) End date
            of statement period
        statement_purchase_amount (float): (Credit Card/Line Of Credit)
            Purchase amount of statement period
        statement_finance_amount (float): (Credit Card/Line Of Credit) Finance
            amount of statement period
        statement_credit_amount (float): (Credit Card/Line Of Credit) Credit
            amount applied in statement period
        reward_earned_balance (int): (Credit Card/Line Of Credit) Earned
            reward balance
        past_due_amount (float): (Credit Card/Line Of Credit) Balance past
            due
        last_payment_amount (float): (Credit Card/Line Of Credit) and
            (Mortgage/Loan) The amount received in the last payment
        last_payment_date (long|int): (Credit Card/Line Of Credit) The date of
            the last payment
        statement_close_balance (float): (Credit Card/Line Of Credit) Balance
            of statement at close
        term_of_ml (string): (Mortgage/Loan) Length of loan in months
        ml_holder_name (string): (Mortgage/Loan) Holder of the mortgage or
            loan
        description (string): (Mortgage/Loan) Description of loan
        late_fee_amount (float): (Mortgage/Loan) Late fee charged
        payoff_amount (float): (Mortgage/Loan) The amount required to payoff
            the loan
        payoff_amount_date (long|int): (Mortgage/Loan) Date of final payment
        original_maturity_date (long|int): (Mortgage/Loan) Original date of
            loan maturity
        principal_balance (float): (Mortgage/Loan) The principal balance
        escrow_balance (float): (Mortgage/Loan) The escrow balance
        interest_period (string): (Mortgage/Loan) Period of interest
        initial_ml_amount (float): (Mortgage/Loan) Original loan amount
        initial_ml_date (long|int): (Mortgage/Loan) Original date of loan
        next_payment_principal_amount (float): (Mortgage/Loan) Amount towards
            principal in next payment
        next_payment_interest_amount (float): (Mortgage/Loan) Amount of
            interest in next payment
        next_payment (float): (Mortgage/Loan) Minimum payment due
        next_payment_date (long|int): (Mortgage/Loan) Due date for the next
            payment
        last_payment_due_date (long|int): (Mortgage/Loan) Due date of last
            payment
        last_payment_receive_date (long|int): (Mortgage/Loan) The date of the
            last payment
        last_payment_principal_amount (float): (Mortgage/Loan) Amount towards
            principal in last payment
        last_payment_interest_amount (float): (Mortgage/Loan) Amount of
            interest in last payment
        last_payment_escrow_amount (float): (Mortgage/Loan) Amount towards
            escrow in last payment
        last_payment_last_fee_amount (float): (Mortgage/Loan) Amount of last
            fee in last payment
        last_payment_late_charge (float): (Mortgage/Loan) Amount of late
            charge in last payment
        ytd_principal_paid (float): (Mortgage/Loan) Principal paid
            year-to-date
        ytd_interest_paid (float): (Mortgage/Loan) Interest paid year-to-date
        ytd_insurance_paid (float): (Mortgage/Loan) Insurance paid
            year-to-date
        ytd_tax_paid (float): (Mortgage/Loan) Tax paid year-to-date
        auto_pay_enrolled (bool): (Mortgage/Loan) Enrolled in autopay (F/Y)
        collateral (string): (Mortgage/Loan) Collateral on loan
        current_school (string): (Mortgage/Loan) Current school
        first_payment_date (long|int): (Mortgage/Loan) First payment due date
        first_mortgage (bool): (Mortgage/Loan) First mortgage (F/Y)
        loan_payment_freq (string): (Mortgage/Loan) Frequency of payments
            (monthly, etc.)
        original_school (string): (Mortgage/Loan) Original school
        recurring_payment_amount (float): (Mortgage/Loan) Recurring payment
            amount
        lender (string): (Mortgage/Loan) Owner of loan
        ending_balance_amount (float): (Mortgage/Loan) Ending balance
        loan_term_type (string): (Mortgage/Loan) Type of loan term
        payments_made (int): (Mortgage/Loan) Number of payments made
        balloon_amount (float): (Mortgage/Loan) Balloon payment amount
        projected_interest (float): (Mortgage/Loan) Projected interest on the
            loan
        interest_paid_ltd (float): (Mortgage/Loan) Interest paid since
            inception of loan (life to date)
        interest_rate_type (string): (Mortgage/Loan) Type of interest rate
        loan_payment_type (string): (Mortgage/Loan) Type of loan payment
        repayment_plan (string): (Mortgage/Loan) Type of repayment plan for
            the student loan
        payments_remaining (int): (Mortgage/Loan) Number of payments remaining
            before loan is paid off
        interest_margin_balance (float): (Investment) Net interest earned
            after deducting interest paid out
        short_balance (float): (Investment) Sum of short balance
        available_cash_balance (float): (Investment) Amount available for cash
            withdrawal
        maturity_value_amount (float): (Investment) amount payable to an
            investor at maturity
        vested_balance (float): (Investment) Vested amount in account
        emp_match_amount (float): (Investment) Employer matched contributions
        emp_pretax_contrib_amount (float): (Investment) Employer pretax
            contribution amount
        emp_pretax_contrib_amount_ytd (float): (Investment) Employer pretax
            contribution amount year to date
        contrib_total_ytd (float): (Investment) Total year to date
            contributions
        cash_balance_amount (float): (Investment) Cash balance of account
        pre_tax_amount (float): (Investment) Pre tax amount of total balance
        after_tax_amount (float): (Investment) Post tax amount of total
            balance
        match_amount (float): (Investment) Amount matched
        profit_sharing_amount (float): (Investment) Amount of balance for
            profit sharing
        rollover_amount (float): (Investment) Amount of balance rolled over
            from original account (401k, etc.)
        other_vest_amount (float): (Investment) Other vested amount
        other_nonvest_amount (float): (Investment) Other nonvested amount
        current_loan_balance (float): (Investment) Current loan balance
        loan_rate (float): (Investment) Interest rate of loan
        buy_power (float): (Investment) Money available to buy securities
        rollover_ltd (float): (Investment) Life to date of money rolled over

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "available_balance_amount":'availableBalanceAmount',
        "posted_date":'postedDate',
        "open_date":'openDate',
        "period_start_date":'periodStartDate',
        "period_end_date":'periodEndDate',
        "period_interest_rate":'periodInterestRate',
        "period_deposit_amount":'periodDepositAmount',
        "period_interest_amount":'periodInterestAmount',
        "interest_ytd_amount":'interestYtdAmount',
        "interest_prior_ytd_amount":'interestPriorYtdAmount',
        "maturity_date":'maturityDate',
        "interest_rate":'interestRate',
        "credit_available_amount":'creditAvailableAmount',
        "credit_max_amount":'creditMaxAmount',
        "cash_advance_available_amount":'cashAdvanceAvailableAmount',
        "cash_advance_max_amount":'cashAdvanceMaxAmount',
        "cash_advance_balance":'cashAdvanceBalance',
        "cash_advance_interest_rate":'cashAdvanceInterestRate',
        "current_balance":'currentBalance',
        "payment_min_amount":'paymentMinAmount',
        "payment_due_date":'paymentDueDate',
        "previous_balance":'previousBalance',
        "statement_start_date":'statementStartDate',
        "statement_end_date":'statementEndDate',
        "statement_purchase_amount":'statementPurchaseAmount',
        "statement_finance_amount":'statementFinanceAmount',
        "statement_credit_amount":'statementCreditAmount',
        "reward_earned_balance":'rewardEarnedBalance',
        "past_due_amount":'pastDueAmount',
        "last_payment_amount":'lastPaymentAmount',
        "last_payment_date":'lastPaymentDate',
        "statement_close_balance":'statementCloseBalance',
        "term_of_ml":'termOfMl',
        "ml_holder_name":'mlHolderName',
        "description":'description',
        "late_fee_amount":'lateFeeAmount',
        "payoff_amount":'payoffAmount',
        "payoff_amount_date":'payoffAmountDate',
        "original_maturity_date":'originalMaturityDate',
        "principal_balance":'principalBalance',
        "escrow_balance":'escrowBalance',
        "interest_period":'interestPeriod',
        "initial_ml_amount":'initialMlAmount',
        "initial_ml_date":'initialMlDate',
        "next_payment_principal_amount":'nextPaymentPrincipalAmount',
        "next_payment_interest_amount":'nextPaymentInterestAmount',
        "next_payment":'nextPayment',
        "next_payment_date":'nextPaymentDate',
        "last_payment_due_date":'lastPaymentDueDate',
        "last_payment_receive_date":'lastPaymentReceiveDate',
        "last_payment_principal_amount":'lastPaymentPrincipalAmount',
        "last_payment_interest_amount":'lastPaymentInterestAmount',
        "last_payment_escrow_amount":'lastPaymentEscrowAmount',
        "last_payment_last_fee_amount":'lastPaymentLastFeeAmount',
        "last_payment_late_charge":'lastPaymentLateCharge',
        "ytd_principal_paid":'ytdPrincipalPaid',
        "ytd_interest_paid":'ytdInterestPaid',
        "ytd_insurance_paid":'ytdInsurancePaid',
        "ytd_tax_paid":'ytdTaxPaid',
        "auto_pay_enrolled":'autoPayEnrolled',
        "collateral":'collateral',
        "current_school":'currentSchool',
        "first_payment_date":'firstPaymentDate',
        "first_mortgage":'firstMortgage',
        "loan_payment_freq":'loanPaymentFreq',
        "original_school":'originalSchool',
        "recurring_payment_amount":'recurringPaymentAmount',
        "lender":'lender',
        "ending_balance_amount":'endingBalanceAmount',
        "loan_term_type":'loanTermType',
        "payments_made":'paymentsMade',
        "balloon_amount":'balloonAmount',
        "projected_interest":'projectedInterest',
        "interest_paid_ltd":'interestPaidLtd',
        "interest_rate_type":'interestRateType',
        "loan_payment_type":'loanPaymentType',
        "repayment_plan":'repaymentPlan',
        "payments_remaining":'paymentsRemaining',
        "interest_margin_balance":'interestMarginBalance',
        "short_balance":'shortBalance',
        "available_cash_balance":'availableCashBalance',
        "maturity_value_amount":'maturityValueAmount',
        "vested_balance":'vestedBalance',
        "emp_match_amount":'empMatchAmount',
        "emp_pretax_contrib_amount":'empPretaxContribAmount',
        "emp_pretax_contrib_amount_ytd":'empPretaxContribAmountYtd',
        "contrib_total_ytd":'contribTotalYtd',
        "cash_balance_amount":'cashBalanceAmount',
        "pre_tax_amount":'preTaxAmount',
        "after_tax_amount":'afterTaxAmount',
        "match_amount":'matchAmount',
        "profit_sharing_amount":'profitSharingAmount',
        "rollover_amount":'rolloverAmount',
        "other_vest_amount":'otherVestAmount',
        "other_nonvest_amount":'otherNonvestAmount',
        "current_loan_balance":'currentLoanBalance',
        "loan_rate":'loanRate',
        "buy_power":'buyPower',
        "rollover_ltd":'rolloverLtd'
    }

    def __init__(self,
                 available_balance_amount=None,
                 posted_date=None,
                 open_date=None,
                 period_start_date=None,
                 period_end_date=None,
                 period_interest_rate=None,
                 period_deposit_amount=None,
                 period_interest_amount=None,
                 interest_ytd_amount=None,
                 interest_prior_ytd_amount=None,
                 maturity_date=None,
                 interest_rate=None,
                 credit_available_amount=None,
                 credit_max_amount=None,
                 cash_advance_available_amount=None,
                 cash_advance_max_amount=None,
                 cash_advance_balance=None,
                 cash_advance_interest_rate=None,
                 current_balance=None,
                 payment_min_amount=None,
                 payment_due_date=None,
                 previous_balance=None,
                 statement_start_date=None,
                 statement_end_date=None,
                 statement_purchase_amount=None,
                 statement_finance_amount=None,
                 statement_credit_amount=None,
                 reward_earned_balance=None,
                 past_due_amount=None,
                 last_payment_amount=None,
                 last_payment_date=None,
                 statement_close_balance=None,
                 term_of_ml=None,
                 ml_holder_name=None,
                 description=None,
                 late_fee_amount=None,
                 payoff_amount=None,
                 payoff_amount_date=None,
                 original_maturity_date=None,
                 principal_balance=None,
                 escrow_balance=None,
                 interest_period=None,
                 initial_ml_amount=None,
                 initial_ml_date=None,
                 next_payment_principal_amount=None,
                 next_payment_interest_amount=None,
                 next_payment=None,
                 next_payment_date=None,
                 last_payment_due_date=None,
                 last_payment_receive_date=None,
                 last_payment_principal_amount=None,
                 last_payment_interest_amount=None,
                 last_payment_escrow_amount=None,
                 last_payment_last_fee_amount=None,
                 last_payment_late_charge=None,
                 ytd_principal_paid=None,
                 ytd_interest_paid=None,
                 ytd_insurance_paid=None,
                 ytd_tax_paid=None,
                 auto_pay_enrolled=None,
                 collateral=None,
                 current_school=None,
                 first_payment_date=None,
                 first_mortgage=None,
                 loan_payment_freq=None,
                 original_school=None,
                 recurring_payment_amount=None,
                 lender=None,
                 ending_balance_amount=None,
                 loan_term_type=None,
                 payments_made=None,
                 balloon_amount=None,
                 projected_interest=None,
                 interest_paid_ltd=None,
                 interest_rate_type=None,
                 loan_payment_type=None,
                 repayment_plan=None,
                 payments_remaining=None,
                 interest_margin_balance=None,
                 short_balance=None,
                 available_cash_balance=None,
                 maturity_value_amount=None,
                 vested_balance=None,
                 emp_match_amount=None,
                 emp_pretax_contrib_amount=None,
                 emp_pretax_contrib_amount_ytd=None,
                 contrib_total_ytd=None,
                 cash_balance_amount=None,
                 pre_tax_amount=None,
                 after_tax_amount=None,
                 match_amount=None,
                 profit_sharing_amount=None,
                 rollover_amount=None,
                 other_vest_amount=None,
                 other_nonvest_amount=None,
                 current_loan_balance=None,
                 loan_rate=None,
                 buy_power=None,
                 rollover_ltd=None,
                 additional_properties = {}):
        """Constructor for the CustomerAccountDetail class"""

        # Initialize members of the class
        self.posted_date = posted_date
        self.available_balance_amount = available_balance_amount
        self.open_date = open_date
        self.period_start_date = period_start_date
        self.period_end_date = period_end_date
        self.period_interest_rate = period_interest_rate
        self.period_deposit_amount = period_deposit_amount
        self.period_interest_amount = period_interest_amount
        self.interest_ytd_amount = interest_ytd_amount
        self.interest_prior_ytd_amount = interest_prior_ytd_amount
        self.maturity_date = maturity_date
        self.interest_rate = interest_rate
        self.credit_available_amount = credit_available_amount
        self.credit_max_amount = credit_max_amount
        self.cash_advance_available_amount = cash_advance_available_amount
        self.cash_advance_max_amount = cash_advance_max_amount
        self.cash_advance_balance = cash_advance_balance
        self.cash_advance_interest_rate = cash_advance_interest_rate
        self.current_balance = current_balance
        self.payment_min_amount = payment_min_amount
        self.payment_due_date = payment_due_date
        self.previous_balance = previous_balance
        self.statement_start_date = statement_start_date
        self.statement_end_date = statement_end_date
        self.statement_purchase_amount = statement_purchase_amount
        self.statement_finance_amount = statement_finance_amount
        self.statement_credit_amount = statement_credit_amount
        self.reward_earned_balance = reward_earned_balance
        self.past_due_amount = past_due_amount
        self.last_payment_amount = last_payment_amount
        self.last_payment_date = last_payment_date
        self.statement_close_balance = statement_close_balance
        self.term_of_ml = term_of_ml
        self.ml_holder_name = ml_holder_name
        self.description = description
        self.late_fee_amount = late_fee_amount
        self.payoff_amount = payoff_amount
        self.payoff_amount_date = payoff_amount_date
        self.original_maturity_date = original_maturity_date
        self.principal_balance = principal_balance
        self.escrow_balance = escrow_balance
        self.interest_period = interest_period
        self.initial_ml_amount = initial_ml_amount
        self.initial_ml_date = initial_ml_date
        self.next_payment_principal_amount = next_payment_principal_amount
        self.next_payment_interest_amount = next_payment_interest_amount
        self.next_payment = next_payment
        self.next_payment_date = next_payment_date
        self.last_payment_due_date = last_payment_due_date
        self.last_payment_receive_date = last_payment_receive_date
        self.last_payment_principal_amount = last_payment_principal_amount
        self.last_payment_interest_amount = last_payment_interest_amount
        self.last_payment_escrow_amount = last_payment_escrow_amount
        self.last_payment_last_fee_amount = last_payment_last_fee_amount
        self.last_payment_late_charge = last_payment_late_charge
        self.ytd_principal_paid = ytd_principal_paid
        self.ytd_interest_paid = ytd_interest_paid
        self.ytd_insurance_paid = ytd_insurance_paid
        self.ytd_tax_paid = ytd_tax_paid
        self.auto_pay_enrolled = auto_pay_enrolled
        self.collateral = collateral
        self.current_school = current_school
        self.first_payment_date = first_payment_date
        self.first_mortgage = first_mortgage
        self.loan_payment_freq = loan_payment_freq
        self.original_school = original_school
        self.recurring_payment_amount = recurring_payment_amount
        self.lender = lender
        self.ending_balance_amount = ending_balance_amount
        self.loan_term_type = loan_term_type
        self.payments_made = payments_made
        self.balloon_amount = balloon_amount
        self.projected_interest = projected_interest
        self.interest_paid_ltd = interest_paid_ltd
        self.interest_rate_type = interest_rate_type
        self.loan_payment_type = loan_payment_type
        self.repayment_plan = repayment_plan
        self.payments_remaining = payments_remaining
        self.interest_margin_balance = interest_margin_balance
        self.short_balance = short_balance
        self.available_cash_balance = available_cash_balance
        self.maturity_value_amount = maturity_value_amount
        self.vested_balance = vested_balance
        self.emp_match_amount = emp_match_amount
        self.emp_pretax_contrib_amount = emp_pretax_contrib_amount
        self.emp_pretax_contrib_amount_ytd = emp_pretax_contrib_amount_ytd
        self.contrib_total_ytd = contrib_total_ytd
        self.cash_balance_amount = cash_balance_amount
        self.pre_tax_amount = pre_tax_amount
        self.after_tax_amount = after_tax_amount
        self.match_amount = match_amount
        self.profit_sharing_amount = profit_sharing_amount
        self.rollover_amount = rollover_amount
        self.other_vest_amount = other_vest_amount
        self.other_nonvest_amount = other_nonvest_amount
        self.current_loan_balance = current_loan_balance
        self.loan_rate = loan_rate
        self.buy_power = buy_power
        self.rollover_ltd = rollover_ltd

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
        available_balance_amount = dictionary.get('availableBalanceAmount')
        posted_date = dictionary.get('postedDate')
        open_date = dictionary.get('openDate')
        period_start_date = dictionary.get('periodStartDate')
        period_end_date = dictionary.get('periodEndDate')
        period_interest_rate = dictionary.get('periodInterestRate')
        period_deposit_amount = dictionary.get('periodDepositAmount')
        period_interest_amount = dictionary.get('periodInterestAmount')
        interest_ytd_amount = dictionary.get('interestYtdAmount')
        interest_prior_ytd_amount = dictionary.get('interestPriorYtdAmount')
        maturity_date = dictionary.get('maturityDate')
        interest_rate = dictionary.get('interestRate')
        credit_available_amount = dictionary.get('creditAvailableAmount')
        credit_max_amount = dictionary.get('creditMaxAmount')
        cash_advance_available_amount = dictionary.get('cashAdvanceAvailableAmount')
        cash_advance_max_amount = dictionary.get('cashAdvanceMaxAmount')
        cash_advance_balance = dictionary.get('cashAdvanceBalance')
        cash_advance_interest_rate = dictionary.get('cashAdvanceInterestRate')
        current_balance = dictionary.get('currentBalance')
        payment_min_amount = dictionary.get('paymentMinAmount')
        payment_due_date = dictionary.get('paymentDueDate')
        previous_balance = dictionary.get('previousBalance')
        statement_start_date = dictionary.get('statementStartDate')
        statement_end_date = dictionary.get('statementEndDate')
        statement_purchase_amount = dictionary.get('statementPurchaseAmount')
        statement_finance_amount = dictionary.get('statementFinanceAmount')
        statement_credit_amount = dictionary.get('statementCreditAmount')
        reward_earned_balance = dictionary.get('rewardEarnedBalance')
        past_due_amount = dictionary.get('pastDueAmount')
        last_payment_amount = dictionary.get('lastPaymentAmount')
        last_payment_date = dictionary.get('lastPaymentDate')
        statement_close_balance = dictionary.get('statementCloseBalance')
        term_of_ml = dictionary.get('termOfMl')
        ml_holder_name = dictionary.get('mlHolderName')
        description = dictionary.get('description')
        late_fee_amount = dictionary.get('lateFeeAmount')
        payoff_amount = dictionary.get('payoffAmount')
        payoff_amount_date = dictionary.get('payoffAmountDate')
        original_maturity_date = dictionary.get('originalMaturityDate')
        principal_balance = dictionary.get('principalBalance')
        escrow_balance = dictionary.get('escrowBalance')
        interest_period = dictionary.get('interestPeriod')
        initial_ml_amount = dictionary.get('initialMlAmount')
        initial_ml_date = dictionary.get('initialMlDate')
        next_payment_principal_amount = dictionary.get('nextPaymentPrincipalAmount')
        next_payment_interest_amount = dictionary.get('nextPaymentInterestAmount')
        next_payment = dictionary.get('nextPayment')
        next_payment_date = dictionary.get('nextPaymentDate')
        last_payment_due_date = dictionary.get('lastPaymentDueDate')
        last_payment_receive_date = dictionary.get('lastPaymentReceiveDate')
        last_payment_principal_amount = dictionary.get('lastPaymentPrincipalAmount')
        last_payment_interest_amount = dictionary.get('lastPaymentInterestAmount')
        last_payment_escrow_amount = dictionary.get('lastPaymentEscrowAmount')
        last_payment_last_fee_amount = dictionary.get('lastPaymentLastFeeAmount')
        last_payment_late_charge = dictionary.get('lastPaymentLateCharge')
        ytd_principal_paid = dictionary.get('ytdPrincipalPaid')
        ytd_interest_paid = dictionary.get('ytdInterestPaid')
        ytd_insurance_paid = dictionary.get('ytdInsurancePaid')
        ytd_tax_paid = dictionary.get('ytdTaxPaid')
        auto_pay_enrolled = dictionary.get('autoPayEnrolled')
        collateral = dictionary.get('collateral')
        current_school = dictionary.get('currentSchool')
        first_payment_date = dictionary.get('firstPaymentDate')
        first_mortgage = dictionary.get('firstMortgage')
        loan_payment_freq = dictionary.get('loanPaymentFreq')
        original_school = dictionary.get('originalSchool')
        recurring_payment_amount = dictionary.get('recurringPaymentAmount')
        lender = dictionary.get('lender')
        ending_balance_amount = dictionary.get('endingBalanceAmount')
        loan_term_type = dictionary.get('loanTermType')
        payments_made = dictionary.get('paymentsMade')
        balloon_amount = dictionary.get('balloonAmount')
        projected_interest = dictionary.get('projectedInterest')
        interest_paid_ltd = dictionary.get('interestPaidLtd')
        interest_rate_type = dictionary.get('interestRateType')
        loan_payment_type = dictionary.get('loanPaymentType')
        repayment_plan = dictionary.get('repaymentPlan')
        payments_remaining = dictionary.get('paymentsRemaining')
        interest_margin_balance = dictionary.get('interestMarginBalance')
        short_balance = dictionary.get('shortBalance')
        available_cash_balance = dictionary.get('availableCashBalance')
        maturity_value_amount = dictionary.get('maturityValueAmount')
        vested_balance = dictionary.get('vestedBalance')
        emp_match_amount = dictionary.get('empMatchAmount')
        emp_pretax_contrib_amount = dictionary.get('empPretaxContribAmount')
        emp_pretax_contrib_amount_ytd = dictionary.get('empPretaxContribAmountYtd')
        contrib_total_ytd = dictionary.get('contribTotalYtd')
        cash_balance_amount = dictionary.get('cashBalanceAmount')
        pre_tax_amount = dictionary.get('preTaxAmount')
        after_tax_amount = dictionary.get('afterTaxAmount')
        match_amount = dictionary.get('matchAmount')
        profit_sharing_amount = dictionary.get('profitSharingAmount')
        rollover_amount = dictionary.get('rolloverAmount')
        other_vest_amount = dictionary.get('otherVestAmount')
        other_nonvest_amount = dictionary.get('otherNonvestAmount')
        current_loan_balance = dictionary.get('currentLoanBalance')
        loan_rate = dictionary.get('loanRate')
        buy_power = dictionary.get('buyPower')
        rollover_ltd = dictionary.get('rolloverLtd')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(available_balance_amount,
                   posted_date,
                   open_date,
                   period_start_date,
                   period_end_date,
                   period_interest_rate,
                   period_deposit_amount,
                   period_interest_amount,
                   interest_ytd_amount,
                   interest_prior_ytd_amount,
                   maturity_date,
                   interest_rate,
                   credit_available_amount,
                   credit_max_amount,
                   cash_advance_available_amount,
                   cash_advance_max_amount,
                   cash_advance_balance,
                   cash_advance_interest_rate,
                   current_balance,
                   payment_min_amount,
                   payment_due_date,
                   previous_balance,
                   statement_start_date,
                   statement_end_date,
                   statement_purchase_amount,
                   statement_finance_amount,
                   statement_credit_amount,
                   reward_earned_balance,
                   past_due_amount,
                   last_payment_amount,
                   last_payment_date,
                   statement_close_balance,
                   term_of_ml,
                   ml_holder_name,
                   description,
                   late_fee_amount,
                   payoff_amount,
                   payoff_amount_date,
                   original_maturity_date,
                   principal_balance,
                   escrow_balance,
                   interest_period,
                   initial_ml_amount,
                   initial_ml_date,
                   next_payment_principal_amount,
                   next_payment_interest_amount,
                   next_payment,
                   next_payment_date,
                   last_payment_due_date,
                   last_payment_receive_date,
                   last_payment_principal_amount,
                   last_payment_interest_amount,
                   last_payment_escrow_amount,
                   last_payment_last_fee_amount,
                   last_payment_late_charge,
                   ytd_principal_paid,
                   ytd_interest_paid,
                   ytd_insurance_paid,
                   ytd_tax_paid,
                   auto_pay_enrolled,
                   collateral,
                   current_school,
                   first_payment_date,
                   first_mortgage,
                   loan_payment_freq,
                   original_school,
                   recurring_payment_amount,
                   lender,
                   ending_balance_amount,
                   loan_term_type,
                   payments_made,
                   balloon_amount,
                   projected_interest,
                   interest_paid_ltd,
                   interest_rate_type,
                   loan_payment_type,
                   repayment_plan,
                   payments_remaining,
                   interest_margin_balance,
                   short_balance,
                   available_cash_balance,
                   maturity_value_amount,
                   vested_balance,
                   emp_match_amount,
                   emp_pretax_contrib_amount,
                   emp_pretax_contrib_amount_ytd,
                   contrib_total_ytd,
                   cash_balance_amount,
                   pre_tax_amount,
                   after_tax_amount,
                   match_amount,
                   profit_sharing_amount,
                   rollover_amount,
                   other_vest_amount,
                   other_nonvest_amount,
                   current_loan_balance,
                   loan_rate,
                   buy_power,
                   rollover_ltd,
                   dictionary)


