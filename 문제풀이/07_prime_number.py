#01. 1안(매우 느리고 성능이 좋지 않음... 숫자 커지면 미친듯이 돌아가더라)
# N = int(input())

# def is_prime(x):
#     true_cnt = 0
#     false_cnt = 0

#     for i in x:
#         if i == True:
#             true_cnt += 1
#         else:
#             false_cnt += 1
    
#     if true_cnt == 2:
#         return True
#     else:
#         return False

# prime_number_count = 0

# for i in range(2, N+1):
#     prime_number_list = list()

#     for j in range(1, i+1):
#         if i%j == 0:
#             prime_number_list.append(True)
#         else:
#             prime_number_list.append(False)
    

#     if is_prime(prime_number_list) == True:
#         prime_number_count += 1

# print(prime_number_count)

#02. 2안 리팩토링
# N = int(input())

# def is_prime(n):
#     if n < 2:
#         return False
#     if n == 2:
#         return True
#     if n % 2 == 0:
#         return False
    
#     # 2부터 √n까지만 확인
#     for i in range(3, int(n**0.5) + 1, 2):
#         if n % i == 0:
#             return False
#     return True

# prime_count = 0
# for i in range(2, N + 1):
#     if is_prime(i):
#         prime_count += 1

# print(prime_count)

#03. 에라토스테네스의 체
N = int(input())

def sieve_of_eratosthenes(n):
    if n < 2:
        return 0
    
    # True로 초기화 (모두 소수라고 가정)
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    
    # 2부터 √n까지
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            # i의 배수들을 모두 제거
            for j in range(i*i, n + 1, i):
                is_prime[j] = False
    
    return sum(is_prime)

print(sieve_of_eratosthenes(N))