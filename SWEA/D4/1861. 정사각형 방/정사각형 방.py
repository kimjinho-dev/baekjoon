def bfs(i,j):
    global cnt
    while True:
        for di, dj in [[-1,0],[0,1],[1,0],[0,-1]]:
            if 0 <= i+di < N and 0 <= j+dj < N and maps[i+di][j+dj] == maps[i][j]+1:
                cnt += 1
                i += di
                j += dj
                break
        else:
            break
            
    if cnt > max_path[1] or (cnt == max_path[1] and val < max_path[0]):
        max_path[1] = cnt
        max_path[0] = val


for test_case in range(1,int(input())+1):
    N = int(input())  # 정점 개수
    maps = [list(map(int,input().split())) for _ in range(N)]
    max_path = [0,0] # [0]은 방위치, [1]은 이동한 방 개수
    for row in range(N):
        for col in range(N):
            val = maps[row][col]
            if max_path[1] <= N ** 2 - val + 1:
                cnt = 1
                bfs(row,col)
    print(f'#{test_case}', *max_path)