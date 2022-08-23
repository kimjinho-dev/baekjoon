import sys
sys.setrecursionlimit(10**6)

di = [-1,1,0,0]
dj = [0,0,-1,1]

def dfs(x,y,key,area):
    for k in range(4):
        dx = x + di[k]
        dy = y + dj[k]
        if 0 <= dx < N and 0 <= dy < N and not visit[dx][dy] and area[dx][dy] == key:
            visit[dx][dy] = True
            dfs(dx,dy,key,area)


N = int(input())
maps = [input() for _ in range(N)]
by_maps = []
for m in maps:
    by_maps.append(m.replace('R','Y').replace('G','Y'))


by_area = 0
rgb_area = 0
visit = [[False]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if by_maps[i][j] == 'B' and not visit[i][j]:
            visit[i][j] = True
            dfs(i,j,'B',by_maps)
            by_area += 1
            rgb_area += 1
        elif by_maps[i][j] == 'Y' and not visit[i][j]:
            visit[i][j] = True
            dfs(i,j,'Y',by_maps)
            by_area += 1

visit = [[False]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if maps[i][j] == 'G' and not visit[i][j]:
            visit[i][j] = True
            dfs(i,j,'G',maps)
            rgb_area += 1
        elif maps[i][j] == 'R' and not visit[i][j]:
            visit[i][j] = True
            dfs(i,j,'R',maps)
            rgb_area += 1

print(rgb_area, by_area)