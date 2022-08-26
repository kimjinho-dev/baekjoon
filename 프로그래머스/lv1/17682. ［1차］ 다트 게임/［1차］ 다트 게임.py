def solution(word):
    word = list(word)
    nums = []
    while word:
        num = int(word.pop(0))
        if word[0] == '0':
            word.pop(0)
            num = 10
        op = word.pop(0)

        if op == 'D':
            num **= 2
        elif op == 'T':
            num **= 3

        if word and word[0] in '*#':
            bonus = word.pop(0)
            if bonus == '*':
                if nums:
                    nums[-1] *= 2
                num *= 2
            elif bonus == '#':
                num *= -1

        nums.append(num)
    return sum(nums)