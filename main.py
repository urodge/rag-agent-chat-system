from fastapi import FastAPI
from pydantic import BaseModel
from agent.local_llm_agent import query_llm

app = FastAPI()

class Query(BaseModel):
    message: str

@app.post("/chat")
def chat(query: Query):
    answer = query_llm(query.message)
    return {"response": answer}
