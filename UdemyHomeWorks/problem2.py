def animal_crackers(a):
    new_list = a.split()
    if new_list[0][0] == new_list[1][0]:
        return True
    else:
        return False


result_1 = animal_crackers('Levelheaded Llama')
result_2 = animal_crackers('Crazy Kangaroo')
print(result_1, result_2)
