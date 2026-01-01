N, M = map(int, input().split())

input_list = list(map(int, input().split()))

result_cnt = 0

for i in range (0, N):
    for j in range (0, N):
        if sum(input_list[i:j]) == M:
            result_cnt += 1

print(result_cnt)