N, M = map(int, input().split())
input_list = list(map(int, input().split()))

left = max(input_list) #dvd 용량은 최소 max분이어야 함
right = sum(input_list) #dvd 용량은 최대 sum일 수 있음
answer = 0

def count_dvd(mid):
    dvd_count = 1
    current_sum = 0
    
    for song in input_list:
        if current_sum + song > mid:
            dvd_count += 1
            current_sum = song
        else:
            current_sum += song
    
    return dvd_count

while left <= right:
    mid = (left + right) // 2
    
    # mid 크기의 DVD로 M개 이하로 녹화 가능한지 확인
    if count_dvd(mid) <= M:
        answer = mid
        right = mid - 1
    else:
        left = mid + 1

print(answer)