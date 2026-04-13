from tools.sql_tool import run_sql
from utils.llm import llm

def sql_node(state):
    query = state["query"]

    prompt = f"""
    Convert the user question into SQL query.

    Table name: stocks

    Columns:
    Date, SP500, Dividend, Earnings, CPI, Long Interest Rate, Real Price, Real Dividend, Real Earnings, PE10

    Rules:
    - Return ONLY raw SQL query
    - DO NOT use ```sql
    - DO NOT explain anything
    - Only SQL

    Question:
    {query}
    """

    sql_query = llm.invoke(prompt).content.strip()

    result = run_sql(sql_query)

    return {
        "response": str(result),
        "decision": state["decision"]
    }