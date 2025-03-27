from random import *
a = input("Sisesta esimene rida: ")
b = input("Sisesta teine rida: ")
a_list = list(a)
b_list = list(b)
print("1. loend")
print(a_list)
print("2. loend")
print(b_list)
print("Valige üks järgmistest valikutest")
while True:
    print("1 - Lisa täht loendisse")
    print("2 - Eemalda element vastavalt indeksile")
    print("3 - Leia esimese esinemise indeks")
    print("4 - Ühenda kaks loendit")
    print("5 - Sorteeri loend kasvavas järjekorras")
    print("6 - Sorteeri loend kahanevas järjekorras")
    print("7 - Loo loend arvude vahemikust")
    print("8 - Kopeeri loend")
    print("9 - Muuda tähemärki loendis")
    print("10 - Eemalda loend")
    print("11 - Kontrolli, kas string on pealkirja vormingus")
    print("12 - Eemalda juhtivad märgid")
    print("13 - Vaheta suur- ja väiketähed")
    print("14 - Muuda esimene täht suureks")
    print("15 - Eemalda lõpus olevad märgid")
    print("0 - Välju")
    try:
        valik = int(input())
    except:
        print("Error")
    if valik == 1:
        V = int(input("Kuhu loendisse soovite tähe lisada (1 või 2): "))
        w = input("Sisesta täht: ")
        if V == 1:
            a_list.append(w)
            print(a_list)
        elif V == 2:
            b_list.append(w)
            print(b_list)
        else:
            print("Error!")
    elif valik == 2:
        V = int(input("Kust loendist soovite tähe eemaldada (1 või 2): "))
        ind = int(input("Sisesta tähe indeks: "))
        if V == 1:
            a_list.pop(ind)
            print(a_list)
        elif V == 2:
            b_list.pop(ind)
            print(b_list)
        else:
            print("Error!")
    elif valik == 3:
        V = int(input("Millises loendis soovite teada esimesena esineva elemendi indeksit (1 või 2): "))
        elem = input("Sisesta element: ")
        if V == 1:
            print(a_list.index(elem))
        elif V == 2:
            print(b_list.index(elem))
        else:
            print("Error!")
    elif valik == 4:
        M = a_list + b_list
        print(M)
    elif valik == 5:
        V = int(input("Millist loendit sooritada sorteerimine (1 või 2): "))
        if V == 1:
            a_list.sort()
            print(a_list)
        elif V == 2:
            b_list.sort()
            print(b_list)
        else:
            print("Error!")
    elif valik == 6:
        V = int(input("Millist loendit sooritada sorteerimine (1 või 2): "))
        if V == 1:
            a_list.sort(reverse=True)
            print(a_list)
        elif V == 2:
            b_list.sort(reverse=True)
            print(b_list)
        else:
            print("Error!")
    elif valik == 7:
        try:
            g = int(input("Sisesta number kuni mille loend ulatub: "))
            c_list = list(range(g))
            print(c_list)
        except ValueError:
            print("Error")
    elif valik == 8:
        V = int(input("Kumb loend soovite kopeerida (1 või 2): "))
        if V == 1:
            a_copy = a_list.copy()
            print(a_copy)
        elif V == 2:
            b_copy = b_list.copy()
            print(b_copy)
        else:
            print("Error!")
    elif valik == 9:
        V = int(input("Millises loendis soovite muuta tähte (1 või 2): "))
        if V == 1:
            while True:
                try:
                    i = int(input("Sisesta number: "))
                    break
                except ValueError:
                    print("Vale formaat!")
            while True:
                k = input("Sisesta ükskõik milline täht/sõna/lausung: ")
                if k.isalpha():
                    break
                else:
                    print("Vale formaat!")
            a_list[i] = k
            print(a_list)
        elif V == 2:
            while True:
                try:
                    i = int(input("Sisesta number: "))
                    break
                except ValueError:
                    print("Vale formaat!")
            while True:
                k = input("Sisesta ükskõik milline täht/sõna/lausung: ")
                if k.isalpha():
                    break
                else:
                    print("Vale formaat!")
            b_list[i] = k
            print(b_list)
        else:
            print("Error!")
    elif valik == 10:
        V = int(input("Kumb loend soovite eemaldada (1 või 2): "))
        if V == 1:
            a_list.clear()
            print(a_list)
        elif V == 2:
            b_list.clear()
            print(b_list)
        else:
            print("Error!")
    elif valik == 11:
        V = int(input("Millist stringi kontrollida (1 või 2): "))
        if V == 1:
            print(a.istitle())
        elif V == 2:
            print(b.istitle())
        else:
            print("Error!")
    elif valik == 12:
        V = int(input("Millise rea eesolevad tähemärgid lahendada(1 või 2): "))
        C = input("Sisesta eemaldatavad tähemärgid ")
        if V == 1:
            print(a.lstrip(C))
        elif V == 2:
            print(b.lstrip(C))
        else:
            print("Error!")
    elif valik == 13:
        V = int(input("Millises reas vahetada juhtmik (1 või 2): "))
        if V == 1:
            print(a.swapcase())
        elif V == 2:
            print(b.swapcase())
        else:
            print("Error!")
    elif valik == 14:
        V = int(input("Millisel real pane esimene märk suurtähtedega (1 või 2): "))
        if V == 1:
            print(a.capitalize())
        elif V == 2:
            print(b.capitalize())
        else:
            print("Error!")
    elif valik == 15:
        V = int(input("Millises loetelus kustutada viimased tähemärgid (1 või 2): "))
        C = input("Sisesta eemaldatavad tähemärgid ")
        if V == 1:
            print(a.rstrip(C))
        elif V == 2:
            print(b.rstrip(C))
        else:
            print("Error!")
    elif valik == 0:
        break
    else:
        print("Error")       
