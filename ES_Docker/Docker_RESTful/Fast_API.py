# FastAPI is a modern, fast (high-performance), web framework for building APIs
# # with Python 3.6+ based on standard Python type hints.

# I am going to use Pipenv for setting up the development environment for our APIs.
# Pipenv makes it easier to isolate your development environment irrespective of what things are installed on your machine

# pip install pipenv
# pip install "uvicorn[standard]" gunicorn

# uvicorn REST_Flask:app --host 0.0.0.0 --port 1234
import uvicorn
from fastapi import FastAPI
import datetime

import lib.Logging.Logging as log

app = FastAPI()
log = log.Create_Logger()

# http://127.0.0.1:1235/hello?self=World
class Hello(str):
    @app.get("/hello")
    def hello(self):
        return {"Hello": self}
1
@app.get("/")
def home():
    log.info(str(datetime.datetime.now()) + ' >> WebServices Started..')
    return {"Hello": "FastAPI"}


if __name__ == "__main__":
    uvicorn.run("Fast_API:app", host="127.0.0.1", port=1235, log_level="info")