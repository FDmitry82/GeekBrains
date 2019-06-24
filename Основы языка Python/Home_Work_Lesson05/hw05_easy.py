# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.
import shutil
import os

print('\nЗадача 1. Напишите скрипт, создающий и удаляющий директории dir_1 - dir_9 в папке'
      '\nСейчас создадим папки dir_1 - dir_9\n')

def make_dir (name):
    try:
        os.makedirs(name)
        print('папка ' + name + ' успешно создана')
    except FileExistsError:
        print('{} - уже существует'.format(name))

quantity_dirs = range(1, 10) # Создаем цикл на вызов функции (создать папки).
for i in quantity_dirs:
    i = str(i)
    make_dir('dir_' + i)


# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.
print('\nЗадача 2. Напишите скрипт, отображающий папки текущей директории.'
      '\nСейчас отобразим созданные папки\n')

def list_dir ():
    buffer = os.listdir()
    print('Список файлов:')
    for index, element in enumerate(buffer, start=1):
        if os.path.isdir(element):
            print('{}. {}'.format(index, element))
list_dir()


# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
print('\nЗадача 1. Напишите скрипт, создающий и удаляющий директории dir_1 - dir_9 в папке'
      '\nСейчас создадим копию файла\n')

def current_file_copy ():
    name_file = os.path.realpath(__file__)
    new_file = name_file +'.copy'
    if os.path.isfile(new_file) != True:
        shutil.copy(name_file, new_file)
        print('Файл успешно создан')
    else:
        print('Файл уже скопирован')
current_file_copy()
