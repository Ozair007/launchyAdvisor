from .finance_agent import FinanceAgent
from .legal_agent import LegalAgent
from .marketing_agent import MarketingAgent
from ollama_utils import get_ollama_llm


class OrchestratorAgent:
    def __init__(self):
        self.finance = FinanceAgent()
        self.legal = LegalAgent()
        self.marketing = MarketingAgent()
        self.llm = get_ollama_llm()

    def route_query(self, query):
        insights = {}
        called_agents = []

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

        prompt = (
            f"""
            You are the OrchestratorAgent. Given the following insights from relevant experts,
            generate a structured JSON response with:\n
            - final_decision (string)\n
            - insights (object with keys: budget, legal, marketing)\n
            - recommendations (list of strings)\n
            Only include agents that were called.\n\n
            User Query: {query}\n\n
            Insights:\n{insights}\n\n
            Return ONLY the JSON object as described above.
            """
        )
        final_response = self.llm.invoke(prompt)
        return final_response
