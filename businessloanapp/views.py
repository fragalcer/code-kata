from django.shortcuts import reverse
from django.views.generic import CreateView, ListView, TemplateView

from businessloanapp.models import Business, AccountingProvider, BalanceSheet


class BusinessCreateView(CreateView):
    model = Business
    fields = '__all__'

    def get_success_url(self):
        return reverse('request_balance_sheet_from_accounting_provider', kwargs={'pk': self.object.id})

class BusinessListView(ListView):
    model = Business


class AccountingProviderCreateView(CreateView):
    model = AccountingProvider
    fields = '__all__'

    def get_success_url(self):
        return reverse('accounting_providers')

class AccountingProvidersListView(ListView):
    model = AccountingProvider

class BalanceSheetCreateView(CreateView):
    model = BalanceSheet
    fields = '__all__'

    def get_success_url(self):
        return reverse('balance_sheets')

class BalanceSheetListView(ListView):
    model = BalanceSheet

class RequestBalanceSheetFromAccountingProvider(ListView):
    model = AccountingProvider
    template_name = "businessloanapp/select_accounting_provider_for_business.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        business = Business.objects.get(pk=self.kwargs['business_pk'])
        context.update({
            "business": business
        })
        return context

class BalanceSheetFromAccountingProvider(ListView):
    model = BalanceSheet
    template_name = 'businessloanapp/balancesheet_list_with_button.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context.update({
            "business": Business.objects.get(pk=self.kwargs['business_pk']),
            "accounting_provider": AccountingProvider.objects.get(pk=self.kwargs['accounting_provider_pk'])
        })
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(business__id=self.kwargs['business_pk']).filter(accounting_provider__id=self.kwargs['accounting_provider_pk'])

class DecisionOutcomeView(TemplateView):
    template_name = 'businessloanapp/decision_outcome.html'

    def get_context_data(self, **kwargs):
        balance_sheet = BalanceSheet.objects.get(business__id=self.kwargs['business_pk'], accounting_provider__id=self.kwargs['accounting_provider_pk'])
        decision = balance_sheet.get_decision()
        context = super().get_context_data(**kwargs)
        context.update({
            "decision": decision
        })
        return context

