import requests
import json

data = {
    'Account': "admin2",
    'Password': "e10adc3949ba59abbe56e057f20f883e",
    'loginDevice': "1"
}
# python数据类型转换为json类型（json.dumps()）
para = json.dumps(data)
# 如果请求头为'Content-Type':'application/json;charset=utf-8'须加上headers，或把data=data改成json=data
headers = {'Content-Type': 'application/json;charset=utf-8'}
# s = requests.session()
r = requests.post(url='http://huineng-test.yunext.com/app/login', data=para, headers=headers)
# 响应的json数据转换为可被python识别的数据类型
json_r = r.json()
print(json_r)
print(r.code)
