import sys
sys.setrecursionlimit(10**6)

di = [-1, 1, 0, 0, -1, -1, 1, 1]
dj = [0, 0, -1, 1, -1, 1, -1, 1]  # 상하좌우,좌상,우상,좌하,우하

def dfs(x, y):
    visit[x][y] = True
    for n in range(8):
        vx = x + di[n]
        vy = y + dj[n]

        if 0 <= vx < h and 0 <= vy < w and land[vx][vy] == 1 and not visit[vx][vy]:
            dfs(vx, vy)


result = []
while 1:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    visit = [[False] * w for _ in range(h)]
    land = [list(map(int, input().split())) for _ in range(h)]
    cnt = 0
    for i in range(h):
        for j in range(w):
            if not visit[i][j] and land[i][j] == 1:
                dfs(i, j)
                cnt += 1
    result.append(cnt)

print(*result, sep='\n')