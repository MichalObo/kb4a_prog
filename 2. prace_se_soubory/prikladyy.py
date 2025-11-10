cesta = "kb4a_prog\\2. prace_se_soubory\data\priklady.txt"

with open(cesta, "r", encoding="utf-8") as file:
    for line in file.readlines():
        print(line)



