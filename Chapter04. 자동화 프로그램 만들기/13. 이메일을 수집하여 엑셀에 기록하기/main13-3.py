import requests
import re


url = 'https://news.v.daum.net/v/20211129144552297'

headers = {
        'User-Agent': 'Mozilla/5.0',
        'Content-Type': 'text/html; charset=utf-8'
        }
# url로 접속
response = requests.get(url, headers=headers)
# 이메일 찾기
results = re.findall(r'[\w\.-]+@[\w\.-]+', response.text)
# 중복 제거
results = list(set(results))

print(results)