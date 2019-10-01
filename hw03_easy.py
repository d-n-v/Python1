# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.


def my_round(number, ndigits):
    return("{:.{prec}f}".format(number, prec=ndigits))


print(my_round(2.1234567, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))


# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить


def lucky_ticket(ticket_number):
    sum1 = 0
    sum2 = 0
    if len(str(ticket_number)) != 6:
        return ("У вас неправильный билет")
    else:
        ticket_number_counter = ticket_number
        while ticket_number_counter > 0:
            if len(str(ticket_number_counter)) > 3:
                el1 = ticket_number_counter % 10
                sum1 = sum1 + el1
                ticket_number_counter = ticket_number_counter // 10
            else:
                el2 = ticket_number_counter % 10
                sum2 = sum2 + el2
                ticket_number_counter = ticket_number_counter // 10
    if sum1 == sum2:
        return("Счастливый билет")
    else:
        return("Обычный билет")


print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
print(lucky_ticket(436755))