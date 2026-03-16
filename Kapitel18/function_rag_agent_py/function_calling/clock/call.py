from datetime import datetime

from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import ChatOllama
from langchain.tools import tool
from langchain.agents import create_tool_calling_agent, AgentExecutor

# 1. Funktion mit @tool Decorator definieren (wichtig: der docstring enthält wertvolle Metadaten für das LLM!)
@tool
def get_current_time(query: str = "") -> str:
    """Gibt die aktuelle Uhrzeit zurück."""
    return datetime.now().strftime("%H:%M:%S")

# 2. Tools Liste
tools = [get_current_time]

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
response = agent_executor.invoke({"input": "Wie spät ist es gerade?"})
print(response["output"])