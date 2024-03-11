import random

Pocetbodu = 0

plusbody = 1

def PocetB (Pocetbodu, plusbody):
    PocetboduF = Pocetbodu + plusbody
    return PocetboduF

def nasobenifunkce (x, y):
    nasobeni = x * y
    return nasobeni

def delenifunkce (x, y):
    deleni = x / y
    return deleni

def minusfunkce (x, y):
    minus = x - y
    return minus

def plusfunkce (x, y):
    plus = x + y
    return plus

for a in range(9):
    x = random.randint(1, 10)
    y = random.randint(1, 10)

    pmdn = random.choice("-+:*")
    print (pmdn)

    print (x, pmdn, y)

    odpoved = float(input("Zadejte svoji odpoved: "))

    if pmdn == "-":
        Spravna_odpoved = minusfunkce (x, y)
    elif pmdn == "+":
        Spravna_odpoved = plusfunkce (x, y)
    elif pmdn == "*":
        Spravna_odpoved = nasobenifunkce (x, y)
    elif pmdn == "/":
        Spravna_odpoved = delenifunkce (x, y)
    
    Rounded_Spravna_odpoved = round(Spravna_odpoved, 2)

    print ("Vase odpoved: ", odpoved)
    print ("Spravna odpoved: ", Rounded_Spravna_odpoved)

    if odpoved == Rounded_Spravna_odpoved:
        print ("Spavně")
        PocetboduF = PocetB(Pocetbodu, plusbody)
        Pocetbodu = PocetboduF
        print ("Mate", PocetboduF, "bodu")
    else:
        print ("Chyba")
        Pocetbodu = PocetboduF
        print ("Mate", PocetboduF, "bodu")

