import requests, json
import alpaca_trade_api as trade_api
import pandas as pd
import pandas_datareader.data as web
import datetime as dt
import bs4 as bs
import yfinance as yf


API_KEY = 'PKCGQRZSPSWL4C473414'  #APCA-API-KEY-ID
API_SECRET = 'XPz2wUSl6L6wDY6BEn7MM4GIicBBEuQtnaawmqvg' #APCA-API-SECRET-KEY
BASE_URL = 'https://paper-api.alpaca.markets'
HEADERS = {'APCA-API-KEY-ID':API_KEY, 'APCA-API-SECRET-KEY':API_SECRET}

ACCOUNT_URL = BASE_URL + '/v2/account'
PRICE_URL = BASE_URL + '/v1/bars'
ORDER_URL = BASE_URL + '/v2/orders'


def get_account():  
    r = requests.get(ACCOUNT_URL, headers=HEADERS)
    return json.loads(r.content)

def get_price(symbol, start, end):
    return web.DataReader(symbol,'yahoo',start,end)

def get_sp500_stocks():
    data = pd.read_html('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
    table = data[0]
    bullish_engulfing_stocks = []
    for index, row in table[['Symbol']].iterrows():
        stock = str(row['Symbol'])
        if stock.isalpha():
            df = get_stock_prices(stock, '5d')
            if is_bullish_engulfing(df):
                bullish_engulfing_stocks.append(stock)
    return bullish_engulfing_stocks


def get_stock_prices(stock, interval):
    ticker = yf.Ticker(stock)
    df = ticker.history(period=interval)
    return df


def buy_stocks(stocks):
    for stock in stocks:
        send_order(stock, 10, "buy", "market", "gtc")
    return None


def sell_stocks(stocks):
    for stock in stocks:
        send_order(stock, 10, "buy", "market", "gtc")
    return None


def is_bullish_engulfing(df):
    is_bullish_engulfing_flag = False

    first_open = float(df.iloc[0,0])
    first_close = float(df.iloc[0,3])
    
    second_open = float(df.iloc[1,0])
    second_close = float(df.iloc[1,3])
    
    third_open = float(df.iloc[2,0])
    third_close = float(df.iloc[2,3])
    
    fourth_open = float(df.iloc[3,0])
    fourth_close = float(df.iloc[3,3])

    last_open = float(df.iloc[4,0])
    last_close = float(df.iloc[4,3])

    if last_close > first_open and last_close > first_close and last_open < first_open and last_open < first_close \
        and last_close > second_open and last_close > second_close and last_open < second_open and last_open < second_close\
        and last_close > third_open and last_close > third_close and last_open < third_open and last_open < third_close\
        and last_close > fourth_open and last_close > fourth_close and last_open < fourth_open and last_open < fourth_close:
        is_bullish_engulfing_flag = True
    return is_bullish_engulfing_flag


def send_order(symbol, qty, side, order_type, time):
    data = {
        "symbol": symbol,
        "qty": qty,
        "side": side,
        "type": order_type,
        "time_in_force": time
    }    
    r = requests.post(ORDER_URL, json=data, headers=HEADERS)
    return json.loads(r.content)


if __name__=="__main__":
    
    api = trade_api.REST(API_KEY,API_SECRET,BASE_URL)    
    
    stocks = get_sp500_stocks()

    account = api.get_account()
    
    if account.buying_power > 10000 and dt.datetime.today().weekday() != 5:
        for stock in stocks:
            send_order(stock, 20, "buy", "market", "gtc")   

    if dt.datetime.today().weekday() == 5:
        portfolio = api.list_positions()
        for position in portfolio:
            send_order(stock, 20, "sell", "market", "gtc")