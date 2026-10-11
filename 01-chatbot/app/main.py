from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI(
    title="DevOps AI Chatbot"
    version="1.0.0"
)
class ChatRequest(BaseModel):
    message: str
@app.get("/")
def root():
     return {
        "message": "DevOps AI Chatbot is running"
    }
@app.post("/chat")
def chat(request: ChatRequest):
    return {
        "user": request.message,
        "answer": f"You said: {requet.message}"
    }
