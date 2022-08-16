from itertools import *

def solution(nums):
    subset_lists = list(combinations(nums, 3))
    cnt = 0
    for subset in subset_lists:
        temp = sum(subset)
        is_sosu = True
        for num in range(temp//2,1,-1):
            if temp % num == 0:
                is_sosu = False
                break
        if is_sosu:
            cnt += 1

    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    print(cnt)

    return cnt