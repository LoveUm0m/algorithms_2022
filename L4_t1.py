from timeit import timeit


def func_1(numss):
    new_arr_1 = []
    for i in range(len(numss)):
        if nums[i] % 2 == 0:
            new_arr_1.append(i)
    return new_arr_1


print(timeit("func_1([3, 0, 0, 0])", "from __main__ import func_1", number=1000000))


def func_2(numss):
    new_arr_2 = []
    for i, j in enumerate(numss):
        if j % 2 == 0:
            new_arr_2.append(i)
    return new_arr_2


print(timeit("func_2([3, 0, 0, 0])", "from __main__ import func_2", number=1000000))

nums = [3, 0, 0, 0]

new_arr = [i if j % 2 == 0 else None for i, j in enumerate(nums)]

print(timeit('''new_arr = [i if j % 2 == 0 else None for i, j in enumerate(nums)]''',
             globals=globals(),
             number=1000000))

'''
Для оптимизации сначала была использована функция "enumerate",
замеры показали уменьшение времени работы функции,
далее цикл был заменён на более совершенный способ формирования списка - 
"list comprehensions" показал более высокую скорость работы по сравнению 
с остальными функциями.
'''