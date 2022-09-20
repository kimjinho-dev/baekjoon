for test_case in range(1,int(input())+1):
    N, M = map(int,input().split())
    if M & (2 ** N - 1) == 2 ** N - 1:
        print(f'#{test_case} ON')
    else:
        print(f'#{test_case} OFF')