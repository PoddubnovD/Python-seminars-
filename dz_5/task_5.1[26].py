# 5.1[26]: Напишите рекурсивную функцию для возведения числа a в степень b. Разрешается использовать только операцию умножения. Циклы использовать нельзя
# Примеры/Тесты:
# <function_name>(2,0) -> 1
# <function_name>(2,1) -> 2
# <function_name>(2,3) -> 8
# <function_name>(2,4) -> 16


def pow_recursive(a, b):
    if b == 1:
        return a
    elif b % 2 == 0:
        res = pow_recursive(a, b // 2)
        return res * res
    else: 
        res = pow_recursive(a, b // 2)
        return res * res * a
a, b = int(input("Введите число: ")), int(input("Введите его степень: "))
print("Результат возведения в степень равен:",pow_recursive(a, b))