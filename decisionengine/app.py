from flask import Flask, request, jsonify
from flask_cors import CORS
import datetime
import json

app = Flask(__name__, template_folder='./myapp/templates')

CORS(app)

@app.route('/process-balance-sheet', methods=['POST'])
def process_balance_sheet():
    # content = request.get_json(silent=True)
    # print(content) # Do your processing
    data = request.json
    balance_sheet = data['balanceSheet']
    business_name = data['businessName']
    loan_amount = int(data['loanAmount'])

    today = datetime.date.today()

    year_established = today.year
    pre_assessment = 20
    profit_or_loss = 0
    assets_value = 0
    if len(balance_sheet) < 12:
        return jsonify({"error": "A balance sheet must include at least 12 months to make an assessment."})
    for index, month in enumerate(balance_sheet):
        if index <= 12:
            year = month['year']
            profit_or_loss += int(month['profitOrLoss'])
            assets_value += int(month['assetsValue'])
            if year < year_established:
                year_established = year
            if profit_or_loss > 0:
                pre_assessment = 60
    if (int(assets_value) / 12) > loan_amount:
        pre_assessment = 100
    return jsonify({
        "business_name": business_name,
        "year_established": year_established,
        "preAssessment": pre_assessment
    })


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8003, debug=True)
