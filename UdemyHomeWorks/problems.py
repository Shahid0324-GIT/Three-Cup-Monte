def lesser_of_two(a, b):
    if a % 2 == 0 and b % 2 == 0:
        if a > b:
            return b
        else:
            return a
    else:
        if a > b:
            return a
        else:
            return b


result = lesser_of_two(2, 6)
result_1 = lesser_of_two(6, 11)
print(result)
print(result_1)
