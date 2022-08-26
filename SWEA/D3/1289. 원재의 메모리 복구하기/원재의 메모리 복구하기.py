for test_case in range(1,int(input())+1):
    code = input()
    cnt = 0
    while not code.find('1') == -1:
        i = code.find('1')
        code = code[:i] + code[i:].replace('1', '2').replace('0', '1').replace('2', '0')
        cnt += 1

    print(f'#{test_case} {cnt}')