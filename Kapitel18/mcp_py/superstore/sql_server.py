from mcp.server.fastmcp import FastMCP
import sqlite3, pandas as pd

mcp = FastMCP("SuperstoreSQLTool")

@mcp.tool()
def run_query(sql: str) -> str:
    """
    SQL-Abfrage auf Superstore-Datenbank ausführen.
    Führt eine SQL-Abfrage auf der Tabelle 'sales' aus.
    """
    conn = sqlite3.connect("superstore.db")
    try:
        df = pd.read_sql_query(sql, conn)
        return df.to_string(index=False)
    except Exception as e:
        return f"Fehler: {e}"
    finally:
        conn.close()

@mcp.tool()
def get_schema() -> str:
    """Gibt das SQL-Schema der Tabelle 'sales' zurück."""
    conn = sqlite3.connect("superstore.db")
    cursor = conn.cursor()
    cursor.execute("PRAGMA table_info(sales);")
    schema = cursor.fetchall()
    conn.close()
    return "\n".join([f"{col[1]} ({col[2]})" for col in schema])


if __name__ == "__main__":
    mcp.run(transport="stdio")