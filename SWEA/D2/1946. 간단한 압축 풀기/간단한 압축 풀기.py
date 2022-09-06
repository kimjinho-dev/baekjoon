for test_case in range(1,int(input())+1):
    print(f'#{test_case}')
    word = ''
    for _ in range(int(input())):
        char, act = input().split()
        word += str(char) * int(act)
        while len(word) >= 10:
            print(word[:10])
            word = word[10:]
    print(word)