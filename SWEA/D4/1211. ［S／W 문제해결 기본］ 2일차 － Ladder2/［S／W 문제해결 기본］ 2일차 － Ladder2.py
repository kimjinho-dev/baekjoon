def chk(row,col,dis,pos):
    global min_dis,min_idx
    if row == 0:
        if min_dis > dis:
            min_dis = dis
            min_idx = col
        return

    if pos != 3 and 0 <= col - 1 < 100 and maps[row][col-1] == '1':
        chk(row, col-1, dis+1,1)
    elif pos != 1 and 0 <= col + 1 < 100 and maps[row][col+1] == '1':
        chk(row, col+1, dis+1,3)
    else:
        chk(row-1, col, dis+1,2)


for _ in range(10):
    test_case = int(input())
    maps = [input().split() for _ in range(100)]
    dis_list = []
    min_idx = 0
    min_dis = 100000
    for j in range(100):
        if maps[99][j] == '1':
            chk(99,j,0,2)
    print(f'#{test_case} {min_idx}')