T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split())
    fly_map = [list(map(int, input().split())) for _ in range(N)]
    sum_count = 0
    fly_sum_max = 0
    x_idx = 0
    y_idx = 0
    while not(sum_count == (N-M+1)**2):
        fly_sum = 0
        for i in range(x_idx, x_idx + M):
            for j in range(y_idx, y_idx + M):
                fly_sum += fly_map[i][j]

        if fly_sum_max < fly_sum:
            fly_sum_max = fly_sum

        y_idx += 1
        if y_idx == N-M+1:
            y_idx = 0
            x_idx += 1

        sum_count += 1

    print(f'#{test_case} {fly_sum_max}')