import math

N = int(input())
a=[list(map(int, input().split())) for _ in range(N)]

sum1 = 0
n = 0
m = 1

for i in range(N):
    j = int(math.floor(N/2))
    
    if i == 0:
        sum1 += a[i][j]

    elif i <= j:
        n += 1
        m += 1
        sum1 += sum(a[i][j-n:j+m])

    else:
        n -= 1
        m -= 1
        sum1 += sum(a[i][j-n:j+m])

print(sum1)
        