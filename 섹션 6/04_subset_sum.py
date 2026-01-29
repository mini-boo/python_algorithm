n = int(input())
m = list(map(int, input().split()))

result_list = []

def dfs(level, subset):
    if level == n:
        if len(subset) > 0:
            # map 객체: 각 원소를 문자열로 변환
            result_list.append(sum(subset))
        return
    
    # level 번째 원소를 포함하는 경우 (왼쪽 가지)
    dfs(level +1, subset + [m[level]])

    # level 번째 원소를 포함하지 않는 경우 (오른쪽 가지)
    dfs(level + 1, subset)

dfs(0, [])

if len(result_list) != len(set(result_list)):
    print("YES")
else:
    print("NO")