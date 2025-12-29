# import sys
# sys.stdin = open("input.txt", "rt") 
N = int(input())

reward = []

for i in range(0, N):
    input_list = list(map(int, input().split()))

    a = input_list[0]
    b = input_list[1]
    c = input_list[2]

    if a == b == c:
        reward.append(10000 + a*1000)
    elif a == b:
        reward.append(1000 + a*100)
    elif a == c:
        reward.append(1000 + a*100)
    elif b == c:
        reward.append(1000 + b*100)
    else:
        reward.append(max(input_list)*100)

print(max(reward))
