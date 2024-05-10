

documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]

directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
}

def get_name(number:str):
    # number = input("Введите номер документа: ")
    flag = False
    for document in documents:
        if number == document['number']:
            flag = document['name']
            return flag
    if flag == False:
        return 'Документ с номером ', number, ' не найден'
    return


def get_shelf(number: str):
    flag = False
    for shelf, id in directories.items():
        if number in id:
            flag = shelf
            return 'Документ', number, 'лежит на полке номер ', flag
    if flag == False:
        return f'Документ с номером ', number, ' не найден'
    return


def get_list(documents):
    list1 = []
    for document in documents:
        for type, values in document.items():
            list1.append(values)
    return list1




"____________________________________________________________________________________________________"

year = [2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011]
animals = ['Дракон', 'Змея', 'Лошадь', 'Овца', 'Обезьяна', 'Петух', 'Собака', 'Свинья', 'Крыса', 'Бык', 'Тигр', 'Заяц']
num = 1

def get_animals(num: int):
    if num not in year:
        while num > 0:
            if num < 2000:
                num = num + 12
            elif num > 2011:
                num = num - 12
            else:
                g = year.index(num)
                return animals[g]
                break
    elif num in year:
        g = year.index(num)
        return animals[g]