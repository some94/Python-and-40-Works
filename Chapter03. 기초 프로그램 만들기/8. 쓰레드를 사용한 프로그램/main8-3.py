import threading

def sum(name, value):
    for i in range(0, value):
        print(f"{name} : {i}")

# 1, 2번 쓰레드 생성
t1 = threading.Thread(target=sum, args=('1번 쓰레드', 10))
t2 = threading.Thread(target=sum, args=('2번 쓰레드', 10))

t1.start()
t2.start()

print("Main Thread")