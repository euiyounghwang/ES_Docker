
# https://tech.madup.com/FastAPI/

from typing import Union

from fastapi import FastAPI, Request
from pydantic import BaseModel
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from pydantic.types import constr, Optional
import uvicorn
import json
import urllib.parse

# pip install "uvicorn[standard]" gunicorn

# uvicorn --app-dir /Users/euiyoung.hwang/ES/Python_Workspace/ES_Docker/Docker_RESTful Fast_Class2_API:app --host 0.0.0.0 --port 1237 --reload
# uvicorn --app-dir /Users/euiyoung.hwang/ES/Python_Workspace/ES_Docker/Docker_RESTful Fast_Class2_API:app --host 0.0.0.0 --port 1237 --reload --workers 4

# python -m gunicorn Fast_Class2_API:app -k uvicorn.workers.UvicornWorker -b 0.0.0.0:1237 --reload
# python -m gunicorn --chdir /Users/euiyoung.hwang/ES/Python_Workspace/ES_Docker/Docker_RESTful Fast_Class2_API:app -k uvicorn.workers.UvicornWorker -w 2 --threads 2 -b 0.0.0.0:1237 --reload

class Item(BaseModel):
    name: str
    # title: constr(max_length=10)
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None
    rating: Optional[str] = None

from lib.Logstash_IF.Logstash_Socket import *
class Logstashs:
    def __init__(self, message):
        self.TCP_SOC = None
        # self.SOCKET_SERVER_IP = '127.0.0.1'
        # Internal docker connect to external host
        self.SOCKET_SERVER_IP = 'host.docker.internal'
        self.TCP_SOC = TCP_SOCKET(self.SOCKET_SERVER_IP, 5958)
        self.TCP_SOC.Connect()
        self.message = message

    def send_socket_msg(self):
        print('Logstash Class -> ', json.dumps(self.message, indent=4))
        self.TCP_SOC.socket_logstash_handler(self.message)
        self.TCP_SOC.Close()

description = """
EUIYOUNG HWANG's app FASTAPI helps you do awesome stuff. 🚀

## Items

You can **read items**.

## Users

You will be able to:

* **Create users** (_not implemented_).
* **Read users** (_not implemented_).
"""

app = FastAPI(
    title="EUIYOUNG HWANG' FastAPI",
    description=description,
    version="0.0.1",
    terms_of_service="http://example.com/terms/",
    contact={
        "name": "Deadpoolio the Amazing",
        "url": "http://x-force.example.com/contact/",
        "email": "dp@x-force.example.com",
    },
    license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    },
)

# old-style
# @app.route("/posts", methods=["POST"])

# new-style (Flask 2.0+)
@app.post("/interface/")
async def create_item(item: Item):
    try:
        print('post -> ', type(item), item)
        print('json - > ', item.json())
        json_results = jsonable_encoder(item)
        # --
        # logstash
        # --
        # Logstashs(json_results).send_socket_msg()
        # return JSONResponse(content=json_results)
        return dict(json_results)
        # print(type(json_results))
        # return item.json()
    finally:
        pass


# --
# Request POST OR GET (Previous METHOD)
@app.post("/interface2")
async def Zero_Shot_Classification(item:Item, request: Request):
    """

    :param item:
    :param request:
    :return:
    """
    # # for value in request.path_params.items():
    # #     print(value)
    # print(request.url.query)
    """
    # Form URL Encoded Method
    # POST q = {'a':1}
    q = await request.body()
    # b'q=%7B%27a%27%3A1%7D'
    # print(q)
    q = str(q).replace('b','')
    q = str(urllib.parse.unquote_plus(str(q))).replace("'", '"')
    # q = "q={"a":1}"
    q = str(q).split("=")
    q = q[1][:-1]
    print(q, json.loads(q))
    return json.loads((q))
    """
    """
    # JSON METHOD
    """
    data = await request.json()
    print(type(data))
    print(data)
    return dict(data)


@app.post("/getInformation")
def getInformation(item : Item):
    return {
        "status" : "SUCCESS",
        "data" : item
    }

if __name__ == "__main__":
    """
    # Python Main
    uvicorn.run(app="main:app", 
                host="0.0.0.0",
                port=80,
                reload=True,
                workers=4) 

    # Command                
    uvicorn main:app --reload --host=0.0.0.0 --port=80 --workers=4
    """
    uvicorn.run("Fast_Class2_API:app", host="127.0.0.1", port=1237, log_level="info", reload=True)