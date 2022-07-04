# ES_Docker
initiial ES_Docker

*Create a Running Docker Container With Gunicorn and Flask**  


```
from flask import Flask
app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return 'Hello world!'

```




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
