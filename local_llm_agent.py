import requests
import json
from tools.fda_tools import get_recent_drug_recalls # type: ignore

OLLAMA_URL = "http://localhost:11434/api/chat"

def query_llm(user_input):
    response = requests.post(OLLAMA_URL, json={
        "model": "mistral",  # Or qwen, llama3, etc.
        "messages": [{"role": "user", "content": user_input}],
        "tools": [{
            "type": "function",
            "function": {
                "name": "get_recent_drug_recalls",
                "description": "Fetch latest drug recalls",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "limit": {
                            "type": "integer",
                            "default": 5
                        }
                    }
                }
            }
        }]
    })
    result = response.json()

    # If function call requested
    if "tool_calls" in result:
        tool_call = result["tool_calls"][0]
        args = json.loads(tool_call["function"]["arguments"])
        recalls = get_recent_drug_recalls(limit=args.get("limit", 5))
        return str(recalls)
    
    return result["message"]["content"]
