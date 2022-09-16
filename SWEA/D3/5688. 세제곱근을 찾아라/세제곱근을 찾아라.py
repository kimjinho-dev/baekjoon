for test_case in range(1, int(input()) + 1):
    N = int(input())
    N_sqrt3 = N ** (1/3)
    N_sqrt3_round = round(N_sqrt3)
    if abs(N_sqrt3 - N_sqrt3_round) <= 1e-9:
        print(f'#{test_case} {N_sqrt3_round}')
    else:
        print(f'#{test_case} -1')