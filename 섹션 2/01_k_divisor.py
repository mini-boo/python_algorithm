# import sys
# sys.stdin = open("input.txt", "rt") 

N = int(input())
K = int(input())

result = list()
for i in range (1, N+1):
    if N % i == 0 :
        result.append(i)

if(len(result) < K):
    print(-1)
else :
    print(result[K-1])

