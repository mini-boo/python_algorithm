a = [list(map(int, input().split())) for _ in range(9)]
false_cnt = 0

# 9개의 3*3 블록을 모두 검사
for block_i in range(3):
    for block_j in range(3):
        # 각 블록의 시작 좌표
        start_i = block_i * 3
        start_j = block_j * 3
        
        # 3*3 블록 추출
        block = []
        for i in range(start_i, start_i + 3):
            for j in range(start_j, start_j + 3):
                block.append(a[i][j])
        
        # 중복 검사
        if len(block) != len(set(block)):
            false_cnt += 1

#행에서 중복 비교
for i in a:
    if len(i) != len(set(i)):
        false_cnt += 1

#열에서 중복 비교
c = -1
for i in range(9):
    c+= 1
    row_list = []
    for j in range(9):
        row_list.append(a[j][c])
    
    if len(row_list) != len(set(row_list)):
        false_cnt += 1

if false_cnt == 0:
    print("YES")
else:
    print("NO")
    