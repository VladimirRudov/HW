from write import *
from read import *

def start():
    print("Возможные действия:\n1 - получить всю информацию о сотрудниках\n2 - добавить сотрудника\n3 - поиск сотрудника\n4 - выход")
    ch = input("Введите цифру: ")
    while True:
        if ch == '1':
            data = Read()
            print_data(data)
            start()
        elif ch == '2':
            Push()
            start()
        elif ch == '3':
            i = input("Введите данные для поиска: ")
            data = Read()
            i = search(i, data)
            if i != None:
                print_data(i, True)
            else:
                print("Данных нет")                
            start()
        elif ch == '4':
            print("Выход")
            break
        else:
            print("Неверный ввод")
            start()
