from ollama_utils import get_ollama_llm


class FinanceAgent:
    def __init__(self):
        self.llm = get_ollama_llm()

    def answer(self, query):
        prompt = (
            f"""
            Finance question: {query}\n
            Return ONLY a JSON object with the following fields:\n
            can_afford (true/false), estimated_cost (number), budget_remaining (number), rationale (string).\n
            Do not include any explanation outside the JSON.
            """
        )
        return self.llm.invoke(prompt)
