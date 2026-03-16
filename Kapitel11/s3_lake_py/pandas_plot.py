import pandas as pd
import matplotlib.pyplot as plt

# 1. Datenquelle (hier als Dictionary simuliert)
data = {
    'Datum': ['2023-11-01', '2023-11-02', '2023-11-03', '2023-11-04',
              '2023-11-05', '2023-11-06', '2023-11-07'],
    'Verkaeufe': [150, 175, 160, 210, 205, 180, 195]
}

# 2. Data Frame erstellen und transformieren
# Die Spalte 'Datum' wird in einen echten Datumstyp umgewandelt.
df = pd.DataFrame(data)
df['Datum'] = pd.to_datetime(df['Datum'])

# 3. Visualisierung
plt.figure(figsize=(10, 5)) # Größe der Zeichenfläche festlegen

# Liniendiagramm erstellen mit Markern für die Datenpunkte
plt.plot(df['Datum'], df['Verkaeufe'], marker='o', linestyle='-')

# Diagramm beschriften
plt.title('Tägliche Verkäufe im November 2023')
plt.xlabel('Datum')
plt.ylabel('Anzahl der Verkäufe')
plt.grid(True) # Ein Gitter zur besseren Ablesbarkeit hinzufügen
plt.tight_layout() # Sorgt für eine saubere Anordnung der Elemente

plt.savefig("/tmp/line.png") # Speichert das Diagramm als PNG