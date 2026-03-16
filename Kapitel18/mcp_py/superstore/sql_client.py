import asyncio
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from langchain_mcp import MCPToolkit
from langgraph.prebuilt import create_react_agent
from langchain_ollama import ChatOllama

# LLM
model = ChatOllama(base_url="http://host.name:11434", model="gpt-oss:latest")

# Server-Parameter für MCP
server_params = StdioServerParameters(
    command="python",
    args=["sql_server.py"],  # Starte den MCP Server
)

async def run_agent():
    """Führt den Agent mit MCP Tools aus."""
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            # Session initialisieren
            await session.initialize()
            # MCP Toolkit erstellen
            toolkit = MCPToolkit(session=session)
            await toolkit.initialize()
            tools = toolkit.get_tools()
            # Agent mit den Tools erstellen
            agent = create_react_agent(model, tools)
            # Agent-Anfrage ausführen (moderne Syntax)
            response = await agent.ainvoke({
                "messages": [{"role": "user", "content": "Wie hoch war der Gewinn 2016?"}]
            })
            # Antwort extrahieren
            print(response["messages"][-1].content)

# Agent ausführen
asyncio.run(run_agent())