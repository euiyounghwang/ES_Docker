
# pip install "uvicorn[standard]" gunicorn
import json

import uvicorn
from fastapi import FastAPI, APIRouter, Request

from pydantic import BaseModel
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

# uvicorn main:app --reload --host=0.0.0.0 --port=80 --workers=4
# uvicorn Fast_Class_API:app --host 0.0.0.0 --port 1236
# Python Path with --app-dir
# uvicorn --app-dir /Users/euiyoung.hwang/ES/Python_Workspace/ES_Docker/Docker_RESTful Fast_Class_API:app --host 0.0.0.0 --port 1236

# python -m gunicorn Fast_Class_API:app -k uvicorn.workers.UvicornWorker -b 0.0.0.0:1237 --reload
# python -m gunicorn --chdir /Users/euiyoung.hwang/ES/Python_Workspace/ES_Docker/Docker_RESTful Fast_Class_API:app -k uvicorn.workers.UvicornWorker -w 2 --threads 2 -b 0.0.0.0:1237 --reload


class GraphBase(BaseModel):
    sample: str
    # end: str
    # distance: int

from typing import List
class GraphList(BaseModel):
    data: List[GraphBase]


class Hello:
    """
    async def vs def feature's difference
    """
    def __init__(self, name: str):
        self.name = name
        self.router = APIRouter()
        self.router.add_api_route("/", self.main, methods=["GET"])
        self.router.add_api_route("/hello", self.hello, methods=["GET"])
        self.router.add_api_route("/posts1", self.posts_1, methods=["POST"])
        # self.router.add_api_route("/posts2", self.posts_2, methods=["POST"])

    def main(self):
        return {"main": self.name}

    def hello(self):
        return {"Hello": self.name}

    """
    def posts(self, request: Request):
        print('request.headers-> ', request.headers.items())
        print('request.query_params -> ', request.query_params.items())
        return {"Hello": self.name}
        # return {"received_request_body": await request.body()}
    """

    def posts_1(self, request: Request, posts: GraphBase):
        print('request.headers-> ', request.headers.items())
        json_results = jsonable_encoder(posts)
        print('request.body@1 -> ', json.dumps(json_results, indent=4))
        print('request.body@2-> ', json_results)
        return JSONResponse(content=json_results)
        # return {"Hello": posts}

app = FastAPI()
hello = Hello("World")
app.include_router(hello.router)



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
    uvicorn.run("Fast_Class_API:app", host="127.0.0.1", port=1236, log_level="info", reload=True)