# Neuronová síť predikující kategorii kvality ovzduší (AQI)
# Dataset: Pakistan Air Quality
# Vstupy: carbon_monoxide, nitrogen_dioxide, sulphur_dioxide, ozone
# Výstupy: aqi_category (Good, Moderate, Unhealthy for Sensitive Groups, Unhealthy, Very Unhealthy)

import csv

from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
from sklearn.metrics import ConfusionMatrixDisplay, classification_report

# ---------- Načtení CSV a úprava dat ----------
X = []  # vstupy
Y = []  # výstupy

# Pouze kategorie, které chceme predikovat (filtrujeme Hazardous)
allowed_categories = {
    "Good",
    "Moderate",
    "Unhealthy for Sensitive Groups",
    "Unhealthy",
    "Very Unhealthy"
}

with open("git\kb4a_prog\pakistan_air_quality_final_clean.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        category = row["aqi_category"]

        # Přeskočíme kategorie mimo náš výběr
        if category not in allowed_categories:
            continue

        try:
            carbon_monoxide  = float(row["carbon_monoxide"])
            nitrogen_dioxide = float(row["nitrogen_dioxide"])
            sulphur_dioxide  = float(row["sulphur_dioxide"])
            ozone            = float(row["ozone"])
        except ValueError:
            continue  # přeskočíme řádky s chybějícími hodnotami

        X.append([carbon_monoxide, nitrogen_dioxide, sulphur_dioxide, ozone])
        Y.append(category)

print(f"Načteno {len(X)} záznamů")

# Statistika kategorií
from collections import Counter
print("Rozložení kategorií:")
for cat, count in sorted(Counter(Y).items()):
    print(f"  {cat}: {count}")

# ---------- Rozdělení na trénování a testování ----------
trening_X, test_X, trening_Y, test_Y = train_test_split(
    X, Y,
    test_size=0.2,
    random_state=42
)

# ---------- Normalizace dat ----------
# Důležité! CO je v řádech stovek, ostatní hodnoty jsou malá čísla.
# Normalizace zabrání tomu, aby jedna proměnná dominovala ostatním.
scaler = StandardScaler()
trening_X = scaler.fit_transform(trening_X)
test_X    = scaler.transform(test_X)

# ---------- Neuronová síť ----------
neural_network = MLPClassifier(
    hidden_layer_sizes=(64, 32, 16),  # 3 skryté vrstvy
    activation="relu",
    max_iter=500,
    verbose=True,
    random_state=42,
    early_stopping=False,
)

neural_network.fit(trening_X, trening_Y)

# ---------- Vyhodnocení ----------
results = neural_network.predict(test_X)

correct = sum(1 for pred, true in zip(results, test_Y) if pred == true)
print(f"\nPřesnost: {correct / len(results):.4f} ({correct}/{len(results)})")

print("\nPodrobná zpráva:")
print(classification_report(test_Y, results))

# ---------- Confusion Matrix ----------
fig, ax = plt.subplots(figsize=(8, 6))
ConfusionMatrixDisplay.from_predictions(
    test_Y, results,
    ax=ax,
    xticks_rotation=30
)
plt.title("Confusion Matrix – AQI Category Prediction")
plt.tight_layout()
plt.savefig("confusion_matrix.png", dpi=150)
plt.show()

# ---------- Křivka učení ----------
plt.figure(figsize=(8, 4))
plt.plot(neural_network.loss_curve_, label="Trénovací ztráta")
if hasattr(neural_network, 'best_loss_') and neural_network.best_loss_ is not None:
    plt.axhline(neural_network.best_loss_, color="red",
                linestyle="--", label=f"Nejlepší validační ztráta: {neural_network.best_loss_:.4f}")
plt.xlabel("Iterace")
plt.ylabel("Ztráta (loss)")
plt.title("Průběh trénování neuronové sítě")
plt.legend()
plt.tight_layout()
plt.savefig("learning_curve.png", dpi=150)
plt.show()

# ---------- Ukázka predikce ----------
print("\n--- Ukázka predikce na nových datech ---")
examples = [
    [400,  10, 3,  40],   # nízké hodnoty → očekáváme Good/Moderate
    [1200, 40, 15, 80],   # střední hodnoty → Moderate/Unhealthy for Sensitive
    [3000, 80, 40, 150],  # vysoké hodnoty → Unhealthy/Very Unhealthy
]
labels = ["Nízké hodnoty", "Střední hodnoty", "Vysoké hodnoty"]
scaled_examples = scaler.transform(examples)
predictions = neural_network.predict(scaled_examples)
probabilities = neural_network.predict_proba(scaled_examples)
classes = neural_network.classes_

print(f"{'Příklad':<20} {'Predikce':<35} {'Pravděpodobnost'}")
print("-" * 80)
for label, pred, probs in zip(labels, predictions, probabilities):
    max_prob = max(probs)
    print(f"{label:<20} {pred:<35} {max_prob:.1%}")
