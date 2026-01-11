N = int(input())

input_list = list(map(int, input().split()))

ra = []
cnt = N

while cnt > 0:
    print(input_list[cnt-1])
    ra.insert(input_list[cnt-1], cnt)
    cnt -= 1

for x in ra:
    print(x,end= ' ')