for _ in range(10):
    test_case = int(input())
    str_list = [input() for _ in range(100)]
    str_list_rot = [''] * 100  # 빈값을 넣으면 다행 생성이 안된다.
    palindrome = ''  # 초기화
    max_cnt = 1
    for i in range(100):
        for j in range(100):
            str_list_rot[i] += str_list[j][i]  # 이차원배열 90도회전(+문자열형태 유지)

    for i in range(100):
        for j in range(100):
            cnt = 0
            while j+cnt <= 100:
                if str_list[i][j:j+cnt] == str_list[i][j:j+cnt][::-1] and max_cnt < cnt:
                    max_cnt = cnt
                if str_list_rot[i][j:j+cnt] == str_list_rot[i][j:j+cnt][::-1] and max_cnt < cnt:
                    max_cnt = cnt
                cnt += 1

    print(f'#{test_case} {max_cnt}')