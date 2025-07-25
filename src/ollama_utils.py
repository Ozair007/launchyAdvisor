from langchain_community.llms import Ollama

def get_ollama_llm(model_name="gemma3n:e2b"):
    return Ollama(model=model_name)