def chk(node):
    if tree[node][0] == 0:
        return tree[node][2]
    else:
        # left = chk(node*2)
        # right = chk(node*2+1)
        left = chk(tree[node][0])
        right = chk(tree[node][1])
        if tree[node][2] == '+':
            return left + right
        elif tree[node][2] == '-':
            return left - right
        elif tree[node][2] == '/':
            return left / right
        else:
            return left * right


for test_case in range(1, 11):
    N = int(input())
    tree = [[0,0,0] for _ in range(N+1)]
    for _ in range(N):
        commands = input().split()  # 부모노드번호, 숫자 혹은 연산자+자식노드번호 입력
        if commands[1] in '+-*/':
            p, op, ch1, ch2 = int(commands[0]), commands[1], int(commands[2]), int(commands[3])
            tree[p] = [ch1, ch2, op]
        else:
            p, num = map(int, commands)
            tree[p][2] = num
    print(f'#{test_case} {int(chk(1))}')