from heapq import heappush, heappop

def dijkstra(start,graph,distance):        # 기본 다익스트라 코드
    distance[start] = 0
    heap = [(0, start)]

    while heap:
        min_dist, min_node = heappop(heap)

        if min_dist > distance[min_node]:
            continue

        for next_node, dist in graph[min_node]:
            new_dist = min_dist + dist
            if new_dist < distance[next_node]:
                distance[next_node] = new_dist
                heappush(heap, (new_dist, next_node))


n, m, x = map(int, input().split())
graph_n_x = [[] for _ in range(n + 1)]
graph_x_n = [[] for _ in range(n+1)]
INF = 99999999
distance_n_x = [INF] * (n + 1)
distance_x_n = [INF] * (n + 1)

for _ in range(m):
    s, e, w = map(int, input().split())
    graph_n_x[s].append((e, w))
    graph_x_n[e].append((s, w))

dijkstra(x,graph_n_x,distance_n_x)
dijkstra(x,graph_x_n,distance_x_n)
result = []
for i in range(1,n+1):
    result.append(distance_x_n[i]+distance_n_x[i])
print(max(result))