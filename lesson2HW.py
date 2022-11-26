import os
os.system('cls')
# Напишите программу, которая принимает на вход
# вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11
# a = input('введите число: ')
# a = a.replace ('.', '')
# i = 0
# sum = 0
# while i<len(a):
#     sum = sum + int(a[i])
#     i += 1
# print (sum)



# Напишите программу, которая принимает на вход
# число N и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
# a = int(input('введите число: '))
# num = 1
# sum = 1
# while num != a+1:
#     sum = sum * num
#     num = num + 1
#     print(sum, end=" ")



# Задайте список из n чисел последовательности
# $(1+\frac 1 n)^n$ и выведите на экран их сумму.
# Пример:
# - Для n = 4: {1: 2, 2: 2.25, 3: 2.37, 4: 2.44}
# # Сумма = 9.06
# n = int(input('введите число: '))
# spisok = []
# for i in range(n+1):
#     if i>0:
#         spisok.append(round(((1+1/i)**i), 2))
# print(spisok)
# print(sum(spisok))

#другое исполнение
# n = int(input('введите число: '))
# sum = 0
# for i in range(1, n+1):
#     num = (1+1/i)**i
#     sum = sum + num
#     print(round(num, 2))
# print('Сумма чисел:', round(sum, 2))



# Задайте список из N элементов, заполненных числами
# из промежутка [-N, N]. Найдите произведение элементов
# на указанных позициях. Позиции хранятся в файле
# file.txt в одной строке одно число.
# n = int(input('введите число: '))
# spisok = []
# for i in range(-n, n+1):
#     spisok.append(i)
# print(spisok)
# print('Введите номера позиций двух элементов списка: ')
# a = int(input())
# b = int(input())
# print('Произведение элементов на этих позициях =', spisok[a]*spisok[b])



# Реализуйте алгоритм перемешивания списка.
# import random
# print('Список, состоящий из 9 элементов')
# spisok = []
# for i in range(9):
#     spisok.append(i)
# print(spisok)
# print('Перемешивание элементов списка: ')
# # random.shuffle(spisok)
# spisok[0], spisok[1], spisok[2] = spisok[2], spisok[0], spisok[1]
# spisok[8], spisok[4], spisok[5] = spisok[5], spisok[8], spisok[4]
# spisok[6], spisok[3], spisok[7] = spisok[7], spisok[6], spisok[3]
# print(spisok)
