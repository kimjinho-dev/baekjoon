for test_case in range(1,int(input())+1):
    N = int(input())
    num_set = set()
    i = 0
    while len(num_set) != 10:
        i += 1
        num_set.update(str(N * i))
    print(f'#{test_case} {N * i}')