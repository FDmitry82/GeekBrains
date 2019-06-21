# Задание-1: Решите задачу (дублированную ниже):

# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за каждый час переработки они получают
# удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"

# С использованием классов.
# Реализуйте классы сотрудников так, чтобы на вход функции-конструктора
# каждый работник получал строку из файла

class Worker:
    def __init__(self, worker):
        self.name = worker[0]
        self.surname = worker[1]
        self.salary = float(worker[2])
        self.rank = worker[3]
        self.normal_hours = float(worker[4])
        self.production = float()
        self.payroll = float()

    def add_production(self, production):
        if production[0] == self.name and production[1] == self.surname:
            self.production = int(production[2])
        else:
            pass

    def payroll_accounting(self):
        if self.production:
            if self.production < self.normal_hours:
                self.payroll = round(self.salary - self.salary/self.normal_hours*(self.normal_hours - self.production), 2)
            else:
                self.payroll = round(self.salary - 2 * self.salary / self.normal_hours * (self.normal_hours - self.production), 2)
        else:
            raise TypeError('Argument production is empty')


with open('data\workers', 'r', encoding="utf8") as workers: #Считываем из файла информацию о работниках
    workers_list = list()
    for line in workers:
        workers_list.append(line.split())

employees = [Worker(worker) for worker in workers_list if worker != workers_list[0]] #Создаем список обектов Worker

with open('data\hours_of', 'r', encoding="utf-8") as hours_of: #Считываем из файла статистику трудовой активности работников
    hours_list = list()
    for line in hours_of:
        hours_list.append(line.split())

for employee in employees:  #Добавляем к каждому работнику информацию о его трудовой активности
    for hours in hours_list:
        employee.add_production(hours)

for employee in employees:  #Для каждого работника расчитываем реальную зарплату
    employee.payroll_accounting()
    print('{} {}: ставка - {}, реальная зарплата - {}'.format(employee.surname, employee.name, employee.salary, employee.payroll))