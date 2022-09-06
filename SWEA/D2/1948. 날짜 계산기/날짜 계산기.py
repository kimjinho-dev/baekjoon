days = [0,31,28,31,30,31,30,31,31,30,31,30,31]

def sol(m1,d1,m2,d2):
    result = d2 - d1
    for i in range(m1,m2):
        result += days[i]
    return result+1

for test_case in range(1,int(input())+1):
    print(f'#{test_case} {sol(*map(int,input().split()))}')