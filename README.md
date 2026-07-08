# Agentic RAG — Router–Retriever Agent System

An experimental multi-agent Retrieval-Augmented Generation (RAG) system that routes user queries to the most appropriate retrieval strategy (PDF, web, or direct LLM) and synthesizes grounded answers. Intended as a research/demo project showing role-based agent orchestration with CrewAI and LangChain.

## Quickstart

1. Clone:
   ```bash
   git clone https://github.com/akumar1903/AgenticRAG-Role-based-agents.git
   cd AgenticRAG-Role-based-agents
   ```

2. Create a virtual environment and install dependencies:
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```

3. Add credentials:
   - Copy `.env.example` to `.env` and populate keys:
     ```
     OPENAI_API_KEY=...
     TAVILY_API_KEY=...
     ```

4. Run the demo notebook:
   ```bash
   jupyter notebook Agentic_RAG.ipynb
   ```

## Architecture
- Router Agent: selects retrieval path (PDF, Web, or LLM).
- Retriever Agent: executes the retrieval using PDFSearchTool or Tavily web search.
- Answer Generator: synthesizes answers grounded in the retrieved context.

## Project layout
- Agentic_RAG.ipynb — notebook demo
- app.py — minimal script (entrypoint scaffold)
- requirements.txt — dependencies

## Contributing
See CONTRIBUTING.md.

## License
MIT — see LICENSE.
