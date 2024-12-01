# Health & Fitness Chatbot

A Python-based chatbot specialized in health and fitness advice, powered by Ollama LLM and featuring a Streamlit user interface.

## Features

- Real-time chat interface
- Health and fitness specialized responses
- Local LLM integration using Ollama
- Clean and intuitive user interface
- Chat history management
- Easy to use and deploy

## Prerequisites

1. Install Ollama from: https://ollama.ai/
2. Pull the Mistral model:
   ```bash
   ollama pull mistral
   ```

## Setup

1. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

2. Start the Ollama service (in a separate terminal):
   ```bash
   ollama serve
   ```

3. Run the application:
   ```bash
   streamlit run src/main.py
   ```

## Usage

1. The chatbot will open in your default web browser
2. Type your health and fitness related questions in the text area
3. Click "Send" to get a response
4. Use "Clear Chat" to start a new conversation

## Project Structure

- `src/`
  - `main.py` - Main application entry point
  - `config.py` - Configuration settings
  - `llm_service.py` - LLM integration service
  - `chat_history.py` - Chat history management
  - `ui_components.py` - Streamlit UI components
- `requirements.txt` - Python dependencies