N, r, c = map(int, input().split())
start = 0

while N != 1:
    if r < 2 ** (N - 1):
        if c < 2 ** (N - 1):
            pass
        else:
            start += (2 ** (2 * N)) / 4
            c = c - (2 ** (N - 1))
    else:
        if c < 2 ** (N - 1):
            start += (2 ** (2 * N)) / 4 * 2
            r = r - (2 ** (N - 1))
        else:
            start += (2 ** (2 * N)) / 4 * 3
            r = r - (2 ** (N - 1))
            c = c - (2 ** (N - 1))
    N -= 1

start = int(start)

if r == 0 and c == 0:
    print(start)
elif r == 0 and c == 1:
    print(start + 1)
elif r == 1 and c == 0:
    print(start + 2)
elif r == 1 and c == 1:
    print(start + 3)
