import streamlit as st
from agent_core import agent

st.set_page_config(page_title="Multi-Tasking AI Agent", page_icon="🤖")
st.title("🤖 Multi-Tasking AI Agent")
st.markdown("Ask me to search Google, YouTube, or check the weather! 🌍📺🌤️")

user_query = st.text_input("What would you like to ask?", placeholder="e.g. Show YouTube videos on LLaMA3")

if st.button("Ask") and user_query:
    with st.spinner("Thinking..."):
        try:
            response = agent.chat(user_query)
            st.success(response)
        except Exception as e:
            st.error(f"Something went wrong: {e}")


