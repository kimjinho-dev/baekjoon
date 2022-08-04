L = int(input())
S = list(map(int, input().split()))
S.sort()
n = int(input())

if S.count(n):
    print(0)
elif n == 1:
    print(S[0] - 2)
else:
    if n < S[0]:
        print(n * (S[0] - n) - 1)
    else:
        for idx in range(len(S)):
            if S[idx] < n < S[idx + 1]:
                print((n - S[idx]) * (S[idx + 1] - n) - 1)
                break