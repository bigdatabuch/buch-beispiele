# Training von Sprachmodellen - Vereinfach, zu Demonstrationszwecken

Dieses Verzeichnis enthält Beispiele zum Training und Fine-Tuning von Sprachmodellen.

## Beispiele

### Torch Training

Ein vereinfachtes Modell ("WinzlingLM") zur Next-Word-Prediction demonstration mit PyTorch.

**Datei:** [train.py](torch_training/train.py)

Das Modell lernt, ausgehend von einem gegebenen Wort das nächste Wort vorherzusagen. Es illustriert die Grundidee hinter modernen Decoder-only-Sprachmodellen wie GPT: die Next-word Prediction.

### Fine-Tuning mit HuggingFace

Fine-Tuning von DistilGPT-2 für Frage/Antwort-Aufgaben mithilfe des HuggingFace Transformers-Frameworks.

**Datei:** [train.py](fine_tune_csv/train.py)

Dieses Beispiel zeigt, wie sich ein vortrainiertes Modell mit wenigen Codezeilen an einen neuen Datensatz anpassen lässt. Das Modell wird mit einem CSV-Datensatz von Frage/Antwort-Paaren feingetuned.

## Verwendung

```bash
# Torch Training
cd torch_training
python train.py

# Fine-Tuning
cd fine_tune_csv
python train.py
```

## Voraussetzungen

- Python 3.10+
- PyTorch
- Transformers von HuggingFace
- Datasets
- pandas