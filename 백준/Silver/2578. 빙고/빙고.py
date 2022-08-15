player_bingo = [list(map(int, input().split())) for _ in range(5)]
answer_bingo = []
for _ in range(5):
    a, b, c, d, e = map(int, input().split())
    answer_bingo.append(a)
    answer_bingo.append(b)
    answer_bingo.append(c)
    answer_bingo.append(d)
    answer_bingo.append(e)
cnt = 0

while cnt != 25:
    for i in range(5):
        for j in range(5):
            if player_bingo[i][j] == answer_bingo[cnt]:
                player_bingo[i][j] = 'X'

    diag_1, diag_2 = 0, 0
    bingo_cnt = 0

    for i in range(5):
        col = 0
        if player_bingo[i].count('X') == 5:
            bingo_cnt += 1
        for j in range(5):
            if player_bingo[j][i] == 'X':
                col += 1
            if i == j and player_bingo[i][j] == 'X':
                diag_1 += 1
            if i + j == 4 and player_bingo[i][j] == 'X':
                diag_2 += 1
        if col == 5:
            bingo_cnt += 1

    if diag_1 == 5:
        bingo_cnt += 1
    if diag_2 == 5:
        bingo_cnt += 1

    cnt += 1
    if bingo_cnt >= 3:
        break

print(cnt)