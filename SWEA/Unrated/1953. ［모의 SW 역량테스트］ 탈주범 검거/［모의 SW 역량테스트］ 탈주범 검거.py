#############################
# 시작지점을 포함하여 시간안에 갈수있는 모든 위치의 개수를 출력하면된다
# 이차원 배열의 형태이며 0부터 시작하므로 별도 인덱스값 조정은 필요없다
# 시작지점은 반드시 터널이 있으므로 검증도 필요없다
# 각 번호에 따라 연결모양이 달라서 두쪽다 연결되어 있어야 이동할수있다
# 시작지점도 1시간을 소요한다
#
# 이어져있는지 검증을 할때는 현재 위치의 통로값을 기반으로 어디를 확인할지 알아본다
# 이어진곳이 0이 아니고 현재위치에서 간 방향의 반대편으로 이어져있다면(우측확인하는데 좌측이 연결된 통로라면)
# 이동이 가능한셈이다
# 만약 현재가 3이라면 왼,우만 체크할것이고 왼쪽을 체크할땐 반드시 오른쪽으로 연결이 되어있어야 이동할수있는곳이다
# 제일 간단하게 알아보는 방법은 상하좌우를 [0,0,0,0] 형식의 값으로 저장할때 상,우,하,좌 식으로 가능한것을 저장해두고
# 만약 오른쪽을 체크시 오른쪽 인덱스는 1 오른쪽에서 있어야할 인덱스는 3이므로 뭐든지 n+2%4의 형태를 만족한다
#
# 반복시 visited 처리해서 불필요한 추가는 막는다.
#############################

pipes = {
    '0': 0,
    '1': (1,1,1,1),
    '2': (1,0,1,0),
    '3': (0,1,0,1),
    '4': (1,1,0,0),
    '5': (0,1,1,0),
    '6': (0,0,1,1),
    '7': (1,0,0,1),
}


def bfs():
    cnt = 1
    while stack:
        x, y, dis = stack.pop(0)
        if dis == hours:
            return cnt

        for dx,dy,pos in [[x-1,y,0],[x,y+1,1],[x+1,y,2],[x,y-1,3]]:
            if 0 <= dx < height and 0 <= dy < width and maps[dx][dy] and not visited[dx][dy]:
                if maps[x][y][pos] and maps[dx][dy][(pos+2)%4]:
                    stack.append((dx,dy,dis+1))
                    visited[dx][dy] = True
                    cnt += 1
    return cnt

for test_case in range(1, int(input())+1):
    height, width, start_x, start_y, hours = map(int,input().split())
    maps = [input().split() for _ in range(height)]
    visited = [[False] * width for _ in range(height)]
    for i in range(height):
        for j in range(width):
            maps[i][j] = pipes[maps[i][j]]
    stack = [(start_x, start_y, 1)]
    visited[start_x][start_y] = True
    result = bfs()
    print(f'#{test_case} {result}')