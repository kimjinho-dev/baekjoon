L, R = input().split()
min_eight = 0
front_check = 0
for idx in range(len(L)):
    if len(L) < len(R):
        break
    if L[idx] == R[idx] and L[idx] == '8':
        if front_check != 1:
            min_eight += 1
    elif L[idx] != R[idx]:
        front_check = 1
print(min_eight)