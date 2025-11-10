import random
emoji1 =["🌺", "🌼", "🌞", "🐻", "❤️‍", "🔥"]
cesta = "kb4a_prog\\2. prace_se_soubory\data\citaty.txt"

with open(cesta, "r", encoding="utf-8") as file:
    obsah = file.read()
    nahodnyradek = random.choice(obsah.splitlines())    
    print("Citát dne je:", nahodnyradek)

    autor = citat.split("-")[-1]

    for i in range (random.randint(3 ,5)):
        print(random.choice(emoji1), end=" ")