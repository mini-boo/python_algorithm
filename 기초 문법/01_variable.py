
# 변수
a=1
A=2
A1=3
print(a, A)

a, b= 10, 20
print(a, b)
a, b = b, a
print(a, b)

print(type(a))

a = 1.2
print(type(a))

a = "student"
print(type(a))

# 출력 방식
print("number")

a, b, c = 1, 2, 3
print(a, b, c)
print("number", a, b, c) # +를 쓰는 건 오류가 나더랑
print(a, b, c, sep=', ')
print(a, end=' ')
print(b, end=' ')
print(c)