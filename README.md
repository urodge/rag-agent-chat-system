# rag-agent-chat-system
# RAG Agent Chat System

A chat-based Retrieval-Augmented Generation (RAG) system using:
- Local LLM via Ollama
- FastAPI backend
- MySQL database
- Basic chat UI

## Features
- Asynchronous tool call agent
- Daily updating data via OpenFDA API
- Simple HTML UI or API interface

## How to Run

1. Set up MySQL and load data via `data_pipeline/fetch_api_data.py`
2. Start Ollama: `ollama run mistral`
3. Run FastAPI: `uvicorn api.main:app --reload`

