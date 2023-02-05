from binance.spot import Spot
import env
import asyncio
import websockets
import json

api_key = 'dcCdJKk7uG15Q89AvmWMfe1Pt8blK8Pjrnp8MiXOooKWNflaFU0zgVyl1jkbZSby'
api_secret = 'C37slYIfvJB2GqOQQ2uuteyTOFSpz1251JlW8HngphqWxXDsl9OocxKgGLL4Ok73'


client = Spot()
# Get server timestamp
# print(client.time())
# Get klines of BTCUSDT at 1m interval
# print(client.klines("BTCUSDT", "1m"))
# Get last 10 klines of BNBUSDT at 1h interval
# print(client.klines("BTCUSDT", "1h", limit=10))

# api key/secret are required for user data endpoints
client = Spot(env.API_KEY, env.API_SECRET)

# Get account and balance information
# print(client.account())

# Post a new order
# params = {
#     'symbol': 'BTCUSDT',
#     'side': 'SELL',
#     'type': 'LIMIT',
#     'timeInForce': 'GTC',
#     'quantity': 0.00738,
#     'price': 23357
# }

params = {
    'symbol': 'BTCUSDT',
    'side': 'BUY',
    'type': 'LIMIT',
    'timeInForce': 'GTC',
    'quantity': 0.00738,
    'price': 23018
}

try:
    # response = client.new_order(**params)
    # print(client.coin_info(**params))
    print('success')
except:
    print('fail')

# client.cancel_open_orders("BTCUSDT")

# try:
#     client.get_open_orders("BTCUSDT")
#     print('here')
# except:
#     print('nothing open')

# print(k)

# snap  = client.account_snapshot('SPOT')
# print(json.dumps(snap,sort_keys=True, indent=4))


# print(json.dumps(client.asset_detail(),sort_keys=True, indent=4))
# print(json.dumps(client.coin_info(),sort_keys=True, indent=4)) # not reqd
print(json.dumps(client.user_asset(),sort_keys=True, indent=4))  # coin balance