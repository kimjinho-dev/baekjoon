N = int(input())
maps = [[0]*100 for _ in range(100)]
size = 0
for _ in range(N):
    x, y = map(int, input().split())
    for i in range(x, 10 + x):
        for j in range(y, 10 + y):
            if not maps[i][j]:
                size += 1
                maps[i][j] = 1
print(size)