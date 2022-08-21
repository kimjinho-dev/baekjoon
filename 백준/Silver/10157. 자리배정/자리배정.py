di = [-1,0,1,0] # 상우하좌
dj = [0,1,0,-1]


def snail(search_num):
    k = 0  # 처음 방향은 위쪽
    cnt = 1
    i, j = row-1, 0
    while cnt:
        maps[i][j] = cnt
        if 0 <= i+di[k] < row and 0 <= j+dj[k] < col and not(maps[i+di[k]][j+dj[k]]):
            pass
        else:
            k = (k+1) % 4
        if search_num == cnt:
            x = j + 1
            y = row - i
            return x, y
        i += di[k]
        j += dj[k]
        cnt += 1
    return 0


col,row = map(int,input().split())
num = int(input())
maps = [[0] * col for _ in range(row)]
if num > col*row:
    print(0)
else:
    print(*snail(num))