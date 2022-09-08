from django.test import TestCase
from businessloanapp.models import AccountingProvider, Business, BalanceSheet
from django.core.exceptions import ValidationError

class BusinessLoanTestCase(TestCase):
    def setUp(self):
        self.xero = AccountingProvider.objects.create(name="Xero")
        self.myob = AccountingProvider.objects.create(name="MYOB")
        self.ox_global = AccountingProvider.objects.create(name="0X Global Pty Ltd")
        self.joseph_palmer = AccountingProvider.objects.create(name="Joseph Palmer & Sons")
        self.count_financial = AccountingProvider.objects.create(name="Count Financial Limited")

        self.woolworths = Business.objects.create(name="Woolworths", loan_amount=5000000000)
        self.commbank = Business.objects.create(name="Commonwealth Bank", loan_amount=300.50)
        self.bhp = Business.objects.create(name="BHP", loan_amount=1500000)
        self.wesfarmers = Business.objects.create(name="Wesfarmers", loan_amount=19500.80)
        self.nike = Business.objects.create(name="Nike", loan_amount=1490.80)


    def test_preassessment_60(self):
        """If a business has made a profit in the last 12 months. The final value to be sent with a field
        "preAssessment": "60" which means the Loan is favored to be approved 60% of the requested value."""
        balancesheet = BalanceSheet.objects.create(
            business=self.woolworths,
            accounting_provider=self.xero,
            balance_sheet=[
                {
                    "year": 2010,
                    "month": 12,
                    "profitOrLoss": 250000,
                    "assetsValue": 1234
                },
                {
                    "year": 2010,
                    "month": 11,
                    "profitOrLoss": 1150,
                    "assetsValue": 5789
                },
                {
                    "year": 2010,
                    "month": 10,
                    "profitOrLoss": 2500,
                    "assetsValue": 22345
                },
                {
                    "year": 2010,
                    "month": 9,
                    "profitOrLoss": -187000,
                    "assetsValue": 223452
                },
                {
                    "year": 2010,
                    "month": 8,
                    "profitOrLoss": -187000,
                    "assetsValue": 223452
                },
                {
                    "year": 2010,
                    "month": 7,
                    "profitOrLoss": -187000,
                    "assetsValue": 223452
                },
                {
                    "year": 2010,
                    "month": 6,
                    "profitOrLoss": -187000,
                    "assetsValue": 223452
                },
                {
                    "year": 2010,
                    "month": 5,
                    "profitOrLoss": -187000,
                    "assetsValue": 223452
                },
                {
                    "year": 2010,
                    "month": 4,
                    "profitOrLoss": -187000,
                    "assetsValue": 223452
                },
                {
                    "year": 2010,
                    "month": 3,
                    "profitOrLoss": -187000,
                    "assetsValue": 223452
                },
                {
                    "year": 2010,
                    "month": 2,
                    "profitOrLoss": -187000,
                    "assetsValue": 223452
                },
                {
                    "year": 2010,
                    "month": 1,
                    "profitOrLoss": -187000,
                    "assetsValue": 223452
                }

            ]
        )
        decision = balancesheet.get_decision()
        self.assertEqual(decision["preAssessment"], 60)


    def test_preassessment_100(self):
        """If the average asset value across 12 months is greater than the loan amount then "preAssessment": "100"."""
        balancesheet = BalanceSheet.objects.create(
            business=self.commbank,
            accounting_provider=self.xero,
            balance_sheet=[
                {
                    "year": 2010,
                    "month": 12,
                    "profitOrLoss": 250000,
                    "assetsValue": 1234
                },
                {
                    "year": 2010,
                    "month": 11,
                    "profitOrLoss": 1150,
                    "assetsValue": 5789
                },
                {
                    "year": 2010,
                    "month": 10,
                    "profitOrLoss": 2500,
                    "assetsValue": 22345
                },
                {
                    "year": 2010,
                    "month": 9,
                    "profitOrLoss": -187000,
                    "assetsValue": 223452
                },
                {
                    "year": 2010,
                    "month": 8,
                    "profitOrLoss": -187000,
                    "assetsValue": 223452
                },
                {
                    "year": 2010,
                    "month": 7,
                    "profitOrLoss": -187000,
                    "assetsValue": 223452
                },
                {
                    "year": 2010,
                    "month": 6,
                    "profitOrLoss": -187000,
                    "assetsValue": 223452
                },
                {
                    "year": 2010,
                    "month": 5,
                    "profitOrLoss": -187000,
                    "assetsValue": 223452
                },
                {
                    "year": 2010,
                    "month": 4,
                    "profitOrLoss": -187000,
                    "assetsValue": 223452
                },
                {
                    "year": 2010,
                    "month": 3,
                    "profitOrLoss": -187000,
                    "assetsValue": 223452
                },
                {
                    "year": 2010,
                    "month": 2,
                    "profitOrLoss": -187000,
                    "assetsValue": 223452
                },
                {
                    "year": 2010,
                    "month": 1,
                    "profitOrLoss": -187000,
                    "assetsValue": 223452
                }

            ]
        )
        decision = balancesheet.get_decision()
        self.assertEqual(decision["preAssessment"], 100)

    def test_preassessment_default_value_20(self):
        """Test that all businesses get at least 20% of the loan approval."""
        balancesheet = BalanceSheet.objects.create(
            business=self.bhp,
            accounting_provider=self.xero,
            balance_sheet=[
                {
                    "year": 2010,
                    "month": 12,
                    "profitOrLoss": -250000,
                    "assetsValue": 0
                },
                {
                    "year": 2010,
                    "month": 11,
                    "profitOrLoss": -1150,
                    "assetsValue": 0
                },
                {
                    "year": 2010,
                    "month": 10,
                    "profitOrLoss": -2500,
                    "assetsValue": 0
                },
                {
                    "year": 2010,
                    "month": 9,
                    "profitOrLoss": -187000,
                    "assetsValue": 0
                },
                {
                    "year": 2010,
                    "month": 8,
                    "profitOrLoss": -187000,
                    "assetsValue": 0
                },
                {
                    "year": 2010,
                    "month": 7,
                    "profitOrLoss": -187000,
                    "assetsValue": 0
                },
                {
                    "year": 2010,
                    "month": 6,
                    "profitOrLoss": -187000,
                    "assetsValue": 0
                },
                {
                    "year": 2010,
                    "month": 5,
                    "profitOrLoss": -187000,
                    "assetsValue": 50
                },
                {
                    "year": 2010,
                    "month": 4,
                    "profitOrLoss": -187000,
                    "assetsValue": 0
                },
                {
                    "year": 2010,
                    "month": 3,
                    "profitOrLoss": -187000,
                    "assetsValue": 50
                },
                {
                    "year": 2010,
                    "month": 2,
                    "profitOrLoss": -187000,
                    "assetsValue": 0
                },
                {
                    "year": 2010,
                    "month": 1,
                    "profitOrLoss": -187000,
                    "assetsValue": 50
                }

            ]
        )
        decision = balancesheet.get_decision()
        self.assertEqual(decision["preAssessment"], 20)

    def test_requested_attributes_in_decision_response(self):
        """Test that we get the requested attributes in the response decision Object."""
        balancesheet = BalanceSheet.objects.create(
            business=self.woolworths,
            accounting_provider=self.xero,
            balance_sheet=[
                {
                    "year": 2010,
                    "month": 12,
                    "profitOrLoss": 250000,
                    "assetsValue": 1234
                },
                {
                    "year": 2010,
                    "month": 11,
                    "profitOrLoss": 1150,
                    "assetsValue": 5789
                },
                {
                    "year": 2010,
                    "month": 10,
                    "profitOrLoss": 2500,
                    "assetsValue": 22345
                },
                {
                    "year": 2010,
                    "month": 9,
                    "profitOrLoss": -187000,
                    "assetsValue": 223452
                },
                {
                    "year": 2010,
                    "month": 8,
                    "profitOrLoss": -187000,
                    "assetsValue": 223452
                },
                {
                    "year": 2010,
                    "month": 7,
                    "profitOrLoss": -187000,
                    "assetsValue": 223452
                },
                {
                    "year": 2010,
                    "month": 6,
                    "profitOrLoss": -187000,
                    "assetsValue": 223452
                },
                {
                    "year": 2010,
                    "month": 5,
                    "profitOrLoss": -187000,
                    "assetsValue": 223452
                },
                {
                    "year": 2010,
                    "month": 4,
                    "profitOrLoss": -187000,
                    "assetsValue": 223452
                },
                {
                    "year": 2010,
                    "month": 3,
                    "profitOrLoss": -187000,
                    "assetsValue": 223452
                },
                {
                    "year": 2010,
                    "month": 2,
                    "profitOrLoss": -187000,
                    "assetsValue": 223452
                },
                {
                    "year": 2010,
                    "month": 1,
                    "profitOrLoss": -187000,
                    "assetsValue": 223452
                }

            ]
        )
        decision = balancesheet.get_decision()
        self.assertTrue("business_name" in decision)
        self.assertTrue("year_established" in decision)
        self.assertTrue("preAssessment" in decision)

    def test_balance_sheet_must_include_at_least_12_months(self):
        """Test that balance sheets must include at least 12 months."""
        balancesheet = BalanceSheet.objects.create(
            business=self.woolworths,
            accounting_provider=self.xero,
            balance_sheet=[
                {
                    "year": 2010,
                    "month": 12,
                    "profitOrLoss": 250000,
                    "assetsValue": 1234
                },
                {
                    "year": 2010,
                    "month": 11,
                    "profitOrLoss": 1150,
                    "assetsValue": 5789
                },
                {
                    "year": 2010,
                    "month": 10,
                    "profitOrLoss": 2500,
                    "assetsValue": 22345
                },
                {
                    "year": 2010,
                    "month": 9,
                    "profitOrLoss": -187000,
                    "assetsValue": 223452
                },
                {
                    "year": 2010,
                    "month": 8,
                    "profitOrLoss": -187000,
                    "assetsValue": 223452
                },
                {
                    "year": 2010,
                    "month": 7,
                    "profitOrLoss": -187000,
                    "assetsValue": 223452
                },
                {
                    "year": 2010,
                    "month": 6,
                    "profitOrLoss": -187000,
                    "assetsValue": 223452
                },
                {
                    "year": 2010,
                    "month": 5,
                    "profitOrLoss": -187000,
                    "assetsValue": 223452
                },
                {
                    "year": 2010,
                    "month": 4,
                    "profitOrLoss": -187000,
                    "assetsValue": 223452
                },
                {
                    "year": 2010,
                    "month": 3,
                    "profitOrLoss": -187000,
                    "assetsValue": 223452
                }
            ]
        )
        with self.assertRaises(ValidationError, msg='A balance sheet must include at least 12 months to make an assessment.'):
            balancesheet.get_decision()

