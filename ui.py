import streamlit as st
from app import app
import os

st.set_page_config(page_title="LangGraph Agent", page_icon="🤖")

st.title("🤖 LangGraph Agent")
st.write("Ask me anything about LangGraph!")

if not os.getenv("GROQ_API_KEY"):
    st.error("GROQ_API_KEY not found in environment variables. Please check your .env file.")
    st.stop()

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("What is your question?"):
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                result = app.invoke({"question": prompt})
                response = result.get("answer", "I couldn't generate an answer.")
                st.markdown(response)
                st.session_state.messages.append({"role": "assistant", "content": response})
            except Exception as e:
                st.error(f"An error occurred: {e}")
