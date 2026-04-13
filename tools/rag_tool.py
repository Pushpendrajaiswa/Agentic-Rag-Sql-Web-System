# REMOVE THIS
from dotenv import load_dotenv
load_dotenv()
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
import os

def load_vector_db():
    return FAISS.load_local(
        "db/vector_db",
        OpenAIEmbeddings(),
        allow_dangerous_deserialization=True   # ✅ ADD THIS
    )

def rag_query(query):
    db = load_vector_db()
    docs = db.similarity_search(query, k=3)
    return "\n".join([doc.page_content for doc in docs])