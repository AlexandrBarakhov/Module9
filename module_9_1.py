from statistics import mean


def apply_all_func(int_list, *functions):
    results = {}
    for func in functions:
        results[func.__name__] = func(int_list)
    return results


# Примеры использования:
list_ = [6, 20, 15, 9]
print(apply_all_func(list_, max, min))
print(apply_all_func(list_, len, sum, sorted))
print(apply_all_func(list_, mean))
