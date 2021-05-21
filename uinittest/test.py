import requests

# 测试file demo
url = "http://127.0.0.1:5000/file/md5"
rsp = requests.get(url)
print(rsp.text)

# 测试main demo
url = "http://127.0.0.1:5000?name=123&number=456"
rsp = requests.get(url)
print(rsp.text)

# 测试user demo
url = "http://127.0.0.1:5000/user/reg"
rsp = requests.get(url)
print(rsp.text)
