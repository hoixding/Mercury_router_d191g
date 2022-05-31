import json
import urllib

import requests

post_headers = {
    "Host": "192.168.0.1",
    "Connection": "keep-alive",
    "Accept": "*/*",
    "Origin": "http://192.168.0.1",
    "X-Requested-With": "XMLHttpRequest",
    "Content-Type": "application/json",
    "Referer": "http://192.168.0.1/",
    "Accept-Encoding": "gzip, deflate, br"
}
data = json.dumps({"method":"do","login":{"password":"**********"}})
url = 'http://192.168.0.1/'
resp = requests.post(url, headers=post_headers, data=data)
# 获取服务器状态响应
print(resp.text)
dict = json.loads(resp.content.decode('utf-8'))
stok=dict.get('stok')
url = 'http://192.168.0.1/stok='+stok+'/pc/WizardEnd.htm'

#print(request.text)
r=requests.get(url)
print(r.text)