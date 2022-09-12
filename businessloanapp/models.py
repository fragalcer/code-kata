from django.db import models


class AccountingProvider(models.Model):
    name = models.CharField(max_length=200, help_text="Name of the accounting provider.")
    logo = models.ImageField(help_text="Logo of the Accounting Provider.")

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
    url = models.URLField(max_length=200, help_text="API url to retrieve data for a specific Business.")
