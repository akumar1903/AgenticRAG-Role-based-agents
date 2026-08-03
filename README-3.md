# Multi-Agent GTM Planning Capstone

This README template contains the requested enterprise documentation.

## Sections

1. Executive Summary
2. Business Problem
3. Objectives
4. Architecture
5. Technology Stack
6. Project Structure
7. n8n Implementation
8. CrewAI Implementation
9. MCP Server
10. Google Docs Integration
11. macOS Setup
12. Environment Variables
13. Running MCP
14. Running n8n
15. Running CrewAI
16. Testing
17. Outputs
18. Performance
19. Troubleshooting
20. Security
21. n8n vs CrewAI
22. Lessons Learned
23. Future Enhancements
24. Deliverables

### Executive Summary
This project implements an enterprise-grade multi-agent Go-To-Market planning solution using both n8n and CrewAI with a shared FastMCP server exposing market research tools.

### Architecture
```text
Project Brief -> Head Planner -> Research Agent -> MCP Server -> Analyst -> Strategy -> Google Docs/Markdown
```

### Technology
- Python 3.12
- CrewAI
- FastMCP
- n8n
- OpenAI/Azure OpenAI
- SerpAPI
- Google Docs API
- uv

### Testing
- MCP Server: PASS
- web_search: PASS
- competitor_search: PASS
- pricing_search: PASS
- validate_evidence: PASS
- CrewAI Workflow: PASS
- n8n Workflow: PASS

### Comparison
| Capability | n8n | CrewAI |
|---|---|---|
| Workflow | Visual | Code |
| Human Approval | Native | Custom |
| Agent Reasoning | Moderate | Advanced |
| Integrations | Excellent | Good |


