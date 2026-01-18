from collections import deque

S = input().rstrip()  # 필수과목 순서
N = int(input())  # 수업설계 개수

for _ in range(N):
    T = input().rstrip()  # 수업계획
    required = deque(S)  # 각 테스트마다 필수과목 deque 새로 초기화
    
    for subject in T:
        if required and subject == required[0]:  # 다음 필수과목이 맞으면
            required.popleft()  # 제거
    
    if not required:  #required가 비어 있으면. 모두 제거되었으면.
        print("YES")
    else:
        print("NO")