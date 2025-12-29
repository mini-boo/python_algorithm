import math

N = int(input())

for i in range (0, N):
    input_data = str(input()).lower()
    input_list = list(input_data)

    false_cnt = 0
    
    for j in range (0, math.floor(len(input_list)/2)):
        if input_list[j] != input_list[-j-1]:
            false_cnt += 1
    
    if false_cnt == 0:
        print("#", i+1, " YES")
    else:
        print("#", i+1, " NO")