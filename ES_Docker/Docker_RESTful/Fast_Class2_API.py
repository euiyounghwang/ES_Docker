
# https://tech.madup.com/FastAPI/

from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
import uvicorn
import json

# pip install "uvicorn[standard]" gunicorn

# uvicorn --app-dir /Users/euiyoung.hwang/ES/Python_Workspace/ES_Docker/Docker_RESTful Fast_Class2_API:app --host 0.0.0.0 --port 1237 --reload
# uvicorn --app-dir /Users/euiyoung.hwang/ES/Python_Workspace/ES_Docker/Docker_RESTful Fast_Class2_API:app --host 0.0.0.0 --port 1237 --reload --workers 4

# python -m gunicorn Fast_Class2_API:app -k uvicorn.workers.UvicornWorker -b 0.0.0.0:1237 --reload
# python -m gunicorn --chdir /Users/euiyoung.hwang/ES/Python_Workspace/ES_Docker/Docker_RESTful Fast_Class2_API:app -k uvicorn.workers.UvicornWorker -w 2 --threads 2 -b 0.0.0.0:1237 --reload

class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None

from lib.Logstash_IF.Logstash_Socket import *
class Logstashs:
    def __init__(self, message):
        self.TCP_SOC = None
        self.SOCKET_SERVER_IP = '127.0.0.1'
        # Internal docker connect to external host
        # self.SOCKET_SERVER_IP = 'host.docker.internal'
        self.TCP_SOC = TCP_SOCKET(self.SOCKET_SERVER_IP, 5958)
        self.TCP_SOC.Connect()
        self.message = message

    def send_socket_msg(self):
        print('Logstash Class -> ', json.dumps(self.message, indent=4))
        self.TCP_SOC.socket_logstash_handler(self.message)
        self.TCP_SOC.Close()


app = FastAPI()


@app.post("/interface/")
async def create_item(item: Item):
    try:
        print('post -> ', type(item), item)
        print('json - > ', item.json())
        json_results = jsonable_encoder(item)
        Logstashs(json_results).send_socket_msg()
        return JSONResponse(content=json_results)
    finally:
        pass


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