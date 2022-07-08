
# import sys
# sys.path.append('/TOM/ES/')
# sys.path.append('/ES/')


import socket
import json

class SOCKET_JSON:
    """
    UDP SOCKET with Logstsh
    """

    socket_logstash_dict = {}

    def socket_json_push(self, key, value):
         if key not in self.socket_logstash_dict.keys():
            self.socket_logstash_dict[key] = value
            # self.socket_logstash_dict[key].append(value)
            # del (self.socket_logstash_dict[key][0])


    def get_socket_json_pop(self):
        return self.socket_logstash_dict


class TCP_SOCKET:
    """
    TCP SOCKET with Logstsh
    """
    def __init__(self, ip, port):
        self.target_server_ip = ip
        self.socket_port = port
        self.TCPClientSocket = None


    def Connect(self):
        self.TCPClientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.TCPClientSocket.connect((self.target_server_ip, self.socket_port))


    def socket_logstash_handler(self, message):
        """

        :param message:
        :return:
        """
        # print("Socket Message Send..." + str(message))
        # message = '{"create_date" : "SNTC2020021821575900000004", "request_server_ip" : "127.0.0.1", "system_id":"law", "company_code" : "30"}'
        # message = '{create_date : SNTC2020021821575900000004, request_server_ip : 127.0.0.1, key : doc0900bf4b9ef20165, company_code : 30, system_id : law, login_id : euiyoung.hwang, Sentence : 배가스 조건 및 조성 . Parameters 포 항. 75MW 100MW. Gas Flow Nhr wet 345000 588000. Temperature 3, Predict : __label__pos, Percent: 0.999}'
        self.TCPClientSocket.send(json.dumps(message, ensure_ascii=False).encode())

    def Close(self):
        self.TCPClientSocket.close()
        # log.info('Socket Closed')
        # print('Socket Closed')



class UDP_SOCKET:
    """
    UDP SOCKET with Logstsh
    """

    def __init__(self, ip, port):
        self.target_server_ip = ip
        self.socket_port = port

    def socket_logstash_handler(self, message):
        # print('@@socket_logstash_handler@@', message)
        UDPClientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        # UDPClientSocket.connect((self.target_server_ip, self.socket_port))
        # UDPClientSocket.send(json.dumps(message, ensure_ascii=False).encode("utf8")) # we must encode the string to bytes\
        UDPClientSocket.sendto(json.dumps(message, ensure_ascii=False).encode("utf8"),
                               (self.target_server_ip, self.socket_port))

        # UDPClientSocket.send(message.encode("utf8")) # we must encode the string to bytes\
        # UDPClientSocket.close()
        # log.info('Socket Closed')


if __name__ == '__main__':

    # SOCKET_SERVER_IP = "127.0.0.1"
    # SOCKET_SERVER_IP = "10.132.11.134"
    # SOCKET_SERVER_IP = "10.132.17.188"
    SOCKET_SERVER_IP = "127.0.0.1"
    # SOCKET_SERVER_IP = "10.132.17.189"

    """
    SOCKET_JSON().socket_json_push('create_date', 'SNTC2020021821575900000004')
    SOCKET_JSON().socket_json_push('request_server_ip', '127.0.0.1')
    print('\n', SOCKET_JSON().get_socket_json_pop())
    """

    # TCP_SOC = TCP_SOCKET(SOCKET_SERVER_IP, 5958)\
    #     .socket_logstash_handler(SOCKET_JSON().get_socket_json_pop())

    # message = "{'create_date' : 'SNTC2020022813562500000003', 'request_server_ip' : '172.31.245.94', 'key' : 'doc0900bf4b9ef20165', 'company_code' : '30', 'system_id' : 'law', 'login_id' : 'euiyoung.hwang', 'Sentence' : '본 계약은 포스코의 마그네슘제련공장 등 위탁설비이하 위탁설비의 운영 가동 및 유지 보전에 필요한 일상점검 정기점검 수리 등 위탁업무 전반에 대해 포스코와 수탁운영사간의 상호 역할과 책임 사고발생시 대응책임과 손해배상 생산성 향상을 위한 성과보상의 범위에 관하여 규정한다..', 'Predict' : '__label__pos', 'Percent': '1.0'}"
    """
    ai_server_log_dic = {
        "TYPE" : "AI_JEAN_LOG",
        "CHAIN_CODE" : "U40A",
        "LOG_LEVEL": "INFO",
        'SSO_EMP_NO': ''.join(('pd292816',)),
        "LOG_TEXT" : "page_num:1,company_code:30,docTitle:Sample.pptx,key:doc0900bf4b9ef20165,page_size:50,loginId:pd292816,predict_sentence:,version:0900bf4b9fca1180,"
    }
    for loop in range(0, 1):
        # message ="create_date : SNTC2020022813562500000003, request_server_ip : 172.31.245.94, key : doc0900bf4b9ef20165, company_code : 30, system_id : law, login_id : euiyoung.hwang, Sentence : 본 계약은 포스코의 마그네슘제련공장 등 위탁설비이하 위탁설비의 운영 가동 및 유지 보전에 필요한 일상점검 정기점검 수리 등 위탁업무 전반에 대해 포스코와 수탁운영사간의 상호 역할과 책임 사고발생시 대응책임과 손해배상 생산성 향상을 위한 성과보상의 범위에 관하여 규정한다.., Predict : __label__pos, Percent: 1.0"
        # message = "page_num:1,company_code:30,docTitle:Sample.pptx,key:doc0900bf4b9ef20165,page_size:50,loginId:pd292816,predict_sentence:,version:0900bf4b9fca1180,"
        # UDP_SOC = UDP_SOCKET(SOCKET_SERVER_IP, 6959)\
        #     .socket_logstash_handler(ai_server_log_dic)
        TCP_SOC = TCP_SOCKET(SOCKET_SERVER_IP, 5958)
        TCP_SOC.Connect()
        TCP_SOC.socket_logstash_handler(ai_server_log_dic)
        TCP_SOC.Close()

        print('\nSEND..')
    """
    from datetime import datetime
    START_DATE = datetime.now()
    END_DATE = datetime.now()

    # Monitoring
    ai_server_log_dic = {
        "TYPE": "AI_JEAN_MODEL",
        "START_DATE": START_DATE.strftime("%Y-%m-%d %H:%M:%S"),
        "END_DATE": END_DATE.strftime("%Y-%m-%d %H:%M:%S"),
        "LOG_LEVEL": "INFO",
        "LOG_TEXT" : "MODEL_UPGRADE",
        "STATUS" : 200
    }
    for loop in range(0, 4):
        # UDP_SOC = UDP_SOCKET(SOCKET_SERVER_IP, 5959).socket_logstash_handler(ai_server_log_dic)
        # print(loop)
        TCP_SOC = TCP_SOCKET(SOCKET_SERVER_IP, 5958)
        TCP_SOC.Connect()
        print(json.dumps(ai_server_log_dic, indent=4))
        TCP_SOC.socket_logstash_handler(ai_server_log_dic)
        TCP_SOC.Close()
