# Dockerfile Build
FROM python:3.9.7
COPY requirements.txt /
RUN pip3 install -r /requirements.txt
COPY . /app
WORKDIR /app
ENTRYPOINT ["./gunicorn_start.sh"]

# docker build -t flask/hello-world .
# docker run -p 8003:8003 flask/hello-world
# curl localhost:8003 -> Hello world!