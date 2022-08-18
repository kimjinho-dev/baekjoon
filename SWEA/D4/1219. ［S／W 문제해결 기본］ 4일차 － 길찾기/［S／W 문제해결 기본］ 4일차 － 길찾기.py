def graph():
    for idx in range(0, path):
        start, end = idx*2, idx*2+1
        if connect1[path_list[start]] == '':
            connect1[path_list[start]] = path_list[end]
        else:
            connect2[path_list[start]] = path_list[end]

def dfs():
    start = 0
    goal = 99
    stack = []
    v = start
    visit[v] = True

    while 1:
        if connect2[v] != '' and visit[connect2[v]] == 0:
            stack.append(v)
            v = connect2[v]
            visit[v] = True
        elif connect1[v] != '' and visit[connect1[v]] == 0:
            stack.append(v)
            v = connect1[v]
            visit[v] = True
        else:
            v = stack[-1]
            stack.pop()

        if v == goal:
            return 1
        if not stack:
            return 0


for _ in range(10):
    test_case, path = map(int, input().split())
    connect1 = [''] * 100
    connect2 = [''] * 100
    visit = [False] * 100
    path_list = list(map(int, input().split()))
    graph()

    S, G = path_list[-2], path_list[-1]
    is_path = dfs()
    print(f'#{test_case} {is_path}')