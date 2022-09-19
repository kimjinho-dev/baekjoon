password_bit = {
    '0001101': 0,
    '0011001': 1,
    '0010011': 2,
    '0111101': 3,
    '0100011': 4,
    '0110001': 5,
    '0101111': 6,
    '0111011': 7,
    '0110111': 8,
    '0001011': 9,
}


def search_password():
    for word in words:
        for idx in range(M-1,-1,-1):
            if word[idx] == '1':
                return word[idx-55:idx+1]


def chk_password(code):
    true_codes = []
    for idx in range(0,len(code),7):
        if code[idx:idx+7] in password_bit:
            true_codes.append(password_bit[code[idx:idx+7]])
        else:
            return 0
    total = 0
    for idx,true_code in enumerate(true_codes):
        if idx % 2 == 0:
            total += true_code * 3
        else:
            total += true_code

    if total % 10 == 0:
        return sum(true_codes)
    else:
        return 0


for test_case in range(1,int(input())+1):
    N, M = map(int,input().split())
    words = [input() for _ in range(N)]
    password = search_password()
    result = chk_password(password)

    print(f'#{test_case} {result}')