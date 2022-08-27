# 이 문제는 특별하게 푸는 방식을 요구하는게 아니다.
# 정말 단순하게 3개의 벽을세우고, 바이러스를 퍼트려서 그중에서 최소값을 찾는 방식이다.
from collections import deque
di = [-1,1,0,0]
dj = [0,0,-1,1]
# 1. BFS
def bfs():
# 1_1 탐색할맵 깊은 복사 및 바이러스 수 초기화
    global max_safe_area
    # temp_maps = copy.deepcopy(maps)  # 시간초과로인한 슬라이싱으로 변환
    temp_maps = [m[:] for m in maps]
    stack = deque()
# 1_2 처음 바이러스 위치 찾기
    for i in range(N):
        for j in range(M):
            if temp_maps[i][j] == 2:
                stack.append((i,j))

# 1_3 바이러스 확산
    while stack:
        x, y = stack.popleft()
        for k in range(4):
            dx = x + di[k]
            dy = y + dj[k]
            if 0 <= dx < N and 0 <= dy < M and not temp_maps[dx][dy]:
                temp_maps[dx][dy] = 2
                stack.append((dx, dy))
    # for s in temp_maps:
    #     print(s)
    # print()
# 1_4 안전지역 찾기
    safe_area = 0
    for i in range(N):
        for j in range(M):
            if temp_maps[i][j] == 0:
                safe_area += 1

# 1_5 안전지역이 최대인지 검증
    if safe_area > max_safe_area:
        max_safe_area = safe_area


# 2. 벽세우기(세우고 BFS 호출)
def make_wall(wall_cnt):
# 2_1 벽을 3개 세우면 BFS 호출
    if wall_cnt == 3:
        # for s in maps:
        #     print(s)
        # print()
        bfs()
        return
# 2_2 for문을 돌면서 빈공간(0)이면 벽을 세우고, 벽을 세우는 함수 재귀, 그리고 다시 벽 지우기

    for i in range(N):
        for j in range(M):
            if maps[i][j] == 0:
                maps[i][j] = 1
                make_wall(wall_cnt+1)
                maps[i][j] = 0

# 3. 메인
N, M = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(N)]
max_safe_area = 0
make_wall(0)

print(max_safe_area)