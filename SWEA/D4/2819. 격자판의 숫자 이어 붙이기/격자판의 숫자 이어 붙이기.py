def dfs(x,y,path,cnt):
    str_path = str(path)
    if (x,y,str_path,cnt) in process_path:
        return
    if cnt == 7:
        seven_path.add(str_path)
        return
    process_path.add((x,y,str_path,cnt))

    for dx,dy in [(x-1,y),(x,y+1),(x+1,y),(x,y-1)]:
        if 0 <= dx < 4 and 0 <= dy < 4:
            dfs(dx, dy, path + [maps[dx][dy]], cnt+1)


for test_case in range(1,int(input())+1):
    maps = [list(map(int,input().split())) for _ in range(4)]
    seven_path = set()
    process_path = set()
    for i in range(4):
        for j in range(4):
            dfs(i,j,[maps[i][j]],1)
    print(f'#{test_case} {len(seven_path)}')