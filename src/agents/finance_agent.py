from utils.ollama_utils import get_ollama_llm
from utils.prompts import FINANCE_AGENT_PROMPT

"""FinanceAgent handles finance-related queries
by providing insights on budget, ROI, investments, and costs.
"""


class FinanceAgent:
    def __init__(self):
        self.llm = get_ollama_llm()

    def answer(self, query):
        prompt = FINANCE_AGENT_PROMPT.format(query=query)
        return self.llm.invoke(prompt)
