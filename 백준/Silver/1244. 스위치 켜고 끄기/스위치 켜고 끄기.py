def chk(left,right):
    left -= 1
    right += 1
    if left > 0 and right < switch_ea + 1:
        if switches[left] == switches[right]:
            chk(left,right)
            return
    for idx_2 in range(left + 1, right):
        if switches[idx_2] == 0:
            switches[idx_2] = 1
        else:
            switches[idx_2] = 0



switch_ea = int(input())
switches = [-1] + list(map(int,input().split()))

for _ in range(int(input())):
    gender, num = map(int,input().split())
    if gender == 1:
        for idx in range(num,switch_ea + 1,num):
            if switches[idx] == 0:
                switches[idx] = 1
            else:
                switches[idx] = 0
    else:
        chk(num,num)

switches = switches[1:]
for idx_3 in range(0,len(switches),20):
    print(*switches[idx_3:idx_3+20])