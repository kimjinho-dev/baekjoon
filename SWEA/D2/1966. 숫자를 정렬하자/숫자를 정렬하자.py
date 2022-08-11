T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    nums = list(map(int, input().split()))

    for i in range(N-1, 0, -1):
        for idx in range(0, i):
            if nums[idx] > nums[idx+1]:
                nums[idx], nums[idx+1] = nums[idx+1], nums[idx]

    print(f'#{test_case}', *nums)