import random

priklad = int(input("Kolik chceš přikladu"))

for i in range (priklad):
   if random.randint(0,1) == 1:
    print(random.randint(0,10), "+", random.randint(0,10),"=",)
   else:
     print(random.randint(0,10), "-", random.randint(0,10),"=",)

vysledek = int(input("vypis vysledsky"))


