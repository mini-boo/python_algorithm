N, M = map(int, input().split())

input_list = []
for i in range(N):
    a = int(input())
    input_list.append(a)

max_length = sum(input_list) // M

while True:
    line_cnt = 0
    for i in input_list:
        line_cnt += i // max_length

    if line_cnt == M:
        print(max_length)
        break
    elif line_cnt < M:
        max_length -= 1
    else:
        max_length += 1