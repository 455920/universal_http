import requests
from app.conf.global_config import g_conf

host = g_conf["server"]["host"]
port = g_conf["server"]["port"]

# 测试file demo
url = "http://" + host + ":" + str(port) + "/file/md5"
rsp = requests.get(url)
print(rsp.text)

# 测试main demo
url = "http://" + host + ":" + str(port) + "/?name=123&number=456"
rsp = requests.get(url)
print(url)
print(rsp.text)

# 测试user demo
url = "http://" + host + ":" + str(port) + "/user/reg"
rsp = requests.get(url)
print(rsp.text)
