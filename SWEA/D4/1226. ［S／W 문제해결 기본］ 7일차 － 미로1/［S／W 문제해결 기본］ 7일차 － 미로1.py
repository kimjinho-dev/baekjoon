di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]  # 상하좌우

def bfs(que):
    global result
    if not que:
        result = 0
        return

    for _ in range(len(que)):
        x_y = que.pop(0)
        for n in range(4):
            vx = x_y[0] + di[n]
            vy = x_y[1] + dj[n]

            if maze[vx][vy] == 3:
                result = 1
                return

            if maze[vx][vy] == 0 and not visit[vx][vy]:
                visit[vx][vy] = True
                que.append([vx, vy])
    bfs(que)


for _ in range(10):
    test_case = int(input())
    visit = [[False] * 16 for _ in range(16)]
    maze = [list(map(int, input())) for _ in range(16)]
    result = 0
    bfs([[1,1]])
    print(f'#{test_case} {result}')