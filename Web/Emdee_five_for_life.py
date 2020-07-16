import requests
import hashlib

try:
    from BeautifulSoup import BeautifulSoup
except ImportError:
    from bs4 import BeautifulSoup


URL = "http://docker.hackthebox.eu:32304"
r=requests.session()

req = r.get(url=URL)
html = BeautifulSoup(req.content)
str_value = html.body.h3.text
payload = {'hash': hashlib.md5(str_value.encode('utf-8')).hexdigest()}

res = r.post(URL, data=payload)
html = BeautifulSoup(res.content)
print(html.body.p.text)
