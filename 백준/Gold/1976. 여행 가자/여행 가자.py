def find_set(node):
    if graph[node] != node:
        graph[node] = find_set(graph[node])
    return graph[node]


N = int(input())
M = int(input())
graph = [num for num in range(N+1)]

for i in range(N):
        line = list(map(int, input().split()))
        for j in range(N):
            if line[j] == 1:
                i_root, j_root = find_set(i + 1), find_set(j + 1)
                if i_root != j_root:
                    if i_root < j_root:
                        graph[i_root] = j_root
                    else:
                        graph[j_root] = i_root


path = list(map(int, input().split()))
start_root = find_set(path[0])
result = "YES"
for i in range(1, M):
    chk = find_set(path[i])
    if start_root != chk:
        result = "NO"
print(result)