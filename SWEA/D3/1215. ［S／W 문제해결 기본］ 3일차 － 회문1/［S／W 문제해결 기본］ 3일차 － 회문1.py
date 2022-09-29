for test_case in range(1,11):
    N = int(input())
    maps = [input() for _ in range(8)]
    cnt = 0
    for i in range(8):
        rows = [[] for _ in range(N)]
        cols = [[] for _ in range(N)]
        for j in range(8):
            for idx in range(N if j >= N else j+1):
                rows[idx].append(maps[i][j])
                cols[idx].append(maps[j][i])
                if len(rows[idx]) == N:
                    if rows[idx] == rows[idx][::-1]:
                        cnt += 1
                    rows[idx] = []
                if len(cols[idx]) == N:
                    if cols[idx] == cols[idx][::-1]:
                        cnt += 1
                    cols[idx] = []

    print(f'#{test_case} {cnt}')