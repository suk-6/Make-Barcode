import pandas
from datetime import datetime
from microbit import switch

now = datetime.now()

xlsx = pandas.read_excel("./data.xlsx", names=['ID','NAME','BARCODE'], engine='openpyxl')
barcode_list = xlsx['BARCODE'].values.tolist()

input_code = ""
input_command = ""

sec = True

#command
add_ID = ""
add_NAME = ""
add_BARCODE = ""

#관리자 암호 불러오기
admin_file = open("../Barcode_2_private/admin_key.txt", "r");
admin_key = admin_file.read()
admin_file.close()

def reload():
    xlsx = pandas.read_excel("./data.xlsx", names=['ID','NAME','BARCODE'], engine='openpyxl')
    barcode_list = xlsx['BARCODE'].values.tolist()
    print("reload Success")

def user_add(add_ID, add_NAME, add_BARCODE):
    out = xlsx.values.tolist()
    out.append([add_ID, add_NAME, add_BARCODE])
    df = pandas.DataFrame(out, columns=['ID', 'NAME', 'BARCODE'])
    df.to_excel('./data.xlsx', index=False)
    
reload()
    
while True:
    input_code = input("code: ")
    if input_code in barcode_list:
        export_data = xlsx[xlsx['BARCODE'] == input_code]
        export1 = export_data.head()
        export = export1.values
        time_now = now.strftime('%Y-%m-%d %H:%M:%S')
        print("출입 허가 : ", export)
        print("출입 시각 : ", time_now)
        switch(1)
    elif input_code == admin_key:
        while True:
            input_command = input("command: ")
            if input_command == "add":
                add_ID = input("ID: ")
                add_NAME = input("NAME: ")
                add_BARCODE = input("BARCODE: ")
                user_add(add_ID, add_NAME, add_BARCODE)
                reload()
                print("Success!")
            elif input_command == "open":
                switch(1)
                time_now = now.strftime('%Y-%m-%d %H:%M:%S')
                print("관리자 출입")
                print("출입 시각 : ", time_now)
                break
            elif input_command == "sec":
                if sec is True:
                    sec = False
                    print("보안 해제")
                elif sec is False:
                    sec = True
                    print("보안 중")
                break
            elif input_command == "reload":
                reload()
                print("User data Reload")
                break
            elif input_command == "exit":
                print("Logout")
                break
    elif input_code == "exit":
        print("Program Exit")
        break
    else:
        if sec is False:
            switch(1)
            time_now = now.strftime('%Y-%m-%d %H:%M:%S')
            print("허가되지 않은 사용자 출입")
            print("출입 시각 : ", time_now)
        elif sec is True:
            time_now = now.strftime('%Y-%m-%d %H:%M:%S')
            print("등록되지 않은 바코드 : ", input_code)
            print("인식 시각 : ", time_now)