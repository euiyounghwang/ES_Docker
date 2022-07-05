
# pigar -p ./requirements.txt - P ./

# Dockerfile Build
FROM python:3.9.7
COPY requirements.txt /
RUN pip3 install -r /requirements.txt
COPY . /app
# COPY /Users/euiyoung.hwang/ES/Python_Workspace/ES_Docker/Docker_REST/ /app
WORKDIR /app
ENTRYPOINT ["./gunicorn_start.sh"]

# dockerfile 지정
# docker build -f /path/to/a/Dockerfile -t flask/hello-world .
# docker build -t flask/hello-world .

# docker run --name flask_web -p 8003:8003 flask/hello-world
# docker run --name flask_web -e PYTHONUNBUFFERED=1 -p 8003:8003 flask/hello-world

# curl localhost:8003 -> Hello world!