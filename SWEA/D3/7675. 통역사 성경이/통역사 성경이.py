for test_case in range(1, int(input())+1):
    N = int(input())
    words = input().split()
    word_cnt = [0] * N
    idx = 0
    for s in words:
        if s[-1] == '.' or s[-1] == '?' or s[-1] == '!':
            if s[0].isupper() and s[1:len(s)-1].islower() and s[:len(s)-1].isalpha():
                word_cnt[idx] += 1
            if len(s) == 2 and s[0].isupper():
                word_cnt[idx] += 1
            idx += 1
        else:
            if s[0].isupper() and s[1:].islower() and s.isalpha():
                word_cnt[idx] += 1
            if len(s) == 1 and s[0].isupper():
                word_cnt[idx] += 1
    print(f'#{test_case}', *word_cnt)