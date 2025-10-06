import random 

def sazeniminci():
    kapital = 100
    vyhra = random.randint(0, 1)
    pokracovani = 1

    while pokracovani == 1:
        sazka = int(input("kolik chceš vsadit?"))
        volba = int(input("vyber si orel(0) nebo panna(1)"))
        if vyhra == volba:
            print("vyhral jsi dostáváš", 2*sazka)
            kapital += 2*sazka
            print("Novy kapital: ", kapital,"Kč")
        else:
            print("prohral jsi")
            kapital -= sazka
            print("Novy kapital", kapital,"Kč")

        pokracovani = int(input(print("Chceš pokračovat? 0/1")))

sazeniminci()
