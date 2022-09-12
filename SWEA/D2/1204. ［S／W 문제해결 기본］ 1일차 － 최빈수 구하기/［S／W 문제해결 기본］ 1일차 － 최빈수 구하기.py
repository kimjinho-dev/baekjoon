for _ in range(int(input())):
    test_case = int(input())
    nums = list(map(int,input().split()))
    nums_set = set(nums)
    max_cnt = 0
    max_num = 0
    for num in nums_set:
        cnt = nums.count(num)
        if max_cnt < cnt:
            max_cnt = cnt
            max_num = num
    print(f'#{test_case} {max_num}')
