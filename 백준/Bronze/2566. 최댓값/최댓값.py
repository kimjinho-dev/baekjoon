size = 9
maps = [list(map(int,input().split())) for _ in range(size)]
max_num = 0

for i in range(size):
    for j in range(size):
        if max_num <= maps[i][j]:
            max_num = maps[i][j]
            pos_i = i+1
            pos_j = j+1

print(max_num)
print(pos_i,pos_j)