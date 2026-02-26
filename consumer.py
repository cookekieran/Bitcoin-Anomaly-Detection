import json
from kafka import KafkaConsumer

consumer = KafkaConsumer(
    'btc_prices',                    
    bootstrap_servers=['localhost:9092'],
    api_version=(3, 7, 0),            
    auto_offset_reset='latest',
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

print("Consumer started... waiting for prices...")

try:
    for message in consumer:
        data = message.value
        price = data['price']
        timestamp = data['timestamp']
        
        print(f"Caught Price: {price} (at {timestamp})")
        
except KeyboardInterrupt:
    print("Stopping consumer...")
finally:
    consumer.close()