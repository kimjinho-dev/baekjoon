N, r, c = map(int, input().split())
start = 0

while N != 1:
    if r < 2 ** (N - 1):  # 1,2사분면
        if c < 2 ** (N - 1):  # 2사분면
            pass
        else:  # 1사분면
            start += (2 ** (2 * N)) / 4
            c = c - (2 ** (N - 1))
    else:  # 3,4사분면
        if c < 2 ** (N - 1):  # 3사분면
            start += (2 ** (2 * N)) / 4 * 2
            r = r - (2 ** (N - 1))
        else:  # 4사분면
            start += (2 ** (2 * N)) / 4 * 3
            r = r - (2 ** (N - 1))
            c = c - (2 ** (N - 1))
    N -= 1

start = int(start)

if r == 0 and c == 0:
    print(start)
elif r == 0 and c == 1:
    print(start + 1)
elif r == 1 and c == 0:
    print(start + 2)
elif r == 1 and c == 1:
    print(start + 3)


# 1제출
# start += 이 아닌 start = 로 지정문제
# 2제출
# 1,3 사분면 잘못 지정
# 3제출
# 아래 판정에서 and 대신 & 사용. 왜 이게 오류일까?

### 파이썬에서는 and != &. 아예 다른 연산자이다.
### &는 비트 연산자로 이진법 변환후 같은 값을 출력하는 비트연산자이다.
### &&이 c에서는 and연산자였으나, 파이썬에는 이런 연산자가 없다.