import requests

url = "http://127.0.0.1:5000/"

rsp = requests.get(url)

print(rsp.text)
