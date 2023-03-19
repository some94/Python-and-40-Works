import pyupbit
import sqlite3

ticker = 'KRW-BTC'
interval = 'minute1'
to = '2021-12-02 11:20'
count = 200

# 비트코인의 분봉 데이터를 가지고 온다. 값은 데이터프레임 형식으로 반환한다.
price_now = pyupbit.get_ohlcv(ticker=ticker,interval=interval,to=to,count=count)

db_path = r"C:\Users\ehdgn\PycharmProjects\파이썬과 40개의 작품들\Chapter05. 크롤링, 이미지처리, 데이터분석 시각화 프로그램 만들기\25. 가상화폐 데이터 획득하여 데이터베이스 저장\coin.db"

# 데이터베이스를 생성한다.
con = sqlite3.connect(db_path, isolation_level=None)
# BTC의 이름으로 데이터를 생성 후 데이터를 추가한다.
price_now.to_sql('BTC', con, if_exists='append')

con.close