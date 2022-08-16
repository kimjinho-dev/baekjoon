def solution(arr):
    arr.remove(min(arr))
    if len(arr):
        answer = arr
    else:
        answer = [-1]
    return answer