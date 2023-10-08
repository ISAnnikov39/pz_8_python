# Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных. 
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал для изменения и удаления данных.
import re

def readfile(filename):
    return open(filename).read().split('\n')
 
def scan(data):
    for i in  data:
        print(i)
        
def search(data):
    flag = 1
    name = input('номер ')
    for line in data:
        if name in line:
            flag = 0
            print(line)
    if flag: print('такого номера нет')

def add(data):
    with open("text.txt", "a") as myfile:
        myfile.write('\n')
        myfile.write(input('введите фамилию, имя и номер через пробел '))

def corr(data):
    old = input('введите данные пользователя (имя, фамилию, номер), которого хотите поменять через пробел ')
    new = input('введите новые данные пользователя (имя, фамилию, номер) через пробел ')
    with open ('text.txt', 'r') as f:
        old_data = f.read()
    new_data = old_data.replace(old, new)
    with open ('text.txt', 'w') as f:
        f.write(new_data)


def del_line(data):
    with open('text.txt') as f:
        lines = f.readlines()
    str = input('введите данные пользователя (имя, фамилию, номер), которые необходимо удалить через пробел ')
    pattern = re.compile(re.escape(str))
    with open('text.txt', 'w') as f:
        for line in lines:
            result = pattern.search(line)
            if result is None:
                f.write(line)

    
data = readfile('text.txt') # При запуске программы (скрипта), она должна считывать содержимое
dict_command = {'1' :  scan, '2' : search, '3' : add, '4' : corr, '5' : del_line} # словарь команд, в значениях функции их исполняющие
 
print('''Команды для работы со справочником:
    Просмотр всех записей справочника:  - 1
    Поиск по справочнику -2
    Добавление новой записи - 3
    Изменение любого поля в определенной записи справочника - 4
    Удаление записи  - 5 ''')
 
while True:
    command = input('Команда: ')
    if command in dict_command:
        dict_command[command](data)
    else:
        print(' command error!')

    
