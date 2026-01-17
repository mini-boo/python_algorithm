from collections import deque

n, k = map(int, input().split())

queue = deque(range(1, n+1))

while len(queue) > 1:
    for _ in range(k-1): #k-1번 회전해서 k번째 사람 찾기
        queue.append(queue.popleft()) #더 앞에 있는 사람은 큐 뒤로 밀어버리기
    queue.popleft() #k번째 사람을 큐에서 제거하기
    
print(queue[0])