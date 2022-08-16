for test_case in range(1, int(input())+1):
    A_str, B_str = input().split()

    cnt = A_str.count(B_str)
    A_str = A_str.replace(B_str, "")
    print(f'#{test_case} {len(A_str)+cnt}')