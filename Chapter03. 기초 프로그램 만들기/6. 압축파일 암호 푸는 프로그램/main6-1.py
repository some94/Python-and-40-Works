import itertools

passwd_string = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

for len in range(1, 4):
    # passwd_string 모든 문자열을 repeat=길이 로 정렬하여 반환한다.
    to_attempt = itertools.product(passwd_string, repeat = len)
    for attempt in to_attempt:
        # 리스트로 반환된 값을 문자열로 변환한다. "구분자.join(리스트)"는 리스트의 값을 문자열로 변환한다.
        passwd = ''.join(attempt)
        print(passwd)