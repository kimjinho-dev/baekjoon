di = [-1,1,0,0]
dj = [0,0,-1,1]

def solution(places):
    result = []

    for maps in places:
        is_end = False
        people = []

        for i in range(5):
            for j in range(5):
                if maps[i][j] == 'P':
                    people.append([i,j])

        if not(people):
            result.append(1)
            continue

        for x_y in people:
            if not(is_end):
                x = x_y[0]
                y = x_y[1]
                for n in range(4):
                    if not(is_end):
                        vx = x + di[n]
                        vy = y + dj[n]
                        if 0 <= vx < 5 and 0 <= vy < 5:
                            if maps[vx][vy] == 'O':
                                for k in range(4):
                                    vx_2 = vx + di[k]
                                    vy_2 = vy + dj[k]
                                    if 0 <= vx_2 < 5 and 0 <= vy_2 < 5 and not(vx_2 == x and vy_2 == y):
                                        if maps[vx_2][vy_2] == 'P':
                                            result.append(0)
                                            is_end = True
                                            break
                            elif maps[vx][vy] == 'P':
                                result.append(0)
                                is_end = True
                                break
                    else:
                        break
            else:
                break
        else:
            result.append(1)
    return result