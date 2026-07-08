Agentic RAG: Router-Retriever System with PDF and Web Search
Overview
This project implements an Agentic Retrieval-Augmented Generation (RAG) system using CrewAI. The system uses multiple role-based AI agents to intelligently answer user questions by selecting the most appropriate information source.
The solution demonstrates agent orchestration, tool usage, reasoning traceability, and source-grounded answer generation.
 
Architecture
The system consists of three specialized agents:
1. Router Agent
•	Analyzes the user's question.
•	Determines the most appropriate route.
•	Selects one of the following:
Route	Description
PDF	Uses the uploaded PDF document
WEB	Uses internet search
LLM	Uses the language model directly
 
2. Retriever Agent
Responsible for retrieving information from the selected source.
Available tools:
PDF Search Tool
•	Searches the uploaded Transformer research paper.
•	Provides domain-specific information.
Tavily Web Search Tool
•	Retrieves current information from the internet.
•	Useful for recent developments and external knowledge.
 
3. Answer Generator Agent
•	Uses retrieved context.
•	Produces the final response.
•	Ensures answers are concise, grounded, and source-aware.
 
Workflow
User Question
↓
Router Agent
↓
Determine Route
↓
Retriever Agent
↓
PDF Search / Web Search / Direct LLM
↓
Answer Generator Agent
↓
Final Response
 
Tools Used
CrewAI
Used for agent orchestration and task management.
PDFSearchTool
Used to search the uploaded PDF document.
TavilySearchTool
Used to retrieve real-time information from the web.
OpenAI GPT-4o Mini
Used as the reasoning engine for all agents.
 
Input Sources
Static Source
Transformer research paper:
Attention Is All You Need
This PDF provides information about:
•	Transformer architecture
•	Self-attention
•	Scaled dot-product attention
•	Multi-head attention
•	Positional encoding
•	Training methodology
•	BLEU scores and evaluation
Dynamic Source
Internet search using Tavily.
 
Project Structure
project/
│
├── Agentic_RAG.ipynb
├── README.md
├── .env
├── agentic_rag_trace.log
├── trasformer_research_paper-dataset.pdf
└── requirements.txt
 
Installation
Install dependencies:
pip install crewai
pip install crewai-tools
pip install tavily-python
pip install langchain-openai
pip install python-dotenv
pip install pypdf
pip install faiss-cpu
 
Environment Variables
Create a .env file:
OPENAI_API_KEY=your_openai_api_key
TAVILY_API_KEY=your_tavily_api_key
 
Agent Roles
Router Agent
Goal
Determine whether the question should be answered using:
•	PDF
•	WEB
•	LLM
 
Retriever Agent
Goal
Retrieve relevant information using the appropriate tool.
 
Answer Generator Agent
Goal
Generate a grounded answer using retrieved context.
 
Example Questions
PDF Route
What is scaled dot-product attention in the Transformer paper?
Source:
•	PDF Search Tool
 
Web Route
What are the latest trends in Retrieval-Augmented Generation?
Source:
•	Tavily Web Search Tool
 
LLM Route
Explain RAG in simple terms.
Source:
•	Direct LLM response
 
Logging and Traceability
The system records interactions in:
agentic_rag_trace.log
The logs contain:
•	Timestamp
•	Agent name
•	Action performed
•	Selected route
•	Retrieved context
•	Generated answer
This enables reasoning traceability and debugging.
 
Why CrewAI?
CrewAI was selected because it:
•	Supports multi-agent orchestration.
•	Enables task delegation and collaboration.
•	Provides transparent reasoning flow.
•	Simplifies tool integration.
•	Supports sequential execution.
•	Closely resembles production Agentic AI architectures.
 
Results
The system successfully demonstrates:
•	Multi-agent collaboration.
•	Dynamic routing.
•	Retrieval-Augmented Generation.
•	Source-grounded responses.
•	Interaction logging and traceability.
•	Integration of static and dynamic knowledge sources.
 
Future Improvements
Possible enhancements include:
•	Memory support.
•	Conversation history.
•	Hybrid retrieval.
•	Reranking models.
•	Vector databases such as FAISS or Chroma.
•	Human-in-the-loop validation.
•	Streamlit user interface.
•	Azure OpenAI and Azure AI Search integration.
 
Conclusion
This project demonstrates how multiple AI agents can collaborate to perform intelligent routing, retrieval, and answer generation. By combining static document knowledge with dynamic web search, the system produces accurate and context-aware responses while maintaining transparency and traceability throughout the reasoning process.

