for test_case in range(1,int(input())+1):
    N, K = map(int, input().split())
    score = [0] * N
    for idx in range(N):
        mid, end, hw = map(int, input().split())
        score[idx] = mid * 0.35 + end * 0.45 + hw * 0.2
    sort_score = sorted(score,reverse=True)
    rank = sort_score.index(score[K-1]) // (N // 10)

    print(f'#{test_case}',['A+','A0','A-','B+','B0','B-','C+','C0','C-','D0'][rank] )