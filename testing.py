import requests, json
import alpaca_trade_api as trade_api


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


def get_price(symbols, period, limit=100):
    data = {
        "symbols": symbols
    }    
    finalurl = PRICE_URL + '/' + period
    r = requests.get(finalurl, json=data, headers=HEADERS)
    return r.content


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
    print(get_account())
    #prices = get_price("AAPL", "minute", 5)
    #print(prices)

    #response = send_order("GOOG", 50, "buy", "market", "gtc")
    #print(response)
