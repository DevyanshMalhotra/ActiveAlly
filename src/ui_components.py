"""Streamlit UI components for the chatbot."""
import streamlit as st

def initialize_session_state():
    """Initialize session state variables."""
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

def render_header(title: str, description: str):
    """Render the app header."""
    st.title(title)
    st.markdown(description)
    st.markdown("---")

def render_chat_message(role: str, content: str):
    """Render a chat message with appropriate styling."""
    if role == "user":
        st.markdown(f"**You:** {content}")
    else:
        st.markdown(f"**Assistant:** {content}")

def render_chat_history(messages):
    """Render the entire chat history."""
    for msg in messages:
        render_chat_message(msg.role, msg.content)

def render_user_input():
    """Render the user input field."""
    return st.text_area(
        "Ask your health and fitness question:",
        key="user_input",
        height=100
    )

def render_clear_button():
    """Render the clear chat button."""
    if st.button("Clear Chat"):
        return True
    return False