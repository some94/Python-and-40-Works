# 사이트에 접속하기 위함
import requests
# IP주소를 찾기 위한 정규식을 사용하기 위함
import re

req = requests.get("http://ipconfig.kr")
out_addr = re.search(r'IP Address : (\d{1,3}\.\d{1.3}\.\d{1.3}\.\d{1.3})', req.text)[1]
print(out_addr)