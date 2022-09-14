def sol(total, idx, ops):
    if idx == N:
        global max_cal, min_cal
        if total > max_cal:
            max_cal = total
        if total < min_cal:
            min_cal = total
        return

    for op_idx in range(4):
        if ops[op_idx]:
            if op_idx == 0:
                next_total = total + nums[idx]
            elif op_idx == 1:
                next_total = total - nums[idx]
            elif op_idx == 2:
                next_total = total * nums[idx]
            else:
                next_total = int(total / nums[idx])
            ops[op_idx] -= 1
            sol(next_total, idx + 1, ops)
            ops[op_idx] += 1


for test_case in range(1,int(input())+1):
    N = int(input())
    cals = list(map(int,input().split()))
    nums = list(map(int,input().split()))

    max_cal = -100000000
    min_cal = 100000000

    sol(nums[0],1,cals)
    print(f'#{test_case} {max_cal-min_cal}')