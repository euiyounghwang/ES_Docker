# ES_Docker

# Create a Running Docker Container With Gunicorn and Flask


**Create Flask**
```
from flask import Flask
app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return 'Hello world!'

```

**Next, let’s write the command that will run the Gunicorn server:**
```
#!/bin/sh
gunicorn --chdir path main:app -w 2 --threads 2 -b 0.0.0.0:8000
```

The parameters are pretty much self-explanatory: We are telling Gunicorn that we want to spawn two worker processes running two threads each. We are also accepting connections from the outside and overriding Gunicorn’s default port (8000).

**Our basic Dockerfile:**
```
FROM python:3.7.3-slim
COPY requirements.txt /
RUN pip3 install -r /requirements.txt
COPY . /app
WORKDIR /app
ENTRYPOINT ["./gunicorn_starter.sh"]
```

**Let’s build our image:**
```
docker build -t flask/hello-world .
```
**And run:**
```
docker run -p 8003:8003 flask/hello-world
```

**And Test:**
$ curl localhost:8003
Hello world!


**Git Interface:**

```sh
echo "# a" >> README.md
git init
git config --global user.name "euiyoung.hwang"
git config --global user.email marieuig@gmail.com
git status  
git add README.md (OR git add .)  
git commit -m "first commit"  
git branch -M master  
git remote add origin https://github.com/euiyounghwang/a.git  
git push -u origin master  
```
