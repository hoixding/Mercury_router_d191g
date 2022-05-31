import json
import requests

#set admin password
headers = {
    "Host": "192.168.0.1",
    "Connection": "keep-alive",
    "Accept": "*/*",
    "Origin": "http://192.168.0.1",
    "X-Requested-With": "XMLHttpRequest",
    "Content-Type": "application/json",
    "Referer": "http://192.168.0.1/",
    "Accept-Encoding": "gzip, deflate, br"
}
data = json.dumps({"method":"do","set_password":{"password":"*********"}})
url = 'http://192.168.0.1/'
resp = requests.post(url, headers=headers, data=data)
dict = json.loads(resp.content.decode('utf-8'))
stok=dict.get('stok')
#ds url
url = 'http://192.168.0.1/stok='+stok+'/ds'

#get connect html
r=requests.get('http://192.168.0.1/stok='+stok+'/pc/Content.htm')
#get set PPPoE html
r=requests.get('http://192.168.0.1/stok='+stok+'/pc/WizardPPPoE.htm')
#set PPPoE account
data = json.dumps({"protocol":{"wan":{"wan_type":"pppoe"},"pppoe":{"username":"******","password":"******"}},"method":"set"})
resp = requests.post(url, headers=headers, data=data)
dict = json.loads(resp.content.decode('utf-8'))
if dict.get('error_code')==0:
    print('ok')
else:
    print('error'+dict.get('error_code'))
#get end html
r=requests.get('http://192.168.0.1/stok='+stok+'/pc/WizardEnd.htm')
#set fact
data = json.dumps({"system":{"sys":{"is_factory":"0"}},"method":"set"})
resp = requests.post(url, headers=headers, data=data)
#set wlan
data = json.dumps({"wireless":{"wlan_host_2g":{"ssid":"***","key":"***","encryption":"1"},"wlan_bs":{"bs_enable":"0"},"wlan_host_5g":{"ssid":"***","key":"***","encryption":"1"}},"method":"set"})
resp = requests.post(url, headers=headers, data=data)


