import os
os.system('cls')
import csv

def vyvod():
    print('1 - Прочитать данные из файла')
    print('2 - Записать данные в файл')
    vybor = input('Какое действие Вы хотите произвести: ')
    if vybor == '1':
        with open('phone.csv', 'r', encoding='utf-8') as i:
            reader = csv.reader(i, delimiter=',')
            for row in reader:
                print (row)
    elif vybor == '2':
        with open('phone.csv', 'a') as i:
            a = input('Укажите фамилию: ')
            b = input('Укажите имя: ')
            c = input('Укажите телефон: ')
            d = input('Укажите примечание: ')
            data = [a, b, c, d]
            writer = csv.writer(i)
            writer.writerow(data)
    else:
        print('Вы ввели неверный символ')
