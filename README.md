

# HOW TO RUN:

Run the commands below:

```docker-compose up```
```docker-compose exec web bash```
```python manage.py migrate```

## URLs available:
  - http://localhost:8000/new-business to create a new Business.
  - http://localhost:8000/businesses to see Business.
  - http://localhost:8000/new-accounting-provider to create a new Accounting Provider.
  - http://localhost:8000/accounting-providers to see Accounting Providers.
  - http://localhost:8000/new-balance-sheet to create a new Balance Sheet.
  - http://localhost:8000/balance-sheets to see Balance Sheets.
  - http://localhost:8000/request-balance-sheet-from-accounting-provider/<business_primary_key>/ to see Request a Balance Sheet.
  - http://localhost:8000/balance-sheet-from-accounting-provider/<business_pk>/<accounting_provider_pk>/ to Request a Loan.

## Run tests:
While docker containers are running, run the command below in a new terminal window:
```docker-compose exec web python manage.py test```