"""Module for managing chat history."""
from dataclasses import dataclass
from typing import List
from datetime import datetime

@dataclass
class ChatMessage:
    role: str
    content: str
    timestamp: datetime

class ChatHistory:
    def __init__(self):
        self.messages: List[ChatMessage] = []
    
    def add_message(self, role: str, content: str):
        """Add a new message to the chat history."""
        message = ChatMessage(
            role=role,
            content=content,
            timestamp=datetime.now()
        )
        self.messages.append(message)
    
    def get_messages(self):
        """Get all messages in the chat history."""
        return self.messages
    
    def clear_history(self):
        """Clear the chat history."""
        self.messages = []