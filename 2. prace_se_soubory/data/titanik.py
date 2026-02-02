import csv
import matplotlib.pyplot as plt


pocet_male = 0
pocet_female = 0
soucet_vek = 0
pocet_pasazeru = 0
cesta= r"2. prace_se_soubory\data\titanic.csv"
with open(cesta, "r",encoding="utf-8") as file:
    for radek in csv.DictReader(file):
        if radek["Sex"] == "male":
            pocet_male += 1
        if radek["Sex"] =="female":
            pocet_female +=1
        
        pocet_pasazeru += 1
        soucet_vek += float(radek["Age"])

prumer_vek = round(soucet_vek/pocet_pasazeru)

print(f"Počet mužů: {pocet_male}")
print(f"Počet žen: {pocet_female}")

plt.bar(["Muži", "Ženy"], [pocet_male, pocet_female])
plt.show()

print(f"Průměrný věk: {prumer_vek}")