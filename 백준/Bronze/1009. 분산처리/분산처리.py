T = int(input())
for tast_case in range(1, T + 1):
    A, B = map(int, input().split())
    B = B % 4
    if B == 0:
        B = 4
    
    if A%10==0:
        print(10)
    else:
        print(A**B % 10)