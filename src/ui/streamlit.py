import streamlit as st
from langchain_core.messages import AIMessage
from agents.orchestrator_agent import OrchestratorAgent
from agents.critic_agent import CriticExpertAgent
from utils.json_formatter import json_formatter
import json

"""
Streamlit app for LaunchyAdvisor, allowing users to interact with the Orchestrator and Critic Expert agents.
Users can ask business, legal, or marketing questions to get a launch plan,
or submit a launch plan for expert critique.
"""


def run_streamlit_app():
    st.set_page_config(page_title="Launchify Advisor", layout="centered")
    st.title("LaunchyAdvisor")

    mode = st.radio(
        "Choose your mode:",
        ("Ask Orchestrator (get a plan)", "Critic Expert Agent (review your plan)")
    )

    if mode == "Ask Orchestrator (get a plan)":
        st.write("Ask your business, legal, or marketing question below:")
        query = st.text_area("Your question", "")
        if st.button("Submit") and query.strip():
            orchestrator = OrchestratorAgent()
            with st.spinner("Thinking..."):
                result = orchestrator.route_query(query)
            try:
                result = json_formatter(result)
                obj = json.loads(result) if isinstance(result, str) else result
            except Exception:
                obj = result
            st.write("### Orchestrator Agent Response")
            st.json(obj, expanded=True)

    elif mode == "Critic Expert Agent (review your plan)":
        st.write("Paste your launch plan below for expert critique:")
        plan_json = st.text_area("Your launch plan", "")
        if st.button("Review Plan") and plan_json.strip():
            critic = CriticExpertAgent()
            with st.spinner("Reviewing..."):
                feedback = critic.review_plan(plan_json)
            try:
                if isinstance(feedback, AIMessage):
                    feedback = feedback.content
                feedback = json_formatter(feedback)
                obj = json.loads(feedback) if isinstance(
                    feedback, str) else feedback
            except Exception:
                obj = feedback
            st.write("### Critic Expert Agent Feedback")
            st.json(obj, expanded=True)
