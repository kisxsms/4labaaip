def zadacha41():
 n = int(input("Введите число: "))
 if n % 3 == 0:
     print("Число делится на 3")
 else:
    print("Число не делится на 3")

def zadacha42():
    n = (input("Введите число: "))
    try:
        rez = 100 / int(n)
        print("Результат деления числа", n, "на 100 равен",rez)
    except ZeroDivisionError:
        print("Ошибка! Введено неверное число.")
    except ValueError:
        print("Ошибка! Введено не число, а строка.")

def zadacha43():
    n = (input("Введите дату: "))
    n = n.split(sep=".")


        print ("Дата является магической")
    else:
        print("Дата не является магической")

def zadacha44():
    n = (input("Введите номер билета: "))
    h = len(n) / 2
    pp = h[:n]
    vp = h[n:]
    sum1 =
    sum2 =
    if sum(pp) == sum(vp):
        print("Билет номер",n,"счастливый")
    else:
        print("Билет номер",n,"несчастливый")
