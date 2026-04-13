from tools.rag_tool import rag_query
from utils.llm import llm

def rag_node(state):
    query = state["query"]

    context = rag_query(query)

    prompt = f"""
    Answer using only this context:
    {context}

    Question: {query}
    """

    response = llm.invoke(prompt).content

    return {"response": response}