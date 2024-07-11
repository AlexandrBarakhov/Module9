def odd_num(x):
    return x % 2 != 0


def sq_num(x):
    return x ** 2


numbers = [1, 2, 5, 7, 12, 11, 35, 4, 89, 10]

# Отбираем нечетные числа
odd_numbers = filter(odd_num, numbers)
# odd_numbers = filter(lambda x: x % 2 != 0, numbers)

# Возводим отобранные числа в квадрат
squared_numbers = map(sq_num, odd_numbers)
# squared_numbers = map(lambda x: x ** 2, odd_numbers)

# Преобразуем генератор в список
result = list(squared_numbers)

print(result)  # Вывод: [1, 25, 49, 121, 1225, 7921]
