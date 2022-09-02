def solution(n):
    answer = 0
    l = []
    while n > 2:
        l.append(n%3)
        n //= 3                             # 3진법 역수로 넣어주기, 
    mul = 3    
    for idx in range(len(l)-1,-1,-1):
        answer += l[idx] * mul
        mul *= 3
    
    return answer + n