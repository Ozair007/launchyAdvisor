from utils.ollama_utils import get_ollama_chat_llm
from utils.prompts import CRITIC_EXPERT_AGENT_PROMPT

"""CriticExpertAgent reviews launch plans
by providing insights on feasibility, budget, and legal compliance.
"""


class CriticExpertAgent:
    def __init__(self):
        self.llm = get_ollama_chat_llm()

    def review_plan(self, plan_json):
        prompt = CRITIC_EXPERT_AGENT_PROMPT.format(plan_json=plan_json)
        return self.llm.invoke(prompt)
