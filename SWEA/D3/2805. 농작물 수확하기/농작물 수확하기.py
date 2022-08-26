for test_case in range(1,int(input())+1):
    N = int(input())
    maps = [list(map(int,input())) for _ in range(N)]
    earn = 0
    for i in range(N):
        if i <= N//2:
            for j in range(N//2 - i, i + N//2 + 1):
                earn += maps[i][j]
        else:
            for j in range(i - N//2, N - i + N//2):
                earn += maps[i][j]

    print(f'#{test_case} {earn}')