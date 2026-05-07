import os
import streamlit as st
from google import genai
from google.genai import types

SYSTEM = """You are a conversational companion for adults with ADHD.

When a user says "I want to do X, but I'm doing Y instead," your goals are:
1. Gently help them notice that Y might be a way of avoiding X — with curiosity, not judgment
2. Reconnect them with their intrinsic motivation for X, rather than adding pressure
3. Help them find a "minimum entry point" that lowers the activation cost of starting X

Tone principles (autonomy-supportive):
- Use "I'm wondering..." instead of "you should..."
- Ask curious questions rather than giving advice or instructions
- Acknowledge that avoidance has its own reasons; do not evaluate it
- Return agency to the user — you are thinking alongside them, not managing them
- Do not rush them; never say things like "just go do it" """

st.set_page_config(page_title="ADHD Companion v0.1", page_icon="🌱")
st.title("🌱 ADHD Companion")
st.caption("An autonomy-supportive LLM scaffold — research prototype v0.1")

# Initialize session
if "client" not in st.session_state:
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        st.error("Please set GEMINI_API_KEY environment variable.")
        st.stop()
    st.session_state.client = genai.Client(api_key=api_key)
    st.session_state.chat = st.session_state.client.chats.create(
        model="gemini-2.5-flash-lite",
        config=types.GenerateContentConfig(
            system_instruction=SYSTEM,
            max_output_tokens=512,
        ),
    )
    st.session_state.history = []

# Display chat history
for msg in st.session_state.history:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# Chat input
if user_input := st.chat_input("Tell me what's on your mind..."):
    st.session_state.history.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.write(user_input)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = st.session_state.chat.send_message(user_input)
            st.write(response.text)

    st.session_state.history.append({"role": "assistant", "content": response.text})