from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

# Load env FIRST
load_dotenv()

# Debug (optional)
print("API KEY:", os.getenv("OPENAI_API_KEY"))

llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0,
    api_key=os.getenv("OPENAI_API_KEY")  # explicitly pass
)