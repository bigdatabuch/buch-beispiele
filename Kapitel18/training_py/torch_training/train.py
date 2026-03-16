import torch
import torch.nn as nn
import torch.optim as optim
# Trainings-Datensatz (Mini-Korpus)
text = "Big Data Analyse Big Data KI Big Data"
tokens = text.split()
vocab = list(set(tokens)) # Eindeutige Wörter: ['Big', 'Data', 'Analyse', 'KI']
stoi = {w:i for i,w in enumerate(vocab)} # Ordnet Wörtern Zahlen zu, z.B. {'Big': 0, 'Data': 1, ...}
itos = {i:w for w,i in stoi.items()} # Umgekehrte Zuordnung zum Dekodieren

# Trainingsdaten (Paare: Input -> nächstes Wort)
data = [(stoi[tokens[i]], stoi[tokens[i+1]])
        for i in range(len(tokens)-1)]
# Modellarchitektur: Embedding Layer + Linear Layer
model = nn.Sequential(
    # Embedding-Schicht: Wandelt Wort-Indizes in dichte 8-dimensionale Vektoren um
    nn.Embedding(len(vocab), 8),
    # Lineare Schicht: Projiziert Embeddings auf Vokabulargröße (4) für Klassifikation
    nn.Linear(8, len(vocab))
)
loss_fn = nn.CrossEntropyLoss() # Loss Funktion
optimizer = optim.Adam(model.parameters(), lr=0.05) # Lernrate von 0,05
# Trainiert für 200 Epochen mit Adam-Optimierer
for epoch in range(200):
    total_loss = 0
    for x,y in data:
        x = torch.tensor([x]) # x: aktueller Wort-Index
        y = torch.tensor([y]) # y: Ziel-Wort-Index (nächstes Wort)
        optimizer.zero_grad() # Gradienten löschen
        logits = model(x) # Vorwärtsdurchlauf
        loss = loss_fn(logits, y) # CrossEntropy-Verlust
        loss.backward() # Gradienten berechnen
        optimizer.step() # Gewichte aktualisieren
        total_loss += loss.item()
    if epoch % 50 == 0:
        print(f"Epoch {epoch}: Loss {total_loss:.4f}")

# Testet, welches Wort das Modell nach "Big" vorhersagt
x = torch.tensor([stoi["Big"]])
logits = model(x)
pred = torch.argmax(logits, dim=1).item()
print(f"'Big' -> '{itos[pred]}'")