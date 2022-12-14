def chk(x, y, rc):   # col, row 함수로 합치기
    global result
    if maps[x][y] == '1':
        rc += 1
        if rc == K:
            result += 1     # 알맞은 칸이 나오면, 일단 result += 1
        elif rc == K + 1:   # 만약 그 다음에도 빈칸이 아니라면, result -= 1
            result -= 1
    else:
        rc = 0              # 빈칸이 나오면 카운터 초기화
    return rc               # row,col 최신화


for tc in range(1, int(input())+1):
    N, K = map(int, input().split())
    maps = [input().split() for _ in range(N)]
    result = 0

    for i in range(N):
        row = 0
        col = 0
        for j in range(N):
            row = chk(i, j, row)  # chk함수로 가로 검사. row 값 갱신
            col = chk(j, i, col)  # chk함수로 세로 검사. col 값 갱신

    print(f'#{tc} {result}')