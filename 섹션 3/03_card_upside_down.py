card_list = list(range(1,21))

result_list = []

for i in range(0, 10):
    N, M = map(int, input().split())
    card_list[N-1:M] = card_list[N-1:M][::-1]

print(card_list)