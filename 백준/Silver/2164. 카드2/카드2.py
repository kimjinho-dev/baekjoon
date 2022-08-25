N = int(input())
card_que = list(range(1, N+1))              # 카드 리스트 생성

while len(card_que) > 1:
    temp = []
    if len(card_que) % 2 == 1:
        temp.append(card_que[-1])
    for i in range(1,len(card_que),2):
        temp.append(card_que[i]) 
    card_que = temp[:]
    
print(card_que[0])