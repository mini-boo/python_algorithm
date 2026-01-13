input_lst = list(input())

stack = []
cnt = 0

for i in range(len(input_lst)):
    if input_lst[i] == '(':
        stack.append(i)
    else:
        if input_lst[i-1] == '(':
            stack.pop()
            cnt += len(stack)
        else:
            stack.pop()
            cnt += 1

print(cnt)
