di = {"left": 0, "up": -1, "right": 0}
dj = {"left": -1, "up": 0, "right": 1}


for _ in range(10):
    test_case = input()
    ladders = [
        [0] + list(map(int, input().split())) + [0] for _ in range(100)
    ]  # 앞뒤 1칸씩 빈값 추가 100칸->102칸
    DIR = "up"  # 초기 방향은 위쪽

    for idx in range(102):
        if ladders[99][idx] == 2:
            end_y = idx
            break  # 마지막 줄에서 2 있는 열 찾기

    x_idx = 98
    y_idx = end_y  # 한칸위로 이동했다는 가정하에, 행은 98부터 열은 2가있는 열로 시작
    while x_idx:  # 행값 0 즉 처음으로 오면 종료
        left_1 = ladders[x_idx][y_idx - 1]
        right_1 = ladders[x_idx][y_idx + 1]  # 좌측 우측값 변수화

        if DIR == "up":
            if left_1:
                DIR = "left"
            elif right_1:
                DIR = "right"  # 위로 이동중에 좌우에 막대가있다면, 그쪽 방향으로 방향을 전환
        elif DIR == "right" and not right_1:
            DIR = "up"  # 우로 이동중에 이동할 다음칸이 없다면, 위쪽 방향으로 전환
        elif DIR == "left" and not left_1:
            DIR = "up"  # 좌로 이동중에 이동할 다음칸이 없다면, 위쪽 방향으로 전환

        x_idx += di[DIR]
        y_idx += dj[DIR]  # 델타값 이동

    print(f'#{test_case} {y_idx-1}')  # 앞에 1개를 추가했기때문에 정상출력을 위해 -1