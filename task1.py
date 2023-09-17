# Дополнить телефонный справочник возможностью изменения и удаления данных.

from pathlib import Path

def menu():
    print("Выберите операцию")
    print("1. Вывести весь справочник")
    print("2. Поиск по справочнику")
    print("3. Добавить данные")
    print("4. Удалить данные")
    print("0. Выход")

def delete(f_path):
    print("Введите ФИО человека, которого хотите удалить из справочника (Можете воспользоваться поиском если не помните все данные человека)")
    s = input()
    count = 0
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        for i in range(len(lines)):
            #print(lines[i][:-15])
            if lines[i][:-15] == s:
                count += 1
            if i == len(lines) - 1:
                if lines[i][:-14] == s:
                    count += 1
    #print(len(lines))
    if count == 0:
        print("Данных для удаления не найдено")
        return

    with open(file_path, 'w', encoding='utf-8') as file:
        for i in range(len(lines)):
            if i != len(lines) - 1:
                if lines[i][:-15].strip() != s.strip():
                    if i+1 == len(lines) - 1 and lines[i+1][:-14].strip() == s.strip():
                        file.write(lines[i].strip())
                    else:
                        file.write(lines[i].strip() + '\n')
                        #print(lines[i][:-15])
            else:
                if lines[i][:-14].strip() != s.strip():
                    file.write(lines[i].strip())
                    #print("asdasdsadsadasdsa")
                    #print(lines[i][:-14])
        print("Данные успешно удалены")
    count = 0
def add(f_path):
    print("Напишите ФИО человека, которого хотите добавить через пробел")
    s = input()
    count = 0
    for i in range(len(s) - 1):
        if s[i] == ' ':
            count+=1
        if s[i] == s[i + 1] == ' ':
            print(error)
            return
    if count != 2:
        print(error)
        return
    number = input("Введите номер человека, которого хотите добавить начиная с +7\n")
    if len(number) != 12 or number[0] != '+' or number[1] != '7':
        print(error)
        return
    for i in range(1, len(number)):
        if number[i] < '0' or number[i] > '9':
            print(error)
            return
    with open(f_path, "a", encoding="utf-8") as file:
        file.write("\n")
        file.write(s)
        file.write(', ')
        file.write(number)
        print("Номер успешно добавлен в справочник")

def output(f_path):
    with open(f_path, "r", encoding="utf-8") as file:
        content = file.read()
        print(content)

def search(f_path, search_info):
    count = 0
    with open(f_path, 'r', encoding="utf-8") as file:
        for line in file:
            if search_info in line:
                print(line, end='')
                count += 1

    if count == 0:
        print("По вашему запросу ничего не найдено")

file_path = Path('telephone_numbers.txt')
error = "Ошибка введенных данных"
print("Добро пожаловать в справочник")
menu()
c = 10
while True:
    c = input()
    if c <= '4' and c >= '0':
        c = int(c)
    if c == 0:
        break
    if c == 1:
        output(file_path)
    elif c == 2:
        print("Напишите информацию для поиска")
        s = input()
        search(file_path, s)
    elif c == 3:
        add(file_path)
    elif c == 4:
        delete(file_path)
    else:
        print(error)
    menu()