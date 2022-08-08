room_num = list(map(int, input()))
count = [0] * 11
max = 0

for num in room_num:
    count[num] += 1

count[6] = (count[6] + count[9]) / 2
if count[6] != int(count[6]):
    count[6] = int(count[6]) + 1
count[9] = 0

for num in count:
    if max < num:
        max = num

print(int(max))
