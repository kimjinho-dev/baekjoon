def solution(n, arr1, arr2):
    answer = []

    for i in range(n):
        line = ""
        for k in range(n-1,-1,-1):
            if arr1[i] & (1 << k) or arr2[i] & (1 << k):
                line += "#"
            else:
                line += " "
        answer.append(line)
    return answer