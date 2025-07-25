from ollama_utils import get_ollama_llm


class MarketingAgent:
    def __init__(self):
        self.llm = get_ollama_llm()

    def answer(self, query):
        prompt = (
            f"""
            Marketing question: {query}\n
            You are a marketing expert evaluating launch strategy and messaging fit.\n
            Tailor your response to region and audience.\n
            Return ONLY a JSON object with the following fields:\n
            launch_score (number 1-10), channels (list of strings e.g ["LinkedIn", "TechCrunch"]), tagline (string e.g ["AI built with EU trust and transparency"]).\n
            Do not include any explanation outside the JSON.
            """
        )
        return self.llm.invoke(prompt)
