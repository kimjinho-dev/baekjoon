def back(word):
    stack = []
    result = ''
    for token in word:
        if token in '()+*':
            if not token or token == '(':
                stack.append(token)
            elif token == '+':
                while stack and stack[-1] != '(':
                    result += stack.pop()
                stack.append(token)
            elif token == '*':
                while stack and stack[-1] == '*':
                    result += stack.pop()
                stack.append(token)
            else:
                while stack[-1] != '(':
                    result += stack.pop()
                stack.pop()
        else:
            result += token

    while stack:
        result += stack.pop()

    return result

def cal(back_word):
    stack = []
    for token in back_word:
        if token in '+*':
            a = int(stack.pop())
            b = int(stack.pop())
            if token == '+':
                stack.append(b+a)
            else:
                stack.append(b*a)
        else:
            stack.append(token)

    return stack[-1]


for test_case in range(1,11):
    N = int(input())
    print(f'#{test_case} {cal(back(input()))}')