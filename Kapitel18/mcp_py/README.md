# Model Context Protocol (MCP)

Dieses Verzeichnis enthält Beispiele für die Verwendung des Model Context Protocol (MCP) zur Integration von LLMs mit externen Datenquellen und Werkzeugen.

## Beispiele

### MCP Calculator

Ein einfaches Beispiel für mathematische Berechnungen über MCP.

#### MCP Calculator Client

**Datei:** [calc_client.py](calculator/calc_client.py)

MCP-Agent für mathematische Berechnungen. Der Agent nutzt den MCP-Server, um Berechnungen durchzuführen.

#### MCP Calculator Server

**Datei:** [calc_server.py](calculator/calc_server.py)

MCP-Server mit Rechenfunktionen.

### MCP Superstore

Ein komplexeres Beispiel für SQL-Abfragen an Superstore-Daten über MCP.

#### MCP SQL Client

**Datei:** [sql_client.py](superstore/sql_client.py)

MCP-Agent für SQL-Abfragen an Superstore-Daten. Der Agent nutzt den MCP-Server, um Datenbankabfragen durchzuführen.

#### MCP SQL Server

**Datei:** [sql_server.py](superstore/sql_server.py)

MCP-Server mit SQL-Datenbank-Funktionen.

#### Datenanalyse

**Datei:** [analyze.py](superstore/analyze.py)

Einfache Analyse des Superstore-Datensatzes mit pandas.

#### Datenkonvertierung

**Datei:** [convert.py](superstore/convert.py)

Konvertierung der Superstore-Daten.

## Verwendung

```bash
# MCP Calculator
cd calculator
# Server starten (in einem Terminal)
python calc_server.py
# Client ausführen (in einem anderen Terminal)
python calc_client.py

# MCP Superstore
cd superstore
# Server starten (in einem Terminal)
python sql_server.py
# Client ausführen (in einem anderen Terminal)
python sql_client.py

# Datenanalyse
cd superstore
python analyze.py
```

## Voraussetzungen

- Python 3.10+
- MCP (Model Context Protocol)
- LangChain MCP
- LangGraph
- Ollama (für lokale LLMs) oder OpenAI-API-Key
- pandas (für Datenanalyse)

## Weitere Ressourcen

- **Offizielle MCP-Dokumentation:** [https://modelcontextprotocol.io](https://modelcontextprotocol.io)
- **MCP GitHub Repository:** [https://github.com/modelcontextprotocol/specification](https://github.com/modelcontextprotocol/specification)
- **LangChain MCP Integration:** [https://python.langchain.com/docs/integrations/toolkits/mcp/](https://python.langchain.com/docs/integrations/toolkits/mcp/)
- **MCP Server Registry:** [https://github.com/modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers)