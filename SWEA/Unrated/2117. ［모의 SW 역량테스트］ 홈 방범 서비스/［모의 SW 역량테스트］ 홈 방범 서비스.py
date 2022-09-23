def bfs_search(x,y):
    global max_cnt
    before_dis = 0
    visited = [[False] * mapsize for _ in range(mapsize)]
    que = [(x,y,1)]
    cnt = maps[x][y]
    visited[x][y] = True
    while que:
        x, y, dis = que.pop(0)
        if dis-1 == before_dis:
            if max_cnt < cnt and cnt * home_val >= dis ** 2 + (dis - 1) ** 2:
                max_cnt = cnt
            before_dis += 1

        for dx, dy in [(x-1,y),(x,y+1),(x+1,y),(x,y-1)]:
            if 0 <= dx < mapsize and 0 <= dy < mapsize and not visited[dx][dy]:
                visited[dx][dy] = True
                if maps[dx][dy]:
                    cnt += 1
                que.append((dx,dy,dis+1))

for test_case in range(1,int(input())+1):
    mapsize, home_val = map(int,input().split())  # 맵 사이즈와 각 집의 가치 변수받기
    maps = [list(map(int,input().split())) for _ in range(mapsize)]
    max_cnt = 0
    for i in range(mapsize):
        for j in range(mapsize):
            bfs_search(i,j)

    print(f'#{test_case} {max_cnt}')