# -*- coding: utf-8 -*-

import sys

import logging
import logging.handlers
from datetime import datetime
from logging.handlers import RotatingFileHandler

file_name = 'RESTful'


def Create_Logger():
    # 오늘 날짜 시 분 초 로그 저장
    #today_date = datetime.today().strftime('%Y-%m-%d %H_%M_%S')
    today_date = datetime.today().strftime('%Y%m%d')

    # logger 인스턴스를 생성 및 로그 레벨 설정
    log = logging.getLogger('TEST_LOGGER.')
    log.setLevel(logging.DEBUG)

    if log.hasHandlers():
        for hdlr in log.handlers:
            log.removeHandler(hdlr)

    if len(log.handlers) > 0:
        return log  # Logger already exists

    # formatter 생성
    # formatter = logging.Formatter('[ %(levelname)-10s | %(filename)s: %(lineno)s\t\t] %(asctime)s > %(message)s')
    formatter = logging.Formatter('[%(levelname)s|%(filename)s:%(lineno)s] %(asctime)s > %(message)s')

    Log_File_Size = 10*1024*1024
    # 스트림 / 파일 로그 출력 핸들러
    # fileHandler = RotatingFileHandler('/ES/ES_UnCopy_Detection/log/'  + str('log_' + today_date) + '.log', mode='a', maxBytes=Log_File_Size, backupCount=5, encoding=None, delay=0)
    fileHandler = RotatingFileHandler('app_log.log', mode='a', maxBytes=Log_File_Size, backupCount=10, encoding=None, delay=0)
    streamHandler = logging.StreamHandler()
    streamHandler.setLevel(logging.DEBUG)

    # 스트림 / 파일 로그 출력 핸들러 + formatter
    fileHandler.setFormatter(formatter)
    streamHandler.setFormatter(formatter)

    log.propagate = False

    # logger 인스턴스 + 핸들러
    log.addHandler(fileHandler)
    log.addHandler(streamHandler)

    return log