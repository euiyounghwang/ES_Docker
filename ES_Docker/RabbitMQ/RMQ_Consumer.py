import pika, socket
import datetime

q_name = 'euiyoung.hwang.queue'

credentials = pika.PlainCredentials('guest', 'guest')
hostname = socket.gethostname()
parameters = pika.ConnectionParameters(host="localhost",
port=5672, virtual_host='/', credentials=credentials)

connection = pika.BlockingConnection(parameters)
channel = connection.channel()

channel.queue_declare(queue=q_name)

def callback(ch, method, properties, body):
    body = str(body).replace("b", "")
    print("{} Received : {}".format(datetime.datetime.now(), body))
    channel.basic_ack(method.delivery_tag)

channel.basic_consume(queue=q_name, on_message_callback=callback,
auto_ack=False)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
