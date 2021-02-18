while True:
    print("Введите, что хотите расчитать (amper, volt, om)")
    print("Введите  exit для выхода")
    num = input("Ваш вариант: ")
    if num == "amper":
        volt = float(input("Введите напряжение: "))
        om = float(input("Введите сопротивление: "))
        print("Сила тока = ", str(volt / om))
        break
    elif num == "volt":
        amper = float(input("Введите силу тока: "))
        om = float(input("Введите сопротивление: "))
        print("Напряжение = ", str(amper * om))
        break
    elif num == "om":
        amper = float(input("Введите силу тока: "))
        volt = float(input("Введите напряжение: "))
        print("Сопротивление = ", str(volt / amper))
        break

    # Выход из программы
    elif num == "exit":
        break