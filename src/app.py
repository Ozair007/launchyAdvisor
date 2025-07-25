import streamlit as st
from agents.orchestrator_agent import OrchestratorAgent
import json

st.set_page_config(page_title="Launchify Orchestrator", layout="centered")
st.title("Launchify Orchestrator Agent")

st.write("Ask your business, legal, or marketing question below:")

query = st.text_area("Your question", "")

if st.button("Submit") and query.strip():
    orchestrator = OrchestratorAgent()
    with st.spinner("Thinking..."):
        result = orchestrator.route_query(query)
        # Try to parse JSON if result is a string
        if isinstance(result, str):
            try:
                result = json.loads(result)
            except Exception:
                st.error("Could not parse response as JSON.")
                st.write(result)
                st.stop()
    st.subheader("Final Decision")
    st.write(result.get("final_decision", "No decision provided."))

    st.subheader("Recommendations")
    for rec in result.get("recommendations", []):
        st.markdown(f"- {rec}")

    st.subheader("Agent Answers")
    with st.expander("See detailed agent responses"):
        st.markdown("**Finance Agent:**")
        st.write(result["finance"])
        st.markdown("**Legal Agent:**")
        st.write(result["legal"])
        st.markdown("**Marketing Agent:**")
        st.write(result["marketing"])
