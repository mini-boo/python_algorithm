N = input().rstrip()
stack = []
result = ""

for i in N:
    if i.isdecimal():
        stack.append(i)
    else:
        a = stack.pop()
        b = stack.pop()

        m = "(" + b + i + a + ")"
        stack.append(m)
    
print(eval(stack[0]))