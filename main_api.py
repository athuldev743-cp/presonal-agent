# main_api.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from agent import process_command

app = FastAPI()

# Allow CORS for frontend (adjust origins as needed)
origins = [
    "https://personal-ai-front.vercel.app/"
    "http://127.0.0.1:5500",  # VS Code Live Server
    "http://localhost:5500",
    "*"  # Allow all for testing
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Command(BaseModel):
    text: str

@app.post("/ask")
def ask_jarvis(cmd: Command):
    try:
        response = process_command(cmd.text)
    except Exception as e:
        response = f"❌ Jarvis AI: Error processing command: {str(e)}"
    return {"response": response}

@app.get("/")
def root():
    return {"message": "Jarvis AI API is running!"}
