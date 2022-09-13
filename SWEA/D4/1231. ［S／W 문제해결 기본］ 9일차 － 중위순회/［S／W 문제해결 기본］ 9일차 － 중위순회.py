def middle(n):
    global result
    if n:
        middle(ch1[n])
        result += arr[n]
        middle(ch2[n])


for test_case in range(1,11):
    N = int(input())
    arr = [''] * (N+1)
    result = ''
    root_idx = 1
    ch1 = [0] * (N+1)
    ch2 = [0] * (N+1)
    par = [0] * (N+1)
    for _ in range(N):
        word = input().split()
        p = int(word[0])
        arr[p] = word[1]
        if len(word) > 2:
            c1 = int(word[2])
            ch1[p] = c1
            par[c1] = p
        if len(word) > 3:
            c2 = int(word[3])
            ch2[p] = c2
            par[c2] = p
    middle(root_idx)
    print(f'#{test_case} {result}')