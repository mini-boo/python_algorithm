N = int(input())

a = [[0]*(N+2) for _ in range(N+2)]

for i in range(N):
    data = list(map(int, input().split()))
    for j in range(N):
        a[i+1][j+1] = data[j]

result_cnt = 0

for i in range(1, N+1):
    for j in range(1, N+1):
        if a[i][j] > a[i-1][j] and a[i][j] > a[i][j-1] and a[i][j] > a[i][j+1] and a[i][j] > a[i+1][j]:
            result_cnt += 1

print(result_cnt)