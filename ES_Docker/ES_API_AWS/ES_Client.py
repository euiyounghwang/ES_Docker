
# https://elasticsearch-py.readthedocs.io/en/6.8.2/

from datetime import datetime
import elasticsearch
from __future__ import absolute_import
import json

# from elasticsearch import Elasticsearch as elasticsearch7

def es_client_set():
    # es = Elasticsearch()
    es = elasticsearch.Elasticsearch("localhost", http_auth=('elastic', 'gsaadmin'), )
    doc = {
        "author": "kimchy",
        'text': 'Elasticsearch: cool. bonsai cool.',
        'timestamp': datetime.now(),
    }
    res = es.index(index="test-index", doc_type='tweet', id=1, body=doc)
    print(res['result'])




# from elasticsearch import Elasticsearch, RequestsHttpConnection
# from requests_aws4auth import AWS4Auth
#
# host = 'YOURHOST.us-east-1.es.amazonaws.com'
# awsauth = AWS4Auth(YOUR_ACCESS_KEY, YOUR_SECRET_KEY, REGION, 'es')
#
# es = Elasticsearch(
#     hosts=[{'host': host, 'port': 443}],
#     http_auth=awsauth,
#     use_ssl=True,
#     verify_certs=True,
#     connection_class=RequestsHttpConnection
# )
# print(es.info())


if __name__ == '__main__':
    es_client_set()