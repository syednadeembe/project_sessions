from flask import Flask, render_template, request
import yfinance as yf

app = Flask(__name__)

def format_ticker(ticker, country):
    if country == 'india':
        return f"{ticker}.NS"
    return ticker.upper()

@app.route('/', methods=['GET', 'POST'])
def index():
    stock_info = None
    error = None

    if request.method == 'POST':
        ticker = request.form['ticker']
        country = request.form['country']

        formatted_ticker = format_ticker(ticker, country)

        try:
            stock = yf.Ticker(formatted_ticker)
            info = stock.info
            stock_info = {
                'symbol': info.get('symbol'),
                'longName': info.get('longName'),
                'currentPrice': info.get('currentPrice'),
                'previousClose': info.get('previousClose'),
                'currency': info.get('currency'),
                'marketCap': info.get('marketCap'),
            }
        except Exception as e:
            error = f"Couldn't fetch data for {ticker}: {str(e)}"

    return render_template('index.html', stock_info=stock_info, error=error)

if __name__ == '__main__':
    app.run(debug=True)

