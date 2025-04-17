import os
import requests
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

API_KEY = " HPACUVIELWE0MWGB"  # Replace with your actual Alpha Vantage API key
ALPHA_VANTAGE_URL = "https://www.alphavantage.co/query"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_stock_price', methods=['GET'])
def get_stock_price():
    symbol = request.args.get('symbol')
    if not symbol:
        return jsonify({'success': False, 'message': 'No stock symbol provided'})

    params = {
        'function': 'TIME_SERIES_INTRADAY',
        'symbol': symbol,
        'interval': '5min',
        'apikey': API_KEY
    }

    try:
        response = requests.get(ALPHA_VANTAGE_URL, params=params)
        data = response.json()
        
        # Debugging: Print the raw response data to check what you're getting from the API
        print(data)  # Add this line for debugging

        # Check for rate limit exceeded
        if "Note" in data:
            return jsonify({'success': False, 'message': 'API rate limit exceeded. Try again later.'})
        
        # Check for invalid or unsupported symbol
        elif "Error Message" in data:
            return jsonify({'success': False, 'message': 'Invalid or unsupported stock symbol.'})

        # Process valid data
        if "Time Series (5min)" in data:
            time_series = data["Time Series (5min)"]
            latest_time = sorted(time_series.keys(), reverse=True)[0]
            latest_price = time_series[latest_time]['1. open']
            return jsonify({'success': True, 'symbol': symbol.upper(), 'price': latest_price, 'time': latest_time})
        else:
            return jsonify({'success': False, 'message': 'Invalid symbol or API limit reached'})

    except Exception as e:
        return jsonify({'success': False, 'message': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
