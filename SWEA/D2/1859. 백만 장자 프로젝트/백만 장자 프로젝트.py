T = int(input())
for test_case in range(1, T + 1):
    lenght = int(input())
    future = list(map(int, input().split()))
    future_temp = []
    earn = 0
    idx = 0
    future_max = max(future)
    idx_max = future.index(future_max)
    while 1:
        if idx_max != 0:
            earn += future_max * idx_max - sum(future[:idx_max])

        if idx_max + 1 == len(future) or len(future) == 1:
            break
        else:
            future = future[idx_max + 1 :]

        future_max = max(future)
        idx_max = future.index(future_max)

    print(f'#{test_case} {earn}')
