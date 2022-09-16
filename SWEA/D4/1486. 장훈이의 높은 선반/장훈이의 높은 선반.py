def build_people(total,people_idx):
    global min_total
    if B <= total < min_total:
        min_total = total
        return

    for idx in range(people_idx, N):
        next_total = total + heights[idx]
        if next_total >= min_total:
            return
        build_people(next_total, idx+1)


for test_case in range(1, int(input())+1):
    N, B = map(int,input().split())
    heights = list(map(int,input().split()))
    min_total = 10000 * 20
    heights.sort()
    build_people(0,0)
    print(f'#{test_case} {min_total - B}')