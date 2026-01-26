N = int(input())
M = str()

while N > 0:
    M += str(N%2)
    N = N//2

print(M)