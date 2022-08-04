def reverse(i, j):
    for a in range(3):
        for b in range(3):
            list_map_A[i + a][j + b] = 1 - list_map_A[i + a][j + b]


n, m = map(int, input().split())
list_map_A = [list(map(int, list(input()))) for _ in range(n)]
list_map_B = [list(map(int, list(input()))) for _ in range(n)]

count = 0
while 1:
    if m < 3 or n < 3:
        break
    for i in range(n - 2):
        for j in range(m - 2):
            if list_map_A[i][j] != list_map_B[i][j]:
                reverse(i, j)
                count += 1
            if j == m - 3:
                if list_map_A[i][j + 1] != list_map_B[i][j + 1]:
                    reverse(i, j)
                    count += 1
                if list_map_A[i][j + 2] != list_map_B[i][j + 2]:
                    reverse(i, j)
                    count += 1

        if i == n - 3:
            if list_map_A[i + 1][j] != list_map_B[i + 1][j]:
                reverse(i, j)
                count += 1
            if list_map_A[i + 2][j] != list_map_B[i + 2][j]:
                reverse(i, j)
                count += 1

        if i == n - 3 and j == m - 3:
            if list_map_A[i + 1][j + 1] != list_map_B[i + 1][j + 1]:
                reverse(i, j)
                count += 1
            if list_map_A[i + 1][j + 2] != list_map_B[i + 1][j + 2]:
                reverse(i, j)
                count += 1
            if list_map_A[i + 2][j + 1] != list_map_B[i + 2][j + 1]:
                reverse(i, j)
                count += 1
            if list_map_A[i + 2][j + 2] != list_map_B[i + 2][j + 2]:
                reverse(i, j)
                count += 1
    break

if list_map_A == list_map_B:
    print(count)
else:
    print(-1)