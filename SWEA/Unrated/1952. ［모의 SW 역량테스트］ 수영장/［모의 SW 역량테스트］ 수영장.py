def buy(start,total):
    global min_total
    if total >= min_total:
        return
    if start >= 12:
        if min_total > total:
            min_total = total
        return
    
    if uses[start] * tickets[0] > tickets[1]:
        buy(start+1,total+tickets[1])
    else:
        buy(start + 1, total + uses[start] * tickets[0])

    buy(start + 3, total + tickets[2])

for test_case in range(1,int(input())+1):
    tickets = list(map(int,input().split()))
    uses = list(map(int,input().split()))
    min_total = tickets[3]
    buy(0,0)
    print(f'#{test_case} {min_total}')