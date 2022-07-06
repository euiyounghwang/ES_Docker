# -*- coding: utf-8 -*-

# gunicorn REST_API_Flask:app -w 2 --threads 2 -b 0.0.0.0:8000

# pip install -U flask-restful
# pip install -U flask-apispec

# pigar export
# pigar -p ./requirements.txt -P ./ -y

import datetime
from flask import Flask, Response, request, redirect, url_for, session, abort, render_template, logging, session, redirect, jsonify
from flask_cors import CORS
from flask_restplus import Resource, Api, reqparse, fields
import jinja2
import copy

# import sys
#
# sys.path.append('/Users/euiyoung.hwang/ES/Python_Workspace/')

import lib.Utils.Util as Utils
import CODE.REST_CODE as CODE
import lib.Logging.Logging as log

app = Flask(__name__)  # Flask app instance initiated

# cors
cors = CORS(app)

my_loader = jinja2.ChoiceLoader([
    app.jinja_loader,
    jinja2.FileSystemLoader('/WebService/templates'), ])
app.jinja_loader = my_loader


api = Api(app=app, version="1.0", default='Swagger-UI', title="Swagger-UI Manger Service", description="Swagger-UI")
model = api.model(
    'Swagger-UI Model',
    {
        'key': fields.String(required=True, example="0900", description="KEY", help="KEY"),
        'company_code': fields.String(required=True, example="30", description="company_code of the model", help="회사코드"),
        'loginId': fields.String(required=True, example="pd292816", description="loginId of the Model", help="로그인ID")
     }
)

log = log.Create_Logger()

@api.route('/interface')
class ModelLoading_Detect_Docuemt_Text_Interface(Resource):
    """
    def get(self):
        '''
        사용자가 보낸 parameter를 통해
        데이터를 보내줍니다.
        :return:
        '''
        return {'msg': 'GET Method Called..whgt'}
    """

    @api.expect(model)
    @api.response(200, 'Run successfully created.')
    def post(self):
        '''
        :return: JSON
        '''

        result = []
        Delay_Time = ''
        StartTime = ''
        EndTime = ''

        try:
            StartTime = datetime.datetime.now()

            print('\n' * 1)
            print(Utils.bcolors().BOLD + '*' * 80)
            print(StartTime, ' : [HTTP REQEUST] REST_API_Flask.py Interface')
            print('# ' + str(request.base_url))
            print('*' * 80 + Utils.bcolors().ENDC)

            parser = reqparse.RequestParser()

            # 쿼리 ID : 예) UUID 외
            # 쿼리 ID : 예) UUID 외
            parser.add_argument('key', required=True, type=str, help='string: unId')
            parser.add_argument('company_code', required=True, type=str, help='string: unId')
            parser.add_argument('loginId', required=True, type=str, help='string: unId')

            args = parser.parse_args()

            log.info('\n\nrequest.get_json() >> ' + str(request.get_json()))

            for key, value in args.items():
                log.info('Predict::post In [' + key + '] -> ' + str(value))

            # **********************************************
            # **********************************************

            EndTime = datetime.datetime.now()

            Runing_Time_Gap = str((EndTime - StartTime).seconds) + '.' + str((EndTime - StartTime).microseconds)[:2]
            Delay_Time = Runing_Time_Gap

            # return jsonify(Reponse_Array_Json)
            RESPONSE_SCHEME = CODE.RESPONSE_SCHEME
            return jsonify(RESPONSE_SCHEME)

        except Exception as e:
            response = copy.deepcopy(CODE.RESPONSE_SCHEME)
            # response['STATUS'] = CODE.STATUS_EXCEPTION
            response['CODE'] = CODE.CODE_EXCEPTION
            response['MESSAGE'] = str(e)
            # print(e)
            # print('\n@@@@@@Error@@@@', e, Session_Object.global_session_user_dic['group_key'])
            log.error(str(e))

            print(Utils.bcolors().BOLD + '\n- HTTP REQUEST SLACK Alert {} >> {}'.format(str(400)))

            return jsonify([response])

        finally:

            Runing_Time_Gap = str((EndTime - StartTime).seconds) + '.' + str((EndTime - StartTime).microseconds)[:2]
            Delay_Time = Runing_Time_Gap

            EndTime = datetime.datetime.now()

            print(Utils.bcolors().BOLD + Utils.bcolors().YELLOW + '\n- HTTP REQUEST Start Time >> {}, HTTP REQUEST End Time >> {}'.format(StartTime, EndTime))
            print(Utils.bcolors().BOLD + '- HTTP REQUEST Running Time >> {} ({} Seconds)'.format(EndTime - StartTime, Delay_Time))
            print(Utils.bcolors().ENDC)



if __name__ == '__main__':

    # /ES/Python_Install/bin/python3.5 /ES/ES_UnCopy_Detection/WebService/REST_API.py 7091 prd
    app.config['JSON_AS_ASCII'] = False
    app.secret_key = 'super secret key'
    # app.secret_key = 'st'
    app.permanent_session_lifetime = datetime.timedelta(minutes=3)

    # app.run(debug=False, host='0.0.0.0', port=int(sys.argv[1]), threaded = True)
    app.run(debug=True, host='0.0.0.0', port=8001, threaded=True)