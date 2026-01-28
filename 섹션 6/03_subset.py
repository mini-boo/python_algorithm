n = int(input())

def dfs(level, subset):
    if level == n+1:
        if len(subset) > 0:
            # map 객체: 각 원소를 문자열로 변환
            print(' '.join(map(str, subset)))
        return
    
    # level 번째 원소를 포함하는 경우 (왼쪽 가지)
    dfs(level +1, subset + [level])

    # level 번째 원소를 포함하지 않는 경우 (오른쪽 가지)
    dfs(level + 1, subset)

dfs(1, [])