for test_case in range(1, int(input())+1):
    word = [input() for _ in range(5)]
    max_col = 0
    for s in word:
        if max_col < len(s):
            max_col = len(s)
            
    print(f'#{test_case}', end=' ')
    for i in range(max_col):
        for j in range(5):
            try:
                print(word[j][i], end='')
            except:
                pass
    print()