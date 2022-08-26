for test_case in range(1,int(input())+1):
    N = int(input())
    nums = list(map(int,input().split()))
    max_dan = -1
    for i in range(N-1):
        for j in range(i+1,N):
            num = nums[i]*nums[j]
            str_num = str(num)
            for k in range(1,len(str_num)):
                if str_num[-k] < str_num[-(k+1)]:
                    break
            else:
                if max_dan < num:
                    max_dan = num
    print(f'#{test_case} {max_dan}')