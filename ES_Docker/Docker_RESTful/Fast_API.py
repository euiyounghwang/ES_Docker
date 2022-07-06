# FastAPI is a modern, fast (high-performance), web framework for building APIs
# # with Python 3.6+ based on standard Python type hints.

# I am going to use Pipenv for setting up the development environment for our APIs.
# Pipenv makes it easier to isolate your development environment irrespective of what things are installed on your machine
# pip install pipenv

# uvicorn REST_Flask:app --host 0.0.0.0 --port 1234

from fastapi import FastAPI
import datetime

app = FastAPI()

@app.get("/")
def home():
    return {"Hello": "FastAPI"}

