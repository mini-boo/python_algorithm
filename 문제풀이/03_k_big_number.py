# import sys
# sys.stdin = open("input.txt", "rt") 
import random
import math

N, K = map(int, input().split())
input_list = list(map(int, input().split()))

result_list = list()

for i in range(math.comb(N, 3)): #N장에서 3개 뽑는 경우의 수
    sum_obj = sum(random.sample(input_list, 3)) #랜덤 뽑기
    result_list.append(sum_obj)

result = sorted(result_list)

print(result[-K])