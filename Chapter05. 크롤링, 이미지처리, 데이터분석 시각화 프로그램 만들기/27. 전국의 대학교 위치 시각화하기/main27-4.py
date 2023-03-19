import folium
# 처음 보영주는 위도와 경도 설정. zoom_start는 지도의 배율
map = folium.Map(location=[37,127],zoom_start=7)
# 위도와 경도에 popup이름으로 파란색의 아이콘 마커를 표시
marker = folium.Marker([37.341435483, 126.733026596],
                    popup='한국공학대학교',
                    icon = folium.Icon(color='blue'))
# 마커 추가
marker.add_to(map)

map.save(r'C:\Users\ehdgn\PycharmProjects\파이썬과 40개의 작품들\Chapter05. 크롤링, 이미지처리, 데이터분석 시각화 프로그램 만들기\27. 전국의 대학교 위치 시각화하기/uni_map.html')