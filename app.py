from flask import Flask, request
import requests

app = Flask(__name__)


def get_data():
    response = requests.get("https://nbu.uz/uz/exchange-rates/json/")
    
    usa = response.json()[-1]
    usd = float(usa['nbu_buy_price'])
    return usd



@app.route('/api/to-usd', methods=['GET'])
def to_usd():
    """
    Convert to USD

    Returns:
        json: Converted amount
    
    Note:
        request data will be like this:
            /api/to-usd?amount=1000
        
        response will be like this:
            {
                "amount": 1000,
                "currency": "UZS",
                "converted": 88.7,
                "convertedCurrency": "USD"
            }
    """
    usd = get_data()
    uzs = request.args.get("amount","not found")
    data = {
                "amount": uzs,
                "currency": "UZS",
                "converted": round((float(uzs))/usd, 2),
                "convertedCurrency": "USD"
            }
    return data
@app.route('/api/to-uzs', methods=['GET'])
def to_uzs():
    """
    Convert to UZS

    Returns:
        json: Converted amount
    
    Note:
        request data will be like this:
            /api/to-uzs?amount=1000
        
        response will be like this:
            {
                "amount": 1000,
                "currency": "USD",
                "converted": 1138070,
                "convertedCurrency": "UZS"
            }
    """
    usd = get_data()
    usd1 = request.args.get("amount","qiymat yo'q")
    uzs = float(usd1) * usd
    data = {
        "amount": usd,
        "currency": "USD",
        "converted": round(uzs,2),
        "convertedCurrency": "UZS"
        }
    return data

if __name__ == '__main__':
    app.run()    