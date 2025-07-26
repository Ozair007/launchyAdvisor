from .finance_agent import FinanceAgent
from .legal_agent import LegalAgent
from .marketing_agent import MarketingAgent
from utils.prompts import ORCHESTRATOR_AGENT_PROMPT
from utils.ollama_utils import get_ollama_llm

"""
OrchestratorAgent coordinates multiple agents to handle queries
by routing them to the appropriate agent based on keywords in the query.

It combines insights from Finance, Legal, and Marketing agents
to provide a comprehensive response.
"""


class OrchestratorAgent:
    def __init__(self):
        self.finance = FinanceAgent()
        self.legal = LegalAgent()
        self.marketing = MarketingAgent()
        self.llm = get_ollama_llm()

    def route_query(self, query):
        insights = {}
        called_agents = []

        """Check for keywords in the query to determine which agents to call."""
        if any(word in query.lower() for word in ["budget", "roi", "invest", "cost", "afford"]):
            insights["budget"] = self.finance.answer(query)
            called_agents.append("FinanceAgent")
        if any(word in query.lower() for word in ["legal", "compliance", "license", "regulation", "gdpr", "law"]):
            insights["legal"] = self.legal.answer(query)
            called_agents.append("LegalAgent")
        if any(word in query.lower() for word in ["marketing", "channel", "tagline", "social media", "outreach", "launch", "position"]):
            insights["marketing"] = self.marketing.answer(query)
            called_agents.append("MarketingAgent")

        if not insights:
            insights["budget"] = self.finance.answer(query)
            insights["legal"] = self.legal.answer(query)
            insights["marketing"] = self.marketing.answer(query)
            called_agents = ["FinanceAgent", "LegalAgent", "MarketingAgent"]

        prompt = ORCHESTRATOR_AGENT_PROMPT.format(
            query=query, insights=insights)

        final_response = self.llm.invoke(prompt)
        return final_response
