N = int(input())
card_que = list(range(1, N+1))

while card_que:
    print(card_que.pop(0), end=' ')
    if card_que:
        card_que.append(card_que.pop(0))
    else:
        break
print()