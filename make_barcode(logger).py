import pandas
from datetime import datetime
from microbit import switch
import logging

# 로그 생성
logger = logging.getLogger()

# 로그의 출력 기준 설정
logger.setLevel(logging.INFO)

# log 출력 형식
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

# log 출력
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)

# log를 파일에 출력
file_handler = logging.FileHandler('access.log')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

code = ""
command = ""

#관리자 암호 불러오기
key_file = open("./private/key", "r");
key = key_file.read()
key_file.close()
    
while True:
    code = input("code: ")
    if code.startswith(('S')):
        logger.info("Access: {code}")
        switch(1)
    elif code == key:
        logger.info("Admin Access")
        switch(1)
        while True:
            command = input("command: ")
            if command == "open":
                logger.info("Open Door")
                switch(1)
                break
            elif command == "exit":
                break
    else:
        logger.info("Unregistered code: {code}")