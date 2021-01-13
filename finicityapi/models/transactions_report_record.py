# -*- coding: utf-8 -*-

import finicityapi.models.transaction_report_constraints
import finicityapi.models.transactions_report_institution

class TransactionsReportRecord(object):

    """Implementation of the 'Transactions Report Record' model.

    The fields used for the Transaction History Report (CRA products).

    Attributes:
        id (string): The Finicity report ID (max 32 characters)
        title (string): Finicity Transactions Report
        customer_type (string): active or testing
        customer_id (long|int): Finicity customer ID
        consumer_id (string): Finicity report consumer ID (max length 32
            characters).
        consumer_ssn (string): Last 4 digits of the report consumer’s Social
            Security number.
        mtype (TypeEnum): Report type
        status (string): inProgress or success or failure.
        created_date (long|int): The date the report was generated.
        constraints (TransactionReportConstraints): Specifies use of
            accountIds, reportCustomFields, includePending, fromDate, and
            toDate when creating the report.
        start_date (long|int): The postedDate of the earliest transaction
            analyzed for this report.
        end_date (long|int): The postedDate of the latest transaction analyzed
            for this report.
        days (long|int): Number of days covered by the report.
        seasoned (bool): true: if the report covers more than 365 days.
        gse_enabled (bool): Finicity internal use only.
        portfolio_id (string): Finicity’s portfolio ID associated with the
            consumer on the report.
        institutions (list of TransactionsReportInstitution): A list of
            institution records, including information about the individual
            accounts used in this report. See the Institution Record
            structure.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id":'id',
        "title":'title',
        "customer_type":'customerType',
        "customer_id":'customerId',
        "consumer_id":'consumerId',
        "consumer_ssn":'consumerSsn',
        "mtype":'type',
        "status":'status',
        "created_date":'createdDate',
        "constraints":'constraints',
        "start_date":'startDate',
        "end_date":'endDate',
        "days":'days',
        "seasoned":'seasoned',
        "gse_enabled":'gseEnabled',
        "portfolio_id":'portfolioId',
        "institutions":'institutions'
    }

    def __init__(self,
                 id=None,
                 title=None,
                 customer_type=None,
                 customer_id=None,
                 consumer_id=None,
                 consumer_ssn=None,
                 mtype=None,
                 status=None,
                 created_date=None,
                 constraints=None,
                 start_date=None,
                 end_date=None,
                 days=None,
                 seasoned=None,
                 gse_enabled=None,
                 portfolio_id=None,
                 institutions=None,
                 additional_properties = {}):
        """Constructor for the TransactionsReportRecord class"""

        # Initialize members of the class
        self.id = id
        self.title = title
        self.customer_type = customer_type
        self.customer_id = customer_id
        self.consumer_id = consumer_id
        self.consumer_ssn = consumer_ssn
        self.mtype = mtype
        self.status = status
        self.created_date = created_date
        self.constraints = constraints
        self.start_date = start_date
        self.end_date = end_date
        self.days = days
        self.seasoned = seasoned
        self.gse_enabled = gse_enabled
        self.portfolio_id = portfolio_id
        self.institutions = institutions

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
        title = dictionary.get('title')
        customer_type = dictionary.get('customerType')
        customer_id = dictionary.get('customerId')
        consumer_id = dictionary.get('consumerId')
        consumer_ssn = dictionary.get('consumerSsn')
        mtype = dictionary.get('type')
        status = dictionary.get('status')
        created_date = dictionary.get('createdDate')
        constraints = finicityapi.models.transaction_report_constraints.TransactionReportConstraints.from_dictionary(dictionary.get('constraints')) if dictionary.get('constraints') else None
        start_date = dictionary.get('startDate')
        end_date = dictionary.get('endDate')
        days = dictionary.get('days')
        seasoned = dictionary.get('seasoned')
        gse_enabled = dictionary.get('gseEnabled')
        portfolio_id = dictionary.get('portfolioId')
        institutions = None
        if dictionary.get('institutions') != None:
            institutions = list()
            for structure in dictionary.get('institutions'):
                institutions.append(finicityapi.models.transactions_report_institution.TransactionsReportInstitution.from_dictionary(structure))

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(id,
                   title,
                   customer_type,
                   customer_id,
                   consumer_id,
                   consumer_ssn,
                   mtype,
                   status,
                   created_date,
                   constraints,
                   start_date,
                   end_date,
                   days,
                   seasoned,
                   gse_enabled,
                   portfolio_id,
                   institutions,
                   dictionary)


