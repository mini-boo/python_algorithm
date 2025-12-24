N = int(input())
input_list = list(map(int, input().split()))

sum_cnt = 0
plus_cnt = 1

for i in range(N):
    if i == 0:
        if input_list[i] == 1:
            sum_cnt += 1
    else:
        if input_list[i] == input_list[i-1] == 1:
            plus_cnt += 1
            sum_cnt += plus_cnt

        elif input_list[i] == 1 and input_list[i] != input_list[i-1]:
            sum_cnt += 1
            plus_cnt = 1

print(sum_cnt)