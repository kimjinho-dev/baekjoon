def func(words):
    top = -1
    stack = []
    for word in words:
        top += 1
        stack.append(word)
        if top - 1 >= 0 and stack[top] == stack[top-1]:
            stack.pop()
            stack.pop()
            top -= 2
    return stack


for test_case in range(1, 11):
    N, password = input().split()
    print(f'#{test_case}', ''.join(func(password)))