password_bit = {
    '112': 0,
    '122': 1,
    '221': 2,
    '114': 3,
    '231': 4,
    '132': 5,
    '411': 6,
    '213': 7,
    '312': 8,
    '211': 9,
}


def make_binary():
    overlap = set()
    for word in words:
        if word in overlap:
            continue
        overlap.add(word)
        line = ""
        for w in word:
            a = bin(int(w,16))[2:]
            while len(a) < 4:
                a = '0' + a
            line += a
        binary_map.append(line)
    binary_map.pop(0)


# password 추출하기
def search_passwords(line):
    if not line:
        return
    line = line.rstrip('0')
    a = [1,1,1]
    val = 0
    is_1_first = True
    is_0_first = True
    # a 인덱스값이 0부터 시작해서 이전값이랑 바뀌는순간 1씩 추가.
    # 총 3번 바뀌면 종료되도록
    for idx in range(len(line)-1,-1,-1):
        if idx-1 >= 0 and line[idx] == line[idx-1]:
            a[val] += 1
        else:
            val += 1
        if val == 3:
            if sum(a) > 6:
                m = min(a)
                a[0] = a[0] // m
                a[1] = a[1] // m
                a[2] = a[2] // m
            passwords.insert(0,password_bit[(str(a[0]) + str(a[1]) + str(a[2]))])
            return search_passwords(line[:idx])

        # if line[idx] == '1':
        #     if is_1_first:
        #         a[0] += 1
        #     else:
        #         a[2] += 1
        #         is_0_first = False
        # else:
        #     if is_0_first:
        #         a[1] += 1
        #         is_1_first = False
        #     else:
        #         while sum(a) > 6:
        #             a[0] //= 2
        #             a[1] //= 2
        #             a[2] //= 2
        #         passwords.insert(0,password_bit[str(a[0]) + str(a[1]) + str(a[2])])
        #         return search_passwords(line[:idx])


def chk_password():
    true_codes = []
    for idx in range(0,len(passwords),8):
        if passwords[idx:idx+8] in true_codes:
            continue
        true_codes.append(passwords[idx:idx+8])

    for true_code in true_codes:
        total = 0
        for idx,n in enumerate(true_code):
            if idx % 2 == 0:
                total += n * 3
            else:
                total += n

        if total % 10 == 0:
            result.append(sum(true_code))


for test_case in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    words = [input()[:M] for _ in range(N)]
    binary_map = []
    passwords = []
    result = []
    make_binary()
    for l in binary_map:
        search_passwords(l)
    chk_password()
    print(f'#{test_case} {sum(result)}')