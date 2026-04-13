from langgraph.graph import StateGraph, END
from state import AgentState

from nodes.router import router_node
from nodes.rag_node import rag_node
from nodes.web_node import web_node
from nodes.sql_node import sql_node


workflow = StateGraph(AgentState)

workflow.add_node("router", router_node)
workflow.add_node("rag", rag_node)
workflow.add_node("web", web_node)
workflow.add_node("sql", sql_node)

workflow.set_entry_point("router")


# 🔹 Router decision
def route_decision(state):
    decision = state["decision"]

    if "SQL" in decision:
        return "sql"
    else:
        return "rag"   # default


workflow.add_conditional_edges(
    "router",
    route_decision,
    {
        "sql": "sql",
        "rag": "rag",
    }
)


# 🔥 NEW: After RAG → decide if WEB needed
def rag_to_next(state):
    response = state.get("response", "")

    # simple heuristic (you can improve later)
    if "I don't know" in response or len(response) < 50:
        return "web"
    else:
        return END


workflow.add_conditional_edges(
    "rag",
    rag_to_next,
    {
        "web": "web",
        END: END,
    }
)


# SQL goes directly to END
workflow.add_edge("sql", END)

# WEB → END
workflow.add_edge("web", END)


app = workflow.compile()