import os
os.system('cls')

# Вычислить число c заданной точностью d
# Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

# from math import pi
# d =  int(input("Какую точность числа Пи вывести: "))
# print(f'Число Пи до {d} знака, после запятой: {round(pi, d)}')


# Задайте натуральное число N. Напишите программу,
# которая составит список простых множителей числа N.

# n = int(input("Введите число: "))
# i = 2
# spisok = []
# while i <= n:
#     if n % i == 0:
#         spisok.append(i)
#         n //= i
#         i = 2
#     else:
#         i += 1
# print(f"Список простых множителей: {spisok}")


# Задайте последовательность чисел. Напишите программу,
# которая выведет список неповторяющихся элементов
# исходной последовательности.

# spisok = input("Введите числа через пробел:").split()
# print(spisok)
# spisok2 = []
# for i in spisok:
#     if i not in spisok2:
#         spisok2.append(i)
# print(spisok2)


# Задана натуральная степень k. Сформировать случайным образом
# список коэффициентов (значения от 0 до 100) многочлена и
# записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

# import random
# k = random.randint(0,101)


# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

# data1 = open('file1.txt', 'a', encoding = 'UTF-8')
# data1.write('2*x + 4*x + 5')
# data1.close()
# data2 = open('file2.txt', 'a', encoding = 'UTF-8')
# data2.write('x + 5*x')
# data2.close()

# x = open("file1.txt")
# a = x.readline()
# y = open("file2.txt")
# b = y.readline()
# print(a, '+', b)
# c = input(str(a, '+', b))
# data3 = open('file3.txt', 'a')
# data3.write(c) # записать в файл не получается
# x.close()
# y.close()
# data3.close()
