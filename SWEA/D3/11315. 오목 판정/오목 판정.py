di = [-1,0,1,1]     # 우상,우,우하,하
dj = [1,1,1,0]

for test_case in range(1,int(input())+1):
    N = int(input())
    maps = [input() for _ in range(N)]
    i, j, = 0, 0
    ohmok = 'NO'
    while ohmok == 'NO':
        if maps[i][j] == 'o':
            for k in range(4):
                check_ohmok = 0
                for p in range(1,5):
                    dx = i + di[k]*p
                    dy = j + dj[k]*p
                    if 0 <= dx < N and 0 <= dy < N and maps[dx][dy] == 'o':
                        check_ohmok += 1
                if check_ohmok == 4:
                    ohmok = 'YES'

        j += 1
        if j == N:
            j = 0
            i += 1
            if i == N:
                break

    print(f'#{test_case} {ohmok}')