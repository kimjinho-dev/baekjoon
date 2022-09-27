def dfs(percent,n):
    global result
    if result > percent:
        return
    if n == N:
        if result < percent:
            result = percent
    for k in range(N):
        if not visited[k] and (maps[n][k] > result or maps[n][k] == 100):
            visited[k] = True
            if n == 0:
                dfs(percent + maps[n][k], n+1)
            elif maps[n][k] > result:
                dfs((percent/100 * maps[n][k]/100) * 100, n+1)
            else:
                return
            visited[k] = False



for test_case in range(1,int(input())+1):
    N = int(input())
    maps = [list(map(int,input().split())) for _ in range(N)]
    result = 0
    visited = [False] * N
    dfs(0,0)

    print(f'#{test_case} {round(result,6):.6f}')