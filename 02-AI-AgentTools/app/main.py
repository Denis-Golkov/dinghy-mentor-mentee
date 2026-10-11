import os

from dotenv import load_dotenv
from fastapi import FastAPI
from openai import OpenAI
from pydantic import BaseModel

# Load environment variables from .env
load_dotenv()

# Check API key
api_key = os.getenv("OPENROUTER_API_KEY")

print("API KEY EXISTS:", bool(api_key))

if not api_key:
    raise RuntimeError("OPENROUTER_API_KEY is not set in .env")

# FastAPI application
app = FastAPI(
    title="DevOps AI Chatbot",
    version="1.0.0"
)

# OpenRouter client
client = OpenAI(
    api_key=api_key,
    base_url="https://openrouter.ai/api/v1"
)


# Request model
class ChatRequest(BaseModel):
    message: str


# Home endpoint
@app.get("/")
def root():
    return {
        "message": "DevOps AI Chatbot is running"
    }


# Health endpoint
@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


# Chat endpoint
@app.post("/chat")
def chat(request: ChatRequest):

    try:
        response = client.chat.completions.create(
            #model="openai/gpt-oss-20b:free",
            model="openai/gpt-oss-20b",
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful DevOps AI assistant."
                },
                {
                    "role": "user",
                    "content": request.message
                }
            ]
        )

        answer = response.choices[0].message.content

        return {
            "user": request.message,
            "answer": answer
        }

    except Exception as e:

        print("ERROR:", repr(e))

        return {
            "error": str(e)
        }
