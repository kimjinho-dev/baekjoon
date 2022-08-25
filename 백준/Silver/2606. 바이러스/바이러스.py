def virus(que):
    global virus_com
    if not que:
        return

    for k in graph[que.pop(0)]:
        if not visit[k]:
            visit[k] = True
            que.append(k)
            virus_com += 1

    virus(que)


com_cnt = int(input())
graph = [[] for _ in range(com_cnt+1)]
visit = [False for _ in range(com_cnt+1)]
virus_com = 0
for _ in range(int(input())):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
visit[1] = True
virus([1])
print(virus_com)