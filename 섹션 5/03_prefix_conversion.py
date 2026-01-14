e = input().rstrip()
stack = list()
result = ""

for i in e:
    # 1. 숫자(피연산자)인 경우: 바로 결과에 추가
    if i.isdecimal():
        result += i
        
    else:
        # 2. 여는 괄호인 경우: 우선순위가 가장 높으므로 일단 스택에 넣음
        if i == '(':
            stack.append(i)
            
        # 3. 곱셈, 나눗셈인 경우 (높은 우선순위)
        elif i == '*' or i == '/':
            # 스택의 맨 위가 곱셈이나 나눗셈이면, 걔네를 먼저 처리(pop)해야 함
            while len(stack) > 0:
                top = stack[-1]
                if top == '*' or top == '/':
                    result += stack.pop()
                else:
                    # 더 이상 나보다 우선순위가 높거나 같은게 없으면 멈춤
                    break
            stack.append(i)
            
        # 4. 덧셈, 뺄셈인 경우 (낮은 우선순위)
        elif i == '+' or i == '-':
            # 스택에 들어있는 '여는 괄호' 전까지의 모든 연산자는 나보다 우선순위가 높거나 같음
            while len(stack) > 0:
                top = stack[-1]
                if top == '(':
                    # 괄호 안쪽까지만 처리해야 하므로 여는 괄호를 만나면 멈춤
                    break
                else:
                    # 괄호 밖의 모든 연산자를 끄집어내서 결과에 추가
                    result += stack.pop()
            stack.append(i)
            
        # 5. 닫는 괄호인 경우
        elif i == ')':
            # 여는 괄호를 만날 때까지 스택의 연산자들을 모두 꺼냄
            while len(stack) > 0:
                top = stack[-1]
                if top == '(':
                    stack.pop() # 여는 괄호 자체는 결과에 넣지 않고 버림
                    break
                else:
                    result += stack.pop()

# 6. 모든 입력 처리가 끝난 후 스택에 남아있는 연산자들을 순서대로 꺼냄
while len(stack) > 0:
    result += stack.pop()

print(result)