import pandas as pd

filePath = r'C:\Users\ehdgn\PycharmProjects\파이썬과 40개의 작품들\Chapter05. 크롤링, 이미지처리, 데이터분석 시각화 프로그램 만들기\27. 전국의 대학교 위치 시각화하기\고등교육기관 하반기 주소록(2020).xlsx'
df_from_excel = pd.read_excel(filePath,engine='openpyxl')
# 번째 위치의 데이터를 column으로 설정
df_from_excel.columns = df_from_excel.loc[4].tolist()
# 0~5줄의 데이터를 버린다.
df_from_excel = df_from_excel.drop(index=list(range(0,5)))

print(df_from_excel.head())

print(df_from_excel['학교명'].values)

print(df_from_excel['주소'].values)