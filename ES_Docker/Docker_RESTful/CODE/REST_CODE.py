
from datetime import datetime

CODE_OK = 200
CODE_NOT_FOUND = 404
CODE_EXCEPTION = 500


STATUS_OK = 'OK'
STATUS_EXCEPTION = 'Internal Server Error'
STATUS_LOCKED = 'Locked'


# 최종리턴값
# RESULT_CODE
# {
#     '201' : 'PATTERN_OK'
#     '401' : 'PATTERN NO'
# }
RESPONSE_SCHEME = {
    'CURRENT_ELAPSED_TIME': 0.0,
    'REQUEST_TIME' : 0.0,
    'RESPONSE_TIME' : 0.0,
    # 'STATUS': STATUS_OK,
    'PATTERN_STATUS' : '',
    'RESPONSE_CODE': CODE_OK,
    'DATA': {
        "total": 2,
        "hits": [
            {
                "_source": {
                    "ACCURACY": 0.975189209,
                    'TRANSACTION_ID': '',
                    'SUGGESTION_NUMBER' : '',
                    'PROPOSE_NM' : '',
                    'SUGGESTION_TYPE': '',
                    'FULL_NAME1': '',
                    'ORGANIZATION_NAME1': '',
                    'SUGGESTION_DATE': ''
                }
            },
            {
                "_source": {
                    'ACCURACY': 0.975189209,
                    'TRANSACTION_ID': '',
                    'SUGGESTION_NUMBER' : '',
                    'PROPOSE_NM' : '',
                    'SUGGESTION_TYPE': '',
                    'FULL_NAME1': '',
                    'ORGANIZATION_NAME1': '',
                    'SUGGESTION_DATE': ''
                }
            }
        ]
    }
}
