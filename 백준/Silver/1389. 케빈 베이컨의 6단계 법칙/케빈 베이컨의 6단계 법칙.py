def bfs(que):
    if not que:
        return
    v = que.pop(0)
    for move in graph[v]:
        if not visit[move]:
            visit[move] = visit[v]+1
            que.append(move)
    bfs(que)

node, line = map(int, input().split())
graph = [[] for _ in range(node+1)]
for _ in range(line):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
min_line = 5000000
for i in range(1,node+1):
    visit = [0] * (node + 1)
    visit[i] = 1
    bfs([i])
    if sum(visit) < min_line:
        min_line = sum(visit)
        min_num = i

print(min_num)