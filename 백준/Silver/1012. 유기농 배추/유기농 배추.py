import sys
sys.setrecursionlimit(10**6)

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]  # 상하좌우

def dfs(x, y):
    visit[x][y] = True
    for n in range(4):
        vx = x + di[n]
        vy = y + dj[n]

        if 0 <= vx < N and 0 <= vy < M and bachu[vx][vy] == 1 and not visit[vx][vy]:
            dfs(vx, vy)


for test_case in range(1, int(input())+1):
    M, N, K = map(int, input().split())
    visit = [[False] * M for _ in range(N)]
    bachu = [[0] * M for _ in range(N)]
    result = 0
    for _ in range(K):
        j, i = map(int, input().split())
        bachu[i][j] = 1
    for i in range(N):
        for j in range(M):
            if not visit[i][j] and bachu[i][j] == 1:
                dfs(i, j)
                result += 1
    print(result)