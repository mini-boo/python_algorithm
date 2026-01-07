N, C = map(int, input().split())

input_list = []

for i in range(N):
    a = int(input())
    input_list.append(a)

input_list.sort()

def cnt_horse(mid):
    horse = 1
    last_position = input_list[0] #말의 마지막 위치

    for i in range(1, len(input_list)):
        if input_list[i] - last_position >= mid: #만약 i의 위치와 마지막 위치의 거리가 기준보다 크거나 같다면 말을 하나 늘리고 최종 포지션을 i로 옮긴다.
            horse += 1 
            last_position = input_list[i]
    
    return horse

left = input_list[1]-input_list[0] #최소 거리
right = input_list[-1]-input_list[0] #최대 거리
answer = 0

while left <= right:
    mid = (left+right) //2 #이진 탐색을 위한 중간

    if cnt_horse(mid) >= C:
        answer = mid
        left = mid + 1
    else:
        right = mid -1

print(answer)