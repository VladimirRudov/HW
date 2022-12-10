import os
os.system('cls')

# ДЗ для оценки ОТЛ( если делаете это ДЗ, то задачи с семинара сдавать не нужно)

# 1. Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

# text1 = 'Когдабв Вы не делабвли МИР'
# print(text1)
# words = text1.split(' ')
# delete = 'абв'
# text2 = []
# for i in words:
#     if delete not in i:
#         text2.append(i)
# print(' '.join(text2))


# 2. Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая
# ход друг после друга. Первый ход определяется жеребьёвкой. За один ход
# можно забрать не более чем 28 конфет. Все конфеты оппонента достаются
# сделавшему последний ход. Сколько конфет нужно взять первому игроку,
# чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

# import random
# ostatok = 100
# shag = 28
# while ostatok != 0:
#     print(f'Остаток {ostatok} конфет')
#     zhrebiy = random.randint(1, 2)
#     print(f'Конфеты берет: {zhrebiy} игрок')
#     if zhrebiy == 1:
#         beru1 = int(input('Введите количество конфет, которые Вы хотите взять: '))
#         if beru1 == 0 or beru1 > ostatok or beru1 > shag:
#             print('Возьмите другое количество конфет')
#             beru1 = int(input('Введите количество от 1 до 28, но не больше остатка: '))
#         ostatok = ostatok - beru1
#         if ostatok == 0:
#             print(f'Победил первый игрок')
#     elif zhrebiy == 2:
#         nesnizhat = shag + 1
#         if ostatok <= shag:
#             beru2 = ostatok
#         elif ostatok == nesnizhat:
#             beru2 = 1
#         elif ostatok > nesnizhat and ostatok <= (nesnizhat + shag):
#             beru2 = ostatok - nesnizhat
#         else:    
#             beru2 = random.randint(1, shag)
#         print(f'Второй игрок взял: {beru2}')
#         ostatok = ostatok - beru2
#         if ostatok == 0:
#             print(f'Победил второй игрок')


# 3. Создайте программу для игры в ""Крестики-нолики"". (бонусное задание)

# 4. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# text = str(input('введите текст: '))
# print(text.__len__())
# count = 1
# data = ''
# i = 0
# while i < text.__len__()-1:
#     if text[i] == text[i+1]:
#         count += 1
#         i += 1
#     elif text[i] != text[i+1]:
#         data = data + str(count) + text[i]
#         count = 1
#         i += 1
# data = data + str(count) + text[i]
# print(data)
