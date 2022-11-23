def master_yoda(string):
    new_string = string.split()
    new_string = new_string[::-1]
    new_string = ' '.join(new_string)
    return new_string


result_1 = master_yoda('I am home')
result_2 = master_yoda('We are ready')

print(result_1)
print(result_2)
