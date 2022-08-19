def dfs(x):
    visit[x] = True
    for vx in graph[x]:
        if visit[vx] == False:
            dfs(vx)


for test_case in range(1,int(input())+1):
    N, M = map(int,input().split())
    graph = [[] for _ in range(N+1)]
    visit = [False] * (N+1)
    cnt = 0

    for _ in range(M):
        v1,v2 = map(int,input().split())
        graph[v1].append(v2)
        graph[v2].append(v1)

    for idx in range(1, N+1):
        if visit[idx] == False:
            cnt += 1
            dfs(idx)

    print(f'#{test_case} {cnt}')