def check(i,j,c):
    for di,dj in [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]:
        l = []
        is_end = False
        dx = i + di
        dy = j + dj
        if 0 <= dx < N and 0 <= dy < N and maps[dx][dy] and maps[dx][dy] != c:
            l.append((dx,dy))
            while not is_end:
                dx += di
                dy += dj
                if 0 <= dx < N and 0 <= dy < N:
                    if maps[dx][dy] == 0:
                        is_end = True
                    elif maps[dx][dy] != c:
                        l.append((dx, dy))
                    elif maps[dx][dy] == c:
                        for c_i,c_j in l:
                            maps[c_i][c_j] = c
                        is_end = True                    
                else:
                    is_end = True

for test_case in range(1,int(input())+1):
    # 1. 입력받고 맵 초기화
    N, M = map(int, input().split())
    maps = [[0]*N for _ in range(N)]
    # 2. 맵 가운데 4자리 할당
    maps[N//2-1][N//2-1] = 2
    maps[N//2-1][N//2] = 1
    maps[N//2][N//2-1] = 1
    maps[N//2][N//2] = 2

    # 3. M만큼 입력받으면서 돌을 두고, 뒤집기 판정
    for _ in range(M):
        y, x, color = map(int, input().split())
        maps[x-1][y-1] = color
        check(x-1,y-1,color)

    # 4. 흑돌 백돌 개수 카운팅(반복문으로 탐색)
    white = 0
    black = 0
    for i in range(N):
        for j in range(N):
            if maps[i][j] == 1:
                black += 1
            elif maps[i][j] == 2:
                white += 1

    print(f'#{test_case} {black} {white}')