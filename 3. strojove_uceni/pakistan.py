import csv

from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn.metrics import ConfusionMatrixDisplay

X = []
Y = []

with open("git\kb4a_prog\pakistan_air_quality_final_clean.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        carbon = float(row["carbon_monoxide"])
        nitrogen = float(row["nitrogen_dioxide"])
        sulphur = float(row["sulphur_dioxide"])
        ozone = float(row["ozone"])

        if row["aqi_category"] == "Very Unhealthy":
            aqi_category = 0
        elif row["aqi_category"] == "Unhealthy":
            aqi_category = 1
        elif row["aqi_category"] == "Unhealthy for Sensitive Groups":
            aqi_category = 2
        elif row["aqi_category"] == "Moderate":
            aqi_category = 3
        elif row["aqi_category"] == "Good":
            aqi_category = 4

        X.append ([carbon, nitrogen, sulphur, ozone])
        Y.append (aqi_category)

trening_X, test_X, trening_Y, test_Y  = train_test_split(
        X, Y,
        test_size=0.2,
        random_state=42)

# ---------- Neuronová síť ----------
neural_network = MLPClassifier(
    hidden_layer_sizes=(32, 16, 16 ),
    activation="relu",
    max_iter=2000,
    verbose=True,
    random_state=4,
    n_iter_no_change=40
)

neural_network.fit(trening_X, trening_Y)

# ---------- Vyhodnocení ----------
results = neural_network.predict(test_X)

correct = 0
for i in range(len(results)):
    if test_Y[i] == results[i]:
        correct += 1
print("Přesnost:", correct / len(results))

# ---------- Confusion matrix ----------
# zobrazuje jaké odpovědi dává neuronka pro dané vstupy
ConfusionMatrixDisplay.from_predictions(
    test_Y, results)
plt.show()
