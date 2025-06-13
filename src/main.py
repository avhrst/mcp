from fastmcp import FastMCP
import oracledb
import os
from typing import List, Dict, Any

mcp = FastMCP("Simple MCP Server")

def get_oracle_connection():
    """Get Oracle database connection"""
    connection_string = os.getenv("ORACLE_CONNECTION_STRING", "localhost:1521/XE")
    username = os.getenv("ORACLE_USERNAME", "hr")
    password = os.getenv("ORACLE_PASSWORD", "password")
    
    return oracledb.connect(
        user=username,
        password=password,
        dsn=connection_string
    )

@mcp.tool()
def hello(name: str = "World") -> str:
    """Say hello to someone"""
    return f"Hello, {name}!"

@mcp.tool()
def add_numbers(a: int, b: int) -> int:
    """Add two numbers together"""
    return a + b

@mcp.tool()
def execute_query(sql: str) -> List[Dict[str, Any]]:
    """Execute a SQL query against Oracle database"""
    try:
        with get_oracle_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(sql)
                columns = [desc[0] for desc in cursor.description] if cursor.description else []
                rows = cursor.fetchall()
                return [dict(zip(columns, row)) for row in rows]
    except Exception as e:
        return [{"error": str(e)}]

@mcp.tool()
def get_tables() -> List[str]:
    """Get list of all tables in the Oracle database"""
    try:
        with get_oracle_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute("SELECT table_name FROM user_tables ORDER BY table_name")
                return [row[0] for row in cursor.fetchall()]
    except Exception as e:
        return [f"Error: {str(e)}"]

@mcp.tool()
def describe_table(table_name: str) -> List[Dict[str, Any]]:
    """Get table structure for a specific Oracle table"""
    try:
        with get_oracle_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute("""
                    SELECT column_name, data_type, nullable, data_default
                    FROM user_tab_columns
                    WHERE table_name = UPPER(:table_name)
                    ORDER BY column_id
                """, {"table_name": table_name})
                columns = [desc[0] for desc in cursor.description]
                rows = cursor.fetchall()
                return [dict(zip(columns, row)) for row in rows]
    except Exception as e:
        return [{"error": str(e)}]

if __name__ == "__main__":
    mcp.run() 