from utils.ollama_utils import get_ollama_llm
from utils.prompts import MARKETING_AGENT_PROMPT

"""MarketingAgent handles marketing-related queries
by providing insights on marketing strategies, channels, and taglines.
"""


class MarketingAgent:
    def __init__(self):
        self.llm = get_ollama_llm()

    def answer(self, query):
        prompt = MARKETING_AGENT_PROMPT.format(query=query)
        return self.llm.invoke(prompt)
