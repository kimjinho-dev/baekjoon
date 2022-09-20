def search_2(wrong_2):
    total = int(wrong_2,2)
    wrong_2 = wrong_2[::-1]
    for idx in range(len(wrong_2)):
        if wrong_2[idx] == '0':
            possible_nums.add(total+2**idx)
        else:
            possible_nums.add(total-2**idx)


def search_3(wrong_3):
    total = int(wrong_3, 3)
    wrong_3 = wrong_3[::-1]
    for idx in range(len(wrong_3)):
        if wrong_3[idx] == '0':
            if total+3**idx in possible_nums:
                return total+3**idx
            elif total+2*(3**idx) in possible_nums:
                return total+2*(3**idx)
        if wrong_3[idx] == '1':
            if total-3**idx in possible_nums:
                return total-3**idx
            elif total+3**idx in possible_nums:
                return total+3**idx
        else:
            if total-3**idx in possible_nums:
                return total-3**idx
            elif total-2*(3**idx) in possible_nums:
                return total-2*(3**idx)


for test_case in range(1,int(input())+1):
    possible_nums = set()
    search_2(input())
    result = search_3(input())
    print(f'#{test_case} {result}')
