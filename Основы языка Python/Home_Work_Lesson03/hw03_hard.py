# Задание-1:
# Написать программу, выполняющую операции (сложение и вычитание) с простыми дробями.
# Дроби вводятся и выводятся в формате:
# n x/y ,где n - целая часть, x - числитель, у - знаменатель.
# Дроби могут быть отрицательные и не иметь целой части, или иметь только целую часть.
# Примеры:
# Ввод: 5/6 + 4/7 (всё выражение вводится целиком в виде строки)
# Вывод: 1 17/42  (результат обязательно упростить и выделить целую часть)
# Ввод: -2/3 - -2
# Вывод: 1 1/3

print("\nЗадание 1. Написать программу, выполняющую операции (сложение и вычитание) с простыми дробями.")
expression = '- 10 2/3 + - 9 4/6'  # input('Введите выражение целиком в виде строки: ')
expression = list(expression.split(' '))
n = []
x = []
y = []
signs = []

for i in range(len(expression)):
    try:
        if float(expression[i]) - int(expression[i]) == 0:
            n.append(int(expression[i]))
    except ValueError:
        if expression[i] == '-':
            signs.append (-1)
        elif expression[i] == '+':
            signs.append (1)
        elif expression[i].find('/') == True:
            xy = expression[i].split ('/')
            x.append(int (xy[0]))
            y.append(int (xy[1]))
        else:
            print('Некорректный ввод')
            break


def edit_signs(signs):
    if len(signs) != 3:
        if len(signs) == 1:
            signs.insert (1, 0)
            signs.insert (1, 2)
        elif len(signs) == 2:
            if expression[0] == '-':
                signs.insert(1, 2)
            else:
                signs.insert(1, 0)
        else:
            print('Некорректный ввод')

edit_signs(signs)
result1 = signs[0] * n[0] * x[0] * y[1] + signs[1] * signs[2] * n[1] * x[1] * y[0]
n_result = result1 // (y[0] * y[1])
x_result = result1 % (y[0] * y[1])
y_result = y[0] * y[1]
print('{} {}/{}'.format(n_result, x_result, y_result))




# Задание-2:
# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки
# они получают удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"

print("\nЗадание 2. Дана ведомость расчета заработной платы. Рассчитайте зарплату всех работников.")
def interpretation_of_file(file_name, new_name):
    with open(file_name, encoding='utf-8') as f:
        name = f.read().split('\n')
        for i in range(len(name)):
            name[i] = name[i].split()
        new_name = name
        return new_name


workers = []
hours = []
workers = interpretation_of_file('data/workers', workers)
hours = interpretation_of_file('data/hours_of', hours)

result = {}
for w in range(len(workers)):
    if w == 0:
        continue
    for h in range(len(hours)):
        if h == 0:
            continue
        elif workers[w][0] == hours[h][0] and workers[w][1] == hours[h][1]:
            full_name = workers[w][0] + ' ' + workers[w][1]
            if hours[h][2] <= workers[w][4]:
                salary = int(hours[h][2]) * int(workers[w][2]) / int(workers[w][4])
            else:
                salary = int(workers[w][2]) + (int(hours[h][2]) - int(workers[w][4])) * 2 * int(
                    workers[w][2]) / int(workers[w][4])
            salary = int(salary)
            result[full_name] = result.get(full_name, salary)

print(result)


# Задание-3:
# Дан файл ("data/fruits") со списком фруктов.
# Записать в новые файлы все фрукты, начинающиеся с определенной буквы.
# Т.е. в одном файле будут все фрукты на букву “А”, во втором на “Б” и т.д.
# Файлы назвать соответственно.
# Пример имен файлов: fruits_А, fruits_Б, fruits_В ….
# Важно! Обратите внимание, что нет фруктов, начинающихся с некоторых букв.
# Напишите универсальный код, который будет работать с любым списком фруктов
# и распределять по файлам в зависимости от первых букв, имеющихся в списке фруктов.
# Подсказка:
# Чтобы получить список больших букв русского алфавита:
# print(list(map(chr, range(ord('А'), ord('Я')+1))))

print("\nЗадание 3. Записать в новые файлы все фрукты, начинающиеся с определенной буквы.")
def creating_fruit_files():
    sorting_fruits = {}
    with open('data/fruits.txt', encoding='utf-8') as f:
        for fruits in f.readlines():
            if fruits == '\n':
                continue
            file_name = 'data/fruits_{}.txt'.format(fruits[0].upper())
            sorting_fruits[file_name] = sorting_fruits.get(file_name, fruits)

    for fruit_file_names in sorting_fruits:
        with open(fruit_file_names, 'w') as f:
            f.write(sorting_fruits[fruit_file_names])
    return sorting_fruits.keys()

a = creating_fruit_files()

for list in a:
    file = open(list, 'w', encoding='utf-8')
    with open('data/fruits.txt', encoding='utf-8') as f:
        for fruits in f.readlines():
            if list[12] == fruits[0]:
                file.write(fruits)
    file.close()
print('Файлы созданы')