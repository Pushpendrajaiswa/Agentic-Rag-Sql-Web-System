# 🤖 Agentic AI System (RAG + SQL + Web)

## 🚀 Overview

This project is a **multi-agent AI system** built using **LangGraph** that intelligently routes user queries between:

* 📚 **RAG Agent** → Answers from static documents (PDF → FAISS vector DB)
* 🗄️ **SQL Agent** → Queries structured stock data (SQLite)
* 🌐 **Web Agent** → Fetches real-time information (Tavily Search)

The system dynamically selects the best agent and uses a **fallback mechanism (RAG → Web)** when needed.

---

## 🧠 Architecture

```
User Query
    ↓
Router (LLM Decision)
    ↓
 ┌───────────────┬───────────────┐
 │               │               │
RAG           SQL             WEB
 │              │               │
 ↓              ↓               ↓
FAISS        SQLite         Tavily API
```

---

## ⚙️ Tech Stack

* **LangGraph** → Agent orchestration
* **LangChain** → LLM integration
* **OpenAI** → LLM + embeddings
* **FAISS** → Vector database (RAG)
* **SQLite** → Structured database
* **Tavily API** → Web search
* **Streamlit** → UI

---

## 📁 Project Structure

```
.
├── app.py                 # Streamlit UI
├── graph.py               # LangGraph workflow
├── state.py               # Shared state

├── nodes/                 # Agent nodes
│   ├── router.py
│   ├── rag_node.py
│   ├── sql_node.py
│   └── web_node.py

├── tools/                 # Tools layer
│   ├── rag_tool.py
│   ├── sql_tool.py
│   └── web_search_tool.py

├── utils/
│   └── llm.py

├── data/
│   ├── rag_docs/
│   └── apple_stock_data.csv

├── db/
│   ├── vector_db/
│   └── stock.db

├── build_vector_db.py
├── build_sql_db.py
└── .gitignore
```

---

## 🔧 Setup Instructions

### 1️⃣ Clone Repository

```
git clone https://github.com/Pushpendrajaiswa/Agentic-Rag-Sql-Web-System.git
cd Agentic-Rag-Sql-Web-System
```

---

### 2️⃣ Create Virtual Environment

```
python -m venv venv
source venv/bin/activate
```

---

### 3️⃣ Install Dependencies

```
pip install -r requirements.txt
```

---

### 4️⃣ Setup Environment Variables

Create a `.env` file:

```
OPENAI_API_KEY=your_openai_key
TAVILY_API_KEY=your_tavily_key
```

---

### 5️⃣ Build Databases

```
python build_vector_db.py
python build_sql_db.py
```

---

### 6️⃣ Run Application

```
streamlit run app.py
```

---

## 🧪 Example Queries

### 📊 SQL Queries

* What is the average SP500?
* Show highest stock price

### 📚 RAG Queries

* What is diversification?
* Explain stock market basics

### 🌐 Web Queries

* Latest news about Apple stock

---

## 🧠 Key Features

* 🔀 Intelligent query routing using LLM
* 🔄 RAG → Web fallback mechanism
* 📊 Natural language → SQL conversion
* ⚡ Modular multi-agent architecture
* 🖥️ Interactive Streamlit UI

---

## 🏆 Interview Highlights

* Built **agentic workflow using LangGraph**
* Designed **multi-agent routing system**
* Integrated **RAG + SQL + Web search**
* Implemented **fallback reasoning pipeline**

---

## ⚠️ Notes

* Do not expose API keys
* Use `.env` for secure configuration

---

## 🚀 Future Improvements

* Chat-based UI (like ChatGPT)
* Graph visualization (SP500 trends 📈)
* Multi-step reasoning (ReAct agents)
* Deployment (AWS / Render / HuggingFace Spaces)

---

## 👨‍💻 Author

**Pushpendra Jaiswal**
M.Tech @ IISc
AI/ML Engineer

