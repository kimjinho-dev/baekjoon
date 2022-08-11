T = int(input())

for tese_case in range(1,T+1):
    puzzle_len, word_len = map(int, input().split())
    puzzle_map = [list(map(int, input().split())) for _ in range(puzzle_len)]
    correct_count = 0
    row_len = 0
    col_len = [0]*puzzle_len

    for i in range(puzzle_len):
        row_len = 0
        for j in range(puzzle_len):
            row_len += puzzle_map[i][j]
            col_len[j] += puzzle_map[i][j]

            if j == puzzle_len-1 or puzzle_map[i][j+1] == 0:
                if row_len == word_len:
                    correct_count += 1
                row_len = 0

            if i == puzzle_len-1 or puzzle_map[i+1][j] == 0:
                if col_len[j] == word_len:
                    correct_count += 1
                col_len[j] = 0

    print(f'#{tese_case} {correct_count}')