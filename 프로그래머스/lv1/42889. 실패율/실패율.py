def solution(N, stages):
    answer = []
    users = len(stages)
    fail_percent = [[0,i] for i in range(1,N+1)]
    for i in range(1,N+1):
        if users != 0:
            fail_cnt = stages.count(i)
            fail_percent[i-1][0] = fail_cnt / users
            users -= fail_cnt
        else:
            break
    fail_percent.sort(key=lambda x:(-x[0],x[1]))
    for i in fail_percent:
        answer.append(i[1])

    return answer