def solution(a, b):
    day = ['SUN','MON','TUE','WED','THU','FRI','SAT']
    month = [31,29,31,30,31,30,31,31,30,31,30,31]
    answer = day[(sum(month[0:a-1]) + b - 1 + 5) % 7]
    
    return answer