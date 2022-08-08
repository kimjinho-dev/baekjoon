# import sys

# sys.stdin = open("input.txt")

for test_case in range(1, 11):
    width = int(input())
    building_list = list(map(int, input().split()))
    now_idx = 2  # 앞 2칸은 무시
    niceview_count = 0  # 좋은 전망 주택수 카운트 변수

    while now_idx < width - 2:  # 마지막 2곳 확인 X
        max_height = 0
        for add_idx in [-2, -1, 1, 2]:
            if max_height < building_list[now_idx + add_idx]:
                max_height = building_list[now_idx + add_idx]
        '''
        현재 위치에서 양옆 2칸에 있는 빌딩의 높이중 제일 높은값 검색
        '''
        if max_height < building_list[now_idx]:
            niceview_count += building_list[now_idx] - max_height
            now_idx += 3
            continue
        '''
        인접 2칸의 빌딩의 높이가 현재 빌딩보다 낮다면, 그 둘의 차이를 카운트 변수에 추가.
        인접 2칸보다 높기만 하다면 그곳이 좋은 전망.
        
        해당 if문이 작동한다면 해당 빌딩은 인접 2칸내에 제일 높은 빌딩이므로 우측 2칸 빌딩은
        무조건 좋은 전망이 없다. 따라서 now_idx에 3을 추가하여 조회 간소화
        '''
        now_idx += 1  # 검색되지 않는다면 다음칸으로 이동

    print(f'#{test_case} {niceview_count}')
