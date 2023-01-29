from binance.spot import Spot

api_key = 'dcCdJKk7uG15Q89AvmWMfe1Pt8blK8Pjrnp8MiXOooKWNflaFU0zgVyl1jkbZSby'
api_secret = 'C37slYIfvJB2GqOQQ2uuteyTOFSpz1251JlW8HngphqWxXDsl9OocxKgGLL4Ok73'

client = Spot()
# Get server timestamp
print(client.time())
# Get klines of BTCUSDT at 1m interval
print(client.klines("BTCUSDT", "1m"))
# Get last 10 klines of BNBUSDT at 1h interval
print(client.klines("BNBUSDT", "1h", limit=10))

# api key/secret are required for user data endpoints
client = Spot(api_key, api_secret)

# Get account and balance information
print(client.account())

# Post a new order
params = {
    'symbol': 'BTCUSDT',
    'side': 'BUY',
    'type': 'LIMIT',
    'timeInForce': 'GTC',
    'quantity': 0.002,
    'price': 9500
}

response = client.new_order(**params)
print(response)