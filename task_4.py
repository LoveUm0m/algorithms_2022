def my_sum(n):
    if n == 1:
        return 1
    else:
        return my_sum(n-1) + (-0.5) ** (n-1)


n = int(input('Введите количество элементов: '))
print(f'Количество элементов - {n}, их сумма -', my_sum(n))
