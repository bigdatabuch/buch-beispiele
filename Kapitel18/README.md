# Kapitel 18: KI-basierte Systeme mit Generativer KI

Dieses Kapitel behandelt die Verwendung großer Sprachmodelle (LLMs) im Kontext von Big Data. Es zeigt praktische Anwendungsszenarien für die Integration von LLMs mit Datenquellen und Werkzeugen.

## Übersicht der Code-Beispiele

### 1. Training von Sprachmodellen (`training_py/`)

- **[Torch Training](training_py/torch_training/train.py)**: Ein vereinfachtes Modell ("WinzlingLM") zur Next-Word-Prediction mit PyTorch
- **[Fine-Tuning mit HuggingFace](training_py/fine_tune_csv/train.py)**: Fine-Tuning von DistilGPT-2 für Frage/Antwort-Aufgaben mithilfe des HuggingFace Transformers-Frameworks

### 2. RAG und Agenten mit Function Calling (`function_rag_agent_py/`)

#### Retrieval-Augmented Generation (RAG)
- **[RAG mit FAISS und Ollama](function_rag_agent_py/rag/rag_faiss.py)**: Lokales RAG-System mit FAISS-Vektordatenbank und dem LLaMA3.1-Modell über Ollama
- **[RAG mit OpenAI](function_rag_agent_py/rag/rag_faiss_openai.py)**: RAG-System mit OpenAI's GPT-4o-mini und OpenAI-Embeddings

#### Function Calling
- **[Uhrzeit-Abfrage](function_rag_agent_py/function_calling/clock/)**: Einfaches Tool zur Abfrage der aktuellen Systemzeit
- **[CSV-Zähler](function_rag_agent_py/function_calling/csv/call_csv.py)**: Tool zum Zählen von Zeilen in CSV-Dateien mit pandas und LLM

#### Agenten
- **[Zuwachs-Berechnung mit Agent](function_rag_agent_py/agent/zuwachs.py)**: Agent mit Python-REPL für Berechnungen und Wikipedia für Recherche

### 3. Model Context Protocol (MCP) (`mcp_py/`)

#### MCP Calculator
- **[MCP Calculator Client](mcp_py/calculator/calc_client.py)**: MCP-Agent für mathematische Berechnungen
- **[MCP Calculator Server](mcp_py/calculator/calc_server.py)**: MCP-Server mit Rechenfunktionen

#### MCP Superstore
- **[MCP SQL Client](mcp_py/superstore/sql_client.py)**: MCP-Agent für SQL-Abfragen an Superstore-Daten
- **[MCP SQL Server](mcp_py/superstore/sql_server.py)**: MCP-Server mit SQL-Datenbank-Funktionen
- **[Datenanalyse](mcp_py/superstore/analyze.py)**: Einfache Analyse des Superstore-Datensatzes mit pandas
- **[Datenkonvertierung](mcp_py/superstore/convert.py)**: Konvertierung der Superstore-Daten

## Weitere Ressourcen

- [README: Training von Sprachmodellen](training_py/README.md)
- [README: RAG und Agenten](function_rag_agent_py/README.md)
- [README: Model Context Protocol](mcp_py/README.md)

## Voraussetzungen

Die Beispiele setzen voraus:
- Python 3.10+
- Ollama (für lokale LLMs) oder Zugriff auf OpenAI-API (alternativ auch mit anderen kompatiblen Endpoints wie beispielsweise openrouter.ai etc.)
- Die benötigten Python-Pakete sind in den `pyproject.toml`-Dateien definiert

## Hinweise

- Die Beispiele sind so konzipiert, dass sie lokal auf handelsüblichen Geräten wie Laptops ausführbar sind
- Für das Training großer Modelle werden GPUs empfohlen, die Beispiele laufen aber auch auf CPU
- Die MCP-Beispiele verwenden die moderne LangGraph-Syntax für Agenten

---

*Letzte Aktualisierung: 14. März 2026*