from langchain_core.messages import HumanMessage, AIMessage, ToolMessage
from langchain_core.tools import tool
from utils.ollama_utils import get_ollama_chat_llm
from .finance_agent import FinanceAgent
from .legal_agent import LegalAgent
from .marketing_agent import MarketingAgent
from utils.prompts import ORCHESTRATOR_AGENT_PROMPT
from utils.agents_input_schema import FinanceInput, LegalInput, MarketingInput


"""
OrchestratorAgent coordinates multiple agents to handle queries
by routing them to the appropriate agent based on the LLM's tool calling ability.

It combines insights from Finance, Legal, and Marketing agents
to provide a comprehensive response.
"""


class OrchestratorAgent:
    def __init__(self):
        self.finance_agent = FinanceAgent()
        self.legal_agent = LegalAgent()
        self.marketing_agent = MarketingAgent()
        self.llm = get_ollama_chat_llm()  # Use ChatOllama for tool calling

        # Define tools using the @tool decorator
        @tool(args_schema=FinanceInput)
        def get_finance_insights(query: str) -> str:
            """Provides insights related to finance, budget, ROI, investments, or costs."""
            return self.finance_agent.answer(query)

        @tool(args_schema=LegalInput)
        def get_legal_insights(query: str) -> str:
            """Provides insights related to legal, compliance, licenses, regulations, GDPR, or law."""
            return self.legal_agent.answer(query)

        @tool(args_schema=MarketingInput)
        def get_marketing_insights(query: str) -> str:
            """Provides insights related to marketing, channels, taglines, social media, outreach, launch, or positioning."""
            return self.marketing_agent.answer(query)

        self.tools = [get_finance_insights,
                      get_legal_insights, get_marketing_insights]
        self.llm_with_tools = self.llm.bind_tools(self.tools)

        self.available_tools = {tool.name: tool for tool in self.tools}

    def route_query(self, query):
        messages = [HumanMessage(content=query)]

        ai_message = self.llm_with_tools.invoke(messages)

        insights = {}
        called_agents = []

        if ai_message.tool_calls:
            for tool_call in ai_message.tool_calls:
                tool_name = tool_call['name']
                tool_args = tool_call['args']

                if tool_name in self.available_tools:
                    tool_function = self.available_tools[tool_name]
                    try:
                        tool_output = tool_function.invoke(tool_args)
                        insights[tool_name.replace("get_", "").replace(
                            "_insights", "")] = tool_output
                        called_agents.append(tool_name)

                        messages.append(
                            AIMessage(content="", tool_calls=[tool_call]))
                        messages.append(ToolMessage(
                            tool_output, tool_call_id=tool_call['id']))
                    except Exception as e:
                        error_message = f"Error executing tool '{tool_name}': {e}"
                        insights[tool_name.replace("get_", "").replace(
                            "_insights", "")] = error_message
                        messages.append(
                            AIMessage(content="", tool_calls=[tool_call]))
                        messages.append(ToolMessage(
                            error_message, tool_call_id=tool_call['id']))
                else:
                    print(f"Warning: LLM requested unknown tool: {tool_name}")

        if not insights:
            pass
        prompt_input = ORCHESTRATOR_AGENT_PROMPT.format(
            query=query, insights=insights, called_agents=called_agents)

        final_response_message = self.llm.invoke(
            messages + [HumanMessage(content=prompt_input)])
        final_response = final_response_message.content

        return final_response
