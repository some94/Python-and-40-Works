# 컴퓨터가 연결된 접속 정보를 받아올 때 사용하는 모듈
import socket

# 연결된 소켓의 이름을 가져와 in_addr 변수와 바인딩
in_addr = socket.gethostbyname(socket.gethostname())

# 내부 IP 확인
print(in_addr)