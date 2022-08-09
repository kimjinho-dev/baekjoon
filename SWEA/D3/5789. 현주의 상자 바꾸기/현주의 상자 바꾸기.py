T = int(input())

for test_case in range(1, T + 1):
    N, Q = map(int, input().split())
    boxs = [0] * N

    for i in range(1, Q + 1):
        L, R = map(int, input().split())
        for idx in range(L - 1, R):
            boxs[idx] = i

    print(f'#{test_case} ', end='')
    print(*boxs)