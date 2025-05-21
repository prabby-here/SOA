import pika
import time
import json
import logging

logging.basicConfig(level=logging.INFO)

def connect_with_retry(retries=10, delay=3):
    for i in range(retries):
        try:
            return pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        except pika.exceptions.AMQPConnectionError:
            logging.warning(f"Connection failed, retrying in {delay} seconds...")
            time.sleep(delay)
    raise Exception("Could not connect to RabbitMQ after several retries.")

def publish_message(message):
    connection = connect_with_retry()
    channel = connection.channel()
    channel.queue_declare(queue='orders', durable=True)
    channel.basic_publish(exchange='', routing_key='orders', body=json.dumps(message))
    logging.info(f"Sent message: {message}")
    connection.close()

if __name__ == "__main__":
    message = {
        'event': 'new_order',
        'data': {
            'order_id': 123,
            'customer': 'John Doe',
            'items': ['item1', 'item2']
        }
    }
    publish_message(message)
