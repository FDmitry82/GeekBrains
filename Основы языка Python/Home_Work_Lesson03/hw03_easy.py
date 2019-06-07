# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.

print("\n")
print("Задание 1. Напишите функцию, округляющую полученное произвольное десятичное число до кол-ва знаков.")
def my_round(number, ndigits):
    number = number * (10 ** ndigits)
    if float(number) - int(number) > 0.5:
         number = number // 1 + 1
    else:
         number = number // 1
    return number / (10 ** ndigits)
print(my_round(2.1234567, 5))
print(my_round(2.3456967, 5))
print(my_round(2.9999967, 5))
print("\n")

# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

print("Задание 2. Определить, является ли билет счастливым.")
#number = int(input('Введите номер билета:'))
#number = 654456
def lucky_ticket(ticket_number):
    if (len(str(ticket_number))!= 6) or (type(ticket_number) is not int):
        return 'Некорректный номер билета'
    else:
        ticket_number1 = list(str(ticket_number))
        sum1 = int(ticket_number1[0]) + int(ticket_number1[1]) + int(ticket_number1[2])
        sum2 = int(ticket_number1[3]) + int(ticket_number1[4]) + int(ticket_number1[5])
        if sum1 == sum2:
            return 'Билет %s счастливый' %ticket_number
        else:
            return 'Билет %s несчастливый' %ticket_number
#print(lucky_ticket(number))

print(lucky_ticket(123006))
print(lucky_ticket(121213))
print(lucky_ticket(436751))