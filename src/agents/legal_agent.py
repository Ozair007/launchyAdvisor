from ollama_utils import get_ollama_llm


class LegalAgent:
    def __init__(self):
        self.llm = get_ollama_llm()

    def answer(self, query):
        prompt = (
            f"""
            Legal question: {query}\n
            You are a legal expert analyzing feasibility and compliance (e.g., GDPR, regional restrictions).\n
            Return ONLY a JSON object with the following fields:\n
            compliant (true/false), issues (list of strings e.g ["Data residency law in Germany"]), recommendation (string).\n
            Do not include any explanation outside the JSON.
            """
        )
        return self.llm.invoke(prompt)
