def is_prime(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if result > 1:
            for i in range(2, int(result ** 0.5) + 1):  # Для небольших чисел пров. все делители до кв. корня из числа
                if result % i == 0:
                    print("Составное")
                    return result
            print("Простое")
        else:
            print("Не натуральное число или оно равно 1")
        return result
    return wrapper


@is_prime
def sum_three(a, b, c):
    return a + b + c


result = sum_three(2, 3, 6)
print(result)
result = sum_three(2, 3, 7)
print(result)
result = sum_three(1, 0, 0)
print(result)
result = sum_three(2, 3, -6)
print(result)
