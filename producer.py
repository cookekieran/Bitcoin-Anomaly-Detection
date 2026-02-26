import time
import json
import requests
from kafka import KafkaProducer

producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

def get_btc_price():
    url = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"
    response = requests.get(url)
    data = response.json()
    return data['price']

print("Starting BTC Price Stream...")

while True:
    try:
        price = get_btc_price()
        message = {"symbol": "BTC", "price": price, "timestamp": time.time()}
        
        producer.send('btc_prices', message)
        
        print(f"Sent to Kafka: {price}")
        time.sleep(2) # Wait 2 seconds
    except KeyboardInterrupt:
        print("Session interrupted, closing")
        exit()
    except Exception as e:
        print(f"Error: {e}")
        time.sleep(5)