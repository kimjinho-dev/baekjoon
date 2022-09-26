N = int(input())
half_N = N // 2
# middle_N = (N + half_N) // 2
max_len = 0
max_list = []

for n in range(half_N, N+1):
    nums = [N, n]
    while nums[-2] >= nums[-1]:
        nums.append(nums[-2] - nums[-1])
    if max_len < len(nums):
        max_len = len(nums)
        max_list = nums[:]

print(max_len)
print(*max_list)
