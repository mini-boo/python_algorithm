N = int(input())

box_list = list(map(int, input().split()))


M = int(input())
for i in range(M):
    box_list.sort()
    
    box_list[-1] -= 1  # 최댓값 1 감소
    box_list[0] += 1   # 최솟값 1 증가

print(max(box_list) - min(box_list))