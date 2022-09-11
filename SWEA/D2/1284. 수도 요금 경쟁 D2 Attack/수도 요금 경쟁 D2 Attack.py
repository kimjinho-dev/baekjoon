for test_case in range(1,int(input())+1):
    P, Q, R, S, W = map(int,input().split())
    a_pay = W * P
    if W <= R:
        b_pay = Q
    else:
        b_pay = Q + (W - R) * S
    print(f'#{test_case} {a_pay if a_pay <= b_pay else b_pay}')
