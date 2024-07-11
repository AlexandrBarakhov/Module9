print('Задача 1: Фабрика Функций')


def create_operation(operation):
    if operation == "add":
        def add(x, y):
            return x + y

        return add
    elif operation == "subtract":
        def subtract(x, y):
            return x - y

        return subtract
    elif operation == "multiply":
        def multiply(x, y):
            return x * y

        return multiply
    elif operation == "divide":
        def divide(x, y):
            try:
                result = x / y
            except ZeroDivisionError:
                raise ZeroDivisionError("Деление на ноль!")
            return result

        return divide
    else:
        return None


my_func_add = create_operation("add")
print(my_func_add(1, 2))

my_func_subtract = create_operation("subtract")
print(my_func_subtract(5, 3))

my_func_multiply = create_operation("multiply")
print(my_func_multiply(2, 4))

my_func_divide = create_operation("divide")
print(my_func_divide(10, 2))
try:
    print(my_func_divide(10, 0))
except ZeroDivisionError as e:
    print(e)

print('Задача 2: Лямбда-Функции')

square_lambda = lambda x: x ** 2


def square_def(x):
    return x ** 2


num = 5
print(f"Квадрат числа {num} равен: {square_lambda(num)}")
print(f"Квадрат числа {num} равен: {square_def(num)}")

print('Задача 3: Вызываемые Объекты')


class Rect:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __call__(self):
        return self.a * self.b

    def __str__(self):
        return f"Прямоугольник {self.a}x{self.b}, площадь: {self()}"


rect = Rect(3, 4)
print(rect)
