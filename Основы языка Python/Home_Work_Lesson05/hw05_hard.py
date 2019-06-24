# Задание-1:
# Доработайте реализацию программы из примера examples/5_with_args.py,
# добавив реализацию следующих команд (переданных в качестве аргументов):
#   cp <file_name> - создает копию указанного файла
#   rm <file_name> - удаляет указанный файл (запросить подтверждение операции)
#   cd <full_path or relative_path> - меняет текущую директорию на указанную
#   ls - отображение полного пути текущей директории
# путь считать абсолютным (full_path) -
# в Linux начинается с /, в Windows с имени диска,
# все остальные пути считать относительными.

# Важно! Все операции должны выполняться в той директории, в который вы находитесь.
# Исходной директорией считать ту, в которой был запущен скрипт.

# P.S. По возможности, сделайте кросс-платформенную реализацию.


# Данный скрипт можно запускать с параметрами:
# python with_args.py param1 param2 param3
import os
import sys
import shutil
print('sys.argv = ', sys.argv)
def print_help():
    print("help - получение справки")
    print("mkdir <dir_name> - создание директории")
    print("ping - тестовый ключ")
    print('cp - создает копию указанного файла')
    print('rm - удаляет указанный файл')
    print('cd - смена директории на указанную')
    print('ls - отображает полный путь текущей директории')

def change_dir ():
    if not dir_name:
        print('Необходимо указать имя директории вторым параметром')
        return
    try:
        os.chdir(dir_name)
        print('Успешно перешли в папку: {}'.format(dir_name))
        print('Текущий каталог: ', os.getcwd())
    except FileNotFoundError:
        print('dir_{} - папки не существует'.format(dir_name))

def file_copy ():
    if not name_file:
        print("Необходимо указать имя файла вторым параметром")
        return
    current_dir = os.getcwd()
    old_file = os.path.join(current_dir, name_file)
    new_file = os.path.join(current_dir, (name_file +'.copy'))
    if os.path.isfile(new_file) != True:
        shutil.copy(old_file, new_file)
        print(new_file + ' - создан')
    else:
        print('Файл уже скопирован')

def del_file ():
    if not name_file:
        print("Необходимо указать имя файла вторым параметром")
        return
    current_dir = os.getcwd()
    old_file = os.path.join(current_dir, name_file)
    if os.path.isfile(old_file):
        answer = input('Вы уверены что хотите удалить файл? y/n: ')
        if answer == 'y':
            os.remove(old_file)
            print(old_file + ' - удален')
        else:
            return
    else:
        print('Файла не существует')

def make_dir():
    if not dir_name:
        print("Необходимо указать имя директории вторым параметром")
        return
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.mkdir(dir_path)
        print('директория {} создана'.format(dir_name))
    except FileExistsError:
        print('директория {} уже существует'.format(dir_name))

def current_dir ():
    print(os.getcwd())

def ping():
    print("pong")

do = {"help": print_help, "mkdir": make_dir, "ping": ping, 'cp': file_copy, 'cd': change_dir, 'rm': del_file, 'ls': current_dir}

#Относится к ключу cp - копирование указанного файла и его же использовал при удалении файла ключ rm
try:
    name_file = sys.argv[2]
except IndexError:
    name_file = None

#относится к копированию папки ключ mkdir, и его же использовал в функции смены директории
try:
    dir_name = sys.argv[2]
except IndexError:
    dir_name = None

try:
    key = sys.argv[1]
except IndexError:
    key = None

if key:
    if do.get(key):
        do[key]()
    else:
        print("Задан неверный ключ")
        print("Укажите ключ help для получения справки")

def start ():
    answer =''
    while answer != '5':
        print('----------------------------------------')
        print('Текущая директория: ' + os.getcwd())
        print('----------------------------------------')
        answer = input('Выберите пункт меню:\n'
                       '1. "help - получение справки"\n'
                       '2. mkdir <dir_name> - создание директории\n'
                       '3. ping - тестовый ключ\n'
                       '4. cp - создает копию указанного файла\n'
                       '5. rm - удаляет указанный файл\n'
                       '6. cd - смена директории на указанную\n'
                       '7. ls - отображает полный путь текущей директории\n'
                       '8. Выход\n')
        if answer =='8':
            break
        if answer == 'help':
            name = input('help - получение справки ')
            print_help()
        elif answer == 'mkdir':
            name = input('mkdir <dir_name> - создание директории: ')
            make_dir(name)
        elif answer == 'ping':
            path_name = input('ping - тестовый ключ: ')
            ping()
        elif answer == 'cp':
            path_name = input('cp - создает копию указанного файла: ')
            file_copy()
        elif answer == 'cd':
            path_name = input('cd - смена директории на указанную: ')
            change_dir()
        elif answer == 'rm':
            path_name = input('rm - удаляет указанный файл: ')
            del_file()
        elif answer == 'ls':
            path_name = input('ls - отображает полный путь текущей директории: ')
            current_dir()

start()