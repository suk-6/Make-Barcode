import pandas
from datetime import datetime
from microbit import switch

now = datetime.now()

xlsx = pandas.read_excel("./data.xlsx", names=['ID','NAME','BARCODE'], engine='openpyxl')

barcode_list = xlsx['BARCODE'].values.tolist()

input_code = ""

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
    elif input_code == "exit":
        print("Program Exit")
        break
    else:
        print("등록되지 않은 바코드 : ", input_code)
    