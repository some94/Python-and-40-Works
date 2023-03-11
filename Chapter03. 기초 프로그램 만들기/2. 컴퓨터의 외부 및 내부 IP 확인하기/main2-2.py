import socket

# 소켓 연결
in_addr = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 구글 접속. https 기본 접속 포트는 443
in_addr.connect(("www.google.co.kr", 443))
# 연결된 소켓의 이름 출력
print(in_addr.getsockname()[0])