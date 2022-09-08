from django.db import models
from datetime import date
from django.core.exceptions import ValidationError


class AccountingProvider(models.Model):
    name = models.CharField(max_length=200, help_text="Name of the accounting provider.")

    def __str__(self):
        return self.name

class Business(models.Model):
    name = models.CharField(max_length=200, help_text="Name of the business.")
    loan_amount = models.FloatField(default=0.0, help_text="Amount requested by this business in Australian dollars.")

    def __str__(self):
        return self.name

class BalanceSheet(models.Model):
    business = models.ForeignKey(Business, on_delete=models.CASCADE, help_text="Business this balance sheet belongs to.")
    accounting_provider = models.ForeignKey(AccountingProvider, models.CASCADE, help_text="Name of the accounting provider.")
    balance_sheet = models.JSONField(
        default=list,
        help_text="Current accounting balance for this business with this accounting provider."
    )

    def get_decision(self) -> dict:
        year_established = date.today().year
        pre_assessment = 20
        profit_or_loss = 0
        assets_value = 0
        if len(self.balance_sheet) < 12:
            raise ValidationError("A balance sheet must include at least 12 months to make an assessment.")
        for index, month in enumerate(self.balance_sheet):
            if index <= 12:
                year = month['year']
                profit_or_loss += month['profitOrLoss']
                assets_value += month['assetsValue']
                if year < year_established:
                    year_established = year
                if profit_or_loss > 0:
                    pre_assessment = 60
        if (assets_value / 12) > self.business.loan_amount:
            pre_assessment = 100
        return {
            "business_name": self.business.name,
            "year_established": year_established,
            "preAssessment": pre_assessment
        }
