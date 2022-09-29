def make_set():
    for num in range(N):
        par.append(num+1)


def find_set(node):
    if par[node] != node:
        par[node] = find_set(par[node])
    return par[node]


def union_set(root_a, root_b):
    if root_a < root_b:
        par[root_b] = root_a
    else:
        par[root_a] = root_b


N = int(input())
M = int(input())
graph = []
par = [0]
result = 0
cnt = 0
make_set()
for _ in range(M):
    a, b, c = map(int,input().split())
    graph.append((c,a,b))
graph.sort()

for g in graph:
    c, a, b = g
    root_a, root_b = find_set(a), find_set(b)
    if root_a != root_b:
        union_set(root_a,root_b)
        result += c
        cnt += 1
        if cnt == N-1:
            break
        

print(result)