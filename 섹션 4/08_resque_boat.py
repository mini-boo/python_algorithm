N, M = map(int, input().split())
weight_list = list(map(int, input().split()))

weight_list.sort()  # 한 번만 정렬

boat_cnt = 0
left = 0
right = N - 1

while left <= right:
    if weight_list[left] + weight_list[right] <= M:
        left += 1   # 가벼운 사람 태움
        right -= 1  # 무거운 사람 태움
    else:
        right -= 1  # 무거운 사람만 태움
    
    boat_cnt += 1  # 어느 경우든 보트 1개 사용

print(boat_cnt)