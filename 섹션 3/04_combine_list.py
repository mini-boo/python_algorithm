result_list = []

N = int(input())
first_list = list(map(int, input().split()))

for i in first_list:
    result_list.append(i)

M = int(input())
second_list = list(map(int, input().split()))

for j in second_list:
    result_list.append(j)

result_list.sort()

print(result_list)