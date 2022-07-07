
# pip install "uvicorn[standard]" gunicorn

import uvicorn
from fastapi import FastAPI, APIRouter

# uvicorn main:app --reload --host=0.0.0.0 --port=80 --workers=4
# uvicorn Fast_Class_API:app --host 0.0.0.0 --port 1236
# Python Path with --app-dir
# uvicorn --app-dir /Users/euiyoung.hwang/ES/Python_Workspace/ES_Docker/Docker_RESTful Fast_Class_API:app --host 0.0.0.0 --port 1236

class Hello:
    """
    async def vs def feature's difference
    """
    def __init__(self, name: str):
        self.name = name
        self.router = APIRouter()
        self.router.add_api_route("/", self.main, methods=["GET"])
        self.router.add_api_route("/hello", self.hello, methods=["GET"])

    def main(self):
        return {"main": self.name}

    def hello(self):
        return {"Hello": self.name}


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
    uvicorn.run("Fast_Class_API:app", host="127.0.0.1", port=1236, log_level="info")