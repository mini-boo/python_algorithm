N = int(input())

player = []
for i in range(N):
    X, Y = map(int, input().split())
    player.append((X, Y))

player.sort(reverse=True)

p_cnt = 0
largest = 0
for x, y in player:
    if y > largest:
        largest = y
        p_cnt += 1
        
print(p_cnt)