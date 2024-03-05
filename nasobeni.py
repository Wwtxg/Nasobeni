import random

body = 0

plusbody = 1

def PocetB (body, plusbody):
    Pocetbodu = body + plusbody
    return Pocetbodu

def nasobenifunkce (x, y):
    nasobeni = x * y
    return nasobeni


for a in range(9):
    x = random.randint(1, 10)
    y = random.randint(1, 10)

    print (x,"*",y)

    odpoved = int(input("Zadejte svoji odpoved: "))

    Spravna_odpoved = nasobenifunkce(x, y)

    print ("Vase odpoved: ", odpoved)
    print ("Spravne odpoved: ", Spravna_odpoved)

    if odpoved == Spravna_odpoved:
        print ("Spavně")
        Pocetbodu = PocetB(body, plusbody)
        print ("Mate", Pocetbodu, "bodu")
    else:
        print ("Chyba")
        print ("Mate", Pocetbodu, "bodu")

