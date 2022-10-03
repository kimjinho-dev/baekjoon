for testCase in range(1, 11):
    INF = 9999999
    V, E = map(int, input().split())
    graph = [[] for _ in range(V + 1)]
    indegree = [0] * (V + 1)
    data = list(map(int, input().split()))
    for i in range(0, E * 2, 2):
        graph[data[i]].append(data[i + 1])
        indegree[data[i + 1]] += 1

    stack = []
    for i in range(1, V + 1):
        if indegree[i] == 0:
            stack.append(i)
    print("#%d" % testCase, end=' ')
    while stack:
        u = stack.pop()
        print(u, end=' ')
        for i in graph[u]:
            indegree[i] -= 1
            if indegree[i] == 0:
                stack.append(i)
    print()