from langchain_ollama import ChatOllama
from langchain.agents import create_tool_calling_agent, AgentExecutor
from langchain_core.prompts import ChatPromptTemplate
from langchain_experimental.tools import PythonREPLTool
from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper

# 1. LLM laden
llm = ChatOllama(base_url="http://host.name:11434", model="gpt-oss:latest")

# 2. Tools - direkt aus LangChain
tools = [
    PythonREPLTool(),
    WikipediaQueryRun(api_wrapper=WikipediaAPIWrapper())
]

# 3. Einfaches Prompt
prompt = ChatPromptTemplate.from_messages([
    ("system", "Du bist ein hilfreicher Assistent. Nutze die verfügbaren Tools."),
    ("human", "{input}"),
    ("placeholder", "{agent_scratchpad}")
])

# 4. Agent
agent = create_tool_calling_agent(llm, tools, prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

# Anfrage
query = (
    "Berechne den Zuwachs, wenn sich Datenmengen "
    "von 1 TB jährlich über 10 Jahre verdoppeln. "
    "Nutze Python für die Berechnung und erkläre "
    "dann mit Bezug auf Wikipedia, warum exponentielles "
    "Datenwachstum für Big Data wichtig ist."
)

response = agent_executor.invoke({"input": query})
print(response["output"])