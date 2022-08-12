T = int(input())

for test_case in range(1,T+1):
    N, M = map(int, input().split())
    max_size = 2
    map_str = [input().replace(" ", "") for _ in range(N)]



    # 가로 검사
    test_zero = 0
    for idx in range(N):
        while max_size != M and map_str[idx].count('1' * (max_size + 1)) != 0:
            max_size += 1
        test_zero += map_str[idx].count('1')

    # 세로 검사
    col_cnt = 0
    for i in range(M):
        if col_cnt > max_size:
            max_size = col_cnt
        col_cnt = 0
        for j in range(N):
            if map_str[j][i] == '1':
                col_cnt += 1
            else:
                if col_cnt > max_size:
                    max_size = col_cnt
                col_cnt = 0
    if col_cnt > max_size:
        max_size = col_cnt
    if test_zero == 0:
        max_size = 0
    print(f'#{test_case} {max_size}')