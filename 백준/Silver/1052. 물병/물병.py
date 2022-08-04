N, K = map(int, input().split())
N_bin = bin(N)[2:]
N_bin_reserve = N_bin[::-1]
buy_bottle = 0
while 1:
    if N_bin.count('1') > K:
        idx = N_bin_reserve.index('1')
        buy_bottle += 2**idx
        N = int(N_bin, 2) + 2**idx
        N_bin = bin(N)[2:]
        N_bin_reserve = N_bin[::-1]
    else:
        break

print(buy_bottle)