N = int(input())
input_list = list(map(int, input().split()))

def reverse(x):
    initial_str = str(x)
    result = ""

    for i in reversed(initial_str):
        result += i

    return int(result)

def isPrime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    # 2부터 √n까지만 확인
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

result_list = []

for i in input_list:
    reverse_input = reverse(i)
    if isPrime(reverse_input) == True:
        result_list.append(reverse_input)

print(result_list)