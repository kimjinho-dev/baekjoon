def second_chk(dx,dy,di,dj,color):
    temp = [(dx,dy)]
    while 0 <= dx+di < board_size and 0 <= dy+dj < board_size:
        dx += di
        dy += dj
        if board[dx][dy] == 0:
            return []
        elif board[dx][dy] != color:
            temp.append((dx, dy))
        else:
            return temp
    return []

def first_chk(x,y,color):
    for di,dj in [[-1,-1],[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1],[0,-1]]:
        dx = x + di
        dy = y + dj
        if 0 <= dx < board_size and 0 <= dy < board_size and board[dx][dy] and board[dx][dy] != color:
            change_pos = second_chk(dx, dy, di, dj, color)
            for dx,dy in change_pos:
                board[dx][dy] = color


for test_case in range(1,int(input())+1):
    board_size, round_cnt = map(int,input().split())
    board = [[0] * board_size for _ in range(board_size)]
    board[board_size//2 - 1][board_size//2 - 1] = 2
    board[board_size // 2 - 1][board_size // 2] = 1
    board[board_size // 2][board_size // 2 - 1] = 1
    board[board_size // 2][board_size // 2] = 2

    for _ in range(round_cnt):
        x, y, color = map(int,input().split())
        board[x-1][y-1] = color
        first_chk(x-1,y-1,color)

    black, white = 0, 0
    for i in range(board_size):
        for j in range(board_size):
            if board[i][j] == 1:
                black += 1
            elif board[i][j] == 2:
                white += 1

    print(f'#{test_case} {black} {white}')