# Задание 1:
# У вас есть идея создать Back-end для игры: "Угадай число."
# Данный код генерирует рандомное число.
###################
# С помощью функции:
#    my_number = int(input("Введите число: "))
# спрашивайте число от пользователя.
# Запустите бесконечный цикл!
# И пытайтесь спрашивать у пользователя какое-то число каждый раз.
# Если пользователь угадал число которое сгенерировал компьютер остановите цикл и скажите пользователю - "Вы угадали!"
# Если пользователь не угадал вы снова спросите у него число.
# Если пользователь 3 раза подряд не угадал число, вы останавливаете цикл и говорите: "Вы проиграли..."
#######################################################################
# from random import random
# my_number = round(random() * 100)
# i = 1
# print("Число сгенерировано. Попробуйте отгадать его.")
# while i <= 3:
#     u = int(input("Введите число: "))
#     if u > my_number:
#         print('Больше заданного')
#     elif u < my_number:
#         print('Меньше заданного')
#     else:
#         print('Вы угадали!' % i)
#         break
#     i += 1
# else:
#     print('Вы проиграли...Число -', my_number)

#Напишите программу, которая циклично запрашивает
# у пользователя номера символов по таблице Unicode и выводит соответствующие им символы.
        # Завершает работу при вводе нуля.
###################################################################
# while True:
#     symbol = int(input("Enter the number of symbol: "))
#     if symbol == 0:
#         break
#     print(chr(symbol))

# Задание 3:
        # Напишите программу, которая измеряет длину введенной строки.
        # Если строка длиннее десяти символов, то выносится предупреждение.
        # Если короче, то к строке добавляется столько символов *,
# чтобы ее длина составляла десять символов, после чего новая строка должна выводиться на экран.
###################################################################
# s = input("Введите: ")
# if len(s) > 10:
#     print("Длиннее десяти символов!")
# else:
#    for i in range(len(s), 10):
#       s += "*"
#    print(s)

# Задание 4:
        # Напишите программу, которая запрашивает у пользователя шесть вещественных чисел.
        # На экран выводит минимальное и максимальное из них, округленные до двух знаков после запятой.
        # Выполните задание без использования встроенных функций min() и max().
####################################################################
# user = []
# for i in range(6):
#     user.append(float(input("Введите числа: ")))
# maxx = user[0]
# minn = user[0]
# for i in user:
#     if maxx > i:
#         maxx = i
#     else:
#         minn = i
# print(f"mах число: {round(maxx, 2)}, min число: {round(minn, 2)}")

# Задание 5:
        # Напишите программу которая принимает
# число любой длины и вытаскивает из него самое большое и самое маленькое число.
####################################################################
# a = input('enter a number: ')
# maximum = max(int(x) for x in str(a))
# minimum = min(int(x) for x in str(a))
# print('max number:', maximum, 'min number:', minimum)


