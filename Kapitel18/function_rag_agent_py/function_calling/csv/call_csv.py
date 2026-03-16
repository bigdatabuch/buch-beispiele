import pandas as pd
from langchain_ollama import ChatOllama
from langchain.agents import create_tool_calling_agent, AgentExecutor
from langchain.tools import tool
from langchain_core.prompts import ChatPromptTemplate


# 1. Funktion mit @tool Decorator definieren
@tool
def count_rows(file_path: str = "data.csv") -> str:
    """Zählt die Anzahl der Zeilen in einer CSV-Datei.

    Args:
        file_path: Pfad zur CSV-Datei (Standard: data.csv)
    """
    try:
        df = pd.read_csv("./" + file_path)
        return f"Die Datei {file_path} enthält {len(df)} Zeilen."
    except Exception as e:
        return f"Fehler beim Lesen der Datei: {str(e)}"


# 2. Tools Liste
tools = [count_rows]

# 3. LLM laden (lokal via Ollama: das LLM muss Function Calling unterstützen)
llm = ChatOllama(base_url="http://host.name:11434", model="gpt-oss:latest")

# 4. Prompt Template erstellen
prompt = ChatPromptTemplate.from_messages([
    ("system", "Du bist ein hilfreicher Assistent. Nutze die verfügbaren Tools, um Fragen zu beantworten."),
    ("human", "{input}"),
    ("placeholder", "{agent_scratchpad}")
])

# 5. Agent erstellen
agent = create_tool_calling_agent(llm, tools, prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

# 6. Anfrage stellen
response = agent_executor.invoke({"input": "Wie viele Zeilen sind in der Datei data.csv?"})
print(response["output"])