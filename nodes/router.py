from utils.llm import llm

def router_node(state):
    query = state["query"]

    prompt = f"""
    You are a routing agent.

    Decide whether the query requires SQL or not.

    Use SQL ONLY if:
    - Query asks for numerical/statistical operations
    - Query involves structured data (SP500, averages, max, min, etc.)

    Otherwise, choose RAG.

    Examples:
    - "What is average SP500?" → SQL
    - "What is a stock market?" → RAG
    - "Explain Apple revenue" → RAG

    Query: {query}

    Answer ONLY one word:
    SQL or RAG
    """

    decision = llm.invoke(prompt).content.strip().upper()

    return {"decision": decision}