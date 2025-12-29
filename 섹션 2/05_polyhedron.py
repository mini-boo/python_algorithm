# import sys
# sys.stdin = open("input.txt", "rt") 
from collections import Counter

N, M = map(int, input().split())

sum_list = list()

#01. 정다면체에서 나올 수 있는 모든 경우의 수
for i in range(N):
    for j in range(M):
        sum_list.append((i+1)+(j+1))

#02. 경우의 수에서 공통된 요소의 최대 개수 구하기
count_value = Counter(sum_list)
max_count = max(count_value.values())

#03. 최대 개수인 공통 요소 구해서 넣기
max_count_element = list()
for i, c in count_value.items():
    if c == max_count:
        max_count_element.append(i)

print(sorted(max_count_element))