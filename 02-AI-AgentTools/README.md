# Step 2: AI Agent + Tools
- Connect the chatbot to an LLM using OpenRouter

**LLM (Large Language Model):** which is a type of artificial intelligence trained to read, write, and understand human language.
Main Uses in Technology An LLM acts like a very smart prediction engine. It looks at billions of words to learn how sentences fit together
It powers modern AI chatbots and writing assistants

Common tasks include:
- Answering user questions
- Writing emails, code, and stories
- Translating text between languages
- Summarizing long articles and documents

  Popular examples include systems that power modern chatbots and search assistants like ChatGPT, Claude, and Gemini.

**OpenRouter:** is a single, unified gateway that lets developers access more than 400 artificial intelligence models from different companies using just one API
Instead of managing separate accounts and code for OpenAI, Anthropic, Google, and others, you authenticate once and connect to a single endpoint

How It Works
- One Endpoint: It uses a format that matches the OpenAI API
- Easy Switch: You change the base URL in your existing code to start using it
- Smart Routing: If a provider goes down, OpenRouter automatically switches your request to another provider that has the same model

Key Benefits
- No Lock-In: You can test and switch between different models instantly
- Better Uptime: Distributed infrastructure keeps your apps running if one server fails
- Simple Billing: You fund one balance and pay regular provider prices without a fixed monthly subscription.


## Install the packages openai ,Inside your activated venv
- Requirements.txt files: is takes all Python packages currently
and installed in your active virtual environment and writes their exact versions into requirements.txt
```
git pull
cd ../../02-AI-AgentTools/app
cp -Rf ../../01-chatbot/app/requirements.txt .
git add .
git commit -m "new"
git push
python -m pip install openai python-dotenv
python -m pip freeze > requirements.txt
cat requirements.txt
ls -a
```
## Set ignore files and folders
- Set it under root Repository 
```
cd <your Repo>
  
cat << EOF > .gitignore
venv/
.env
__pycache__/
*.pyc
EOF

cat .gitignore
git pull
git add .
git commit -m "git ignore files"
git push
ls -a
```
 ## Set the OpenRouter Key
 - from site ``` https://openrouter.ai/workspaces/default/keys ```
```
cat << EOF > .env
OPENROUTER_API_KEY=your_api_key_here
EOF

cat .env
git add .
git commit -m "nn"
git pull
git push
ls -a

```
## Create new main python file, which including AI modules
- Its same file as main-for-practise.py file
```
cd labs/02-AI-AgentTools/app
cat << EOF > main.py
import os
from dotenv import load_dotenv
from fastapi import FastAPI
from openai import OpenAI
from pydantic import BaseModel

load_dotenv()

app = FastAPI(
    title="DevOps AI Chatbot",
    version="1.0.0"
)

client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)


class ChatRequest(BaseModel):
    message: str


@app.get("/")
def root():
    return {
        "message": "DevOps AI Chatbot is running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


@app.post("/chat")
def chat(request: ChatRequest):

    response = client.chat.completions.create(
        model="openai/gpt-oss-20b:free",
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
EOF
```

## Run and test the app
- Go to to the Troubleshooting step,
  In case you get Error key or 500 Internal Server Error
  means FastAPI is running, but something inside /chat crashed
```
python -m uvicorn main:app --reload

 # Open
http://127.0.0.1:8000/docs
 # Click on
POST /chat → Try it out
 # Type message below instead of string
What is Kubernetes

```
  - In case it is not work check 
## TBD
