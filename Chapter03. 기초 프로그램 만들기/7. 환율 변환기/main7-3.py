import requests
from bs4 import BeautifulSoup

def get_exchange_rate(target1, target2):
    # 헤더 추가. 헤더 없이 접속하면 사이트에서 정보를 주지 않는다.
    headers = {
        'User-Agent': 'Mozilla/5.0',
        'Content_Type': 'text/html; charset=utf-8'
    }
    # requests 라이브러리를 이용하여 사이트에서 응답값을 가지고 온다.
    response = requests.get("https://kr.investing.com/currencies/{}-{}".format(target1, target2), headers=headers)
    # BeautifulSoup 라이브러리를 이용하여 html로 보기 값을 찾기 좋게 한다.
    content = BeautifulSoup(response.content, 'html.parser')
    # 마지막 환율 정보를 찾는다.
    containers = content.find('span', {'data-test' : 'instrument-price-last'})
    print(containers.text)

# 달러-원화 비율을 크롤링하여 출력
get_exchange_rate('usd', 'krw')