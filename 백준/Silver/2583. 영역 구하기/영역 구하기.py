import sys
sys.setrecursionlimit(10**6)

di = [-1,1,0,0]
dj = [0,0,-1,1]

def dfs(row,col):
    global cnt
    for k in range(4):
        dx = row + di[k]
        dy = col + dj[k]
        if 0 <= dx < M and 0 <= dy < N and not(visit[dx][dy]) and not(maps[dx][dy]):
            visit[dx][dy] = True
            cnt += 1
            dfs(dx,dy)


M,N,K = map(int,input().split())  # 세로,가로,좌표(줄)수
# 왼쪽아래 x,y 오른쪽위 x,y x는 가로, y는 세로
maps = [[0] * N for _ in range(M)]  # 가로 N, 세로 M 이차원배열
visit = [[False] * N for _ in range(M)]
# 0 2 4 4
# 2 0~3 3 뒤는 -1씩 좌표는 뒤집어야함
for _ in range(K):
    x1,y1,x2,y2 = map(int,input().split())
    area_list = []

    for i in range(y1,y2):
        for j in range(x1,x2):
            maps[i][j] = 1

for i in range(M):
    for j in range(N):
        if not maps[i][j] and not visit[i][j]:
            cnt = 1
            visit[i][j] = True
            dfs(i,j)
            area_list.append(cnt)

area_list.sort()
print(len(area_list))
if not area_list:
    print(0)
else:
    print(*area_list)