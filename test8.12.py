import csv

cesta = r"2. prace_se_soubory\data\vira_v_cesku.csv"

with open(cesta, "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    vyber =int(input("Vyber ulohu [1] statistiky pro vybrané náboženství, [2] ulož výsledky Brna, [3] Graf víry"))
    if vyber == 1:
        nabozenstvi_vyber = input("Vyber náboženství")
        with open(cesta, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            nabozenstvi = []
            hodnoty = 0
            pocet_vericich = []
            maximum = 0

            for radek in reader:
                if radek["vira_txt"] == nabozenstvi_vyber:
                    hodnota_vericich = int(radek["hodnota"])
                    hodnoty += hodnota_vericich
                    pocet_vericich.append(hodnota_vericich)

            for i in range(len(pocet_vericich)):
                if pocet_vericich[i] > maximum:
                    maximum = pocet_vericich[i]

    elif vyber == 2:
        with open("nabozenstvi_v_brne.txt", "a", encoding="utf-8") as file1:
            reader = csv.DictReader(file)

            for radek in reader:
                if radek["uzemi_txt"] == "Brno":
                        nazev = "vira_txt"
                        cislo_vericich = "hodnota"
                        file.write(nazev,":", cislo_vericich)
    elif vyber == 3:
        with open(cesta, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            bez_viry = "vira_txt.Bez náboženské víry" + "vira_txt.ateimus"
            neuvedeno = "vira.txt_Neuvedeno"
            verici = "vira_txt"-"vira_txt.Bez náboženské víry"-"vira_txt.ateimus"-"vira.txt_Neuvedeno"