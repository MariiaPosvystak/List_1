from audioop import reverse
from random import*
a=input("Введите первую строку: ")
b=input("Введите вторую строку: ")
a_list=list(a)
b_list=list(b)
print("1 список")
print(a_list)
print("2 список")
print(b_list)
print("Выберети один из предложеных вариантов")
while True:
    print("1 - Дабавить букву в список")
    print("2 - Удалить элемент по его индексу")
    print("3 - Получение индекса первого вхождения элемента")
    print("4 - Объединение двух списков")
    print("5 - Сортировка списка по возрастанию")
    print("6 - Сортировка списка по убыванию")
    print("7 - ")
    print("8 - ")
    print("9 - ")
    print("10- ")
    valik=int(input())
    if valik==1:
        V=input("Какой из списков отсортировать")
        if V==1:
            w=input("Введите букву: ")
            a_list.append(w)
            print(a_list)
        elif V==2:
            w=input("Введите букву: ")
            b_list.append(w)
            print(b_list)
        else:
            print("Error!")
    elif valik==2:
        V=input("Какой из списков отсортировать")
        if V==1:
            ind=input("Введите индекс символа")
            a_list.pop(ind)
            print(a_list)
        elif V==2:
            ind=input("Введите индекс символа")
            b_list.pop(ind)
            print(b_list)
        else:
            print("Error!")
    elif valik==3:
        V=input("Какой из списков отсортировать")
        if V==1:
            a=input("Введите элемент:")
            il=a_list.index(a)
            print(il)
        elif V==2:
            a=input("Введите элемент:")
            il=b_list.index(a)
            print(il)
        else:
            print("Error!")
    elif valik==4:
        M=a_list + b_list
        print(M)
    elif valik==5:
        V=input("Какой из списков отсортировать")
        if V==1:
            a_list.sort()
            print(a_list)
        elif V==2:
            b_list.sort()
            print(b_list)
        else:
            print("Error!")
    elif valik==6:
        V=input("Какой из списков отсортировать")
        if V==1:
            a_list.sort(reverse=True)
            print(a_list)
        elif V==2:
            b_list.sort(reverse=True)
            print(b_list)
        else:
            print("Error!")
    elif valik==7:
    elif valik==8:
    elif valik==9:
    elif valik==10:

        V=input("Какой из списков отсортировать")
        if V==1:
        elif V==2:
        else:
            print("Error!")