import json

import pika, socket
import uuid

def start_rmq_handler(q_name, id, password, hosts="localhost"):

    try:
        credentials = pika.PlainCredentials(id, password)
        hostname = socket.gethostname()
        parameters = pika.ConnectionParameters(host=hosts,
        port=5672, virtual_host='/', credentials=credentials)

        connection = pika.BlockingConnection(parameters)
        channel = connection.channel()

        msg_props = pika.BasicProperties()

        # msg_props.content_type = "text/plain"
        # msg = str(uuid.uuid1()) + 'Hello World!'

        msg_props.content_type = "application/json"
        # SEARCH-199: Add 'Delete /omni/entity/{entityId}' endpoint with param
        json_msg = {
            "entity_id" : "kraken_document-289857"
        }
        # Add 'Delete /omni/delete/entity' endpoint with json
        # json_msg = {
        #     'entity_type': 37,
        #     'id' : '289857'
        # }
        msg = json.dumps(json_msg)
        # msg_props.content_type = "application/json"
        # msg = {"entity_id" : "kraken_document-289857"}
        channel.queue_declare(queue=q_name, durable=True)
        channel.basic_publish(exchange='', routing_key=q_name, body=msg , properties=msg_props)

        print("[{}] Sent..'".format(msg))

    finally:
        connection.close()

login = ['guest', 'guest']
start_rmq_handler('omnisearch_deleting', login[0], login[1])