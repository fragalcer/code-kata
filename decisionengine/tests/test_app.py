import json

def test_json_data(client, app):
    with app.app_context():
        response = client.post(
            "/process-balance-sheet",
            json={
                "loanAmount": 5000,
                "businessName": "TestBusiness",
                "balanceSheet": [
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
            }
        )
        assert response.status_code == 200
        data = json.loads(response.data.decode("utf-8"))
        assert data['year_established'] == 2010
        assert data['preAssessment'] == 100
        assert data['business_name'] == "TestBusiness"

def test_preassessment_60(client, app):
    with app.app_context():
        response = client.post(
            "/process-balance-sheet",
            json={
                "loanAmount": 5000000000,
                "businessName": "TestBusiness",
                "balanceSheet": [
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
            }
        )
        assert response.status_code == 200
        data = json.loads(response.data.decode("utf-8"))
        assert data['year_established'] == 2010
        assert data['preAssessment'] == 60
        assert data['business_name'] == "TestBusiness"


def test_preassessment_100(client, app):
    with app.app_context():
        response = client.post(
            "/process-balance-sheet",
            json={
                "loanAmount": 300,
                "businessName": "TestBusiness",
                "balanceSheet": [
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
            }
        )
        assert response.status_code == 200
        data = json.loads(response.data.decode("utf-8"))
        assert data['year_established'] == 2010
        assert data['preAssessment'] == 100
        assert data['business_name'] == "TestBusiness"


def test_balance_sheet_must_include_at_least_12_months(client, app):
    with app.app_context():
        response = client.post(
            "/process-balance-sheet",
            json={
                "loanAmount": 300,
                "businessName": "TestBusiness",
                "balanceSheet": [
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
            }
        )
        assert response.status_code == 200
        data = json.loads(response.data.decode("utf-8"))
        assert data['error'] == "A balance sheet must include at least 12 months to make an assessment."
