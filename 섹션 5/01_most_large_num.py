N, M = map(int, input().split())

N = str(N)
stack = []
remove_count = M

for digit in N:
    # 스택의 마지막 숫자가 현재 숫자보다 작으면 제거
    while stack and remove_count > 0 and stack[-1] < digit:
        stack.pop()
        remove_count -= 1
    stack.append(digit)

# 아직 제거할 개수가 남았다면 뒤에서부터 제거
if remove_count > 0:
    stack = stack[:-remove_count]

print(''.join(stack))