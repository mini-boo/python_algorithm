a = [list(map(int, input().split())) for _ in range(7)]

result_cnt = 0

row1 = []
for i in a:
    row1 = i
    for j in range(3):
        if row1[j] == row1[j+4] and row1[j+1]==row1[j+3]:
                result_cnt +=1

c = -1
for i in range(7):
    c+= 1
    row2 = []
    for j in range(7):
        row2.append(a[j][c])

    for x in range(3):
         if row2[x] == row2[x+4] and row2[x+1]==row2[x+3]:
              result_cnt += 1

print(result_cnt)