"""Service for interacting with the LLM."""
import ollama

class LLMService:
    def __init__(self, model_name, base_url, system_prompt):
        self.model_name = model_name
        self.base_url = base_url
        self.system_prompt = system_prompt
        
    def get_response(self, user_input):
        """Get a response from the LLM."""
        try:
            response = ollama.chat(
                model=self.model_name,
                messages=[
                    {
                        "role": "system",
                        "content": self.system_prompt
                    },
                    {
                        "role": "user",
                        "content": user_input
                    }
                ]
            )
            return response['message']['content']
        except Exception as e:
            return f"Error: Unable to get response from LLM. {str(e)}"