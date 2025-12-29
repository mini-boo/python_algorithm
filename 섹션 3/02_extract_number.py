N = str(input())

input_list = list(N)

extract_str = ""

for i in input_list:
    if i.isdigit():
        extract_str += i

extract_number = int(extract_str)

print(extract_number)

measure_cnt = 0
for j in range(1, extract_number+1):
    if extract_number % j == 0:
        measure_cnt += 1

print(measure_cnt)