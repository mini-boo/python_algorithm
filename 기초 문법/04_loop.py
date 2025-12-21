'''
반복문(for, while)
'''

# a=range(10)
# print(a)
# print(list(a))

# for i in range(10):
#     print("hello")

# for i in range(10):
#     print(i)

# for i in range(1, 11):
#     print(i)

# for i in range(10, 0): #아무 일도 안 일어남
#     print(i) 

# for i in range(10, 0, -1):
#     print(i) 

# i=1
# while i<=10:
#     print(i)
#     i=i+1

# i=10
# while i>=1:
#     print(i)
#     i=i-1

# i=1
# while True:
#     print(i)
#     if i==10:
#         break
#     i+=1

# for i in range(1, 11):
#     if i%2==0:
#         continue
#     print(i)

# for i in range(1, 11):
#     print(i)
#     if i==5:
#         break
#     else:
#         print(11)

a=int(input())

# 홀수 구하기
# for i in range(1, a+1):
#     if(i%2 == 1):
#         print(i)

#1부터 N까지 합을 구하기
# sum=0

# for i in range(1, a+1):
#     sum += sum+i
#     print(sum)

#n의 약수 출력하기
for i in range(1, a+1):
    if a%i == 0:
        print(i, end=' ')

    
