di = [1,0,-1,0] # 하,우,상,좌
dj = [0,1,0,-1]


def snail(search_num):
    k = 0  # 처음 방향은 아래
    cnt = N**2
    i, j = 0, 0
    while cnt:
        maps[i][j] = cnt
        if 0 <= i+di[k] < N and 0 <= j+dj[k] < N and not(maps[i+di[k]][j+dj[k]]):
            pass
        else:
            k = (k+1) % 4
        if search_num == cnt:
            si = i+1
            sj = j+1
        i += di[k]
        j += dj[k]
        cnt -= 1

    for m in maps:
        print(*m)
    print(si, sj)


N = int(input())
M = int(input())
maps = [[0] * N for _ in range(N)]

snail(M)