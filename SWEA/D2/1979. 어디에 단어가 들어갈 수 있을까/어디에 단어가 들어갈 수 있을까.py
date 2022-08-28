def chk(x, y, rc):
    global result
    if maps[x][y] == '1':
        rc += 1
        if rc == K:
            result += 1
        elif rc == K + 1:
            result -= 1
    else:
        rc = 0    
    return rc


for tc in range(1, int(input())+1):
    N, K = map(int, input().split())
    maps = [input().split() for _ in range(N)]
    result = 0

    for i in range(N):
        row = 0
        col = 0
        for j in range(N):
            row = chk(i, j, row)
            col = chk(j, i, col)

    print(f'#{tc} {result}')