from collections import deque

n, k = map(int, input().split())
m = list(map(int, input().split()))

queue = deque([(m[i], i) for i in range(n)]) #큐에 튜플로 저장
cnt = 0

while queue:
    current = queue.popleft() #현재 큐(위험도, 순번)

    if any(current[0] < q[0] for q in queue): #큐에 있는 문서들 중에서 현재 문서보다 우선순위가 높은 문서가 하나라도 있는지 검색
        queue.append(current) #우선 순위가 더 높은 게 있으면 뒤로 보냄
    else:
        cnt += 1 #카운트 늘림
        if current[1] == k: #만약 원하는 인덱스가 같으면
            print(cnt) #카운트 출력
            break #끝
