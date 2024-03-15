def zadacha1():
 n = int(input("Введите число: "))
 if n % 3 == 0:
     print("Число делится на 3")
 else:
    print("Число не делится на 3")

def zadacha2():
    n = (input("Введите число: "))
    try:
        rez = 100 / int(n)
        print("Результат деления числа", n, "на 100 равен",rez)
    except ZeroDivisionError:
        print("Ошибка! Введено неверное число.")
    except ValueError:
        print("Ошибка! Введено не число, а строка.")

zadacha2()