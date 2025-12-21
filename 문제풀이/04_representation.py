# import sys
# sys.stdin = open("input.txt", "rt") 

N = int(input())
input_list = list(map(int, input().split()))

#01. 평균 구하기
avg_score = int(round(sum(input_list) / N, 0))

# 평균과 값 비교하기
closer_score = int()
closer_index = int()
closer_abs = 100000

for i in range(N):
    #평균값 차이 절댓값 구하기
    j = abs(avg_score - input_list[i])

    #학생의 점수가 평균값에 더 가까운 경우
    if j < closer_abs:
        closer_abs = j
        closer_score = input_list[i]
        closer_index = i+1
    
    #학생의 점수가 평균값 차이와 같은 경우
    elif j == closer_abs:
        closer_abs = j

        #점수 비교
        if input_list[i] > closer_score:
            closer_score = input_list[i]
            closer_index = i+1
        
        #점수가 같은 경우
        elif input_list[i] == closer_score:
            #학생 번호 비교 (이때 i는 +1을 해줘야 실제 번호와 일치시킬 수 있음!)
            if i+1 < closer_index:
                closer_score = input_list[i]
                closer_index = i+1

print(avg_score, closer_index)