import requests
import json

# data = {"uid" : "dycni", "upw" : "c4ca4238a0b923820dcc509a6f75849b"}
# header = {
#     'Referer':'https://localhost/',
#     'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:63.0) Gecko/20100101 Firefox/63.0'
# }

# session = requests.Session()

# login = session.post("http://localhost/login.do",headers=header ,data=data)

# if login.status_code == 200:
#     report_data = {"sl_id": "0", "equip":"ALL","equip_sel":"0","report_type":"m","data_type":"60","sdate":"2022-07-19","edate":"2022-07-19"}
#     main = session.post("http://localhost/getReport.do",data=report_data)
#     _data = json.loads(main.text)
#     print(_data)

########## 위에는 로그인이 필요한 경우 
session = requests.Session()

test = session.get("http://localhost/test")
print(test.text)






