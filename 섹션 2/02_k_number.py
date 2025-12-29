# import sys
# sys.stdin = open("input.txt", "rt") 

#주의 사항 : 입력값 처리하는 방법 기억하기 / 기존 리스트에 .sort()는 사용할 수 없으니 sorted() 를 사용하기
T= int(input())

for t in range(T):
    N, s, e, k = map(int, input().split())
    input_list = list(map(int, input().split()))

    result_list  = sorted(input_list[s-1:e-1])
    print(result_list[k-1])