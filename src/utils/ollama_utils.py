from langchain_ollama.chat_models import ChatOllama

"""
Retrieves an Ollama LLM instance with a specified model name.

Falling back to a backup model if the primary model fails to load.
"""


def get_ollama_chat_llm(model_name="llama3.1", backup_model="llama3"):
    try:
        return ChatOllama(model=model_name)
    except Exception as e:
        print(f"Error loading model '{model_name}': {e}")
        print(f"Falling back to backup model '{backup_model}'")
        return ChatOllama(model=backup_model)
