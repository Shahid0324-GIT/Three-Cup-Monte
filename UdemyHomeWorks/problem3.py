def almost_there(num):
    if num <= 100:
        if (100 - num) <= 10:
            return True
        else:
            return False
    elif num <= 111:
        if (num - 100) <= 10:
            return True
        else:
            return False
    elif num <= 200:
        if (200 - num) <= 10:
            return True
        else:
            return False
    elif num < 211:
        if (num - 200) <= 10:
            return True
        else:
            return False


res_1 = almost_there(90)
res_2 = almost_there(104)
res_3 = almost_there(150)
res_4 = almost_there(209)

print(res_1, res_2, res_3, res_4)
