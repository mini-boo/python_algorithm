# import sys
# sys.stdin = open("input.txt", "rt") 
from collections import Counter

N = int(input())
input_list = list(map(int, input().split()))

#자연수 자릿수의 합을 구하는 함수
def digit_sum(x):
    nums = 0
    for j in range(input_len):
        nums += int(str(input_list[i])[-j])
    
    return nums

#더한 값을 모두 리스트에 저장하고 해당 값을 비교하여 최대값의 첫 번째 인덱스 값을 프린트하는 함수
sum_list = list()

for i in range(N):
    input_len = len(str(input_list[i]))
    sum_nums = digit_sum(input_len)
    
    sum_list.append(sum_nums)

max_value = max(sum_list)

for t, x in enumerate(sum_list):
    if x == max_value:
        print(input_list[t])
        break