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

def callback(ch, method, properties, body):
    message = json.loads(body)
    logging.info(f"Received message: {message}")

def consume_messages():
    connection = connect_with_retry()
    channel = connection.channel()
    channel.queue_declare(queue='orders', durable=True)
    channel.basic_consume(queue='orders', on_message_callback=callback, auto_ack=True)
    logging.info("Waiting for messages. To exit press CTRL+C")
    channel.start_consuming()  # This keeps the consumer running!

if __name__ == "__main__":
    consume_messages()
