N, K = map(int, input().split())
temp = list(map(int, input().split()))

# 슬라이딩 윈도우 알고리즘
temp_sum = sum(temp[:K])
max_sum = temp_sum

for idx in range(1, N-K+1):
    temp_sum -= temp[idx-1]
    temp_sum += temp[idx+K-1]

    if max_sum < temp_sum:
        max_sum = temp_sum

print(max_sum)