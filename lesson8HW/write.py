def Write(data, name):
    with open(name, 'a+') as file:
        file.write(";".join(map(str, data)))
        file.write(f"\n")

def count(name):
    with open(name, 'r') as file:
        data = file.read()
    return data.count('\n')

def input_data():
    dct = dict()
    Id = count("name.csv") 
    dct["id"] = Id
    dct["surname"] = input('Введите фамилию: ')
    dct["name"] = input('Введите имя: ')
    dct["dolzh"] = input('Укажите должность: ')
    dct["salary"] = input('Укажите зарплату: ')
    dct["city"] = input('Введите город: ')
    dct["street"] = input('Введите улицу: ')
    dct["house"] = input('Введите номер дома: ')
    dct["apartament"] = input('Введите номер квартиры: ')
    return dct

def Push():
    dct = input_data()
    Write([dct.get("id"), dct.get("surname"), dct.get("name"), dct.get("dolzh"), dct.get("salary")], "name.csv")
    Write([dct["id"], dct["city"], dct["street"], dct["house"], dct["apartament"]], "adress.csv")
