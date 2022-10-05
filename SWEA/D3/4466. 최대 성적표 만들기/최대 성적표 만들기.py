for test_case in range(1,int(input())+1):
    N, K = map(int,input().split())
    scores = list(map(int,input().split()))
    # result = get_score()
    result = sum(sorted(scores,reverse=True)[:K])
    print(f'#{test_case} {result}')