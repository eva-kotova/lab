def lab1_task1():
    x = 1
    y = 2
    print(x)
    print(y)
    z = input("Введите значение переменной: ")
    print(z)


def lab1_task2():
    x = int(input("Введите значение переменной: "))
    print(x+2)


def lab1_task3():
    x = int(input("Введите возраст: "))
    if x >= 18:
        print("Доступ разрешен")
    else:
        print("Извините, пользование данным ресурсом только с 18")


def lab1_task4():
    x = 0
    while True:
        x = int(input("Введите число: "))
        if 0 < x < 10:
            print(x**2)
            break
        else:
            print("Число неверное! Введите от 0 до 10")


def lab1_task5():
    a = int(input("Введите значение переменной a: "))
    b = int(input("Введите значение переменной b: "))
    a, b = b, a
    print("Значение переменной а = ", a)
    print("Значение переменной b = ", b)


def lab1_task6():
    name = input("Введите имя: ")
    surname = input("ведите фамилию: ")
    age = int(input("Введите возраст: "))
    weight = int(input("Введите вес: "))
    if age < 30 and 50 < weight < 120:
        print(f"{name} {surname}, {age} год, вес {weight} - хорошее состояние")
    if 30 <= age < 40 and not 50 < weight < 120:
        print(f"{name} {surname}, {age} год, вес {weight} - следует заняться собой")
    if age >= 40 and not 50 < weight < 120:
        print(f"{name} {surname}, {age} год, вес {weight} - следует обратиться к врачу!")