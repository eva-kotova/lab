def lab2_task1(test_str):
    if test_str == "КАИ":
        print("ДА")
    else:
        print("НЕТ")


def lab2_task2(test_str):
    if "КАИ" in test_str:
        print("ДА")
    else:
        print("НЕТ")


def lab2_task3():
    lst = []
    for i in range(3):
        lst.append(input("Введите строку: "))
    if "Один" in lst and "Два" in lst and "Три" in lst:
        print("Верно!")
    else:
        print("Неверно!")


def lab2_task4():
    one = input("Введите строку: ")
    two = input("Введите строку: ")
    three = input("Введите строку: ")
    if one == "Один" or one == "Раз" and two == "Два" and three == "Три":
        print("Верно!")
    else:
        print("Неверно!")


def lab2_task5():
    one = input("Введите строку: ")
    two = input("Введите строку: ")
    three = input("Введите строку: ")
    if one == "Один" or one == "Раз" or one == "1" and two == "Два" or two == "2" and three == "Три" or three == "3":
        print("Верно!")
    else:
        print("Неверно!")


def lab2_task6(lst):
    max_width = 0
    for fruit in lst:
        if len(fruit) > max_width:
            max_width = len(fruit)

    for i in range(len(lst)):
        print(f"{i}. {lst[i].rjust(max_width)}")


def lab2_task7(lst1, lst2):
    lst2 = list(set(lst2))
    for elem in lst1:
        if elem in lst2:
            lst1.remove(elem)
    print(lst1)


def lab2_task8():
    pass


def lab2_task9():
    pass


def lab2_task10():
    pass


def lab2_task11():
    pass


def lab2_task12():
    pass


def lab2_task13():
    pass


def lab2_task14():
    pass
