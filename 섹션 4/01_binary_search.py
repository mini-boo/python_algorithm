N, M = map(int, input().split())
input_list = list(map(int, input().split()))
input_list.sort()

# for i in range(N):
#     if input_list[i] == M:
#         print(i+1)

left = 0
right = N-1

while left <= right:
    mid = (left+right)//2

    if input_list[mid] == M:
        print(mid+1)
        break
    elif input_list[mid] < M:
        left = mid+1
    else:
        right = mid-1