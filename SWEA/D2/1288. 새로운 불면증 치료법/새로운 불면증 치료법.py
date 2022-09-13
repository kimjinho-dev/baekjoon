for test_case in range(1,int(input())+1):
    N = int(input())
    num_set = set()
    i = 1
    while len(num_set) != 10:
        words = str(N * i)
        num_set.update(words)
        i += 1
    print(f'#{test_case} {int(words)}')