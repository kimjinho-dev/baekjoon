
def bfs(root):
    stack = []
    visited[root] = True
    dis_max = 0
    num_max = 0
    if graph[root]:
        for n in graph[root]:
            visited[n] = True
            stack.append((n,1))
    else:
        return nums[root]

    while stack:
        node,dis = stack.pop(0)
        visited[node] = True
        for n in graph[node]:
            if not visited[n]:
                visited[n] = True
                stack.append((n, dis+1))
        if dis_max < dis:
            dis_max = dis
            num_max = nums[node]
        elif dis_max == dis and num_max < nums[node]:
            num_max = nums[node]
    return num_max


for test_case in range(1, 11):
    length, start = map(int,input().split())
    line = list(map(int,input().split()))
    nums = sorted(list(set(line)))
    graph = [[] for _ in range(len(nums))]
    visited = [False] * len(nums)
    for idx in range(length//2):
        s, e = line[idx*2], line[idx*2+1]
        graph[nums.index(s)].append(nums.index(e))
    start_index = nums.index(start)
    result = bfs(start_index)
    print(f'#{test_case} {result}')