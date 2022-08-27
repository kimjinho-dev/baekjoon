import sys
from collections import deque
# import copy
# input = sys.stdin.readline



def turn(line):
    for l in line:
        if l != 0:
            l2 = 2**l
            board1 = [[] for _ in range(N2)]
            for n in range(0, N2, l2):
                for j in range(N2):
                    for i in range(l2 - 1, -1, -1):
                        board1[j % (l2) + n].append(board[i + n][j])
        else:
            board1 = [item[:] for item in board]
        melt(board1)
    return


def melt(board2):
    global board
    board = [item[:] for item in board2]
    for i in range(N2):
        for j in range(N2):
            if board2[i][j] > 0:
                cnt = 0
                for n in range(len(dx)):
                    mx, my = i + dx[n], j + dy[n]
                    if 0 <= mx < 2 ** N and 0 <= my < 2 ** N and board2[mx][my] > 0:
                        cnt += 1
                    if cnt == 3:
                        break
                if cnt < 3:
                    board[i][j] -= 1
    return


# def chk(x, y):
#     global cnt
#     visit[x][y] = True
#     cnt += 1
#     for n in range(len(dx)):
#         mx, my = x + dx[n], y + dy[n]
#         if 0 <= mx < 2 ** N and 0 <= my < 2 ** N and board[mx][my] != 0 and not visit[mx][my]:
#             chk(mx, my)
#     return


def chk(i, j):
    cnt = 0
    queue = deque([(i, j)])
    visit[i][j] = True
    while queue:
        x, y = queue.popleft()
        cnt += 1
        for n in range(len(dx)):
            mx, my = x + dx[n], y + dy[n]
            if 0 <= mx < 2 ** N and 0 <= my < 2 ** N and board[mx][my] != 0 and not visit[mx][my]:
                visit[mx][my] = True
                queue.append((mx, my))
    return cnt



dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


N, Q = map(int, input().split())
N2 = 2**N
board = [list(map(int, input().split())) for _ in range(N2)]
visit = [[False] * N2 for _ in range(N2)]
L = list(map(int, input().split()))
turn(L)
highest_cnt = 0
for i in range(N2):
    for j in range(N2):
        if board[i][j] != 0 and not visit[i][j]:
            # cnt = 0
            # chk(i, j)
            cnt = chk(i, j)
            if highest_cnt < cnt:
                highest_cnt = cnt
print(sum(list(map(sum, board))))
print(highest_cnt)


