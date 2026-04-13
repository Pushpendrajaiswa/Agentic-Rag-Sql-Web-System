import streamlit as st
from graph import app
from utils.llm import llm

import os


st.set_page_config(page_title="Agentic AI System", layout="wide")

st.title("🤖 Agentic AI (RAG + WEB + SQL)")
st.markdown("Ask anything — system will decide the best agent")

# Session memory
if "history" not in st.session_state:
    st.session_state.history = []

# Input box
query = st.text_input("Enter your query:")

if st.button("Run Agent"):
    if query:
        with st.spinner("Thinking..."):
            result = app.invoke({
                "query": query
            })

            response = result["response"]
            decision = result.get("decision", "Unknown")

            # Save history
            st.session_state.history.append({
                "query": query,
                "response": response,
                "agent": decision
            })

# Show latest result
if st.session_state.history:
    last = st.session_state.history[-1]

    st.subheader("🧠 Selected Agent")
    st.success(last["agent"])

    st.subheader("💬 Response")
    st.write(last["response"])

# Chat history
st.sidebar.title("📜 History")

for item in reversed(st.session_state.history):
    st.sidebar.markdown(f"**Q:** {item['query']}")
    st.sidebar.markdown(f"**Agent:** {item['agent']}")
    st.sidebar.markdown("---")