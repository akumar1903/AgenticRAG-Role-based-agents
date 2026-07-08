# ============================================================
# Agentic RAG: Router-Retriever System with PDF and Web Search
# ============================================================

# Install required packages first:
# pip install crewai crewai-tools langchain langchain-community langchain-openai langchain-tavily faiss-cpu pypdf python-dotenv

import os
import json
import logging
from datetime import datetime
from dotenv import load_dotenv

from crewai import Agent, Task, Crew, Process
from crewai_tools import PDFSearchTool
from langchain_tavily import TavilySearch
from langchain_openai import ChatOpenAI