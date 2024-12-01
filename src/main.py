"""Main application file for the Health & Fitness Chatbot."""
import streamlit as st
from config import (
    OLLAMA_MODEL,
    OLLAMA_BASE_URL,
    SYSTEM_PROMPT,
    APP_TITLE,
    APP_DESCRIPTION
)
from llm_service import LLMService
from chat_history import ChatHistory
from ui_components import (
    initialize_session_state,
    render_header,
    render_chat_history,
    render_user_input,
    render_clear_button
)

def main():
    # Initialize services
    llm_service = LLMService(OLLAMA_MODEL, OLLAMA_BASE_URL, SYSTEM_PROMPT)
    
    # Initialize session state
    initialize_session_state()
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = ChatHistory()
    
    # Render UI
    render_header(APP_TITLE, APP_DESCRIPTION)
    
    # Handle clear chat
    if render_clear_button():
        st.session_state.chat_history.clear_history()
        st.rerun()
    
    # Display chat history
    render_chat_history(st.session_state.chat_history.get_messages())
    
    # Handle user input
    user_input = render_user_input()
    if st.button("Send"):
        if user_input.strip():
            # Add user message to history
            st.session_state.chat_history.add_message("user", user_input)
            
            # Get LLM response
            response = llm_service.get_response(user_input)
            
            # Add assistant response to history
            st.session_state.chat_history.add_message("assistant", response)
            
            # Clear input and rerun to update UI
            st.session_state.user_input = ""
            st.rerun()

if __name__ == "__main__":
    main()