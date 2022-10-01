"""
Proxy service to send REST calls to Kafka
"""

import json
from flask import Flask, request
from kafka import KafkaProducer

app = Flask(__name__)
producer = KafkaProducer(bootstrap_servers='localhost:9092', value_serializer=lambda v: json.dumps(v).encode('utf-8'))

@app.route('/', methods=['PUT'])
def route_data():
    record = json.loads(request.data)
    producer.send('clickstream', record)
    print(record, flush=True)
    return '',200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)