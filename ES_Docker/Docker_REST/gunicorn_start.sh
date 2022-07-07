#!/bin/sh
#gunicorn --chdir app main:app -w 2 --threads 2 -b 0.0.0.0:8000
gunicorn REST_Flask:app -w 2 --threads 2 -b 0.0.0.0:8003
#python -m gunicorn REST_Flask:app -w 2 --threads 2 -b 0.0.0.0:8003
#python -m gunicorn --chdir /Users/euiyoung.hwang/ES/Python_Workspace/ES_Docker/Docker_REST  REST_Flask:app -w 2 --threads 2 -b 0.0.0.0:8003
