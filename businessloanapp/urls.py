from django.urls import path

from . import views

urlpatterns = [
    path('new-business', views.BusinessCreateView.as_view(), name='new_business'),
    path('businesses', views.BusinessListView.as_view(), name='businesses'),
    path('new-accounting-provider', views.AccountingProviderCreateView.as_view(), name='new_accounting_provider'),
    path('accounting-providers', views.AccountingProvidersListView.as_view(), name='accounting_providers'),
    path('new-balance-sheet', views.BalanceSheetCreateView.as_view(), name='new_balance_sheet'),
    path('balance-sheets', views.BalanceSheetListView.as_view(), name='balance_sheets'),
    path(
        'request-balance-sheet-from-accounting-provider/<int:business_pk>/<int:accounting_provider_pk>/',
        views.BalanceSheetFromAccountingProvider.as_view(),
        name='request_balance_sheet_from_accounting_provider'
    ),
    path(
        'balance-sheet-from-accounting-provider/<int:business_pk>/<int:accounting_provider_pk>/',
        views.DecisionOutcomeView.as_view(),
        name='request_loan'
    )
]