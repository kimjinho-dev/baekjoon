V, E = map(int,input().split())
start = int(input())
graph = [[] for _ in range(V+1)]

for _ in range(E):
    s, e, v = map(int,input().split())
    graph[s].append((e,v))

INF = 99999999
visited = [False] * (V + 1)
distance = [INF] * (V + 1)
distance[start] = 0
visited[start] = True

for e,v in graph[start]:
    if distance[e] > v:
        distance[e] = v

for _ in range(V-1):

    min_dis = INF
    min_i = 0
    for i in range(1,V+1):
        if not visited[i] and distance[i] < min_dis:
            min_i = i
            min_dis = distance[min_i]

    if min_i == 0:
        break

    visited[min_i] = True

    for e,v in graph[min_i]:
        if distance[e] > min_dis + v:
            distance[e] = min_dis + v

for i in range(1,V+1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])