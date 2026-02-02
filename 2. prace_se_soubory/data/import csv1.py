import csv

pocet_her = 0
delka_her = 0
cesta = r"snakes_count_10000.csv"
with open (cesta, "r",encoding="utf-8") as file:
    for radek in csv.DictReader(file):
        pocet_her += 1

        delka_her += float(radek["Game_Length"])

prumer_hry = delka_her/pocet_her

print(f"Prumerna delka hry: {prumer_hry}")
