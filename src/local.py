from agents.orchestrator_agent import OrchestratorAgent

def main():
    print("Welcome to Launchify Orchestrator Agent (Terminal Mode)")
    print("Type your business, legal, or marketing question below.\n")
    query = input("Your question: ").strip()
    if not query:
        print("No question entered. Exiting.")
        return

    orchestrator = OrchestratorAgent()
    print("\nProcessing...\n")
    result = orchestrator.route_query(query)
    print("Orchestrator Agent Response:\n")
    print(result)

if __name__ == "__main__":
    main()