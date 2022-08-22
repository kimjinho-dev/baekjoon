def back(word):
    op_stack = []
    result = ''
    for s in word:
        if s in '+-()/*':
            if not op_stack or s == '(':
                op_stack.append(s)
            elif s in '+-':
                while op_stack and op_stack[-1] != '(':
                    result += op_stack.pop()
                op_stack.append(s)

            elif s in '*/':
                while op_stack and op_stack[-1] in '*/':
                    result += op_stack.pop()
                op_stack.append(s)

            elif s == ')':
                while op_stack and op_stack[-1] != '(':
                    result += op_stack.pop()
                op_stack.pop()
        else:
            result += s

    while op_stack:
        result += op_stack.pop()

    return result


def calculator(word):
    stack = []
    for s in word:
        if s in '+-*/':
            a = stack.pop()
            b = stack.pop()
            if s == '+':
                stack.append(a+b)
            elif s == '-':
                stack.append(a-b)
            elif s == '*':
                stack.append(a*b)
            else:
                stack.append(a/b)
        else:
            stack.append(int(s))
    return stack[-1]

for tese_case in range(1,11):
    amount = int(input())
    back_op = back(input())
    print(f'#{tese_case} {calculator(back_op)}')