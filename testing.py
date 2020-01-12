import requests, json
import alpaca_trade_api as trade_api
import pandas as pd
import pandas_datareader.data as web
import datetime as dt
import bs4 as bs


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
    stocks = []
    for index, row in table[['Symbol']].iterrows():
        stocks.append(str(row['Symbol']))
    return stocks


def get_all_(stocks):
    dic = {}
    for stock in stocks:
        start = dt.datetime.now() - dt.timedelta(1)       
        end = dt.datetime.now()
        if stock.isalpha():
            data = web.DataReader(stock,'yahoo',start,end)
            dic[stock] = float(data['Open'].values)
    return dic


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
    #print(get_account())

    '''
    start = dt.datetime.now() - dt.timedelta(1)
    end = dt.datetime.now()

     = get_price('GOOG',start,end)
    print()
    '''
    
    # = get_price("GOOG", "minute", 5)

    sp500_list = get_sp500_stocks()
    #print(sp500_list)
    sp500_ = get_all_(sp500_list)
    print(sp500_)

    #response = send_order("GOOG", 50, "buy", "market", "gtc")
    #print(response)
