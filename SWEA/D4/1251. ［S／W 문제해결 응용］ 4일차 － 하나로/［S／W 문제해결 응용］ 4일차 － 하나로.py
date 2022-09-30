from heapq import heappush, heappop


def prim(start):
    visited = [False] * (n + 1)
    heap = [(0, start)]  
    cost = 0  

    while heap:
        min_dist, min_node = heappop(heap)  
        if visited[min_node]:
            continue  

        visited[min_node] = True
        cost += min_dist

        for next_node, dist in graph[min_node]:
            if not visited[next_node]:
                heappush(heap, (dist, next_node))

    return cost

for test_case in range(1, int(input())+1):
    n = int(input())
    graph = [[] for _ in range(n + 1)]
    pos = [[],[]]

    pos[0] = list(map(int,input().split()))
    pos[1] = list(map(int,input().split()))
    tariff = float(input())
    for i in range(n-1):
        for j in range(i+1,n):
            x1, y1 = pos[0][i], pos[1][i]
            x2, y2 = pos[0][j], pos[1][j]
            weight = (abs(x1-x2) ** 2 + abs(y1-y2) ** 2) * tariff
            graph[i+1].append((j+1, weight))
            graph[j+1].append((i+1, weight))

    print(f'#{test_case} {round(prim(1))}')  # 1번 정점에서 시작