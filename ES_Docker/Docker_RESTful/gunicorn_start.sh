#!/bin/sh
#gunicorn --chdir app main:app -w 2 --threads 2 -b 0.0.0.0:8000
#/Users/euiyoung.hwang/opt/anaconda3/bin/gunicorn REST_API_Flask:app -w 2 --threads 2 -b 0.0.0.0:8004
#gunicorn REST_API_Flask:app -w 2 --threads 2 -b 0.0.0.0:8004
#python ./REST_API_Flask.py
#python -m gunicorn --chdir /Docker_RESTful Fast_Class2_API:app -k uvicorn.workers.UvicornWorker -w 2 --threads 2 -b 0.0.0.0:1237
python -m gunicorn --chdir . Fast_Class2_API:app -k uvicorn.workers.UvicornWorker -w 2 --threads 2 -b 0.0.0.0:1237