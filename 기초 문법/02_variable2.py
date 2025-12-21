''' 
변수 입력과 연산자
'''

# a=input()
# print(a)

# a, b=input("숫자를 입력하세요 : ").split() #지금 a와 b는 문자형으로 취급되고 있음
# print(a, b)

a, b=map(int, input("숫자를 입력하세요 : ").split())
print(a+b)