import pika, json
from src.settings import AMQP_URL

params = pika.URLParameters(AMQP_URL)

connection = pika.BlockingConnection(params)

channel = connection.channel()


def publish(method, body) -> None:
    properties = pika.BasicProperties(method)
    channel.basic_publish(
        exchange="", routing_key="product", body=json.dumps(body), properties=properties
    )
