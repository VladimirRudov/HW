def print_data(data):
    if len(data) > 0:
        print("id".center(5), "Фамилия".center(10), "Имя".center(10), "Должность".center(10), "Зарплата".center(10), "Город".center(10), "Улица".center(15), "Дом".center(10), "Квартира".center(10))
        for item in data:
            print(item[0].center(5), item[1].center(10), item[2].center(10), item[3].center(10), item[4].center(10), item[5].center(10), item[6].center(15), item[7].center(10), item[8].center(10))
    else:
        print("Пусто")

def Read():
    list_name = []
    with open('name.csv', 'r') as file:
        for line in file:
            temp = line.strip().split(';')
            list_name.append(temp)
    list_adress = []
    with open('adress.csv', 'r') as file:
        for line in file:
            temp = line.strip().split(';')
            list_adress.append(temp)
    list = []
    for i in range(len(list_name)):
        list.append([list_name[i][0], list_name[i][1], list_name[i][2], list_name[i][3], list_name[i][4], list_adress[i][1], list_adress[i][2], list_adress[i][3], list_adress[i][4]])
    return list

def search(word, data):
    if len(data) > 0:
        list = []
        for i in data:
            if word in i:
                list.append(i)
    else:
        return list
