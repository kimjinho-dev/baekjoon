for _ in range(1,11):
    test_case = int(input())
    queue = list(map(int, input().split()))
    cnt = 1

    while queue[-1]:
        temp = queue.pop(0) - cnt  # 앞에것을 빼서 계산해주기
        if temp < 0:
            temp = 0
        queue.append(temp)         # 뺀값 뒤에 다시 넣어주기 
        cnt = cnt % 5 + 1  # 1~5   # 빼야하는값 계산
        
    print(f'#{test_case}', *queue)