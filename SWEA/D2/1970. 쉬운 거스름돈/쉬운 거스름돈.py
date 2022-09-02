for test_case in range(1,int(input())+1):
    N = int(input())
    moneys = [50000,10000,5000,1000,500,100,50,10]
    print(f'#{test_case}')
    for idx in range(8):
        print(N // moneys[idx], end=' ')
        N %= moneys[idx]
    print()