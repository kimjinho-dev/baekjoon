def solution(numbers, hand):
    answer = ''
    maps = [[3,1],[0,0],[0,1],[0,2],[1,0],[1,1],[1,2],[2,0],[2,1],[2,2],[3,0],[3,2]]
    left = 10
    right = 11

    while numbers:
        action = numbers.pop(0)
        if action in [1,4,7]:
            left = action
            answer += 'L'
        elif action in [3,6,9]:
            right = action
            answer += 'R'
        else:
            left_idx = maps[left]
            right_idx = maps[right]
            action_idx = maps[action]
            left_distance = abs(action_idx[0] - left_idx[0]) + abs(action_idx[1] - left_idx[1])
            right_distance = abs(action_idx[0] - right_idx[0]) + abs(action_idx[1] - right_idx[1])
            if left_distance == right_distance:
                if hand == 'right':
                    right = action
                    answer += 'R'
                else:
                    left = action
                    answer += 'L'
            elif left_distance > right_distance:
                right = action
                answer += 'R'
            else:
                left = action
                answer += 'L'

    return answer