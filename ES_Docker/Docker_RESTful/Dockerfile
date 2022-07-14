
#https://basketdeveloper.tistory.com/66

# pigar -p ./requirements.txt -P ./

# Flask-RESTful is an extension for Flask that adds support for quickly building REST APIs.
# Flask-RESTful encourages best practices with minimal setup.
# If you are familiar with Flask, Flask-RESTful should be easy to pick up.

# Swagger allows you to describe the structure of your APIs so that machines can read them.
# By reading the API structure, Swagger can automatically build beautiful and interactive API documentation
# and also generates client libraries for the API in many languages.
# Swagger does this by asking your API to return a YAML or JSON that contains a detailed description of your entire API.
# This file is essentially a resource listing of your API which adheres to OpenAPI Specification.

# Dockerfile Build
FROM python:3.9.7
ENV PYTHONUNBUFFERED 1
RUN python -m pip install --upgrade pip
COPY requirements.txt /
# RUN pip3 uninstall -r /requirements.txt -y
RUN pip3 install -r /requirements.txt
# COPY . /app
COPY . /ES_Docker_RESTful
# COPY /Users/euiyoung.hwang/ES/Python_Workspace/ES_Docker/Docker_REST/ /app
WORKDIR /ES_Docker_RESTful
# WORKDIR /app
ENTRYPOINT ["./gunicorn_start.sh"]

# dockerfile 지정
# docker build -f /Users/euiyoung.hwang/ES/Python_Workspace/ES_Docker/Docker_RESTful/Dockerfile/Dockerfile -t flaskrest/swagger .
# docker build -t flaskrest/swagger .

# docker run --name flask_web_api -p 8003:8003 flaskrest/swagger
# docker run --name flask_web_api -e PYTHONUNBUFFERED=1 -p 9001:1237 flaskrest/swagger
# external connect test
# docker run --name flask_web_api -p 9001:1237 flaskrest/swagger --add-host host.docker.internal:host-gateway
# docker run --name flask_web_api -e PYTHONUNBUFFERED=1 -p 9001:1237 flaskrest/swagger --add-host host.docker.internal:host-gateway

# curl localhost:8003 -> Hello world!