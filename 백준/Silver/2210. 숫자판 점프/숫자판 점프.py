di = [-1,1,0,0]
dj = [0,0,-1,1]  # 상하좌우

def snake(now_pos,path,cnt):
    if cnt == 6:
        if not(path in path_list):
            path_list.append(path[:])
        return

    for k in range(4):
        dx = now_pos[0] + di[k]
        dy = now_pos[1] + dj[k]
        if 0 <= dx < 5 and 0 <= dy < 5:
            path += maps[dx][dy]
            snake([dx,dy],path,cnt+1)
            path.pop()

maps = [list(input().split()) for _ in range(5)]
path_list = []
for i in range(5):
    for j in range(5):
        snake([i,j],[],0)

print(len(path_list))