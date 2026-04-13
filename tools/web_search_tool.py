# REMOVE THIS
from dotenv import load_dotenv
load_dotenv()
from langchain_community.tools.tavily_search import TavilySearchResults

tavily_tool = TavilySearchResults(k=3)

def web_search(query):
    results = tavily_tool.invoke(query)

    formatted_results = ""

    for r in results:
        formatted_results += f"""
        Title: {r.get('title')}
        Content: {r.get('content')}
        URL: {r.get('url')}
        """

    return formatted_results.strip()