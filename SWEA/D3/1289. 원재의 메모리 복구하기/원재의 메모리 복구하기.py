for test_case in range(1,int(input())+1):
    code = input()
    cnt = 0
    while not code.find('1') == -1:
        i = code.find('1')
        temp = code[i:]
        temp = temp.replace('1', '2').replace('0', '1').replace('2', '0')
        temp = code[:i] + temp
        code = temp[:]
        cnt += 1

    print(f'#{test_case} {cnt}')