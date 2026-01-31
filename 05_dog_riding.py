x, n = map(int, input().split())
m = []

for i in range (n):
    a = int(input())
    m.append(a)

result_list = []

def dfs(level, subset):
    if level == n:
        if len(subset) > 0:
            result_list.append(sum(subset))
        return
    
    # level 번째 원소를 포함하는 경우 (왼쪽 가지)
    dfs(level +1, subset + [m[level]])

    # level 번째 원소를 포함하지 않는 경우 (오른쪽 가지)
    dfs(level + 1, subset)

dfs(0, [])

max = 0

for i in result_list:
    if i > max and i <= x:
        max = i

print(max)