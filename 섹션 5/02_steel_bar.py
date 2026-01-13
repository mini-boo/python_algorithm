input_lst = list(input())

stack = []
cnt = 0

for i in range(len(input_lst)):
    if input_lst[i] == '(':
        stack.append(i)
    else:
        stack.pop()
        if input_lst[i-1] == '(':
            cnt += len(stack)
        else:
            cnt += 1

print(cnt)
