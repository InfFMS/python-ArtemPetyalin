# Задача 10: Уравнение прямой
# Напишите программу, которая находит значение y в уравнении прямой y = kx + b для заданных x, k и b.
# Пример:
# Ввод: k = 2, b = 3, x = 5
# Вывод: y = 13
x = int(input())
k = int(input())
b = int(input())
print ('y = ' + str(k * x + b))