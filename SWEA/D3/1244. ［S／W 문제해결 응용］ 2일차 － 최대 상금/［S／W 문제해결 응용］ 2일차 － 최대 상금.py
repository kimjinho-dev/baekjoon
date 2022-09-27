def perfect_serach(n, cnt):
    global result
    str_n = ''.join(n)
    if cnt == change_cnt:
        if int(str_n) > result:
            result = int(str_n)
        return

    if (cnt,str_n) in before_search:
        return
    before_search.add((cnt,str_n))

    for idx_1 in range(N-1):
        for idx_2 in range(idx_1+1,N):
            n[idx_1], n[idx_2] = n[idx_2], n[idx_1]
            perfect_serach(n,cnt+1)
            n[idx_1], n[idx_2] = n[idx_2], n[idx_1]


for test_case in range(1, int(input()) + 1):
    nums, change_cnt = input().split()
    N = len(nums)
    change_cnt = int(change_cnt)
    sort_nums = sorted(nums, reverse=True)
    before_search = set()
    result = 0
    perfect_serach(list(nums),0)
    print(f'#{test_case} {result}', )