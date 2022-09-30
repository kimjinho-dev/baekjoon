from heapq import heappush, heappop
def dijkstra(start):
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


n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
INF = 99999999

for _ in range(m):
    s, e, w = map(int, input().split())
    graph[s].append((e, w))
    graph[e].append((s, w))
v1, v2 = map(int,input().split())

distance = [INF] * (n + 1)
dijkstra(v1)
dis_v1_v2 = distance[1] + distance[v2]
dis_v2_v1 = distance[n]
distance = [INF] * (n + 1)
dijkstra(v2)
dis_v1_v2 += distance[n]
dis_v2_v1 += distance[1] + distance[v1]
if dis_v1_v2 >= INF and dis_v2_v1 >= INF:
    print('-1')
else:
    print(dis_v1_v2 if dis_v1_v2 < dis_v2_v1 else dis_v2_v1)