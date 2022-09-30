from heapq import heappush, heappop

def dijkstra(start_x,start_y):
    distance[start_x][start_y] = maps[start_x][start_y]
    heap = [(distance[start_x][start_y], start_x, start_y)]

    while heap:
        min_dist, min_x, min_y = heappop(heap)
        if min_dist > distance[min_x][min_y]:
            continue
        for next_x, next_y, dist in graph[min_x][min_y]:
            new_dist = min_dist + dist
            if new_dist < distance[next_x][next_y]:
                distance[next_x][next_y] = new_dist
                heappush(heap, (new_dist, next_x, next_y))


test_case = 1
while 1:
    N = int(input())
    if not N:
        break
    graph = [[[] for _ in range(N)] for _ in range(N)]
    INF = 99999999  # 나올 수 없는 임의의 큰 수
    distance = [[INF] * N for _ in range(N)]

    maps = [list(map(int,input().split())) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for dx,dy in [(i+1,j), (i,j+1), (i-1,j), (i,j-1)]:
                if 0 <= dx < N and 0 <= dy < N:
                    graph[i][j].append((dx,dy,maps[dx][dy]))

    dijkstra(0,0)
    print(f'Problem {test_case}: {distance[-1][-1]}')
    test_case += 1