for test_case in range(1,int(input())+1):
    N, M = map(int,input().split())
    result = N * M
    start_end = 0
    wbr = [[0,0,0] for _ in range(N - 2)]
    # 첫줄 검증
    for s in input():
        if s != 'W':
            start_end += 1
    # 중간줄 검증
    # 1. 모든 중간라인 wbr값 확인
    maps = [input() for _ in range(N-2)]
    for i in range(N-2):
        for j in range(M):
            if maps[i][j] == 'W':
                wbr[i][0] += 1
            elif maps[i][j] == 'B':
                wbr[i][1] += 1
            else:
                wbr[i][2] += 1
    # 2. 파랑 줄수 정하기, 그에 따라 나머지 값 구하기
    for blue_start in range(N-2):
        for blue_end in range(blue_start + 1,N-1):
            white, blue, red = 0, 0, 0
            for idx in range(blue_start):
                white += wbr[idx][1]
                white += wbr[idx][2]
            for idx in range(blue_start,blue_end):
                blue += wbr[idx][0]
                blue += wbr[idx][2]
            for idx in range(blue_end,N-2):
                red += wbr[idx][0]
                red += wbr[idx][1]
            if result > white + blue + red:
                result = white + blue + red

    # 마지막줄 검증
    for s in input():
        if s != 'R':
            start_end += 1

    result += start_end

    print(f'#{test_case} {result}')