'''
리스트와 내장함수
'''

import random as r

# a = []
# b=list()
# print(a)
# print(b)

# a=[1, 2, 3, 4, 5]

# b=list(range(1, 11))
# print(b)

# c=a+b
# print(c)

# print(a)
# a.append(6)
# print(a)

# a.insert(3, 7)
# print(a)

# a.pop()
# print(a)

# a.remove(4) #인덱스가 아니라 값을 찾아서 삭제 함
# print(a)

# print(a.index(5))

# a = list(range(1,11))
# print(sum(a))
# print(max(a))
# print(min(a))
# print(min(7, 5))


# r.shuffle(a)
# print(a)

# a.sort()
# print(a)

# a.sort(reverse=True)
# print(a)

# a.clear()
# print(a)

a = [23, 12, 36, 53, 19]
# print(a[:2])

# for i in range(len(a)):
#     print(a[i], end=' ')
    
# print()

# for x in a:
#     if x%2 == 1:
#      print(x, end=' ')

# for x in enumerate(a):
#     print(x)

# b = (1, 2, 3, 4, 5)
# print(b[0])
# b[0] = 7 # 이러면 에러가 남. 튜플은 변경이 불가능하기 때문에

for x in enumerate(a):
    print(x[0], x[1])

# print()

# for index, value in enumerate(a):
#     print(index, value)

# if all(60>x for x in a):
#     print("YES")
# else:
#     print("NO")
