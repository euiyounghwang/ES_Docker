
# https://betterprogramming.pub/create-a-running-docker-container-with-gunicorn-and-flask-dcd98fddb8e0
# gunicorn REST_Flask:app -w 2 --threads 2 -b 0.0.0.0:8000
# pigar export
# pigar -p ./requirements.txt - P ./

import datetime
from flask import Flask
import sys

# sys.path.append('/Users/euiyoung.hwang/ES/Python_Workspace/')
# import ES_Docker.Docker_REST.lib.Utils.Util as Util

import lib.Utils.Util as Util

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    print(Util.bcolors().BOLD + str(datetime.datetime.now()) + ' >> WebServices Started..' + Util.bcolors().ENDC)
    return 'Hello world!'



if __name__ == '__main__':

    # /ES/Python_Install/bin/python3.5 /ES/ES_UnCopy_Detection/WebService/REST_API.py 7091 prd
    app.config['JSON_AS_ASCII'] = False
    app.secret_key = 'super secret key'
    # app.secret_key = 'st'
    app.permanent_session_lifetime = datetime.timedelta(minutes=3)

    # app.run(debug=False, host='0.0.0.0', port=int(sys.argv[1]), threaded = True)
    app.run(debug=True, host='0.0.0.0', port=8001, threaded=True)


