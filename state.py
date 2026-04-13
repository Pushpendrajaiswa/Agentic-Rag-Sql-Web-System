from typing import TypedDict

class AgentState(TypedDict):
    query: str
    decision: str
    response: str