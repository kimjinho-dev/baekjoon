maps = [input() for _ in range(8)]
white = list(range(0,16,2))
total = 0
# 하얀칸은 왼쪽위 기준으로 번갈아가면서 칠해져있다.
for i in range(8):
    for j in range(8):
        if i+j in white and maps[i][j] == 'F':
            total += 1
print(total)