N = int(input())

c_time = []
for i in range(N):
    X, Y = map(int, input().split())
    a = (X, Y)
    c_time.append(a)

c_time.sort(key=lambda x: (x[1], x[0]))

c_cnt = 1
end_time = c_time[0][1]

for i in range(1, N):
    if c_time[i][0] >= end_time:  # 다음 회의가 현재 회의 종료 후 시작
        c_cnt += 1
        end_time = c_time[i][1]  # 종료시간 갱신

print(c_cnt)