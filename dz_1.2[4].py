# 1.2[4]. Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. Сколько журавликов сделал каждый ребенок, если известно, 
# что Петя и Сережа сделали одинаковое количество журавликов, а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
# Примеры/Тесты:
# 6 >>>  1  4  1
# 24 >>> 4  16  4
# 60 >>> 10  40  10

a = int(input("Введите сумму из примера: "))
k = int((a/3)*2)
p = int((k/2)/2)
s = int(p)
print(f'Петя-{p}')
print(f'Катя-{k}')
print(f'Сережа-{s}')