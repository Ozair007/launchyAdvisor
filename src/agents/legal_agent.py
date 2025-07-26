from utils.ollama_utils import get_ollama_llm
from utils.prompts import LEGAL_AGENT_PROMPT

"""LegalAgent handles legal-related queries
by providing insights on compliance, regulations, and legal recommendations.
"""


class LegalAgent:
    def __init__(self):
        self.llm = get_ollama_llm()

    def answer(self, query):
        prompt = LEGAL_AGENT_PROMPT.format(query=query)
        return self.llm.invoke(prompt)
