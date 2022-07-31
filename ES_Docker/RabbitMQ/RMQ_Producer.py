import pika, socket
import uuid

q_name = 'euiyoung.hwang.queue'

credentials = pika.PlainCredentials('guest', 'guest')
hostname = socket.gethostname()
parameters = pika.ConnectionParameters(host="localhost",
port=5672, virtual_host='/', credentials=credentials)

connection = pika.BlockingConnection(parameters)
channel = connection.channel()

msg_props = pika.BasicProperties()
msg_props.content_type = "text/plain"
msg = str(uuid.uuid1()) + 'Hello World!'
channel.queue_declare(queue=q_name)
if channel.basic_publish(exchange='', routing_key=q_name, body=msg , properties=msg_props):
     print("Message Acknowledged")
# else:
#      print("Message Lost")

print("[{}] Sent..'".format(msg))
connection.close()