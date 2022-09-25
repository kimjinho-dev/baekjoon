from collections import deque

def f(num,rotation,pos):
    if 0 <= num < 4 and maps[num][2 * -1 * pos] != maps[num-pos][2 * pos]:
        f(num+pos, rotation * -1, pos)
        maps[num].rotate(rotation)

for test_case in range(1,int(input())+1):
    actions = int(input())
    maps = [deque(map(int,input().split())) for _ in range(4)]
    for _ in range(actions):
        num, rotation = map(int,input().split())
        num -= 1
        f(num-1, rotation * -1, -1)
        f(num+1, rotation * -1, 1)
        maps[num].rotate(rotation)

    result = maps[0][0]+maps[1][0]*2+maps[2][0]*4+maps[3][0]*8
    print(f'#{test_case} {result}')