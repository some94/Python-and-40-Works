import pandas as pd
import sqlite3

db_path = r"C:\Users\ehdgn\PycharmProjects\파이썬과 40개의 작품들\Chapter05. 크롤링, 이미지처리, 데이터분석 시각화 프로그램 만들기\25. 가상화폐 데이터 획득하여 데이터베이스 저장\coin.db"
con = sqlite3.connect(db_path, isolation_level=None)

# pandas를 이용하여 BTC 데이터를 읽는다.
readed_df = pd.read_sql("SELECT * FROM 'BTC'", con, index_col = 'index')

print(readed_df)