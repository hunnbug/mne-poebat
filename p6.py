def ploshad(leng, wid):
    if leng < 0:
        print("длина не может быть отрицательной")
        return 0
    if wid < 0:
        print("ширина не может быть отрицательной")
        return 0
    if wid == 0:
        print("ширина не может равняться нулю")
        return 0
    if leng == 0:
        print("длина не может равняться нулю")
            # обработка длин
    if leng.is_integer is False:
        print("введите числовое значение для длины")
        return 0
    if wid.is_integer is False:
        print("введите числовое значение для ширины")
        return 0
    # обработка правильности вводимых данных
    plosh = leng * wid
    return plosh
# если длина и ширина положительные, возвращаем значение равное длине * ширине

print(ploshad(2,4))
