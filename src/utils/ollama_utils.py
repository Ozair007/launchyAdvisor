from langchain_community.llms import Ollama

"""
Retrieves an Ollama LLM instance with a specified model name.

Falling back to a backup model if the primary model fails to load.
"""


def get_ollama_llm(model_name="gemma3n:e2b", backup_model="llama3:latest"):
    try:
        return Ollama(model=model_name)
    except Exception as e:
        print("Error loading model '{model_name}': {e}")
        print("Falling back to backup model '{backup_model}'")
        return Ollama(model=backup_model)
