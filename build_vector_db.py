from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
import os
from dotenv import load_dotenv

load_dotenv()

# Path to your PDF
PDF_PATH = "/data2/2_Suvrajit_Mullick/Pushpendra_Jaiswal/Stock_Data_Agent/data/rag_docs/NLP book 1.pdf"

# Output folder
DB_PATH = "db/vector_db"

def build_vector_db():
    print("📄 Loading PDF...")
    loader = PyPDFLoader(PDF_PATH)
    documents = loader.load()

    print(f"Loaded {len(documents)} pages")

    # Split into chunks
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )

    docs = text_splitter.split_documents(documents)

    print(f"Created {len(docs)} chunks")

    # Create embeddings
    embeddings = OpenAIEmbeddings()

    print("🔍 Creating vector DB...")
    vector_db = FAISS.from_documents(docs, embeddings)

    # Save locally
    os.makedirs(DB_PATH, exist_ok=True)
    vector_db.save_local(DB_PATH)

    print(f"✅ Vector DB saved at {DB_PATH}")


if __name__ == "__main__":
    build_vector_db()