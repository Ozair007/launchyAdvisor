# LaunchyAdvisor

A modular agent-based system for answering business, legal, and marketing questions using local LLMs (Ollama) and LangChain, with a Streamlit UI.

## Features

- **Orchestrator Agent**: Calls the appropriate expert agents and synthesizes a structured final response.
- **Finance, Legal, Marketing Agents**: Specialized modules for domain-specific answers.
- **Local LLM**: Uses Ollama for privacy and speed.
- **Streamlit UI**: Simple web interface for interactive querying.
- **Terminal Mode**: Run queries from the command line.

## Setup

1. **Clone the repository**
   ```sh
   git clone https://github.com/Ozair007/launchyAdvisor.git
   cd launchify
   ```

2. **Set up Python environment**
   ```sh
   python -m venv .venv
   .venv\Scripts\activate   # Windows
   source .venv/bin/activate # macOS/Linux
   pip install -r requirements.txt
   ```

3. **Install Ollama and download your desired model**
   - [Ollama installation guide](https://ollama.com/download)
   - Example: `ollama pull gemma3n:e2b`

4. **Run the Streamlit app**
   ```sh
   streamlit run src/app.py
   ```

5. **Run in terminal mode**
   ```sh
   python src/local.py
   ```

## Project Structure

```
launchify/
│
├── src/
│   ├── agents/
│   │   ├── finance_agent.py
│   │   ├── legal_agent.py
│   │   ├── marketing_agent.py
│   │   └── orchestrator_agent.py
│   ├── ui
│   │   └── streamlit.py
│   ├── utils
│   │   ├── json_formatter.py
│   │   ├── ollama_utils.py
│   │   └── prompts.py
│   ├── app.py
│   └── local.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Example Output

```json
{
  "final_decision": "Consider outsourcing, but with careful legal and budget considerations.",
  "insights": {
    "budget": { ... },
    "legal": { ... },
    "marketing": { ... }
  },
  "recommendations": [
    "Conduct a thorough legal risk assessment for each country.",
    "Implement robust data protection and security measures.",
    "Engage local legal counsel.",
    "Develop a phased outsourcing approach with clear KPIs.",
    "Consider a pilot program to test the outsourcing model."
  ]
}
```