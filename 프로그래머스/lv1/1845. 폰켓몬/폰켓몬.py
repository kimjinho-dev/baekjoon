def solution(nums):
    result = len(set(nums))
    if result > len(nums) // 2:
        result = len(nums) // 2
    return result