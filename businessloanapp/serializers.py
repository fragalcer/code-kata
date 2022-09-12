from businessloanapp.models import AccountingProvider, BalanceSheet, Business
from rest_framework import serializers


class AccountingProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountingProvider
        fields = '__all__'


class BalanceSheetSerializer(serializers.ModelSerializer):
    class Meta:
        model = BalanceSheet
        fields = '__all__'


class BusinessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Business
        fields = '__all__'