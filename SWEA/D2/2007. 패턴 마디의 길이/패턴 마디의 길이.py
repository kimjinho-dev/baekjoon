for test_case in range(1,int(input())+1):
    sentence = input()

    for repeat_len in range(1,11):
        temp = sentence[:repeat_len] * 30
        temp = temp[:30]
        if sentence == temp:
            print(f'#{test_case} {repeat_len}')
            break
