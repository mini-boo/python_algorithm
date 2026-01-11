N = int(input())

input_list = list(map(int, input().split()))
lr_list = []
standard = 0

while input_list:
    left = input_list[0]
    right = input_list[-1]

    if left > standard and right > standard:
        if left < right:
            standard = left
            lr_list.append("L")
            input_list.pop(0)
        else:
            standard = right
            lr_list.append("R")
            input_list.pop()
    
    elif left > standard:
        standard = left
        lr_list.append("L")
        input_list.pop(0)

    elif right > standard:
        standard = right
        lr_list.append("R")
        input_list.pop()

    else:
        break

print(len(lr_list))
print(lr_list)