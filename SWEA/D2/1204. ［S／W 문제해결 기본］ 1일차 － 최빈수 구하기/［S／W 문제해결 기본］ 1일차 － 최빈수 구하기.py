T = int(input())
for test_case in range(1, T + 1):
    test_case_value = input()
    scores_list = list(map(int, input().split()))
    scores_list_set = set(scores_list)
    max_count = 0
    max_score = 0
    while len(scores_list_set):
        score = scores_list_set.pop()
        if max_count < scores_list.count(score) or (
            max_count == scores_list.count(score) and max_score < score
        ):
            max_count = scores_list.count(score)
            max_score = score
    print(f'#{test_case} {max_score}')