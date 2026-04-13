from tools.web_search_tool import web_search
from utils.llm import llm

def web_node(state):
    query = state["query"]

    results = web_search(query)

    prompt = f"""
    Use this web data:
    {results}

    Answer the question:
    {query}
    """

    response = llm.invoke(prompt).content

    return {"response": response}