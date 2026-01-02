import math

N = int(input())
persimmon =[list(map(int, input().split())) for _ in range(N)]
M = int(input())

for i in range(M):
    a, b, c = map(int, input().split())

    if b == 0:
        persimmon[a-1] = persimmon[a-1][c:] + persimmon[a-1][:c]
    elif b == 1:
        persimmon[a-1] = persimmon[a-1][-c:] + persimmon[a-1][:-c]

sum1 = 0
n = 0
m = 0

for i in range(N):
    j = int(math.floor(N/2))

    if i == 0:
        sum1 += sum(persimmon[0])

    elif i <= j:
        n+=1
        m+=1

        sum1 += sum(persimmon[i][n:-m])

    elif i == N-1:
        sum1 += sum(persimmon[N-1])

    else:
        n-=1
        m-=1

        sum1 += sum(persimmon[i][n:-m])

print(sum1)