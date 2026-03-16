# RAG und Agenten mit Function Calling

Dieses Verzeichnis enthält Beispiele für Retrieval-Augmented Generation (RAG), Function Calling und Agenten-basierte LLM-Anwendungen.

## Beispiele

### Retrieval-Augmented Generation (RAG)

RAG verbindet Sprachmodelle mit externen Datenquellen, um die Vertrauenswürdigkeit und Aktualität der Antworten zu verbessern.

#### RAG mit FAISS und Ollama

**Datei:** [rag_faiss.py](rag/rag_faiss.py)

Lokales RAG-System mit FAISS-Vektordatenbank und dem LLaMA3.1-Modell über Ollama.

#### RAG mit OpenAI

**Datei:** [rag_faiss_openai.py](rag/rag_faiss_openai.py)

RAG-System mit OpenAI's GPT-4o-mini und OpenAI-Embeddings.

### Function Calling

Function Calling ermöglicht es LLMs, externe Funktionen oder Tools aufzurufen.

#### Uhrzeit-Abfrage

**Verzeichnis:** [clock/](function_calling/clock/)

Einfaches Tool zur Abfrage der aktuellen Systemzeit.

#### CSV-Zähler

**Datei:** [call_csv.py](function_calling/csv/call_csv.py)

Tool zum Zählen von Zeilen in CSV-Dateien mit pandas und LLM.

### Agenten

Agenten erweitern Function Calling um mehrere Iterationen und Werkzeuge.

#### Zuwachs-Berechnung mit Agent

**Datei:** [zuwachs.py](agent/zuwachs.py)

Agent mit Python-REPL für Berechnungen und Wikipedia für Recherche. Der Agent plant mehrere Arbeitsschritte, ruft Tools wiederholt auf und kombiniert deren Ergebnisse.

## Verwendung

```bash
# RAG mit Ollama
cd rag
python rag_faiss.py

# RAG mit OpenAI
cd rag
python rag_faiss_openai.py

# Function Calling (CSV-Zähler)
cd function_calling/csv
python call_csv.py

# Agent
cd agent
python zuwachs.py
```

## Voraussetzungen

- Python 3.10+
- LangChain
- LangChain Ollama
- LangChain OpenAI
- FAISS
- Wikipedia (für Agenten)
- Ollama (für lokale LLMs) oder OpenAI-API-Key