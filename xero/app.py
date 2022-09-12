from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__, template_folder='./myapp/templates')
CORS(app)

@app.route('/balancesheet/<customer_pk>')
def get_balancesheet(customer_pk):
    if customer_pk == "1":
        return jsonify(
            [
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
    elif customer_pk == "2":
        return jsonify(
            [
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


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8002, debug=True)
