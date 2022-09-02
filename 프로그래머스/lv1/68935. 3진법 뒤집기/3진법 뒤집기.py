def solution(n):
    l = []
    while n > 2:
        if l:
            l.append(n%3)
            for idx in range(len(l)-1):
                l[idx] *= 3
        else:
            l.append(n%3)
        n //= 3
    for idx in range(len(l)):
        l[idx] *= 3   
    answer = sum(l) + n
    return answer