N, M = map(int,input().split())
chess_map = [input() for _ in range(N)]
chess_sum = 64

# 슬라이드 윈도우 기법 X
for x in range(N-7):
    for y in range(M-7):
        total1 = 0  # 하얀색시작
        total2 = 0  # 검은색시작
        for i in range(8):
            for j in range(8):
                if (i+j) % 2 == 0 and chess_map[x+i][y+j] == 'B':
                    total1 += 1
                elif (i+j) % 2 == 0 and chess_map[x+i][y+j] == 'W':
                    total2 += 1
                elif (i+j) % 2 == 1 and chess_map[x+i][y+j] == 'W':
                    total1 += 1
                elif (i+j) % 2 == 1 and chess_map[x+i][y+j] == 'B':
                    total2 += 1
        if total1 < chess_sum:
            chess_sum = total1
        if total2 < chess_sum:
            chess_sum = total2

print(chess_sum)