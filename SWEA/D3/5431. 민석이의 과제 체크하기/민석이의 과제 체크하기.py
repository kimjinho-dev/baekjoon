for test_case in range(1, int(input())+1):
    N, K = map(int, input().split())
    students = list(range(1, N+1))
    submit_students = list(map(int, input().split()))

    for idx in range(K):
        students.remove(submit_students[idx])
    print(f'#{test_case}', *students)