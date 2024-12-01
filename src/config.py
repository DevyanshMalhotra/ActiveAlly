"""Configuration settings for the chatbot."""

# Ollama API settings
OLLAMA_MODEL = "mistral"
OLLAMA_BASE_URL = "http://localhost:11434"

# System prompt to specialize the model for health and fitness
SYSTEM_PROMPT = """You are a knowledgeable health and fitness expert. Your role is to provide accurate, 
science-based information about health, nutrition, exercise, and wellness. Always:
- Base answers on scientific evidence
- Provide practical, actionable advice
- Include relevant disclaimers when necessary
- Encourage consulting healthcare professionals for medical advice
- Stay within the scope of general health and fitness guidance
- Be supportive and motivating
"""

# UI Configuration
APP_TITLE = "Health & Fitness Assistant"
APP_DESCRIPTION = """Welcome to your personal Health & Fitness Assistant! 
Ask me anything about exercise, nutrition, wellness, and healthy living."""