

## Business Loan Application by Francisco Gallardo Cervantes

# Services included are:

* Frontend: Vue.js client based Node.js server to communicate with the backend service.
* Backend: Django app, which works like a "bridge" between the frontend and external microservices, such as XERO, MYOB, and the decision engine. 
* MYOB: Flask based application which simulates an external XERO service. It provides balance sheets in JSON format for a specific business. 
* XERO: Flask based application which simulates an external MYOB service. It provides balance sheets in JSON format for a specific business.
* Decision Engine: It contains business logic to determine and assess a loan amount for a business.

### How to run the application

```bash
# Start the application with the command below:
docker-compose up

# Run necessary database migrations:
docker-compose exec backend python manage.py migrate

# Run the three commands below to add some mock data in the database:
docker-compose exec backend python manage.py loaddata accounting_providers.yaml
docker-compose exec backend python manage.py loaddata businesses.yaml
docker-compose exec backend python manage.py loaddata balance_sheets.yaml

# Visit the url http://localhost:8080 to interact with the frontend Vue.js application.
```
# Visit the url http://localhost:8080 to interact with the frontend Vue.js application.
# You can also interact with the API endpoints available in the Django Rest Framework application visiting the url http://localhost:8000/swagger/

### The application has been built using the Django Rest Framework, but if you need to interact directly with the database you can use the URLs below:
  - http://localhost:8000/new-business to create a new Business.
  - http://localhost:8000/businesses to see Business.
  - http://localhost:8000/new-accounting-provider to create a new Accounting Provider.
  - http://localhost:8000/accounting-providers to see Accounting Providers.
  - http://localhost:8000/new-balance-sheet to create a new Balance Sheet.
  - http://localhost:8000/balance-sheets to see Balance Sheets.


### You should be able to see how the external APIs for XERO and MYOB work by visiting the urls below:

http://127.0.0.1:8001/balancesheet/1 for MYOB and http://127.0.0.1:8002/balancesheet/2 for XERO

## Run tests:
### While docker containers are running, run the command below in a new terminal window:
```docker-compose exec decisionengine pytest```
