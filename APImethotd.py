from binance import Client, ThreadedWebsocketManager, ThreadedDepthCacheManager
import pandas as pd

api_key = 'dcCdJKk7uG15Q89AvmWMfe1Pt8blK8Pjrnp8MiXOooKWNflaFU0zgVyl1jkbZSby'
api_secret = 'C37slYIfvJB2GqOQQ2uuteyTOFSpz1251JlW8HngphqWxXDsl9OocxKgGLL4Ok73'

try:
    client = Client(api_key, api_secret)
except:
    print('error')

# get market depth
# pd.DataFrame(client.get_order_book(symbol='BTCUSDT'))
k = client.get_historical_klines('BTCUSDT','1m' ,'5 m ago UTC + 05:30')
pd.DataFrame(k)
