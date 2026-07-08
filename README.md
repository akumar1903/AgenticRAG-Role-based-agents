# Agentic RAG: Router–Retriever System with PDF and Web Search

An Agentic Retrieval-Augmented Generation (RAG) system that uses multiple role-based AI agents to answer domain-specific questions by selecting the most suitable source (PDF, web, or direct LLM).

## Table of Contents

- Overview
- Architecture
  - Router Agent
  - Retriever Agent
  - Answer Generator Agent
- Workflow
- Tools Used
- Input Sources
- Project Structure
- Installation
- Environment Variables
- Agent Roles
- Example Questions
- Logging and Traceability
- Why CrewAI?
- Results
- Future Improvements
- Conclusion

---

## Overview

This project implements an Agentic RAG system using CrewAI. The system coordinates multiple role-based agents to determine the best retrieval path, fetch relevant context from static or dynamic sources, and produce concise, source-grounded answers. It demonstrates agent orchestration, tool usage, reasoning traceability, and source-grounded answer generation.

## Architecture

The system consists of three specialized agents:

### 1) Router Agent
- Analyzes the user's question.
- Determines the most appropriate route: PDF, WEB, or LLM.
- Routes to the appropriate retriever/strategy:
  - PDF — use an uploaded PDF document as the source.
  - WEB — use an internet search to retrieve up-to-date information.
  - LLM — answer directly from the language model when retrieval is not required.

### 2) Retriever Agent
- Responsible for retrieving information from the selected source.
- Available tools:
  - PDF Search Tool — searches the uploaded Transformer research paper and other PDFs.
  - Tavily Web Search Tool — retrieves current information from the internet (useful for recent developments).

### 3) Answer Generator Agent
- Uses the retrieved context to produce the final response.
- Ensures answers are concise, grounded in sources, and include source attribution when appropriate.

## Workflow

User question → Router Agent → Selected route → Retriever Agent → (PDF / Web / LLM) → Answer Generator Agent → Final response

## Tools Used

- CrewAI — agent orchestration and task management
- PDFSearchTool — search uploaded PDF documents
- TavilySearchTool — web search for dynamic information
- OpenAI GPT-4o Mini — reasoning engine used by the agents

## Input Sources

- Static Source
  - Transformer research paper: *Attention Is All You Need* (used for domain-specific knowledge such as transformer architecture, self-attention, multi-head attention, positional encoding, training methodology, and BLEU evaluations).

- Dynamic Source
  - Internet search using Tavily for recent developments and external knowledge.

## Project Structure

project/
├── Agentic_RAG.ipynb
├── README.md
├── .env
├── agentic_rag_trace.log
├── transformer_research_paper-dataset.pdf
└── requirements.txt

> Note: I fixed a filename typo ("trasformer" → "transformer"). If your actual filename differs, please update the Project Structure section or rename the file in the repo.

## Installation

Install dependencies (example):

```bash
pip install -r requirements.txt
```

If you prefer installing packages individually:

```bash
pip install crewai crewai-tools tavily-python langchain-openai python-dotenv pypdf faiss-cpu
```

## Environment Variables

Create a `.env` file with:

```
OPENAI_API_KEY=your_openai_api_key
TAVILY_API_KEY=your_tavily_api_key
```

## Agent Roles

- Router Agent — decide whether to use the PDF, the web, or the LLM directly.
- Retriever Agent — fetch relevant passages or documents using the chosen tool.
- Answer Generator Agent — synthesize a concise, grounded answer from the retrieved context.

## Example Questions

- PDF Route
  - Q: "What is scaled dot-product attention in the Transformer paper?"
  - Source: PDF Search Tool

- Web Route
  - Q: "What are the latest trends in Retrieval-Augmented Generation?"
  - Source: Tavily Web Search Tool

- LLM Route
  - Q: "Explain RAG in simple terms."
  - Source: Direct LLM response

## Logging and Traceability

Interactions are recorded in `agentic_rag_trace.log`. Logs typically include:
- Timestamp
- Agent name
- Action performed
- Selected route
- Retrieved context
- Generated answer

These logs enable reasoning traceability and debugging.

## Why CrewAI?

CrewAI was selected because it:
- Supports multi-agent orchestration and sequential execution
- Enables task delegation and collaboration between agents
- Provides a transparent reasoning flow
- Simplifies tool integration and closely resembles production Agentic AI architectures

## Results

The system demonstrates:
- Multi-agent collaboration
- Dynamic routing between sources
- Retrieval-Augmented Generation with source grounding
- Interaction logging and traceability
- Integration of static and dynamic knowledge sources

## Future Improvements

Possible enhancements include:
- Memory support and conversation history
- Hybrid retrieval and reranking models
- Use of vector databases such as FAISS or Chroma
- Human-in-the-loop validation
- Streamlit or other web UI for interaction
- Azure OpenAI and Azure AI Search integration

## Conclusion

This project shows how multiple AI agents can collaborate to perform intelligent routing, retrieval, and answer generation. By combining static document knowledge with dynamic web search, the system provides grounded, up-to-date, and traceable answers for domain-specific questions.
