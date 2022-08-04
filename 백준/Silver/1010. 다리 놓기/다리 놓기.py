def fact(n):
    if n == 1:
        return 1
    else:
        return fact(n - 1) * n

def con(A, B):
    if B == 0:
        return 1
    else:
        return con(A - 1, B - 1) * A

T = int(input())

for tase_case in range(T):
    B, A = map(int, input().split())
    print(int(con(A, B) / fact(B)))