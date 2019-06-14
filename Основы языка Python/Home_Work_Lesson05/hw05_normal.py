# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py
import shutil
import os

def make_dir (name):
    try:
        os.makedirs(name)
        print('папка ' + name + ' успешно создана')
    except FileExistsError:
        print('{} - уже существует'.format(name))

def remove_dir (name):
    try:
        os.removedirs(name)
        print('папка ' + name + ' успешно удалена')
    except FileNotFoundError:
        print('{} - папка не существует'.format(name))

def change_dir (path):
    try:
        os.chdir(path)
        return 'Успешно перешли в папку: {}'.format(path)
    except FileNotFoundError:
        return ('dir_{} - папки не существует'.format(path))

def list_dir ():
    buffer = os.listdir(path=".")
    print('Список файлов:')
    for index, element in enumerate(buffer, start=1):
        if os.path.isdir(element):
            print('{}. {}'.format(index, element))



def start ():
    answer =''
    while answer != '5':
        print('----------------------------------------')
        print('Текущая директория: ' + os.getcwd())
        print('----------------------------------------')
        answer = input('Выберите пункт меню:\n'
                       '1. Создать папку\n'
                       '2. Удалить папку\n'
                       '3. Перейти в папку\n'
                       '4. Помотреть содержимое текущей папки\n'
                       '5. Выход\n')
        if answer =='5':
            break
        if answer == '1':
            name = input('Введите имя новой папки: ')
            make_dir(name)
        elif answer == '2':
            name = input('Введите имя удаляемой папки: ')
            remove_dir(name)
        elif answer == '3':
            path_name = input('Укажите папку для перехода: ')
            change_dir(path_name)
        elif answer == '4':
            list_dir()

start()